#!/usr/bin/env python3
"""
Datenschutzpruefung: findet Namen und Muster, die nicht nach draussen duerfen.

Aufruf aus der Wurzel der Wissensbasis bzw. des Repos:

    python3 _meta/check_privacy.py              # gesamten Bestand pruefen
    python3 _meta/check_privacy.py --staged     # nur die zum Commit vorgemerkten Dateien
    python3 _meta/check_privacy.py --list       # geladene Eintraege anzeigen, nichts pruefen

Nur Standardbibliothek — keine Installation noetig.
Exit-Code 1 = Treffer gefunden.

## Die Entitaetenliste

Das Skript ist generisch. Die schuetzenswerten Namen stehen in einer LOKALEN Datei:

    _meta/privacy-entities.txt

Diese Datei darf NIEMALS eingecheckt werden — sie ist selbst das Leck, das sie
verhindern soll. Sie gehoert in die .gitignore. Fehlt sie, laufen nur die
generischen Muster, und das Skript sagt das deutlich.

Format der Liste — eine Angabe pro Zeile:

    Beispielkunde GmbH        Wortweise Suche, Gross-/Kleinschreibung egal
    =ABC                      Fuehrendes '=': exakte Schreibweise, Wortgrenzen
                              (kein Treffer auf Kleinschreibung oder Wortbestandteile)
    re:PRJ-\\d{4}              Fuehrendes 're:': regulaerer Ausdruck
    # Kommentar               Zeilen mit '#' werden ignoriert

## Escape-Hatch

Eine Zeile, die die Zeichenfolge `jumpstart-ignore` enthaelt, wird uebersprungen.
Sparsam verwenden und immer mit einer Begruendung daneben.

## Grenze des Verfahrens

Das Skript findet, was es kennt, und was eine Form hat. Es findet NICHT die
umschriebene Fallbeschreibung ohne Namen, die trotzdem eindeutig zuzuordnen ist.
Dagegen hilft nur die Konstruktionsregel: nicht uebernehmen, sondern abstrahieren.
Faustregel — ergibt eine Passage ohne den konkreten Fall immer noch Sinn, muss der
konkrete Fall raus; traegt sie ohne ihn nicht mehr, gehoert sie gar nicht ins Paket.
"""

import os
import re
import subprocess
import sys

ENTITY_FILE = os.path.join("_meta", "privacy-entities.txt")
errors = []
IGNORE_TOKEN = "jumpstart-ignore"

# workspace/ ist die operative Schicht: Klarnamen und Zahlen sind dort ausdruecklich
# erlaubt, und sie wird nie versioniert. Wuerde sie mitgeprueft, blockierte jede
# normale Meeting-Notiz das Sichern.
SKIP_DIRS = {".git", ".github", ".obsidian", "workspace", "node_modules", "__pycache__", ".venv"}
SKIP_FILES = {"privacy-entities.txt", "check_privacy.py"}
TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml", ".json", ".py", ".sh", ".toml", ".cfg", ""}

# Generische Muster — greifen auch ohne Entitaetenliste.
GENERIC = [
    ("Mailadresse", re.compile(r"\b[\w.+-]+@[\w-]+\.[A-Za-z]{2,}\b")),
    ("Lokaler Benutzerpfad", re.compile(r"(/Users/|/home/|C:\\\\Users\\\\)[A-Za-z0-9._-]+")),
    ("Betrag mit Waehrung", re.compile(r"(\d[\d.,]*\s?(?:€|EUR|\$|USD|CHF)|(?:€|EUR|\$|USD|CHF)\s?\d[\d.,]*)")),
    ("IBAN", re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{10,30}\b")),
    ("Telefonnummer", re.compile(r"(?<![\w.-])\+\d{2}[\s/-]?\(?\d{2,5}\)?[\s/-]?\d{3,}[\s\d/-]*")),
    ("Moegliches Token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{16,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})\b")),
]


def flexible(term):
    """Leerzeichen im Suchbegriff auch als Bindestrich oder Unterstrich zulassen.

    Grund: Dateinamen sind kebab-case. 'Musterkunde AG' muss auch in
    'musterkunde-ag-analyse.md' anschlagen, sonst rutscht ein Name ueber den
    Dateinamen durch.
    """
    return r"[\s_-]+".join(re.escape(part) for part in term.split())


def load_entities():
    """Gibt (Liste von (Label, Regex), Fehlertext, Hinweistext) zurueck.

    Fehlt die Liste oder ist sie leer, ist das ein HARTER Fehler und kein Hinweis:
    Das Skript wuerde sonst "Sauber" melden, obwohl es keinen einzigen eigenen Namen
    kennt — falsche Sicherheit genau dort, wo Schutz gebraucht wird. Besonders auf
    einem zweiten Geraet, wo die Liste per .gitignore systematisch fehlt.

    Bewusst ohne Eintraege arbeiten geht, aber nur als Entscheidung: eine Zeile
    "# bewusst leer" in der Datei quittiert das.
    """
    if not os.path.isfile(ENTITY_FILE):
        return [], (
            f"Keine Entitaetenliste unter {ENTITY_FILE}. Ohne sie pruefen nur die "
            "generischen Muster — eigene Kunden-, Arbeitgeber- und Personennamen werden "
            "NICHT gefunden. Datei anlegen (Vorlage: privacy-entities.example.txt) und "
            "in .gitignore eintragen. Bewusst ohne Eintraege: Zeile '# bewusst leer' "
            "in die Datei schreiben."
        ), None
    entries = []
    bewusst_leer = False
    with open(ENTITY_FILE, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if line.startswith("#"):
                if "bewusst leer" in line.lower():
                    bewusst_leer = True
                continue
            if not line:
                continue
            if line.startswith("re:"):
                entries.append((f"Regel {line[3:]}", re.compile(line[3:])))
            elif line.startswith("="):
                term = line[1:]
                entries.append((f"Entitaet {term}", re.compile(r"(?<!\w)" + flexible(term) + r"(?!\w)")))
            else:
                entries.append(
                    (f"Entitaet {line}", re.compile(r"(?<!\w)" + flexible(line) + r"(?!\w)", re.IGNORECASE))
                )
    if not entries:
        if bewusst_leer:
            return [], None, (
                f"{ENTITY_FILE} ist bewusst leer — es laufen nur die generischen Muster."
            )
        return [], (
            f"{ENTITY_FILE} enthaelt keinen einzigen Eintrag. Ohne Eintraege pruefen nur "
            "die generischen Muster. Eigene Namen eintragen — oder die Zeile "
            "'# bewusst leer' setzen, wenn das so gewollt ist."
        ), None
    return entries, None, None


def staged_files():
    try:
        out = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
            capture_output=True, text=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("FEHLER   git nicht verfuegbar oder kein Repository — --staged nicht moeglich.")
        sys.exit(1)
    return [f for f in out.splitlines() if f.strip()]


def all_files():
    found = []
    for dirpath, dirnames, filenames in os.walk("."):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in filenames:
            found.append(os.path.relpath(os.path.join(dirpath, filename), "."))
    return found


def is_text(path):
    return os.path.splitext(path)[1].lower() in TEXT_SUFFIXES


def in_skipped_dir(path):
    return any(part in SKIP_DIRS for part in path.replace("\\", "/").split("/"))


def scan(paths, entities):
    hits = []
    checks = entities + GENERIC
    for path in paths:
        base = os.path.basename(path)
        if base in SKIP_FILES or not os.path.isfile(path) or not is_text(path):
            continue
        if in_skipped_dir(path):
            continue

        # Auch der Pfad selbst wird geprueft — ein Name im Dateinamen ist ein Treffer.
        for label, pattern in checks:
            if pattern.search(path):
                hits.append((path, 0, label, path))

        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                for number, line in enumerate(fh, start=1):
                    if IGNORE_TOKEN in line:
                        continue
                    for label, pattern in checks:
                        match = pattern.search(line)
                        if match:
                            hits.append((path, number, label, match.group(0).strip()[:60]))
        except OSError as exc:
            print(f"HINWEIS  {path}: nicht lesbar ({exc})")
    return hits


def main():
    args = set(sys.argv[1:])
    entities, fehler, note = load_entities()

    if "--list" in args:
        print(f"{len(entities)} Eintrag/Eintraege aus {ENTITY_FILE}:")
        for label, _ in entities:
            print(f"  {label}")
        print(f"{len(GENERIC)} generische Muster.")
        sys.exit(0)

    if fehler:
        errors.append(fehler)
    if note:
        print(f"HINWEIS  {note}\n")

    paths = staged_files() if "--staged" in args else all_files()
    if not paths:
        print("Nichts zu pruefen.")
        sys.exit(0)

    hits = scan(paths, entities) if entities or not errors else []

    seen = set()
    for path, number, label, snippet in hits:
        key = (path, number, label)
        if key in seen:
            continue
        seen.add(key)
        stelle = f"{path}:{number}" if number else f"{path} (Dateiname)"
        print(f"TREFFER  {stelle} — {label}: {snippet!r}")

    for e in errors:
        print(f"FEHLER   {e}")

    print()
    if seen or errors:
        if seen:
            print(f"Nicht freigegeben: {len(seen)} Treffer in {len(paths)} geprueften Datei(en).")
            print("Jeden Treffer entweder entfernen, abstrahieren oder bewusst mit")
            print(f"'{IGNORE_TOKEN}' und Begruendung freigeben.")
        if errors:
            print("Die Datenschutzpruefung ist nicht einsatzbereit — siehe FEHLER oben.")
        sys.exit(1)
    print(f"Sauber. {len(paths)} Datei(en) geprueft, keine Treffer.")
    sys.exit(0)


if __name__ == "__main__":
    main()
