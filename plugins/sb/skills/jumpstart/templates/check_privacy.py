#!/usr/bin/env python3
"""
Datenschutzpruefung: findet Namen und Muster, die nicht nach draussen duerfen.

Aufruf aus der Wurzel der Wissensbasis bzw. des Repos:

    python3 _meta/check_privacy.py              # gesamten Bestand pruefen
    python3 _meta/check_privacy.py --staged     # nur die vorgemerkten Dateien, Inhalt
                                                # aus dem Index statt vom Datentraeger
    python3 _meta/check_privacy.py --list       # geladene Eintraege anzeigen, nichts pruefen

Nur Standardbibliothek — keine Installation noetig.
Exit-Code 1 = Treffer oder Klaerungsfall gefunden.

## Die Entitaetenliste

Das Skript ist generisch. Die schuetzenswerten Namen stehen in einer LOKALEN Datei:

    _meta/privacy-entities.txt

Diese Datei darf NIEMALS eingecheckt werden — sie ist selbst das Leck, das sie
verhindern soll. Sie gehoert in die .gitignore. Fehlt sie, ist das ein harter Fehler.

Format der Liste — eine Angabe pro Zeile:

    Beispielkunde GmbH        Wortweise Suche, Gross-/Kleinschreibung egal
    =ABC                      Fuehrendes '=': exakte Schreibweise, Wortgrenzen
                              (kein Treffer auf Kleinschreibung oder Wortbestandteile)
    re:PRJ-\\d{4}              Fuehrendes 're:': regulaerer Ausdruck
    ?Firma GmbH               Fuehrendes '?': KLAERUNGSFALL statt Sperre — siehe unten
    # Kommentar               Zeilen mit '#' werden ignoriert

Die Praefixe lassen sich kombinieren: '?=ABC' und '?re:...' sind gueltig.

## Klaerungsfaelle ('?') — der eigene Arbeitgeber

Der eigene Arbeitgeber ist der blinde Fleck jeder Namensprueflung. Er gehoert NICHT
als Sperre auf die Liste: Sein Name steht zwangslaeufig im eigenen Profil, in den
Karrierestationen und in Quellenangaben — als Sperre wuerde er jede Sicherung
blockieren. Sein Material ist trotzdem regelmaessig das schutzbeduerftigste im
ganzen Bestand (interne Strategie, Sprechregeln, Wettbewerbsbewertungen).

Deshalb die zweite Klasse: '?Name' sperrt nicht, sondern loest EINMAL PRO DATEI eine
Rueckfrage aus. Sie wird beantwortet, indem irgendwo in der Datei — sinnvollerweise
im Frontmatter — der Vermerk steht:

    jumpstart-checked: Vertraulichkeitspruefung Frage 4 durchgefuehrt, <Begruendung>

Danach ist die Datei dauerhaft still. Der Vermerk trifft genau den Moment, in dem die
Frage ohnehin ansteht: die Aufnahme des Dokuments.

Beim Arbeitgeberwechsel wird aus dem Klaerungsfall eine Sperre — ein Zeichen weniger:
aus '?Firma GmbH' wird 'Firma GmbH'. Die bestehenden Karrierestationen bekommen dann
'jumpstart-ignore' mit Begruendung.

## Escape-Hatch

Eine Zeile, die die Zeichenfolge `jumpstart-ignore` enthaelt, wird uebersprungen.
Sparsam verwenden und immer mit einer Begruendung daneben.

## Platzhalter

Die Eintraege der mitgelieferten Beispielliste sind dem Skript bekannt. Ueberlebt einer
davon in der echten Liste, ist das ein harter Fehler: Eine Liste aus Platzhaltern meldet
"Sauber", ohne einen einzigen echten Namen geprueft zu haben — falsche Sicherheit, die
von allein nie auffaellt.

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
CHECKED_TOKEN = "jumpstart-checked"

# Eintraege der mitgelieferten Beispielliste. Exakt, nicht heuristisch: So gibt es
# keine Fehlalarme auf echte Namen, und der gemeinte Fall wird sicher erkannt.
PLACEHOLDERS = {
    "beispielagentur gmbh",
    "beispielkunde ag",
    "beispielkunde gmbh",
    "beispielprodukt",
    "vorname nachname",
    "meingeraet",
    "meinbenutzername/mein-repo",
    "=xyz",
    "=abc",
    "re:prj-\\d{4}",
}

# workspace/ ist die operative Schicht: Klarnamen und Zahlen sind dort ausdruecklich
# erlaubt, und sie wird nie versioniert. Wuerde sie mitgeprueft, blockierte jede
# normale Meeting-Notiz das Sichern. _zu-loeschen/ ist der Ausgangskorb: Claude kann
# in verbundenen Ordnern nicht loeschen, nur verschieben — Verschobenes darf die
# naechste Sicherung nicht blockieren.
SKIP_DIRS = {".git", ".github", ".obsidian", "workspace", "_zu-loeschen",
             "node_modules", "__pycache__", ".venv"}
SKIP_FILES = {"privacy-entities.txt", "check_privacy.py"}
TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml", ".json", ".py", ".sh", ".toml", ".cfg", ""}

# Generische Muster — greifen auch ohne Entitaetenliste. Nie Klaerungsfaelle.
GENERIC = [
    ("Mailadresse", re.compile(r"\b[\w.+-]+@[\w-]+\.[A-Za-z]{2,}\b"), False),
    ("Lokaler Benutzerpfad", re.compile(r"(/Users/|/home/|[A-Za-z]:[\\\\/]+Users[\\\\/]+)[A-Za-z0-9._-]+"), False),
    ("Betrag mit Waehrung", re.compile(r"(\d[\d.,]*\s?(?:€|EUR|\$|USD|CHF)|(?:€|EUR|\$|USD|CHF)\s?\d[\d.,]*)"), False),
    ("IBAN", re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{10,30}\b"), False),
    ("Telefonnummer", re.compile(r"(?<![\w.-])\+\d{2}[\s/-]?\(?\d{2,5}\)?[\s/-]?\d{3,}[\s\d/-]*"), False),
    ("Moegliches Token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{16,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})\b"), False),
]


def flexible(term):
    """Leerzeichen im Suchbegriff auch als Bindestrich oder Unterstrich zulassen.

    Grund: Dateinamen sind kebab-case. 'Musterkunde AG' muss auch in
    'musterkunde-ag-analyse.md' anschlagen, sonst rutscht ein Name ueber den
    Dateinamen durch.
    """
    return r"[\s_-]+".join(re.escape(part) for part in term.split())


def compile_entry(line, klaerung):
    """Eine Listenzeile (ohne '?') in (Label, Regex, Klaerung) uebersetzen."""
    art = "Klaerung" if klaerung else "Entitaet"
    if line.startswith("re:"):
        return (f"{'Klaerungsregel' if klaerung else 'Regel'} {line[3:]}",
                re.compile(line[3:]), klaerung)
    if line.startswith("="):
        term = line[1:]
        return (f"{art} {term}",
                re.compile(r"(?<!\w)" + flexible(term) + r"(?!\w)"), klaerung)
    return (f"{art} {line}",
            re.compile(r"(?<!\w)" + flexible(line) + r"(?!\w)", re.IGNORECASE), klaerung)


def load_entities():
    """Gibt (Liste von (Label, Regex, Klaerung), Fehlertext, Hinweistext) zurueck.

    Fehlt die Liste oder ist sie leer, ist das ein HARTER Fehler und kein Hinweis:
    Das Skript wuerde sonst "Sauber" melden, obwohl es keinen einzigen eigenen Namen
    kennt — falsche Sicherheit genau dort, wo Schutz gebraucht wird. Besonders auf
    einem zweiten Geraet, wo die Liste per .gitignore systematisch fehlt.

    Ueberlebende Platzhalter aus der Beispielliste sind ebenfalls ein harter Fehler,
    aus demselben Grund: Sie zaehlen als Eintraege, schuetzen aber nichts.

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
    platzhalter = []
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
            if line.lower() in PLACEHOLDERS:
                platzhalter.append(line)
                continue
            klaerung = line.startswith("?")
            if klaerung:
                line = line[1:].strip()
                if not line:
                    continue
                if line.lower() in PLACEHOLDERS:
                    platzhalter.append("?" + line)
                    continue
            entries.append(compile_entry(line, klaerung))

    if platzhalter:
        return [], (
            f"{ENTITY_FILE} enthaelt noch Platzhalter aus der Beispielliste: "
            + ", ".join(repr(p) for p in platzhalter)
            + ". Diese Eintraege schuetzen nichts, zaehlen aber als Eintraege — die "
            "Meldung 'Sauber' waere wertlos. Durch echte Namen ersetzen oder streichen."
        ), None

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


def index_content(path):
    """Inhalt aus dem Git-Index lesen — nicht vom Datentraeger.

    Der Unterschied ist sicherheitsrelevant: Wird eine Datei mit einem
    schuetzenswerten Namen gestaged und danach im Arbeitsverzeichnis bereinigt,
    pruefte die alte Fassung die bereinigte Version und liess die unbereinigte
    committen. Genau der Pfad, den der Hook absichern soll.
    """
    try:
        out = subprocess.run(["git", "show", f":{path}"],
                             capture_output=True, check=True)
        return out.stdout.decode("utf-8", errors="replace")
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def scan(paths, entities, from_index=False):
    """Gibt (Treffer, Klaerungsfaelle) zurueck.

    Klaerungsfaelle werden hoechstens EINMAL pro Datei gemeldet und verschwinden
    ganz, sobald die Datei den Vermerk CHECKED_TOKEN traegt. Sonst feuerte die
    Rueckfrage bei jeder Sicherung erneut und wuerde weggeklickt.
    """
    hits = []
    klaerungen = []
    checks = entities + GENERIC
    for path in paths:
        base = os.path.basename(path)
        if base in SKIP_FILES or not is_text(path):
            continue
        if not from_index and not os.path.isfile(path):
            continue
        if in_skipped_dir(path):
            continue

        if from_index:
            text = index_content(path)
            if text is None:
                print(f"HINWEIS  {path}: nicht aus dem Index lesbar.")
                continue
        else:
            try:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
            except OSError as exc:
                print(f"HINWEIS  {path}: nicht lesbar ({exc})")
                continue

        quittiert = CHECKED_TOKEN in text
        klaerung_gemeldet = False

        # Auch der Pfad selbst wird geprueft — ein Name im Dateinamen ist ein Treffer.
        for label, pattern, klaerung in checks:
            if not pattern.search(path):
                continue
            if klaerung:
                if not quittiert and not klaerung_gemeldet:
                    klaerungen.append((path, 0, label, path))
                    klaerung_gemeldet = True
            else:
                hits.append((path, 0, label, path))

        for number, line in enumerate(text.splitlines(), start=1):
            if IGNORE_TOKEN in line:
                continue
            for label, pattern, klaerung in checks:
                match = pattern.search(line)
                if not match:
                    continue
                snippet = match.group(0).strip()[:60]
                if klaerung:
                    if not quittiert and not klaerung_gemeldet:
                        klaerungen.append((path, number, label, snippet))
                        klaerung_gemeldet = True
                else:
                    hits.append((path, number, label, snippet))
    return hits, klaerungen


def stelle(path, number):
    return f"{path}:{number}" if number else f"{path} (Dateiname)"


def melden(eintraege, wort):
    gesehen = set()
    for path, number, label, snippet in eintraege:
        key = (path, number, label)
        if key in gesehen:
            continue
        gesehen.add(key)
        print(f"{wort}  {stelle(path, number)} — {label}: {snippet!r}")
    return gesehen


def main():
    args = set(sys.argv[1:])
    entities, fehler, note = load_entities()

    if "--list" in args:
        gesperrt = [e for e in entities if not e[2]]
        zu_klaeren = [e for e in entities if e[2]]
        print(f"{len(gesperrt)} sperrende(r) Eintrag/Eintraege aus {ENTITY_FILE}:")
        for label, _, _ in gesperrt:
            print(f"  {label}")
        print(f"{len(zu_klaeren)} Klaerungsfall/-faelle:")
        for label, _, _ in zu_klaeren:
            print(f"  {label}")
        print(f"{len(GENERIC)} generische Muster.")
        if fehler:
            print(f"FEHLER   {fehler}")
            sys.exit(1)
        sys.exit(0)

    if fehler:
        errors.append(fehler)
    if note:
        print(f"HINWEIS  {note}\n")

    paths = staged_files() if "--staged" in args else all_files()
    if not paths:
        print("Nichts zu pruefen.")
        sys.exit(0)

    staged = "--staged" in args
    if entities or not errors:
        hits, klaerungen = scan(paths, entities, from_index=staged)
    else:
        hits, klaerungen = [], []

    seen = melden(hits, "TREFFER")
    offen = melden(klaerungen, "KLAERUNG")

    for e in errors:
        print(f"FEHLER   {e}")

    print()
    if seen or offen or errors:
        if seen:
            print(f"Nicht freigegeben: {len(seen)} Treffer in {len(paths)} geprueften Datei(en).")
            print("Jeden Treffer entweder entfernen, abstrahieren oder bewusst mit")
            print(f"'{IGNORE_TOKEN}' und Begruendung freigeben.")
        if offen:
            print(f"Offene Klaerung: {len(offen)} Datei(en) mit Material aus einer Quelle,")
            print("die nicht gesperrt, aber pruefungsbeduerftig ist (Praefix '?').")
            print("Vertraulichkeitspruefung Frage 4 durchfuehren — interne Strategie,")
            print("Sprechregeln, Wettbewerbsbewertungen, Konditionen? Danach den Vermerk")
            print(f"'{CHECKED_TOKEN}: <Begruendung>' in die Datei setzen.")
        if errors:
            print("Die Datenschutzpruefung ist nicht einsatzbereit — siehe FEHLER oben.")
        sys.exit(1)
    print(f"Sauber. {len(paths)} Datei(en) geprueft, keine Treffer.")
    sys.exit(0)


if __name__ == "__main__":
    main()
