#!/usr/bin/env python3
"""
Release-Konsistenzpruefung fuer das Jumpstart-Repo.

Aufruf aus der Repo-Wurzel:

    python3 _meta/check_release.py

Nur Standardbibliothek. Exit-Code 1 = nicht releasefaehig.

Geprueft wird:

  1. VERSION existiert und ist ein gueltiges MAJOR.MINOR.PATCH.
  2. plugins/sb/VERSION stimmt damit ueberein (Kopie fuer den Plugin-Cache).
  3. plugins/sb/.claude-plugin/plugin.json -> version stimmt damit ueberein.
  4. .claude-plugin/marketplace.json fuehrt KEIN version-Feld im Plugin-Eintrag
     (die Doku raet davon ab: der plugin.json-Wert gewinnt kommentarlos).
  5. CHANGELOG.md hat einen Eintrag fuer genau diese Version, als juengsten.
  6. Der Eintrag ist vollstaendig: Klasse, Betrifft, Dateien, Abschnitt Migration.
  7. Die Klasse passt zum Sprung gegenueber dem vorherigen Changelog-Eintrag.
  8. Die unter "Dateien" genannten Pfade existieren.
  9. Die im Repo aktiv benutzten Schutzkopien sind mit ihren ausgelieferten
     Vorlagen deckungsgleich. Driften sie auseinander, schuetzt das Repo sich
     selbst mit einem aelteren Stand als den, den es weitergibt.
 10. Die Standangabe in README.md nennt dieselbe Version wie VERSION. Sie ist der
     erste Satz, den ein Empfaenger liest — eine veraltete Angabe genau dort
     beschaedigt das Kernversprechen des Projekts.
"""

import json
import os
import re
import sys

VERSION_FILE = "VERSION"
PLUGIN_DIR = os.path.join("plugins", "sb")
PLUGIN_VERSION_FILE = os.path.join(PLUGIN_DIR, "VERSION")
PLUGIN_MANIFEST = os.path.join(PLUGIN_DIR, ".claude-plugin", "plugin.json")
MARKETPLACE = os.path.join(".claude-plugin", "marketplace.json")
CHANGELOG = "CHANGELOG.md"
README = "README.md"
README_STAND = re.compile(r"\*\*Stand:\s*(\d+\.\d+\.\d+)")
TEMPLATES = os.path.join(PLUGIN_DIR, "skills", "jumpstart", "templates")

# Aktiv benutzte Kopie -> ausgelieferte Vorlage. Eine Quelle, zwei Orte.
SPIEGEL = [
    (os.path.join("_meta", "check_privacy.py"),
     os.path.join(TEMPLATES, "check_privacy.py")),
    (os.path.join(".githooks", "pre-commit"),
     os.path.join(TEMPLATES, "pre-commit")),
]

SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
ENTRY = re.compile(r"^##\s+v(\d+\.\d+\.\d+)\s+—\s+(\d{4}-\d{2}-\d{2})\s*$", re.M)

errors = []
notes = []


def read_text(path):
    if not os.path.isfile(path):
        errors.append(f"{path} fehlt.")
        return None
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def parse_entries(text):
    """Gibt Liste von (version, datum, body) zurueck, in Dateireihenfolge."""
    matches = list(ENTRY.finditer(text))
    out = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((m.group(1), m.group(2), text[start:end]))
    return out


def expected_class(new, old):
    n = [int(x) for x in new.split(".")]
    o = [int(x) for x in old.split(".")]
    if n[0] > o[0] and n[1] == 0 and n[2] == 0:
        return "MAJOR"
    if n[0] == o[0] and n[1] > o[1] and n[2] == 0:
        return "MINOR"
    if n[0] == o[0] and n[1] == o[1] and n[2] > o[2]:
        return "PATCH"
    return None


def main():
    raw = read_text(VERSION_FILE)
    if raw is None:
        report()
        return
    version = raw.strip()
    if not SEMVER.match(version):
        errors.append(f"{VERSION_FILE}: '{version}' ist kein MAJOR.MINOR.PATCH.")
        report()
        return

    # 2. Kopie im Plugin
    plugin_raw = read_text(PLUGIN_VERSION_FILE)
    if plugin_raw is not None and plugin_raw.strip() != version:
        errors.append(
            f"{PLUGIN_VERSION_FILE}: '{plugin_raw.strip()}' weicht von {VERSION_FILE} "
            f"('{version}') ab. Ohne diese Kopie findet der Upgrade-Skill bei Stufe 3 "
            "keine Version."
        )

    # 3. Manifest
    manifest_raw = read_text(PLUGIN_MANIFEST)
    if manifest_raw is not None:
        try:
            manifest = json.loads(manifest_raw)
        except json.JSONDecodeError as exc:
            errors.append(f"{PLUGIN_MANIFEST}: kein gueltiges JSON ({exc}).")
            manifest = {}
        mv = manifest.get("version")
        if mv is None:
            errors.append(f"{PLUGIN_MANIFEST}: Feld 'version' fehlt — ohne es bekommt niemand ein Update.")
        elif mv != version:
            errors.append(f"{PLUGIN_MANIFEST}: version '{mv}' weicht von {VERSION_FILE} ('{version}') ab.")

    # 4. Marketplace darf keine Version fuehren
    mk_raw = read_text(MARKETPLACE)
    if mk_raw is not None:
        try:
            mk = json.loads(mk_raw)
            for entry in mk.get("plugins", []):
                if "version" in entry:
                    errors.append(
                        f"{MARKETPLACE}: Plugin-Eintrag '{entry.get('name')}' fuehrt ein "
                        "version-Feld. Der Wert aus plugin.json gewinnt kommentarlos — "
                        "hier gepflegt taeuscht er ein Release vor, das niemanden erreicht."
                    )
                src = entry.get("source")
                if isinstance(src, str) and src.startswith("./") and not os.path.isdir(src):
                    errors.append(
                        f"{MARKETPLACE}: source '{src}' existiert nicht. Die Installation "
                        "bricht mit 'Source path does not exist' ab."
                    )
        except json.JSONDecodeError as exc:
            errors.append(f"{MARKETPLACE}: kein gueltiges JSON ({exc}).")

    # 5.-8. Changelog
    log_raw = read_text(CHANGELOG)
    if log_raw is not None:
        entries = parse_entries(log_raw)
        if not entries:
            errors.append(f"{CHANGELOG}: kein Eintrag im Format '## vX.Y.Z — JJJJ-MM-TT'.")
        elif entries[0][0] != version:
            errors.append(
                f"{CHANGELOG}: juengster Eintrag ist v{entries[0][0]}, "
                f"{VERSION_FILE} sagt {version}."
            )
        else:
            _, _, body = entries[0]
            for feld in ("Klasse:", "Betrifft:", "Dateien:"):
                if f"**{feld}" not in body:
                    errors.append(f"{CHANGELOG} v{version}: Feld '{feld[:-1]}' fehlt.")
            if "### Migration" not in body:
                errors.append(
                    f"{CHANGELOG} v{version}: Abschnitt '### Migration' fehlt. "
                    "Ein Eintrag ohne Migrationshinweis gilt als unfertig."
                )
            klasse = re.search(r"\*\*Klasse:\*\*\s*(MAJOR|MINOR|PATCH)", body)
            if klasse and len(entries) > 1:
                erwartet = expected_class(version, entries[1][0])
                if erwartet is None:
                    errors.append(
                        f"{CHANGELOG}: Sprung v{entries[1][0]} -> v{version} ist kein "
                        "gueltiger Versionsschritt (Luecke oder Rueckschritt)."
                    )
                elif klasse.group(1) != erwartet:
                    errors.append(
                        f"{CHANGELOG} v{version}: Klasse '{klasse.group(1)}' passt nicht "
                        f"zum Sprung von v{entries[1][0]} (erwartet: {erwartet})."
                    )
            dateien = re.search(r"\*\*Dateien:\*\*\s*(.+)", body)
            if dateien:
                for pfad in [p.strip() for p in dateien.group(1).split(",") if p.strip()]:
                    if pfad.lower() in ("keine", "-", "—"):
                        continue
                    if not os.path.exists(pfad):
                        notes.append(f"{CHANGELOG} v{version}: genannter Pfad '{pfad}' existiert nicht.")

    # 10. Standangabe der README
    readme = read_text(README)
    if readme is not None:
        m = README_STAND.search(readme)
        if not m:
            errors.append(
                f"{README}: keine Standangabe der Form '**Stand: X.Y.Z' gefunden. "
                "Sie ist der erste Satz, den ein Empfaenger liest."
            )
        elif version and m.group(1) != version:
            errors.append(
                f"{README} nennt Stand {m.group(1)}, {VERSION_FILE} steht auf {version}. "
                "Die Angabe im Fliesstext nachziehen."
            )

    # 9. Schutzkopien gegen ihre Vorlagen
    for kopie, vorlage in SPIEGEL:
        if not os.path.isfile(vorlage):
            errors.append(f"{vorlage} fehlt — Vorlage nicht auslieferbar.")
            continue
        if not os.path.isfile(kopie):
            errors.append(f"{kopie} fehlt — das Repo schuetzt sich selbst nicht.")
            continue
        with open(vorlage, "rb") as fh:
            a = fh.read()
        with open(kopie, "rb") as fh:
            b = fh.read()
        if a != b:
            errors.append(
                f"{kopie} weicht von {vorlage} ab. Das Repo arbeitet mit einem anderen "
                "Stand als dem, den es weitergibt. Vorlage darueberkopieren."
            )

    report(version)


def report(version=None):
    for n in notes:
        print(f"HINWEIS  {n}")
    for e in errors:
        print(f"FEHLER   {e}")
    print()
    if errors:
        print(f"Nicht releasefaehig: {len(errors)} Fehler.")
        sys.exit(1)
    print(f"Releasefaehig{f': v{version}' if version else ''}. {len(notes)} Hinweis(e).")
    sys.exit(0)


if __name__ == "__main__":
    main()
