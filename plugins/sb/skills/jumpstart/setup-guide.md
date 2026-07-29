# SB Jumpstart — persönliche Wissensbasis mit Claude einrichten

> **Für dich als Leser:** Diese Datei ist eine Anleitung *an Claude*, kein Handbuch zum
> Durcharbeiten. So benutzt du sie:
>
> 1. Besorge dir einen Claude-Zugang. Empfohlen ist die Claude-Desktop-App, damit Claude
>    mit Ordnern auf deinem Rechner arbeiten kann.
> 2. Lege einen leeren Ordner namens **`Knowledge Hub`** an und verbinde ihn in einer
>    Claude-Session („Ordner hinzufügen"). Für große Original-Dateien kommt später ein
>    zweiter Ordner namens **`Knowledge Asset Library`** dazu — Claude richtet ihn mit dir
>    ein. Die Namen sind die Konvention dieser Anleitung; wer sie ändert, sollte sie
>    überall konsequent ändern.
> 3. Gib Claude diese Datei mit — zusammen mit `user-readme.md`, der Erklärung für dich
>    als Nutzer — und schreibe dazu: **„Richte mir nach dieser Anleitung mein Second Brain
>    ein."**
>
> Claude führt dich dann durch ein kurzes Interview und baut die Struktur mit dir zusammen
> auf. Du musst nichts vorab entscheiden — auch nicht, welche der drei Ausbaustufen zu dir
> passt. Das klärt Claude im Gespräch. Wenn du wissen willst, was die Stufen unterscheidet,
> steht das kurz und ohne Fachsprache in `docs/tracks.md`.

---

## An Claude: Auftrag

Du richtest für die Person, mit der du sprichst, eine persönliche Wissensbasis („Second
Brain") ein. Architektur und Regeln stehen in dieser Datei. Sie stammen aus einem
erprobten, produktiven Setup und sind bewusst allgemein gehalten — deine Aufgabe ist, sie
auf das Leben und die Arbeitsweise **dieser** Person zu übertragen, nicht sie stur zu
kopieren.

Grundhaltung:

* **Interview vor Struktur.** Lege nichts an, bevor du nicht verstanden hast, welche
  Lebens- und Arbeitsbereiche die Person dokumentieren will.
* **Vorschlag vor Ausführung.** Zeige jede geplante Struktur erst zur Freigabe, dann erst
  schreiben.
* **Klein anfangen.** Ein Second Brain wächst durch Benutzung, nicht durch leere
  Ordnergerüste. Lieber drei gefüllte Dokumente als dreißig leere.
* **Die Stufe nicht überschätzen.** Der häufigste Fehler beim Aufsetzen ist, jemandem
  Werkzeug zu geben, das er nicht bedienen will. Im Zweifel die kleinere Stufe wählen —
  aufsteigen ist jederzeit möglich, ein überfrachteter Start dagegen tötet die Nutzung.

## Die drei Ausbaustufen

Das Setup gibt es in drei Ausprägungen. Sie unterscheiden sich **nicht** im Wissensmodell
— Ordnerlogik, Typ-Vokabular, Extrakt-Regel und Versionierung sind in allen drei gleich.
Sie unterscheiden sich darin, **wie die Basis betrieben wird** und **wie Aktualisierungen
des Setups ankommen**.

**Stufe 1 — Lokal.** Der Hub ist ein normaler Ordner auf einem Rechner. Kein Git, kein
Cloud-Sync-Konflikt, keine Werkzeugkette. Versionierung läuft über das `version`-Feld und
`log.md`; die Mechanik ist identisch zu den größeren Stufen, nur ohne Werkzeug darunter.
Aktualisierungen holt der Upgrade-Skill selbst von der Adresse, die als `setup_source` im
Hub vermerkt ist; heruntergeladen werden muss nichts. Das ist der Standardweg für alle, die anfangen.

**Stufe 2 — Verteilt.** Der Hub wird ein eigenes Git-Repository, in der Regel bei GitHub.
Damit arbeitet die Person über mehrere Geräte hinweg an derselben Basis; das Remote ist
die verbindliche Fassung, lokale Kopien sind gleichberechtigte Klone. Dazu kommen die
Werkzeuge, die dieser Betrieb erzwingt: ein Commit-Ablauf mit Prüf-Gate, automatische
Vergabe der Versions-Tags, ein Abgleich des tatsächlichen Stands vor jedem Schreibzugriff.

**Stufe 3 — Mitlaufend.** Wie Stufe 2, zusätzlich ist das Jumpstart-Repository als
Plugin-Quelle eingebunden. Neue Fassungen der **Skills** kommen darüber an — aber nur die
Skills: Regeldateien und Prüfskripte im Hub der Person fasst kein Plugin-Update an, dafür
bleibt der Upgrade-Skill zuständig. Und die automatische Aktualisierung ist bei eigenen
Quellen standardmäßig ausgeschaltet; sie muss einmalig eingeschaltet werden.

**Wie du die Stufe bestimmst:** nicht durch Selbsteinschätzung der Person („bist du
fortgeschritten?"), sondern aus ihren Antworten in Phase 1. Die Ableitung steht dort.

Die gewählte Stufe wird im Hub festgehalten — im Frontmatter der Wurzel-`index.md` als
`setup_track` (`lokal`, `verteilt` oder `mitlaufend`), zusammen mit `setup_version`, der
Version dieses Setups. Beide Felder braucht der Upgrade-Skill später, um zu wissen, was er
anbieten darf. Sie stehen bewusst dort und nicht in einer eigenen Datei: Ein zweiter
Ablageort wäre ein zweiter Ort zum Vergessen.

## Die Architektur in einem Absatz

Das Setup besteht aus **zwei Ablagen und drei Schichten**. Ablage eins ist der **Hub**
(Ordnername: `Knowledge Hub`): ein Ordner aus reinen Markdown-Dateien — hier liegt das
destillierte, wiederverwendbare Wissen. Ablage zwei ist die **Asset Library** (Ordnername:
`Knowledge Asset Library`, lokal oder cloud-synchronisiert): der Ort für große
Originaldateien (Präsentationen, PDFs, Bilder), die ein Repository sprengen würden. Im Hub
gibt es drei Schichten: den **Wissensbestand** (versioniert, mit Metadaten, nur nach
Freigabe beschreibbar), den **Workspace** (operatives Tagesgeschäft, unversioniert, frei
beschreibbar) und die **Meta-Schicht** (die Regeln selbst: eine Bedienungsanleitung für
Claude, ein Konventionen-Dokument, ein Prüfskript, optional wiederverwendbare Routinen).
Wissen fließt in eine Richtung: Rohes entsteht im Workspace, wird in einem wöchentlichen
Review destilliert und wandert generalisiert in den Wissensbestand — Originaldateien
parallel in die Asset Library, verlinkt aus dem Hub.

## Warum diese Bauweise

* **Markdown statt Notiz-App:** offenes Format, keine Plattformbindung, jeder Editor und
  jede KI kann es lesen. Als Format-Standard bewährt sich das **Open Knowledge Format
  (OKF v0.1)** von Google Cloud — Markdown mit YAML-Frontmatter, ein einziges Pflichtfeld
  (`type`), reservierte Dateinamen `index.md` und `log.md`, ein Concept ist eine Datei,
  der Pfad ist die Identität. Optional, aber empfohlen: Es kostet fast nichts und hält die
  Basis maschinenlesbar und werkzeugneutral. Kanonische Quellen am Ende dieser Datei.
* **Trennung Hub / Asset Library:** Versionsverwaltung ist für Text gebaut, nicht für
  Multi-GB-Binärdateien. Originale bleiben in der Asset Library, der Hub hält den Extrakt
  plus Verweis. So bleibt die Basis klein und das Wissen trotzdem vollständig erreichbar.
* **Trennung Wissensbestand / Workspace:** Wer jede Meeting-Notiz sofort „ins Wissen"
  schreibt, bekommt ein Archiv statt einer Wissensbasis. Der Workspace darf schnell und
  unordentlich sein; der Wissensbestand bleibt kuratiert, weil nur Destilliertes und
  Freigegebenes hineinwandert.
* **Progressive Disclosure plus aktiver Abgleich:** Jeder Ordner hat eine `index.md` als
  Inhaltsverzeichnis; Claude navigiert darüber und lädt nur, was die Aufgabe braucht. Das
  allein reicht nicht — ab einer gewissen Größe verschwindet Wissen, das quer zur
  aktuellen Aufgabe liegt. Deshalb kommt ein mechanischer Bestandsabgleich dazu (Phase 3).
* **Ein Prüfskript statt Disziplin:** Regeln, die niemand prüft, verfallen. Das Setup
  bringt ein kleines Python-Skript mit, das die harten Regeln maschinell durchsetzt.

## Datenschutz — die Grundzusage

Dieses Setup verarbeitet berufliche Daten. Bei vielen Anwendern heißt das: Daten Dritter,
die vertraglich oder rechtlich geschützt sind. Drei Zusagen bilden die Grundlage und sind
nicht verhandelbar:

**Erstens: Der Jumpstart ist eine Einbahnstraße.** Es gibt keinen Rückkanal. Nichts aus der
Wissensbasis eines Anwenders erreicht den Urheber dieses Setups oder irgendeinen Dritten.
Das Setup meldet nichts, misst nichts, sendet nichts. Sag das der Person beim Aufsetzen
ausdrücklich — es ist die Aussage, die eine berechtigte Sorge tatsächlich ausräumt.

**Zweitens: Nichts verlässt den Rechner ohne ausdrückliche Zustimmung im Einzelfall.**
Diese Regel gehört als eigener Punkt in den Block „Nicht verhandelbar" der `CLAUDE.md` und
gilt auch für die unauffälligen Nebenwege: ein Beispiel in einem ausgehenden Text, ein
Auszug in einer Nachricht, ein Screenshot.

**Drittens: Die Stufenwahl ist eine Datenexport-Entscheidung.** Wer Stufe 2 oder 3 wählt,
schiebt seinen Wissensbestand auf einen fremden Server. Das muss als solches gesagt und
entschieden werden, nicht als Komfortfrage nebenbei. Die Ableitung in Phase 1.4 führt das
aus.

Was die Architektur dafür schon leistet: Der `workspace/` mit Klarnamen ist von der
Versionierung ausgenommen. Die Asset Library mit den Originalen liegt außerhalb des
Bestands. Die Extrakt-Regel entkernt, bevor etwas in den Bestand wandert. Und `check_privacy.py`
prüft mechanisch gegen eine lokale Liste eigener Namen — Kunden, Arbeitgeber, Personen,
Projektkennungen —, die selbst niemals eingecheckt wird.

**Was die Prüfung nicht leistet, und das gehört gesagt:** Ein Skript findet, was es kennt
und was eine Form hat. Es findet nicht die umschriebene Fallbeschreibung ohne Namen, die
trotzdem eindeutig zuzuordnen ist. Dagegen hilft nur eine Faustregel, die in jede
Freigabeentscheidung gehört: *Ergibt eine Passage ohne den konkreten Fall immer noch Sinn,
muss der konkrete Fall raus. Trägt sie ohne ihn nicht mehr, gehört sie gar nicht nach
draußen.*

Ein letzter Punkt der Ehrlichkeit: Wer mit einem KI-Assistenten arbeitet, verarbeitet seine
Daten bei einem Anbieter. Daran ändert dieses Setup nichts, und es soll das auch nicht
verschweigen. Sag es der Person einmal klar, statt es zu umgehen.

## Ablauf in Phasen

| Phase | Inhalt |
|-------|--------|
| 0 | Orientierung geben |
| 1 | Interview, inklusive Ableitung der Ausbaustufe |
| 2 | Grundgerüst anlegen (nach Freigabe) |
| 3 | `CLAUDE.md` schreiben |
| 4 | `conventions.md` und `okf-conformance.md` schreiben |
| 5 | Infodump: erste Befüllung mit Vorhandenem |
| 6 | Routinen etablieren |
| — | Abschluss |

---

## Phase 0 — Orientierung geben

### 0.1 Ablageort verifizieren — vor allem anderen

**Erster Schritt, ohne Ausnahme, noch vor der Orientierung.** Der Startprompt setzt voraus,
dass der richtige Ordner verbunden ist. Ist er es nicht, entsteht die Wissensbasis lautlos
am falschen Ort — im ungünstigsten Fall in einem fremden Repository, das versioniert und
gepusht wird. Das ist der wahrscheinlichste Bedienfehler beim Erstkontakt.

Liste die verbundenen Ordner auf und ordne jeden einer der drei Lagen zu:

* **Leerer Ordner** (oder nur `.DS_Store`, `.git` ohne Inhalt) → Kandidat für einen
  Neuaufbau.
* **Bestehende Wissensbasis** — erkennbar an einer Wurzel-`index.md` mit `setup_track` im
  Frontmatter → Kandidat für den Wiedereinstieg (siehe unten).
* **Etwas anderes** — ein Code-Repository, ein Dokumentenordner, das Jumpstart-Repository
  selbst → **niemals** Ziel eines Aufbaus.

Ist genau ein Kandidat vorhanden, nenne ihn und lass ihn bestätigen. Bei mehreren
Kandidaten frag, welcher gemeint ist. Trifft keine der ersten beiden Lagen zu, **halte an
und frag nach** — rate nicht, und lege unter keinen Umständen ungefragt los. Ein falsch
angelegter Bestand fällt oft erst auf, wenn er schon in einer fremden Historie steht.

Ist überhaupt kein passender Ordner verbunden, ist das kein Abbruch: Die Person sagt
einfach, welchen Ordner sie meint, und du forderst ihn an. Das geht in laufender Sitzung.

### 0.2 Orientierung

Die Datei `user-readme.md` liegt neben dieser Anleitung im
selben Ordner — lies sie und zeige der Person **zu
Beginn** deren Inhalt oder eine kurze Zusammenfassung mit Verweis auf die Datei, damit sie
versteht, was gleich entsteht. Viele Nutzer sind neu im Umgang mit einem Second Brain und
mit agentischer KI-Arbeit. Lege die Datei später in Phase 2 als `README.md` in die Wurzel
des Hub-Ordners, damit sie dauerhaft zum Nachlesen bereitliegt.

Fehlt die Datei, erzeuge eine gleichwertige README in einfacher, jargonfreier Sprache: Was
ist ein Second Brain, welche Bausteine hat dieses Setup (Hub, Asset Library, Workspace,
Regel-Dateien), welche Spielregeln gelten (Lesen frei, Schreiben nur mit Freigabe;
Versionierung; Vertraulichkeit), wie sieht der Alltag aus (normales Arbeiten, Sichern auf
Zuruf, Weekly Review). Passe die README nach dem Interview an das konkrete Setup an —
insbesondere an die gewählte Stufe: Ein Stufe-1-Nutzer soll nichts über Commits und Tags
lesen müssen.

Sag außerdem, wie lange das Ganze dauert: Interview und Grundgerüst rund eine halbe
Stunde, der Infodump so lange, wie die Person Material mitbringt. Wer das nicht weiß,
bricht in der Mitte ab.

**Und sag, dass Abbrechen erlaubt ist.** Das Setup läuft über mehrere Phasen; niemand muss
sie an einem Stück durchziehen. Beim Wiedereinstieg genügt „lass uns mein Setup
weiterbauen".

**Wiedereinstieg — was du dann tust:** Erst den vorhandenen Stand lesen, bevor du irgendetwas
anlegst. Woran du erkennst, wo ihr wart: Existiert der Ordner überhaupt schon? Steht eine
`CLAUDE.md` mit gefüllten Regeln oder noch mit Platzhaltern in `<spitzen Klammern>`? Trägt
die Wurzel-`index.md` bereits `setup_track` und `setup_version`? Gibt es fachliche Concepts
oder nur das Gerüst? Fass den erkannten Stand in zwei Sätzen zusammen, lass ihn bestätigen
und setz an der nächsten offenen Phase an. **Fang nicht von vorn an** — das ist der
sicherste Weg, jemanden endgültig zu verlieren.

## Phase 1 — Interview

Kläre im Gespräch die folgenden Punkte. Bündele sie, verhöre nicht. Biete Optionen mit
einer klaren Empfehlung an, statt offene Fragen zu stellen — die meisten Leute können auf
eine Empfehlung reagieren, aber keine Struktur aus dem Nichts entwerfen.

### 1.1 Lebensbereiche

Welche Hauptstränge soll die Basis haben? Bewährtes Muster: `professional/` (Beruf),
`personal/` (Privates, Interessen), `private-projects/` (eigene Vorhaben). Passe die
Stränge an die Person an — ein Studierender, eine Selbstständige und ein Angestellter
schneiden anders. Frage nach, was die Person tatsächlich dokumentieren *will*, nicht was
sie theoretisch könnte.

### 1.2 Beruflicher Kern

Was macht die Person? Daraus ergeben sich die Unterordner — etwa Stationen und Projekte,
wiederverwendbare Arbeitsergebnisse, gesammelte Studien. Diese Frage entscheidet später
auch, welche Routinen sinnvoll sind.

### 1.3 Vertraulichkeit

Arbeitet die Person mit Kunden-, Arbeitgeber- oder Personendaten, die nicht in versionierte
oder geteilte Dokumente gehören? Die Antwort bestimmt, wie streng die Extrakt-Regel
gefahren wird und wie ausführlich die Vertraulichkeits-Checkliste in `conventions.md`
ausfällt. Bei einem klaren Ja gehört zusätzlich in den Block „Nicht verhandelbar", dass
ausgehende Dokumente anonymisiert werden.

### 1.4 Ableitung der Ausbaustufe

Diese Frage entscheidet mehr als den Werkzeugkasten: **Ab Stufe 2 verlässt der
Wissensbestand den eigenen Rechner.** Behandle sie entsprechend — nicht als Komfortfrage,
sondern als bewusste Entscheidung darüber, wo die Daten dieser Person liegen.

Frage **nicht** „welche Stufe willst du". Frage nach der Situation und leite ab:

* **Arbeitest du an einem Gerät oder an mehreren?** Ein Gerät spricht für Stufe 1.
* **Nutzt du Git oder GitHub schon — beruflich oder privat?** Ein Nein ist kein Hindernis,
  aber ein deutliches Signal für Stufe 1.
* **Willst du die Verfahren automatisch nachgeliefert bekommen, statt sie selbst zu
  aktualisieren?** Ein Ja führt zu Stufe 3.

Und bei einem Ja aus Punkt 1.3 zusätzlich: **Dürfen die Daten, mit denen du arbeitest,
überhaupt auf einen fremden Server?** Wer mit Kundendaten arbeitet, hat dazu oft
vertragliche Bindungen — Geheimhaltungsvereinbarungen, Vereinbarungen zur
Auftragsverarbeitung, Vorgaben des Arbeitgebers. Weise darauf hin, empfehle bei Stufe 2 und
3 ausdrücklich ein privates Repository, und sag klar: Diese Anleitung kann auf die
Entscheidung hinweisen, sie aber nicht treffen und keine Rechtsberatung ersetzen. Im Zweifel
Stufe 1.

**Prüfe die Voraussetzungen, bevor die Stufe feststeht — nicht danach.** Frage konkret
nach und verlasse dich nicht auf Vermutungen:

* Für **Stufe 1**: nichts. Frag insbesondere **nicht** nach Python — die Prüfskripte laufen
  dort, wo du auf den Ordner zugreifst, nicht auf dem Rechner der Person. Probier sie
  einfach aus. Die Frage erzeugt sonst eine Hürde, die es gar nicht gibt, und liefert ein
  falsches Argument für die kleinere Stufe.
* Für **Stufe 2**: Gibt es einen GitHub-Account? Ist ein Git-Programm installiert
  (empfiehl **GitHub Desktop** namentlich — es bringt Git mit und ist auf Klicken ausgelegt)?
  **Ist Python 3 auf dem Gerät vorhanden?** Diese Frage ist hier berechtigt, anders als bei
  Stufe 1: Der `pre-commit`-Hook läuft auf dem Gerät der Person, nicht in deiner Umgebung.
  Ohne Interpreter blockiert er jeden Commit — bewusst, aber unerwartet.
* Für **Stufe 3**: zusätzlich die Bereitschaft, die Plugin-Quelle einzurichten.

Fehlt etwas, ist das **kein Fehler, sondern ein Argument für die kleinere Stufe**. Sag das
auch so. Wer auf Stufe 2 landet und drei Phasen später an einem fehlenden Werkzeug
hängenbleibt, bricht ab — und zwar endgültig.

Ableitungsregel: **Stufe 1 ist der Default.** Stufe 2 nur, wenn Mehrgeräte-Betrieb ein
echtes Bedürfnis ist *und* Git-Erfahrung vorhanden oder ausdrücklich gewünscht ist. Stufe 3
nur zusätzlich zu Stufe 2, und nur wenn die Person bereit ist, die Plugin-Quelle
einzurichten und die automatische Aktualisierung einzuschalten.

Sag der Person, was sie mit der Wahl bekommt und was sie sich spart — und dass ein
Aufstieg jederzeit geht, ein Abstieg auch. Notiere die nicht gewählten Stufen als offene
Ausbaustufe in `CLAUDE.md` (Phase 3), damit sie nicht vergessen werden.

**Bei Stufe 1 gilt zusätzlich:** Die Versionierung läuft trotzdem von Anfang an über
`version` und `log.md`. Nicht weglassen mit dem Argument, es gebe ja kein Git — die
Mechanik ist der Punkt, nicht das Werkzeug. Wer später aufsteigt, hat dann eine Historie,
die sich sauber übernehmen lässt.

### 1.5 Betriebsort der Ordner

Wo soll der Hub liegen, wo die Asset Library?

Für die **Asset Library** ist ein Cloud-Ordner (iCloud, OneDrive, Google Drive, Dropbox)
ideal, ein einfacher lokaler Ordner außerhalb des Hubs reicht zum Start aber völlig aus.
Wichtig ist nur die Trennung vom Hub. Weise darauf hin, dass Cloud-Sync oder ein Backup
später nachgezogen werden sollte, damit die Originale nicht an einem einzelnen Rechner
hängen — als Empfehlung, nicht als Muss.

Für den **Hub** gilt bei Stufe 2 und 3 eine harte Regel: **nicht in einen
Cloud-Sync-Ordner legen.** Zwei Synchronisationssysteme auf demselben Verzeichnis erzeugen
Konfliktkopien und beschädigen die Git-Verwaltungsdaten; das Remote-Repository *ist*
bereits die Cloud-Schicht. Der Hub gehört auf die interne Platte. Bei Stufe 1 ist ein
Cloud-Ordner unproblematisch und sogar sinnvoll, weil er das Backup ersetzt.

### 1.6 Sprache und Ton

In welcher Sprache und welchem Register soll Claude mit der Person arbeiten? Gibt es
persönliche No-Gos — Formulierungen, Formatierungen, Themen —, die von Anfang an in die
Zusammenarbeitsregeln gehören? Frage konkret nach: „Was nervt dich an KI-Antworten?"
liefert bessere Regeln als „welchen Ton möchtest du?".

**Das ist der Rohstoff für das Zusammenarbeits-Profil**, das in Phase 2 als Datei angelegt
und in Phase 3 gefüllt wird. Notiere die Antworten wörtlich genug, dass daraus Regeln
werden können — „keine Aufzählungen in Fließtexten" ist eine Regel, „lieber sachlich" nicht.

### 1.7 Skill-Bedarf (Kandidaten sammeln, nichts festzurren)

Gibt es wiederkehrende Aufgaben, bei denen Claude künftig nach festem Ablauf unterstützen
soll — Texte in eigenem Stil, Berichte, Dokument-Aufnahme, Recherche-Routinen? Sammle erste
Kandidaten. Die Liste wird in Phase 5 mit dem verfeinert, was der Infodump an
wiederkehrenden Mustern zeigt, und in Phase 6 in konkrete Skills übersetzt. Entschieden
wird hier nichts.

### Abschluss von Phase 1

Fasse zusammen, bevor du irgendetwas anlegst: gewählte Stufe mit Begründung, geplante
Ordnerstränge, Ablageorte, die wichtigsten persönlichen Regeln, die Skill-Kandidaten. Dann
Freigabe einholen. Erst danach Phase 2.

---

## Phase 2 — Grundgerüst anlegen (nach Freigabe)

Datei- und Ordnernamen in **englischem kebab-case** (klein, Bindestriche, portabel),
Inhalte in der Sprache der Person. Der Anzeigename steht im Frontmatter-Feld `title`, nicht
im Dateinamen.

### Der Hub

```
Knowledge Hub/
├── README.md              ← Erklärung für die Person (aus Phase 0)
├── CLAUDE.md              ← Bedienungsanleitung für Claude (Phase 3)
├── conventions.md         ← Regelwerk der Basis (Phase 4)
├── okf-conformance.md     ← Format-Regeln und bewusste Abweichungen (Phase 4)
├── index.md               ← Wurzel-Inhaltsverzeichnis, trägt version/setup_version/setup_track
├── log.md                 ← Änderungshistorie (neueste zuerst)
├── _meta/
│   ├── check_okf.py       ← Formatprüfung
│   ├── check_privacy.py   ← Datenschutzprüfung
│   └── privacy-entities.txt ← eigene Namen, NIEMALS versioniert
├── <bereich-1>/           ← z. B. professional/, mit eigener index.md
│   └── profile/
│       └── zusammenarbeit.md  ← Zusammenarbeits-Profil, Pflicht (Phase 3)
├── <bereich-2>/           ← z. B. personal/
├── _zu-loeschen/          ← Ausgangskorb, nicht versioniert (Claude kann nicht löschen)
└── workspace/             ← operative Schicht, nicht versioniert
    ├── README.md          ← Workspace-Regeln
    └── TASKS.md           ← offene Punkte, Zusagen, Wiedervorlagen
```

**`zusammenarbeit.md` ist keine Kür.** Die `CLAUDE.md` macht es zur Pflichtlektüre vor der
ersten inhaltlichen Aktion, und die Lern-Mechanik „Selbstlernen nach Korrektur" schreibt
dorthin. Ohne die Datei zeigen beide ins Leere, und zwar unbemerkt. Lege sie in Phase 2 leer
mit Frontmatter an (`type: Profile`, `title: Zusammenarbeit mit Claude`, `tags: [profil,
zusammenarbeit]`) und fülle sie in Phase 3 aus den Antworten von Interview 1.6. Der Pfad
gehört namentlich in die `CLAUDE.md` — nicht als „sobald vorhanden".

**Anlegen, was gefüllt wird — nicht mehr.** Ein Strang entsteht erst, wenn im Interview ein
konkreter Inhalt dafür genannt wurde. Wer nur beruflich dokumentieren will, bekommt keinen
leeren `personal/`-Strang mit Platzhalter-Index; das ist genau der Fehler, vor dem die
Grundhaltung warnt („lieber drei gefüllte Dokumente als dreißig leere"). Nicht gewählte
Stränge kommen als Zeile in den Abschnitt „Ausbaustufen" der `CLAUDE.md` und lassen sich
jederzeit nachziehen.

Ab **Stufe 2** kommt hinzu: `git init -b main` — **der Hauptbranch muss `main` heißen**,
weil der mitgelieferte Auto-Tag-Workflow darauf horcht; ältere Git-Fassungen legen sonst
`master` an, und die Tag-Vergabe läuft dann stillschweigend nie. Dazu eine `.gitignore`
(mindestens `workspace/`, `_meta/privacy-entities.txt`, Betriebssystem-Müll, Editor-Ordner)
und `.github/workflows/auto-tag.yml`. Erster Commit **ohne** Tag: Das Tag `v1.0.0` setzt die
Action beim ersten Push. Lokal wird nie getaggt.

Bei **Stufe 1** entfällt das ersatzlos. `version` und `log.md` werden trotzdem von Anfang
an geführt.

Die **Entitätenliste** `_meta/privacy-entities.txt` wird beim Aufsetzen gemeinsam mit der
Person befüllt: **Kunden, Mandate, Produktnamen, Personen Dritter, Projektkennungen** und
technische Bezeichner wie Gerätenamen. Sie steht bei Stufe 2 und 3 in der `.gitignore` und
darf unter keinen Umständen versioniert werden — sie ist selbst genau das Leck, das sie
verhindern soll.

Drei Dinge dazu sind nicht verhandelbar:

**Die eigene Person gehört nicht hinein.** Ihr Name steht zwangsläufig in der eigenen
Wissensbasis — im Profil, in den Karrierestationen, im Kopf der `CLAUDE.md`. Als Sperre
schlüge er bei jeder Sicherung gegen Dateien an, die das Setup selbst angelegt hat. Er ist
Karrierekontext, kein Schutzgegenstand. Dasselbe gilt für die Adresse der eigenen
Wissensbasis: Sie steht als `setup_source` im Kopf und gehört deshalb nicht auf die Liste.

**Der eigene Arbeitgeber gehört als Klärungsfall hinein, mit vorangestelltem `?`.** Als
Sperre erzeugte er dasselbe Problem wie der eigene Name. Sein Material ist aber regelmäßig
das schutzbedürftigste im ganzen Bestand: interne Strategie, Sprechregeln,
Wettbewerbsbewertungen, Konditionen — alles Treffer auf Prüffrage 4 der Extrakt-Checkliste.
Ohne Eintrag kann die Prüfung dort strukturell nie anschlagen, und der Schutz für die größte
zusammenhängende Materialmenge hinge allein an Disziplin. Das `?` löst deshalb **einmal pro
Datei** eine Rückfrage aus statt einer Sperre; beantwortet wird sie mit dem Vermerk
`jumpstart-checked: <Begründung>` in der Datei. Erkläre der Person diesen einen Mechanismus
ausdrücklich — er ist der einzige, der von ihr eine Antwort verlangt.

**Platzhalter sind ein Fehler, kein Startzustand.** Die Beispieleinträge der mitgelieferten
Vorlage kennt das Prüfskript; überlebt einer davon, bricht die Prüfung ab. Der Grund: Eine
Liste aus Platzhaltern meldet „Sauber", ohne einen einzigen echten Namen geprüft zu haben.
Fülle die Liste deshalb mit echten Einträgen, **bevor** das erste echte Material aufgenommen
wird — nicht danach. Fällt der Person beim Aufsetzen nichts ein, ist das kein Grund
weiterzugehen: Frag nach den letzten drei Projekten und den letzten drei Ansprechpartnern.
Die Liste wächst danach im Weekly Review mit.

Beide Prüfskripte gehören **in allen drei Stufen** dazu. Erwähne es beim
Anlegen nur beiläufig — ein Anfänger muss es nicht verstehen. Scharf geschaltet wird es
erst in Phase 6. **Die Regel ist in allen Stufen dieselbe:** Schlägt eine Prüfung hart an,
wird nicht gesichert. Was sich unterscheidet, ist nur der Zeitpunkt — bei Stufe 2 und 3
zusätzlich automatisch vor jedem Commit. Die Datenschutzprüfung dagegen erklärst du kurz — sie ist der einzige Teil
des Setups, dessen Zweck jemand verstehen muss, damit er ihn ernst nimmt.

### Ausbaustufe 2 einrichten (nur Stufe 2 und 3)

Der Teil, an dem es ohne Anleitung hakt. Geh ihn mit der Person Schritt für Schritt durch
und mach jeden Schritt sichtbar — sie soll wissen, was gerade passiert.

**1. Repository auf GitHub anlegen.** Auf github.com, Schaltfläche „New repository".
**Sichtbarkeit auf „Private" stellen** — das ist bei beruflichen Inhalten die Vorgabe, nicht
die Option. Alle Initialisierungs-Häkchen (README, .gitignore, Lizenz) **abwählen**: Der
Ordner ist schon gefüllt, ein zweiter Startpunkt erzeugt sonst einen Konflikt beim ersten
Verbinden. Sag dazu, dass die Sichtbarkeit später nur mit Aufwand zu ändern ist.

**2. Lokalen Ordner zum Repository machen.** `git init -b main` im Hub-Ordner. Der
Branchname `main` ist nicht Geschmackssache: Der mitgelieferte Auto-Tag-Workflow horcht
darauf, und mit `master` läuft die Tag-Vergabe stillschweigend nie.

**3. Verknüpfen und erstmals hochladen.** In GitHub Desktop: „Add existing repository",
dann „Publish repository" — dabei erneut prüfen, dass „Keep this code private" gesetzt ist.
Wer die Kommandozeile nutzt, nimmt die Befehle, die GitHub nach dem Anlegen anzeigt.

**4. Nachsehen, ob es angekommen ist.** Repository im Browser öffnen: Sind die Dateien da,
steht der Branch auf `main`, hat die Action gelaufen und das Tag `v1.0.0` gesetzt? Diese
Kontrolle gehört dazu — eine Automatik, die man nie geprüft hat, ist eine Annahme.

**5. Berechtigungen der Action prüfen.** Unter Settings → Actions → General muss „Read and
write permissions" gesetzt sein, sonst kann der Workflow das Tag nicht schreiben. Läuft das
Tag in Schritt 4 nicht durch, ist das die erste Stelle zum Nachsehen.

**6. Sperre vor dem Speichern anbieten** (siehe Phase 6). Freiwillig, aber erklärt.

### Das zweite Gerät

Eine eigene Checkliste, weil hier vier Dinge fehlen, die man leicht übersieht:

1. **Repository klonen**, nicht kopieren.
2. **`core.hooksPath` erneut setzen** — die Einstellung liegt in der lokalen Konfiguration
   und wandert nicht mit dem Klon.
3. **Entitätenliste neu anlegen.** Sie ist von der Versionierung ausgenommen und ist auf dem
   zweiten Gerät deshalb **nicht vorhanden**. Ohne sie prüft die Datenschutzprüfung nur
   generische Muster — sie meldet das inzwischen als Fehler, aber die Person muss wissen,
   warum. **Nicht per Mail oder Cloud übertragen**: Das wäre genau der Export, den die Liste
   verhindern soll. Neu tippen, es sind ein paar Zeilen.
4. **Python 3 sicherstellen**, sonst laufen die Prüfungen dort nicht.

Sag außerdem zwei Dinge deutlich, die sonst später für Verwirrung sorgen: Der `workspace/`
wird **nicht** synchronisiert und sieht auf jedem Gerät anders aus. Und wenn die Asset
Library nicht in einer Cloud liegt, sind auf dem zweiten Gerät alle Verweise auf Originale
tot — bei Mehrgeräte-Betrieb ist Cloud-Sync der Library daher keine Empfehlung mehr,
sondern Voraussetzung.

### Wenn zwei Geräte sich in die Quere kommen

Das passiert, und zwar nicht ausnahmsweise: Jede Sicherung ändert `index.md` und `log.md` an
derselben Stelle. Wer auf zwei Geräten arbeitet, ohne vorher zu holen, bekommt genau dort
einen Konflikt.

**Vorbeugen:** vor der Arbeit holen, nach dem Sichern hochladen. Das ist die ganze Regel.

**Wenn es doch passiert**, gibt es zwei Fälle, und der häufigere ist nicht der
offensichtliche.

*Fall eins, der Regelfall:* Beide Geräte haben auf **dieselbe** Versionsnummer erhöht. Dann
gibt es in `index.md` gar keinen Konflikt — beide schrieben dasselbe —, und der Konflikt
sitzt allein in `log.md` innerhalb einer Überschrift. Auflösung: beide Aufzählungspunkte
unter der einen Überschrift zusammenführen, Konfliktmarker entfernen, dann **eine Version
überspringen und neu sichern**, damit die übersprungene Nummer nicht auf einem Stand liegt,
den nur ein Gerät kennt.

*Fall zwei:* Unterschiedliche Versionsnummern. Dann die **höhere** behalten und beide
Log-Blöcke übereinander stehen lassen, neuester oben.

In beiden Fällen: Die Konfliktmarker `<<<<<<<`, `=======` und `>>>>>>>` müssen vollständig
verschwinden — das Prüfskript wertet stehengebliebene Marker als harten Verstoß. Wer nicht
mit der Kommandozeile arbeitet, löst das im Git-Programm über „Resolve conflicts" oder lässt
Claude die Datei aufräumen.

**Der Sonderfall, den kein Skript findet:** Haben beide Geräte unabhängig auf dieselbe
Versionsnummer erhöht, ist nach dem Zusammenführen alles lokal stimmig — aber das Tag zeigt
auf den Stand des ersten Geräts. Dann eine Version überspringen und neu sichern. Weise die
Person einmal darauf hin; sie muss es nicht können, aber sie soll es wiedererkennen.

### Die Wurzel-`index.md`

Ihr Frontmatter trägt vier Felder, die zusammengehören:

```yaml
---
okf_version: "0.1"
version: "1.0.0"          # Reife der eigenen Wissensbasis
setup_version: "0.3.0"    # Version dieses Setups, aus der die Basis entstand
setup_source: "https://github.com/dutch-vdl/sb-jumpstart"   # woher Aktualisierungen kommen
setup_track: "lokal"      # lokal | verteilt | mitlaufend
title: Knowledge Hub
description: …
timestamp: …
---
```

`version` und `setup_version` sind zwei verschiedene Dinge und werden getrennt geführt: Die
eine misst, wie weit die eigene Wissensbasis ist, die andere, auf welchem Stand des
Bauplans sie steht. Der Body der Datei ist ein knappes Inhaltsverzeichnis der Hauptstränge
mit je einem Satz.

### Die Asset Library

Separater Ordner namens `Knowledge Asset Library`, in jedem Fall **außerhalb** des
Hub-Ordners — sonst landen Binärdateien doch im Repository. Bewährtes Schema:

* Pro Arbeitgeber, Station oder Großprojekt ein Ordner in Großbuchstaben-Kürzel.
* Übergreifende Wissenskategorien als Buckets in Kleinschreibung: `frameworks/`,
  `learning/`, `insights/`, `personal/`.
* `TBD/` für noch Unsortiertes. Der Ordner ist kein Makel, sondern ein Ventil — ohne ihn
  bleibt Material außerhalb der Basis liegen.

Die interne Gliederung spiegelt grob den Hub, damit man sich nicht zweimal orientieren
muss. Verweise aus dem Hub auf Originale nutzen den Pfad relativ zur Library-Wurzel mit
Präfix `asset:/…` — so bleiben sie stabil, egal wo die Library liegt.

### Der Workspace

`workspace/README.md` hält die Sonderregeln fest: Klarnamen und Zahlen sind hier erlaubt,
kein Frontmatter-Zwang, freies Schreiben ohne Freigabe-Pflicht. Hier zählt
Arbeitsgeschwindigkeit. Aber: **Nichts verlässt den Workspace unanonymisiert**, und der
Workspace ist **Arbeitsstand, kein Archiv** — Verallgemeinerbares wird im Review destilliert
und in den Wissensbestand gehoben, Erledigtes verschwindet.

**Löschen kann Claude nicht.** In verbundenen Ordnern sind `rm` und `rmdir` nicht erlaubt,
nur Verschieben. „Erledigtes raus" heißt deshalb konkret: nach `_zu-loeschen/` in der Wurzel
verschieben — der Ordner ist von beiden Prüfungen und von der Versionierung ausgenommen —
und **berichten, was dorthin gewandert ist**. Das endgültige Löschen macht die Person selbst
im Dateimanager. Behaupte nie, aufgeräumt zu haben, wenn nur verschoben wurde.

Bewährte Unterstruktur: `TASKS.md`, ein Notizordner für Termine
(`meetings/JJJJ-MM-TT-thema.md`), je nach Beruf Projekt- oder Vorgangsdateien. Vorlagen
bekommen einen Unterstrich als Präfix (`_vorlage-meeting.md`), damit sie in der
Sortierung oben stehen und nicht mit echten Vorgängen verwechselt werden.

**Bei Stufe 2 und 3 wichtig:** Der Workspace ist gitignored und existiert damit auf jedem
Gerät verschieden. Das ist gewollt, muss der Person aber gesagt werden — sonst sucht sie
ihre Notizen auf dem zweiten Rechner.

---

## Phase 3 — `CLAUDE.md` schreiben

`CLAUDE.md` ist das wichtigste Dokument des Setups: die Datei, die Claude in jeder
künftigen Session zuerst liest. Erzeuge sie aus dem Interview. Halte sie **kurz** — sie
wird jedes Mal gelesen. Alles, was Nachschlagewissen ist, gehört in `conventions.md`.

### Block „Nicht verhandelbar"

An die Spitze, mit dem ausdrücklichen Vermerk, dass er im Konfliktfall gewinnt. Diese fünf
sind der Kern; ergänze die persönlichen Regeln aus dem Interview:

* **Kontext vor Handlung.** Vor der ersten inhaltlichen Aktion einer Session
  `conventions.md` **und** das Zusammenarbeits-Profil lesen. Beide werden beim Aufsetzen
  angelegt; kein „sobald vorhanden" — ein Vorbehalt an dieser Stelle macht die Lücke
  unsichtbar, falls das Profil doch fehlt.
* **Vorschlag vor großer Aktion.** Schreibzugriffe auf den Wissensbestand, Massen- oder
  Strukturänderungen erst als Vorschlag vorlegen; zurückgeschrieben wird nur mit
  ausdrücklicher Freigabe.
* **Vertraulichkeit.** In ausgehenden Dokumenten sensible Namen und Zahlen anonymisieren;
  Klarnamen bleiben in den privaten Ablagen.
* **Fakt und Einschätzung trennen.** Bei Unsicherheit über Fakten zur Person nachfragen
  statt raten.
* **Versionierung.** Die Versionsnummer wird nur beim Sichern erhöht, nie zwischendurch.

### Betriebsanleitung

Was bei Session-Start zu lesen ist (Wurzel-`index.md`, dann Navigation über die
Ordner-Indizes statt Volltext-Laden). Dass Lesen keine Rückfrage erfordert, Schreiben in
den Wissensbestand immer. Die Sonderregeln des `workspace/`. Und der Abschnitt
**„Anreichern"**: Claude schreibt nie automatisch zurück, sondern fragt aktiv, wenn
dauerhaft dokumentierenswertes Wissen entstanden ist. Benenne die typischen Auslöser —
neues Projekt wird ein `Deliverable`, neue Methode ein `Framework`, wiederverwendbarer
Guide ein `Learning`, neue Erkenntnis über die Person ein Profil-Update, relevante externe
Studie ein `Insight`.

### Arbeitsregeln, die sich in der Praxis als nötig erwiesen haben

Diese fünf sind der Unterschied zwischen einer Wissensbasis, die genutzt wird, und einer,
die nur wächst. Nimm sie auf, auch wenn sie beim Start übertrieben wirken:

**Bestandsabgleich vor nicht-trivialen Aufgaben.** Bevor Claude eine substanzielle Aufgabe
beginnt, prüft es **mechanisch**, ob die Basis dazu schon etwas hergibt: erst eine Suche
über Dateinamen und Titel der Wissensordner — billig, nur Namen —, dann gezielt die ein bis
drei einschlägigen Treffer vollständig lesen. Der Befund wird **sichtbar gemacht**: Auch
ein „nichts Einschlägiges gefunden" ist eine bewusste Aussage und keine Auslassung. Grund:
Navigation über Indizes lädt, was zur Aufgabe passt — sie findet nicht, was quer dazu
liegt. Der Aufwand skaliert mit der Trefferzahl, nicht mit der Größe der Basis.

**Konventions-Selbstcheck vor jeder Vorlage.** Neue Artefakte hält Claude unaufgefordert
gegen `conventions.md` und legt Abweichungen als Entscheidungsliste vor, statt sie
stillschweigend zu übergehen.

**Machbarkeit vor Bau.** Bei technischen Lösungen erst Dokumentation und Machbarkeit
klären, dann bauen. Die umgekehrte Reihenfolge kostet regelmäßig mehrere Runden Nacharbeit.

**Entscheidungsformate.** Entscheidungsfragen werden gebündelt als nummerierte oder
gebuchstabte Optionen mit klarer Empfehlung vorgelegt, damit Kurzfreigaben möglich sind
(„ja", „B", „1+3"). Einzelne Rückfragen im Minutentakt sind der schnellste Weg, ein Setup
unbenutzbar zu machen.

**Abgleich des tatsächlichen Stands (nur Stufe 2 und 3).** Vor Aussagen über den Stand der
Basis und vor jedem Schreibzugriff den realen Repository-Stand frisch einlesen — Version,
letzte Commits, betroffene Dateien — statt dem Session-Kontext zu trauen. Sobald jemand mit
mehreren Sessions oder mehreren Geräten arbeitet, ist das keine Kür.

### Lern-Mechaniken

Das System soll sich aus der Nutzung heraus verbessern. Verankere ausdrücklich:

* **Selbstlernen nach Korrektur.** Korrigiert die Person Claude — Stil, Vorgehen, Fakten —,
  wird die zugrunde liegende Regel dauerhaft festgehalten: Stil- und Verhaltensregeln im
  Zusammenarbeits-Dokument, Inhaltliches im passenden Bereich. Eine zweimal angemahnte
  Regel ist keine Präferenz mehr, sondern Regelwerk.
* **Muster-Ernte.** Wiederkehrende Entscheidungen, Formulierungs-Vorlieben und
  Ablauf-Muster werden als Regel-Kandidaten vorgemerkt und im Weekly Review gebündelt zur
  Aufnahme vorgeschlagen — nicht sofort einzeln nachgefragt, sonst nervt das System.
* **Skill-Reife.** Wiederholt sich ein Ablauf zum dritten Mal, schlägt Claude vor, ihn als
  Skill zu formalisieren.

### Abschnitt „Ausbaustufen"

Was beim Setup bewusst weggelassen wurde: die nicht gewählten Stufen aus Phase 1, ein noch
fehlendes Backup der Asset Library, aufgeschobene Skill-Kandidaten. Claude erinnert von
selbst daran — spätestens, wenn die Basis spürbar gewachsen ist (etwa ab zwanzig Concepts
oder nach einigen Wochen Nutzung), im Rahmen des Weekly Review. Ton: Empfehlung zur
Datensicherheit, kein Druck.

---

## Phase 4 — `conventions.md` und `okf-conformance.md` schreiben

Zwei Dateien mit klarer Arbeitsteilung: `okf-conformance.md` hält die **externen**
Format-Regeln fest und dokumentiert bewusste Abweichungen davon; `conventions.md` enthält
die **eigenen** Festlegungen. Die Trennung macht Standardtreue prüfbar statt behauptet.

### Typ-Vokabular

Jedes Wissensdokument („Concept") trägt im Frontmatter ein `type`-Feld. Starte klein und
erweitere, was die Person braucht:

| type | Verwendung | Haltbarkeit |
|------|------------|-------------|
| `Framework` | Erklärt eine Strategie oder Vorgehensweise. | Langlebig, altert kaum |
| `Learning` | Guide zu einem Thema. | Mittel, kann veralten |
| `Insight` | Externe Studien, Marktdaten, Reports. | Kurz, veraltet schnell |
| `Deliverable` | Markdown-Extrakt eines Originals aus der Asset Library, mit Verweis. | — |
| `Project` | Ein eigenes Vorhaben. | — |
| `Profile` | Verdichtetes Profil — **zwei Dateien**: Personenprofil (Kompetenzen, Domänen) und Zusammenarbeits-Profil (`profile/zusammenarbeit.md`). | — |
| `Person` | Eine relevante Person. | — |
| `Reference` | Meta- oder Nachschlage-Dokument. | — |

Neue Typen werden hier ergänzt, damit sie konsistent bleiben. Ein Typ, der nur einmal
vorkommt, ist meist keiner.

### Haltbarkeits-Hierarchie und Haltbarkeitsvermerk

**Frameworks > Learning > Insights.** Die Pflege-Kadenz läuft umgekehrt: Insights werden am
häufigsten geprüft und ausgemistet, Frameworks am seltensten angefasst. Alle drei tragen
ein `timestamp`.

Mischt ein Concept einen dauerhaften Methodenkern mit verfallenden Bestandteilen — konkrete
Zahlen, Marktstände, Details einer Benutzeroberfläche —, bekommt es einen Abschnitt
`# Haltbarkeit / Stand`, der beides trennt: den **stabilen Kern**, der übertragbar bleibt,
und den **verfallenden Anteil**, der mit Datum veraltet. Das schärft die Aktualitätsprüfung
im Weekly Review: Geprüft wird gezielt der verfallende Teil, der stabile Kern bleibt
unangetastet. Empfohlen für `Insight`, optional für `Learning`.

### Frontmatter-Standard

Pflicht ist `type`. Empfohlen: `title`, `description`, `tags`, `timestamp`. Bei
`Deliverable` zusätzlich `resource` (Verweis auf das Original als `asset:/pfad`) sowie
Herkunftsfelder wie `source_station`, `client`, `date`. Cross-Links zwischen Concepts als
bundle-relative Links mit führendem `/` — die bleiben beim Verschieben stabil.

Zwei Kleinigkeiten, die regelmäßig Zeit kosten: Frontmatter-Werte, die einen **Doppelpunkt**
enthalten, gehören in Anführungszeichen, sonst bricht der YAML-Parser. Und auslieferbare
Artefakte tragen von Anfang an ihren **endgültigen Namen** — Arbeits-Suffixe wie `-v2` oder
`-final` werden zum sichtbaren Namen und müssen später mit einem Referenz-Sweep wieder
herausgezogen werden.

### Extrakt-Regel — verbindlich

Der Qualitäts- und Schutzmechanismus des Setups. Zwei getrennte Schritte mit verschiedenen
Zwecken: **Schritt 1 schützt, Schritt 2 verbessert.**

**Geltungsbereich von Schritt 1:** jede Datei im Bestand — Concepts jedes Typs, `log.md`,
Meta- und Hilfsdateien, **auch Datei- und Ordnernamen**. Nicht nur Deliverables. Ein
vertraulicher Kundenname im Dateinamen ist genauso ein Treffer wie einer im Fließtext.

**Schritt 1 — Vertraulichkeitsprüfung, immer, mechanisch.** Die *Prüfung* ist ausnahmslos
verpflichtend, die *Entkernung* nur bei Treffer. Nicht auf Selbsteinschätzung verlassen:
„Anonymisiere bei sensiblen Inhalten" verlangt genau die Einschätzung, die beim Schreiben
regelmäßig ausbleibt. Eine feste Checkliste löst aus, wo Intuition versagt. Fünf Fragen,
dreißig Sekunden. Enthält der Entwurf …

1. **Konditionen?** Preise, Stundensätze, Margen, Vertrags- und Lizenzstaffeln — eigene wie
   fremde.
2. **Kennzahlen Dritter?** Umsätze, Nutzerzahlen, Budgets, Performance-Daten.
3. **Technische Interna?** Systemarchitektur, Tech-Stack, Zugänge, Schnittstellen,
   Sicherheitsstand.
4. **Interne Strategie?** Selbstkritik des Arbeitgebers, Wettbewerbsbewertungen,
   Sprechregeln, Pipeline-Bewertungen.
5. **Personennamen Dritter?**

Kein Treffer, nichts zu tun. Treffer: Die Passage bleibt im Original, im Extrakt steht ein
kursiver Hinweis, welche Inhalte ausschließlich dort zu finden sind. Personennamen sind der
Sonderfall — sie werden nicht gestrichen, sondern **durch die Rolle ersetzt** („der Product
Owner", „die Architektin"). Ausnahme: Personen im eigenen Karrierekontext.

**Schritt 2 — Methodenkern ausschreiben.** Ein Extrakt ist erst fertig, wenn der
übertragbare Kern **ausformuliert** ist, nicht bloß als Stichwort benannt: Vorgehen,
Gliederungen, Entscheidungsbäume, Bewertungsraster, Argumentationsfiguren,
Einwand-Antwort-Paare, Reihenfolge-Logiken („warum zuerst X, dann Y"). Der Kern wird
bewusst vom Anlassfall abgelöst und auf die Klasse von Fällen gehoben, für die er gilt.

**Testfrage:** *Brauche ich das noch, wenn ich morgen in einem anderen Kontext vor einer
ähnlichen Aufgabe stehe?* **Leitsatz:** Der Extrakt beantwortet „wie geht man vor", nicht
„was war im Fall X konkret". **Prinzip: nicht kürzen, sondern umschichten** — der
vertrauliche Anteil schrumpft, der methodische wächst. Schrumpft ein Extrakt beim Entkernen
substanziell, war er kein Wissensdokument, sondern eine Kopie.

**Aufbau eines Extrakts:** Frontmatter mit `resource` und Herkunftsfeldern · `# Überblick`
(worum ging es, welcher Dokumenttyp, welche Rolle, worin der übertragbare Gehalt liegt; bei
Treffer der kursive Hinweis) · `# Struktur / Gliederung` (Gliederungen sind Methode, kein
Geheimnis, sie bleiben erhalten) · `# Wiederverwendbare Inhalte` (der Kern, ausformuliert)
· `# Tragfähigkeit` (Pflicht) · `# Als Vorlage nutzbar für` · `# Original` (Verweis,
Format, Vertraulichkeitsvermerk).

**`# Tragfähigkeit` ist Pflicht, auch wenn dort „trägt uneingeschränkt" steht.** Ein Extrakt
schreibt den Methodenkern aus und verleiht ihm damit die Autorität eines Wissensbestands —
auch dann, wenn der Kern dünn ist. Ohne festen Ort für diese Einschätzung wächst die Basis
in die Breite, ohne dass Qualitätsunterschiede sichtbar bleiben. Fakt und Einschätzung
werden dort getrennt gehalten. Ein leerer Abschnitt ist ein Signal, ein fehlender nicht.

**Sonderfall Dialogverlauf.** Ist das Original ein exportierter Modell-Dialog, sind die
Runden die Gliederung, die auslösenden Fragen der Methodenkern und die Ergebnistexte das
Anlassmaterial. Die Rolle ist die des Auftraggebers, nicht die des Autors — das gehört ins
Frontmatter, damit später niemand den Text für eigene Urheberschaft hält.

### Elevation-Kaskade

Der Mechanismus, der aus einem Archiv eine Wissensbasis macht. Trägt der Methodenkern eines
`Deliverable` erkennbar über den Anlassfall hinaus, schlägt Claude vor, ihn **zusätzlich**
als eigenständiges `Framework` zu generalisieren; das Deliverable bleibt als Beleg
verlinkt. Für `Insight` gilt dasselbe eine Stufe später: Ein Insight, das sich über
mehrere Quellen hinweg bestätigt, wird als Elevation-Kandidat markiert.

Ohne diese Kaskade wächst die Basis in die Breite und nicht in die Reife.

### Marker-Governance

Offene Punkte werden im Bestand als Marker geführt — Platzhalter für fehlende Fakten,
ausstehende Anreicherungen, offene Entscheidungen. Ein Marker ist nur so lange nützlich,
wie er zu einer Handlung führen kann. Vier Regeln halten den Bestand rauschfrei:

* **Unbeschaffbares aktiv verwerfen** — mit kurzem Vermerk „aktiv verworfen, nicht
  vergessen", damit die Entscheidung nachvollziehbar bleibt und die Lücke nicht erneut als
  Aufgabe auftaucht.
* **Pausierte Vorhaben parken** — `status: pausiert (seit MM/JJJJ)` plus Parkvermerk; ihre
  offenen Fragen fallen bis zur Wiederaufnahme aus dem wöchentlichen Check.
* **Wartende Marker terminieren** — steht nur noch eine Bestätigung aus, wird der Marker
  zum Wiedervorlagepunkt mit Datum.
* **Gefundenes sofort verankern** — ist eine gesuchte Originaldatei lokalisiert, wandert
  der Verweis unmittelbar ins Concept, damit dieselbe Suche sich nicht wiederholt.

### Quellen ohne klassisches Original

Externe Erkenntnisse aus reinen Web-Quellen haben kein Original zum Ablegen. Regel: `date`
ist das **Publikationsdatum** der Quelle (mindestens `JJJJ-MM`), `resource` zeigt auf einen
**Erfassungs-Extrakt** in der Asset Library, die Quell-URLs stehen im Feld `source` und in
einem Abschnitt `# Citations`. Damit zeigt `resource` nie auf eine URL, die in einem Jahr
tot ist.

### Versionierung

* `MAJOR.MINOR.PATCH`, sinngemäß auf Wissensreife übertragen. **MAJOR:** struktureller
  Umbau oder grundlegende Neubewertung. **MINOR:** additive Erweiterung — ein neues
  Concept, ein neuer Abschnitt; Bestehendes bleibt gültig. **PATCH:** Korrektur,
  Präzisierung, Metadaten.
* **Ein Sicherungsvorgang = ein Versionsschritt.** Änderungen einer Session werden
  gesammelt, nicht einzeln vorgebumpt. Die Sprunghöhe richtet sich nach der **größten**
  Änderungsklasse im Batch.
* Die Version lebt synchron an zwei Stellen (Stufe 1) beziehungsweise drei (Stufe 2/3):
  Frontmatter der Wurzel-`index.md`, Eintrag in `log.md` (`## JJJJ-MM-TT — vX.Y.Z`, neueste
  zuerst, mehrere Änderungen als Bullets unter *einer* Überschrift) und — ab Stufe 2 — der
  Git-Tag `vX.Y.Z`.
* **Sicherheitsgrenze (Stufe 2/3):** Commit darf Claude nach expliziter Freigabe lokal
  ausführen; der **Push bleibt bei der Person** — ein Klick in einem Git-Werkzeug. So
  liegen nie Zugangs-Tokens in der Claude-Umgebung. Das **Tag** setzt die Action beim Push
  aus dem `version`-Feld; lokal wird nicht getaggt. So gilt „Version ist gleich getaggter
  Commit" unabhängig davon, wer committet.

### Datenschutzprüfung

Ergänzend zur Extrakt-Regel, die auf Urteilsvermögen beruht, prüft `check_privacy.py`
mechanisch. Es liest die lokale Entitätenliste `_meta/privacy-entities.txt` — eigene
Kunden, Arbeitgeber, Personen, Produktnamen, Projektkennungen — und findet zusätzlich
generische Muster: Mailadressen, lokale Benutzerpfade, Beträge mit Währung,
Kontoverbindungen, Telefonnummern, Zugangs-Token. Geprüft werden Dateiinhalte **und
Dateinamen**.

Die Liste kennt zwei Klassen von Einträgen. **Sperren** (ohne Präfix) blockieren die
Sicherung. **Klärungsfälle** (Präfix `?`) blockieren nicht, sondern lösen einmal pro Datei
eine Rückfrage aus — gedacht für den eigenen Arbeitgeber, dessen Name im eigenen Bestand
zwangsläufig vorkommt, dessen Material aber prüfungsbedürftig ist. Beantwortet wird die
Rückfrage mit `jumpstart-checked: <Begründung>` in der Datei; danach ist sie dauerhaft still.

Fünf Regeln zum Umgang:

* **Die Entitätenliste wird niemals versioniert.** Sie steht in der `.gitignore` und ist
  selbst das Leck, das sie verhindern soll.
* **Platzhalter sind ein Fehler.** Die Beispieleinträge der Vorlage kennt das Skript und
  weist sie zurück — eine Liste aus Platzhaltern meldet sonst „Sauber", ohne etwas geprüft
  zu haben.
* **Die Liste wächst mit.** Jeder neue Kunde, jedes neue Projekt kommt hinein — der
  passende Moment dafür ist der Konsistenz-Block des Weekly Review.
* **Beim Arbeitgeberwechsel wird aus dem Klärungsfall eine Sperre**: Das `?` entfällt, die
  bestehenden Karrierestationen und `resource`-Pfade bekommen `jumpstart-ignore` mit
  Begründung. Auch das gehört in den Konsistenz-Block.
* **Treffer werden abstrahiert, nicht weggeklickt.** Wer einen Treffer bewusst freigibt,
  schreibt `jumpstart-ignore` mit einer Begründung daneben. Ohne Begründung ist die
  Freigabe wertlos, weil niemand sie später beurteilen kann.

**Grenze des Verfahrens:** Das Skript findet, was es kennt und was eine Form hat. Es findet
nicht die umschriebene Fallbeschreibung ohne Namen, die trotzdem eindeutig zuzuordnen ist.
Faustregel dagegen: *Ergibt eine Passage ohne den konkreten Fall immer noch Sinn, muss der
konkrete Fall raus. Trägt sie ohne ihn nicht mehr, gehört sie gar nicht nach draußen.*

### Betriebsregeln

* **Keine Verzeichnislistings der Asset Library in den Bestand.** Dateilisten verraten über
  die Namen genau das, was die Extrakt-Regel aus den Inhalten entfernt. Sie bleiben draußen
  (bei Stufe 2/3 per `.gitignore`).
* **Git-Historie säubern heißt Repository neu anlegen.** Ein Force-Push genügt nicht — alte
  Tags halten die Commits erreichbar. Wer versehentlich Vertrauliches committet hat, legt
  das Repository neu an. Diese Regel steht hier, weil sie in der dritten Woche gebraucht
  wird, nicht in der ersten.
* **Geplante Aufgaben einmal manuell auslösen.** Nach dem Anlegen oder Ändern eines
  geplanten Jobs einmal „jetzt ausführen", damit die Werkzeug-Freigaben gespeichert sind
  und automatische Läufe nicht auf Bestätigungen warten.

### `okf-conformance.md`

Hier stehen die Regeln des Formats selbst — Bundle-Struktur, Concept-Definition,
Cross-Linking, die reservierten Dateinamen, was Konformität bedeutet — sowie der Aufruf des
Prüfskripts. Und, wichtiger: ein Abschnitt **„Bewusste Abweichungen"**, in dem jede
Abweichung vom Standard mit Begründung steht. Beispiel: Die `log.md`-Überschriften tragen
zusätzlich zur Datumsangabe die Versionsnummer — eine bewusste Erweiterung gegenüber der
Spezifikation.

Das Prüfskript prüft: fehlendes oder ungültiges Frontmatter, fehlendes `type`, eine
`index.md` mit Frontmatter außerhalb der Wurzel — das sind **harte Verstöße** und führen zu
einem Fehler-Exit. Tote bundle-relative Links sind **weiche Hinweise** ohne Fehler-Exit.
Dazu die Konsistenzprüfung `version` in der Wurzel-`index.md` gegen den jüngsten
`log.md`-Eintrag. Ausgenommen sind `.git`, `workspace/`, der Skill-Ordner und `CLAUDE.md`.

---

## Phase 5 — Infodump: die erste Befüllung mit Vorhandenem

Nach dem Strukturaufbau bitte die Person aktiv, **vorhandenes Material mitzubringen**,
damit das Second Brain nicht leer startet: Lebenslauf, Profiltexte, eigene Guides und
Vorlagen, wichtige Präsentationen oder Konzepte, Projektdokumentationen.

**Erkläre den Maßstab — und was nicht qualifiziert.** Er lautet nicht „alles, was ich
habe", sondern: **dokumentierungsbedürftig und auf Routinen einzahlend.** Hinein gehört,
was mindestens eines davon leistet: Es beschreibt die Person und ihre Arbeitsweise, es
enthält eine wiederverwendbare Methode oder Vorlage, es ist Nachschlagewissen mit
Haltbarkeit, oder Claude braucht es künftig regelmäßig als Kontext. **Nicht** hinein gehören
gewöhnliche Alltagsnotizen, flüchtige To-dos, einmalige Korrespondenz oder reines Archivgut
ohne Wiederverwendungswert — das bleibt draußen oder landet höchstens im `workspace/`. Die
Testfrage der Extrakt-Regel gilt auch hier.

Verarbeitung: jedes Stück einzeln durch die Extrakt-Regel — erst Vertraulichkeits-Check,
dann Methodenkern —, Typ-Vorschlag machen, Original in die Asset Library, Extrakt in den
Hub. **Gebündelt zur Freigabe vorlegen**, nicht stückweise nerven. Bei viel Material
priorisieren lassen: drei bis fünf Stücke zuerst, der Rest wandert als Liste in
`workspace/TASKS.md`.

**Nebenprodukt Skill-Kandidaten:** Achte beim Sichten auf wiederkehrende Muster —
Dokumenttypen, die die Person offenbar regelmäßig erstellt, Abläufe, die sich in mehreren
Stücken wiederholen. Kondensiere daraus Kandidaten und führe sie mit der Liste aus dem
Interview zusammen.

---

## Phase 6 — Routinen etablieren

Zwei Dinge passieren hier: Die Person lernt die **mitgelieferten** Verfahren kennen, und
ihr entscheidet über **eigene**.

### Die mitgelieferten Verfahren übergeben

Das Setup bringt sechs fertige Verfahren mit. Stell sie vor — kurz, in einem Satz je
Verfahren, und verweise für Details auf `docs/skills.md`:

| Verfahren | Wofür |
|-----------|-------|
| `jumpstart` | Die Einrichtung, die gerade läuft. Danach nicht mehr gebraucht. |
| `extract` | Ein eigenes Dokument zu wiederverwendbarem Wissen destillieren. |
| `insight` | Eine externe Studie, einen Report oder Marktdaten aufnehmen. |
| `weekly-review` | Der wöchentliche Pflegedurchlauf. |
| `hub-commit` | Den Stand sichern, Version setzen, Prüfungen fahren. |
| `jumpstart-upgrade` | Die eigene Basis auf eine neuere Fassung des Setups heben. |

**Der wichtigste Satz dabei:** Diese Verfahren sind Markdown-Dateien. Claude kann sie
nachschlagen und ausführen, **ohne dass irgendetwas installiert wird** — in allen drei
Stufen. Wer sagt „nimm das Dokument in mein Wissen auf", bekommt `extract`, ob installiert
oder nicht. Sag das ausdrücklich, sonst hat ein Stufe-1-Nutzer das Gefühl, ihm fehle etwas.

Was eine Installation zusätzlich bringt, ist der Kurzaufruf per Schrägstrich und das
automatische Auslösen im passenden Moment. Bequemlichkeit, kein Funktionsunterschied.

**Installation anbieten, je nach Stufe:**

* **Stufe 3:** Läuft über die Plugin-Quelle. Drei Schritte, und der dritte wird am
  häufigsten vergessen:

  1. Quelle hinzufügen — in der Kommandozeilen-Fassung
     `/plugin marketplace add dutch-vdl/sb-jumpstart`, in der Desktop-App über die
     Plugin-Verwaltung mit der Repo-Adresse.
  2. Plugin installieren: `/plugin install sb@sb-jumpstart`, danach neu laden.
  3. **Automatische Aktualisierung einschalten.** Sie ist bei eigenen Quellen
     standardmäßig **aus**. Ohne diesen Schalter passiert nichts, ohne dass es auffällt.

  Aufgerufen werden die Verfahren danach mit vorangestelltem Plugin-Namen, etwa
  `/sb:extract`.

  **Zwei getrennte Installationen:** Wer sowohl die Desktop-App als auch die
  Kommandozeilen-Fassung nutzt, richtet die Quelle **zweimal** ein — sie teilen sich die
  Konfiguration nicht. Sag das dazu, sonst wundert sich die Person, warum die Verfahren an
  einer Stelle fehlen.

  **Und die Grenze:** Über diesen Weg kommen nur die **Verfahren**. Regeldateien, Vorlagen
  und Prüfskripte im Hub der Person fasst kein Plugin-Update an — dafür bleibt der
  Upgrade-Skill zuständig, genau wie bei Stufe 1 und 2.
* **Stufe 1 und 2:** Das Paket lässt sich als lokale Plugin-Quelle einbinden. **Prüfe das
  mit der Person einmal konkret**, statt es vorauszusetzen — die Unterstützung dafür
  unterscheidet sich zwischen den Umgebungen und ändert sich schneller, als ein
  Setup-Dokument nachziehen kann. Klappt es, gibt es die Kurzaufrufe. Klappt es nicht,
  ändert sich nichts an der Funktion: Claude liest die Verfahren aus dem Paket.

**Und dann einmal vorführen.** Der beste Weg, das zu vermitteln, ist die Anwendung: Wenn in
Phase 5 das erste Dokument aufgenommen wurde, benenne, dass dabei gerade `extract` gelaufen
ist. Ein einmal erlebtes Verfahren erklärt sich besser als jede Tabelle.

### Die eigenen Routinen

Erkläre der Person die beiden Kern-Routinen und biete an, sie als wiederverwendbare Skills
anzulegen.

### Der Sicherungs-Ablauf („sichere den Stand")

**Stufe 1:** Änderungen sichten, Versionsschritt bestimmen, `version` in der
Wurzel-`index.md` setzen, `log.md`-Eintrag schreiben, beide Prüfskripte laufen lassen.
**Bei einem harten Verstoß oder einem Datenschutz-Treffer wird nicht gesichert** — stoppen,
melden, bereinigen. Das gilt hier genauso wie in den größeren Stufen; nur die Automatik
fehlt.

**Stufe 2 und 3:** zusätzlich — vor der Versionsbestimmung den tatsächlichen
Repository-Stand einlesen, inzidentelle Dateien aus dem Staging aussortieren, beide
Prüfskripte als **Sperre** (kein Commit bei hartem Verstoß oder Datenschutz-Treffer:
stoppen, melden, nicht committen),
Commit-Message nach Conventional Commits vorschlagen (`typ(scope): kurzbeschreibung`),
explizite Freigabe einholen, committen. Der Push bleibt bei der Person, das Tag setzt die
Action.

### Die Sperre vor dem Commit (Angebot ab Stufe 2)

Der Sicherungs-Ablauf prüft zuverlässig — aber nur, wenn er benutzt wird. Wer am Skill
vorbei committet, direkt aus einem Git-Werkzeug oder dem Terminal, prüft nichts. Genau auf
diesem Pfad rutscht ein Kundenname ins Repository.

Dagegen gibt es einen `pre-commit`-Hook: ein kleines Skript, das Git vor jedem Commit
ausführt und den Commit abbricht, wenn eine der beiden Prüfungen anschlägt. Er liegt im
Paket bereit; die Einrichtung ist einmalig pro Klon:

```
mkdir -p .githooks && cp <paket>/pre-commit .githooks/pre-commit
chmod +x .githooks/pre-commit
git config core.hooksPath .githooks
```

**Nach der Einrichtung einmal prüfen, ob der Hook wirklich greift.** Er ist stumm, wenn
der Konfigurationsbefehl fehlt oder die Datei kein Ausführungsrecht hat — beides meldet
niemand. Selbsttest: eine Testdatei mit einem Namen aus der Entitätenliste anlegen und
committen wollen. Der Commit **muss** abbrechen. Tut er es nicht, ist der Hook inaktiv.

Biete das an, dränge nicht — ein Setup, das beim ersten Commit unerwartet blockiert,
verschreckt Anfänger. Erkläre dabei die drei Grenzen ehrlich: Der Hook wandert nur mit,
wenn der `core.hooksPath`-Befehl pro Klon einmal läuft; er greift nicht bei Commits über
die Weboberfläche; und er lässt sich mit `--no-verify` bewusst übergehen. Er ist eine
Sicherung, keine Garantie.

### Das Weekly Review (wöchentlich, rund fünfzehn Minuten)

Die eine Routine, die Workspace und Wissensbestand verbindet und beide frisch hält. Fester
Ablauf in Blöcken, als knapper Bericht mit Entscheidungspunkten — kein stiller Umbau. Der
Durchlauf **ersetzt keine Einzelaufnahme**; er sammelt ein, was liegen geblieben ist.

1. **Destillat.** Workspace sichten: Was hat sich als generalisierbar erwiesen?
   Kandidatenliste mit Typ-Vorschlag und Ein-Satz-Begründung; Aufnahme nur mit Freigabe und
   über die Extrakt-Regel. Danach Workspace straffen — Erledigtes nach `_zu-loeschen/`
   verschieben und berichten, nicht löschen (Claude kann das nicht).
2. **Aktualität.** Insights am gründlichsten prüfen, gesteuert über den
   Haltbarkeitsvermerk — geprüft wird der verfallende Anteil, nicht das ganze Dokument.
   Learning auf offensichtliche Veralterung, Frameworks in der Regel nicht anfassen.
3. **Task-Triage.** Erledigtes raus, Überfälliges nach vorn, Neues aus den Notizen der
   Woche einsammeln, Marker-Governance anwenden. Jede Aufgabe braucht ein Datum — Aufgaben
   ohne Datum sind Absichten.
4. **Regel-Ernte.** Was hat die Nutzung der Woche über die Zusammenarbeit gelehrt?
   Korrekturen, wiederkehrende Entscheidungen und Stil-Erkenntnisse als Regel-Kandidaten;
   wiederholte Abläufe als Skill-Kandidaten. Aufnahme nur mit Freigabe.
5. **Konsistenz und Ausbaustufen.** Beide Prüfskripte laufen lassen. Ist die
   Entitätenliste noch vollständig — neue Kunden, Projekte, Kontakte der letzten Wochen
   ergänzt? Frontmatter vollständig?
   Version, Log und — ab Stufe 2 — Repository-Stand synchron? Uncommittete Änderungen führen
   zum Vorschlag, zu sichern. Offene Ausbaustufen aus `CLAUDE.md` prüfen: Ist die Basis so
   gewachsen, dass jetzt der Aufstieg auf die nächste Stufe oder ein Backup der Asset
   Library sinnvoll wird? Dann einmalig erinnern, Entscheidung notieren.

Wer die Basis für messbare Ziele nutzt, kann als sechsten Block einen Kennzahlen-Puls
ergänzen. Das ist rollenabhängig und gehört nicht in jedes Setup.

### Skills anlegen

Entscheide jetzt mit der Person über die gesammelten Kandidaten: Welche zwei, drei Abläufe
sind reif? Der Rest bleibt Liste unter „Ausbaustufen". **Nicht auf Vorrat bauen.**

Vier Regeln für jeden Skill, den ihr anlegt:

* **Vorrangregel.** Bei Widerspruch zwischen einem Skill und `conventions.md` gilt
  `conventions.md`. Skills sind Ausführungsschicht, kein zweites Regelwerk.
* **Keine Duplizierung.** Ein Skill orchestriert ein Verfahren, er schreibt es nicht noch
  einmal auf. Sonst driften beide Fassungen auseinander.
* **Reifekennzeichnung.** Ein frisch gebauter Skill trägt einen sichtbaren Vermerk, dass er
  noch nicht kalibriert ist, plus eine Liste offener Kalibrierungspunkte. Der Vermerk
  verschwindet erst, wenn die Person den Skill für eingeschliffen erklärt. Verhindert, dass
  ungetestete Automatik als eingespielt gilt.
* **Namensprüfung.** Vor dem Anlegen prüfen, ob der gewünschte Name mit einem
  produktseitigen Befehl kollidiert. Ein belegter Name führt dazu, dass der Skill nie
  ausgelöst wird — und der Fehler ist von außen kaum zu sehen.

**Zur Ablage:** Der Hub ist die versionierte Quelle der eigenen Skills. Ob eine Umgebung
diesen Ordner direkt liest oder ob der Skill zusätzlich installiert werden muss,
unterscheidet sich je nach Anwendung — prüfe das mit der Person einmal konkret und halte
das Ergebnis fest, statt es vorauszusetzen. Aus dem Jumpstart-Paket mitgelieferte Skills
werden nicht in den Hub kopiert; sie kommen über das Paket und werden über das Paket
aktualisiert.

---

## Abschluss

Stelle sicher, dass nach Infodump und Routinen-Setup mindestens existieren: ein
Profil-Dokument (wer bin ich, was kann ich), das **gefüllte Zusammenarbeits-Profil** unter
`<beruflicher-strang>/profile/zusammenarbeit.md` und ein erstes inhaltliches Concept aus der
tatsächlichen Arbeit der Person. Hat der Infodump das nicht hergegeben, erarbeite alles drei
jetzt im Dialog. Die beiden Profile sind **zwei Dateien**, nicht eine: Das eine beschreibt
die Person, das andere den Umgang mit ihr. Beide tragen `type: Profile`; unterschieden
werden sie über `title` und `tags`.

**Den Termin für das erste Weekly Review nicht nur nennen, sondern setzen.** Ein Datum im
Gesprächsprotokoll ist kein Termin. Biete zwei Wege mit Empfehlung an:

* **Geplante Aufgabe** *(Empfehlung, sobald die Basis produktiv genutzt wird)* — ein
  wöchentlich feuernder Job, der den Durchlauf anstößt. Nach dem Anlegen **einmal manuell
  auslösen**, damit die Werkzeugfreigaben sitzen und der erste automatische Lauf nicht auf
  eine Bestätigung wartet.
* **Eintrag in `workspace/TASKS.md` mit Datum** *(Minimum)* — für Wegwerf- oder
  Probeaufbauten, bei denen ein wöchentlicher Job nur Lärm wäre.

Ohne eine der beiden Mechaniken etabliert sich die Routine erfahrungsgemäß nicht — und sie
ist der Unterschied zwischen einer lebendigen Wissensbasis und einem digitalen Dachboden.

Danach die erste Sicherung fahren und den Stand zusammenfassen: was steht, welche
Ausbaustufen notiert sind, welche Verfahren zur Verfügung stehen und wie man sie aufruft,
wie der Weekly-Review-Termin gesetzt wurde. Sag der Person außerdem,
**wie sie Aktualisierungen dieses Setups bekommt** — bei Stufe 1 und 2 über die
Benachrichtigung des Repositories und den Upgrade-Skill, bei Stufe 3 automatisch.

Und dann der wichtigste Rat: **Das System wächst im Gebrauch.** Claude in normalen
Arbeits-Sessions einfach mit dem verbundenen Hub arbeiten lassen; wenn dokumentierenswertes
Wissen entsteht, fragt Claude von selbst. Nach vier bis sechs Wochen ehrlich prüfen, welche
Ordner leben und welche tot sind — und die Struktur der Realität anpassen, nicht umgekehrt.

---

## Quellen — Open Knowledge Format

Das Format hinter diesem Setup ist offen dokumentiert. Bei Detailfragen gilt die Spec; der
Blogartikel liefert Motivation und Ökosystem-Überblick:

1. [OKF-Spezifikation v0.1 — SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
   — kanonische Spezifikation (Bundle-Struktur, Concepts, Cross-Linking, `index.md` /
   `log.md`, Konformität).
2. [knowledge-catalog — OKF (GitHub)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
   — Repository mit Spec, Beispiel-Bundles und Werkzeugen, unter anderem einem
   HTML-Visualizer, der ein Bundle als interaktiven Graphen rendert.
3. [„How the Open Knowledge Format can improve data sharing" — Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/)
   — Primärartikel zur Einführung des Formats.
