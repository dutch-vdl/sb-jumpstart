#!/usr/bin/env python3
"""
Konformitaetspruefung fuer eine OKF-Wissensbasis (Open Knowledge Format v0.2).

Aufruf aus der Wurzel der Wissensbasis:

    python3 _meta/check_okf.py              # gesamten Bestand pruefen
    python3 _meta/check_okf.py --staged     # nur die zum Commit vorgemerkten Dateien

Der --staged-Modus ist fuer den pre-commit-Hook gedacht: Ohne ihn wuerde ein
unfertiger Entwurf, der gar nicht committet werden soll, den Commit blockieren.
Die Versionskonsistenz (index.md gegen log.md) wird in beiden Modi geprueft.

Nur Standardbibliothek — keine Installation noetig.

Exit-Code 1 = harter Verstoss, es wird nicht gesichert.
Exit-Code 0 = konform; weiche Hinweise koennen trotzdem ausgegeben werden.

Geprueft wird:

  HART   fehlendes oder unlesbares Frontmatter in einem Concept
  HART   fehlendes Pflichtfeld `type` in einem Concept
  HART   `index.md` ausserhalb der Wurzel mit Frontmatter
  HART   Wurzel-`index.md` ohne `version`
  HART   `version` in der Wurzel-`index.md` weicht vom juengsten log.md-Eintrag ab
  HART   nicht aufgeloeste Merge-Konfliktmarker in einer Datei

  WEICH  toter bundle-relativer Link (Ziel existiert nicht)
  WEICH  Concept ohne `generated` (oder noch mit dem alten `timestamp`)
  WEICH  `generated` ohne `by` oder ohne `at`
  WEICH  `status` ausserhalb von draft/stable/deprecated
  WEICH  `stale_after` unlesbar oder ueberschritten

Die harten Kriterien pruefen Konformitaet, die weichen den Pflegezustand. Deshalb
blockiert kein weicher Hinweis eine Sicherung: Ein ueberschrittenes Verfallsdatum ist
kein Formatfehler, und eine Pruefung, die daran scheitert, wird umgangen statt befolgt.
"""

import os
import re
import subprocess
import sys
from datetime import date

# Verzeichnisse, die nicht Teil des Wissensbestands sind.
SKIP_DIRS = {".git", ".github", ".obsidian", "_meta", "workspace", "_zu-loeschen",
             ".claude", "node_modules"}

# Dateien in der Wurzel, die bewusst kein Frontmatter tragen.
EXEMPT_FILES = {"CLAUDE.md", "README.md", "log.md"}

VALID_STATUS = {"draft", "stable", "deprecated"}

FM_DELIM = "---"
LINK_RE = re.compile(r"\[[^\]]*\]\((/[^)]+)\)")
LOG_HEADING_RE = re.compile(r"^##\s+\d{4}-\d{2}-\d{2}\s+[—-]\s+v(\d+\.\d+\.\d+)\s*$")

# Nicht aufgeloeste Merge-Konfliktmarker. Sie passieren sonst jede Pruefung und
# landen unbemerkt in der Historie — bei zwei Geraeten der wahrscheinlichste Unfall.
CONFLICT_RE = re.compile(r"^(<{7}|={7}|>{7})(\s|$)", re.M)

hard = []
soft = []


def parse_frontmatter(text):
    """Gibt (dict, gefunden) zurueck. Flacher key: value-Parser, bewusst simpel."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != FM_DELIM:
        return {}, False
    data = {}
    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == FM_DELIM:
            return data, True
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1] in (" ", "\t", "-"):  # verschachtelte Werte: ignorieren
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data, False  # Delimiter nie geschlossen


def check_trust_fields(relpath, data):
    """Weiche Pruefung der OKF-v0.2-Felder (Provenance, Lebenszyklus, Haltbarkeit)."""
    generated = data.get("generated")
    if generated is None:
        if "timestamp" in data:
            soft.append(f"{relpath}: hat noch 'timestamp' statt 'generated' (v0.1-Feld).")
        else:
            soft.append(f"{relpath}: kein 'generated'.")
    elif generated.strip():
        # Inline-Mapping. Ein Block-Mapping ueber mehrere Zeilen sieht der flache
        # Parser nicht — dann wird nicht geraten, sondern nichts gemeldet.
        if "by:" not in generated:
            soft.append(f"{relpath}: 'generated' ohne 'by' — der Urheber fehlt.")
        if "at:" not in generated:
            soft.append(f"{relpath}: 'generated' ohne 'at' — der Zeitpunkt fehlt.")

    status = data.get("status")
    if status and status not in VALID_STATUS:
        soft.append(
            f"{relpath}: status '{status}' ist kein Lebenszyklus-Wert "
            f"({'/'.join(sorted(VALID_STATUS))}). Eigene Zustaende gehoeren in ein "
            "eigenes Feld, etwa 'project_status'."
        )

    stale = data.get("stale_after")
    if stale:
        try:
            faellig = date.fromisoformat(stale)
        except ValueError:
            soft.append(f"{relpath}: stale_after '{stale}' ist kein Datum der Form JJJJ-MM-TT.")
        else:
            if faellig < date.today():
                soft.append(
                    f"{relpath}: stale_after {stale} ist ueberschritten — pruefen und "
                    "entweder ein neues Datum setzen oder 'verified' nachtragen."
                )


def newest_log_version(root):
    path = os.path.join(root, "log.md")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            match = LOG_HEADING_RE.match(line.rstrip())
            if match:
                return match.group(1)
    return None


def check_links(root, relpath, text):
    for match in LINK_RE.finditer(text):
        target = match.group(1).split("#", 1)[0]
        if not target or target == "/":
            continue
        candidate = os.path.join(root, target.lstrip("/"))
        if os.path.exists(candidate) or os.path.exists(candidate.rstrip("/")):
            continue
        soft.append(f"{relpath}: toter Link -> {target}")


def index_content(path):
    """Inhalt aus dem Git-Index statt vom Datentraeger.

    Sicherheitsrelevant: Wird eine Datei gestaged und danach im Arbeitsverzeichnis
    veraendert, pruefte die alte Fassung die falsche Version.
    """
    try:
        out = subprocess.run(["git", "show", f":{path}"], capture_output=True, check=True)
        return out.stdout.decode("utf-8", errors="replace")
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def staged_markdown():
    """Nur die zum Commit vorgemerkten Markdown-Dateien."""
    try:
        out = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
            capture_output=True, text=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        hard.append("git nicht verfuegbar oder kein Repository — --staged nicht moeglich.")
        return []
    out_paths = []
    for rel in out.splitlines():
        rel = rel.strip()
        if not rel.endswith(".md"):
            continue
        if any(part in SKIP_DIRS for part in rel.split("/")):
            continue
        if os.path.isfile(rel):
            out_paths.append(rel)
    return out_paths


def collect(root, staged_only):
    if staged_only:
        return staged_markdown()
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in sorted(filenames):
            if filename.endswith(".md"):
                found.append(os.path.relpath(os.path.join(dirpath, filename), root))
    return found


def main():
    root = os.getcwd()
    staged_only = "--staged" in sys.argv[1:]

    root_index = os.path.join(root, "index.md")
    if not os.path.isfile(root_index):
        hard.append("index.md in der Wurzel fehlt.")
        report()
        return

    for rel in collect(root, staged_only):
        filename = os.path.basename(rel)
        full = os.path.join(root, rel)
        is_root_level = os.path.dirname(rel) == ""

        if staged_only:
            text = index_content(rel)
            if text is None:
                hard.append(f"{rel}: nicht aus dem Index lesbar.")
                continue
        else:
            try:
                with open(full, encoding="utf-8") as fh:
                    text = fh.read()
            except OSError as exc:
                hard.append(f"{rel}: nicht lesbar ({exc})")
                continue

        if CONFLICT_RE.search(text):
            hard.append(f"{rel}: nicht aufgeloeste Merge-Konfliktmarker.")
            continue

        check_links(root, rel, text)

        if is_root_level and filename in EXEMPT_FILES:
            continue

        data, closed = parse_frontmatter(text)

        # index.md ausserhalb der Wurzel: reines Inhaltsverzeichnis, kein Frontmatter.
        if filename == "index.md" and not is_root_level:
            if text.lstrip().startswith(FM_DELIM):
                hard.append(f"{rel}: index.md ausserhalb der Wurzel darf kein Frontmatter tragen.")
            continue

        if not text.lstrip().startswith(FM_DELIM):
            hard.append(f"{rel}: kein Frontmatter.")
            continue
        if not closed:
            hard.append(f"{rel}: Frontmatter nicht geschlossen (fehlendes '---').")
            continue

        if filename == "index.md" and is_root_level:
            if "version" not in data:
                hard.append("index.md: Feld 'version' fehlt.")
            continue

        if "type" not in data:
            hard.append(f"{rel}: Pflichtfeld 'type' fehlt.")
        check_trust_fields(rel, data)

    # Versionskonsistenz Wurzel-index.md <-> log.md
    with open(root_index, encoding="utf-8") as fh:
        index_data, _ = parse_frontmatter(fh.read())
    index_version = index_data.get("version")
    log_version = newest_log_version(root)
    if index_version and log_version and index_version != log_version:
        hard.append(
            f"Version inkonsistent: index.md sagt {index_version}, "
            f"juengster log.md-Eintrag sagt {log_version}."
        )
    elif index_version and log_version is None:
        soft.append("log.md hat keinen Eintrag im Format '## JJJJ-MM-TT — vX.Y.Z'.")

    report()


def report():
    for item in soft:
        print(f"HINWEIS  {item}")
    for item in hard:
        print(f"FEHLER   {item}")
    if hard:
        print(f"\nNicht konform: {len(hard)} harte(r) Verstoss/Verstoesse.")
        sys.exit(1)
    print(f"\nKonform. {len(soft)} Hinweis(e).")
    sys.exit(0)


if __name__ == "__main__":
    main()
