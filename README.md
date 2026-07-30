# SB Jumpstart

Bauplan für eine persönliche Wissensbasis für die tägliche Arbeit mit einem LLM wie Claude. Sie entsteht als Sammlung einfacher Markdown-Dateien
nach dem offenen **Open Knowledge Format (OKF v0.1)**, welches die Lesbarkeit von Agenten und Menschen zugleich ermöglicht.

Dieses Projekt wird primär an Peers des Autors weitergegeben und auf Deutsch entwickelt.

**Stand: 0.3.0 — Vorabfassung.** Die Struktur steht und ist geprüft, aber noch nicht an
genügend echten Einrichtungen erprobt. Rechne in dieser Phase mit Änderungen, die auch
bestehende Wissensbasen betreffen können. Mit 1.0.0 gilt das Setup als produktiv erprobt.

---

## In drei Schritten loslegen

Du brauchst dafür einen Claude-Zugang, am besten die Desktop-App. Sonst nichts.

**1. Zwei Ordner anlegen.** Lege irgendwo auf deinem Rechner einen leeren Ordner namens
`Knowledge Hub` an. Dort entsteht dein Wissen. Ein zweiter Ordner für große
Original-Dateien kommt später dazu — darum kümmert sich Claude mit dir.

**2. Den Ordner mit Claude verbinden.** Öffne die Claude-Desktop-App, starte eine neue
Cowork-Aufgabe und füge über „Ordner hinzufügen" deinen Ordner `Knowledge Hub` hinzu.

**3. Diesen Text an Claude schicken:**

> Ich möchte mit dir eine persönliche Wissensbasis aufbauen. Die Anleitung dafür liegt
> öffentlich auf GitHub unter `github.com/dutch-vdl/sb-jumpstart`. <!-- jumpstart-ignore: Repo-Adresse gehört in den Startprompt, sonst findet niemand die Anleitung -->
>
> Lies dort bitte zuerst `README.md`, dann `docs/tracks.md` und danach die vollständige
> Anleitung unter `plugins/sb/skills/jumpstart/setup-guide.md`. Im selben Ordner liegen
> `user-readme.md` (die Erklärung für mich) und die Vorlagen unter `templates/`.
>
> Richte mich anschließend nach dieser Anleitung ein. Der Ordner `Knowledge Hub` ist
> bereits mit dieser Sitzung verbunden.

Das war's. Claude führt dich durch ein Interview und baut die Struktur mit dir zusammen
auf. Du musst vorher nichts entscheiden und nichts installieren.

**Zeitrahmen:** Interview und Grundgerüst rund eine halbe Stunde. Danach kommt das Aufnehmen
von vorhandenem Material — das dauert so lange, wie du Material mitbringst, und muss nicht
am selben Tag passieren.

**Wenn du zwischendurch aufhören musst:** kein Problem. Sag beim nächsten Mal einfach
„lass uns mein Setup weiterbauen" — Claude erkennt am angelegten Stand, wo ihr wart.

---

## Was dabei entsteht

Ein Ordner voller einfacher Textdateien, in dem dein Wissen strukturiert liegt: dein
Profil, deine Methoden, wiederverwendbare Dokumente, gesammelte Erkenntnisse. Claude liest
das in jeder Sitzung als Kontext, statt jedes Mal bei null anzufangen.

Dazu ein paar Regeln, die verhindern, dass daraus mit der Zeit ein Zettelberg wird, und
feste Verfahren für die wiederkehrenden Aufgaben.

Ausführlich und ohne Fachsprache steht das in [`docs/tracks.md`](docs/tracks.md) — dort
findest du auch, welche der drei Ausbaustufen zu dir passt. Entscheiden musst du das nicht
vorab; Claude leitet es im Gespräch ab.

## Worauf das aufsetzt

Deine Wissensbasis bekommt **kein Eigenformat**. Sie folgt dem **Open Knowledge Format
(OKF v0.1)** — einer offen dokumentierten Konvention für Wissenssammlungen aus
Markdown-Dateien: ein Verzeichnisbaum als „Bundle", jede Datei ein abgeschlossener Gedanke
mit einem kurzen Kopf aus Metadaten, `index.md` als Inhaltsverzeichnis, `log.md` als
Änderungstagebuch, Verweise untereinander über stabile Pfade.

Praktisch bedeutet das zweierlei. Was du aufbaust, liegt in Dateien, die jeder Texteditor
öffnet — es gibt nichts zu exportieren, weil nichts eingesperrt ist. Und die Regeln sind
nicht von mir erfunden, sondern nachlesbar; wo dieses Setup bewusst abweicht, steht das mit
Begründung in deiner `okf-conformance.md`. Mitgeliefert ist ein kleines Prüfprogramm, das
die Formattreue misst, statt sie zu behaupten.

*Einordnung, damit die Erwartung stimmt:* OKF ist ein junges Format aus Googles
`knowledge-catalog`-Projekt, und das Werkzeug-Ökosystem drumherum ist entsprechend klein.
Der Nutzen liegt heute vor allem in der Nachvollziehbarkeit und darin, dass du auf einer
dokumentierten Konvention sitzt statt auf einer Privatvereinbarung — nicht in einer breiten
Werkzeuglandschaft, die es noch nicht gibt.

* [OKF-Spezifikation v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
  — kanonisch; bei Detailfragen gilt sie, nicht dieses Repository.
* [knowledge-catalog auf GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
  — Spec, Beispiel-Bundles und Werkzeuge, unter anderem ein Visualizer, der ein Bundle als
  Graphen rendert.
* [Einführungsartikel im Google-Cloud-Blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/)
  — Motivation und Hintergrund.

## Was du brauchst

| | Stufe 1 · Lokal | Stufe 2 · Verteilt | Stufe 3 · Mitlaufend |
|---|---|---|---|
| Claude-Zugang, Desktop-App | ja | ja | ja |
| Ein Ordner auf dem Rechner | ja | ja | ja |
| GitHub-Account | nein | ja | ja |
| Git-Programm (empfohlen: GitHub Desktop) | nein | ja | ja |
| Python 3 auf dem Gerät | nur wenn du die Prüfungen selbst fahren willst | ja | ja |

Die Stufe legst du nicht vorher fest. Claude prüft im Interview, was vorhanden ist, und
schlägt die passende vor. Fehlt etwas, ist das kein Fehler, sondern ein Argument für die
kleinere Stufe — aufsteigen kannst du jederzeit.

## Was drin liegt

| Pfad | Inhalt |
|------|--------|
| [`docs/tracks.md`](docs/tracks.md) | Die drei Ausbaustufen, ohne Fachsprache. Fang hier an. |
| [`docs/skills.md`](docs/skills.md) | Die sechs Verfahren: wann du welches brauchst. |
| [`docs/upgrade.md`](docs/upgrade.md) | Wie du eine neue Fassung dieses Setups übernimmst. |
| `plugins/sb/skills/jumpstart/setup-guide.md` | Die vollständige Anleitung. Richtet sich an Claude, nicht an dich. |
| `plugins/sb/skills/` | Die sechs Verfahren als Textdateien. |
| `docs/versioning.md`, `docs/release-gate.md` | Betriebsdoku für den, der dieses Repo pflegt. |

## Aktualisierungen mitbekommen

Oben rechts auf **Watch → Custom → Releases** stellen. Dann bekommst du eine Mail, sobald
eine neue Fassung erscheint, mit den Änderungen im Klartext.

Zum Übernehmen sagst du Claude: **„Prüf mein Setup gegen den neuen Stand."** Claude
vergleicht deine Fassung mit der neuen, zeigt dir die Unterschiede und arbeitet nach
deiner Freigabe ein, was zu dir passt. Es wird nie neu aufgesetzt, immer nur die Differenz.

## Datenschutz in einem Absatz

Dieses Setup hat **keinen Rückkanal**. Es meldet nichts, misst nichts, sendet nichts. Was
in deinen Ordnern liegt, bleibt in deinen Ordnern. Der Ordner für dein Tagesgeschäft, in
dem echte Namen und Zahlen erlaubt sind, ist von allem ausgenommen, was jemals kopiert
wird. Und wenn du dich für Ausbaustufe 2 entscheidest, liegt deine Wissensbasis auf einem
fremden Server — das ist eine Entscheidung über deine Daten, und Claude weist dich beim
Aufsetzen ausdrücklich darauf hin. Details in `docs/tracks.md`.
