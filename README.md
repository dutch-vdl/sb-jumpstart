# SB Jumpstart

**Bauplan für eine persönliche Wissensbasis, mit der Claude dich kennt, statt jedes Mal bei
null anzufangen.** Dein Wissen entsteht als Sammlung einfacher Markdown-Dateien nach dem
offenen **Open Knowledge Format (OKF v0.2)** — lesbar für Menschen und für Agenten,
ohne Plattformbindung, ohne Export-Problem.

Das Projekt wird primär an Peers des Autors weitergegeben und auf Deutsch entwickelt.

> **Stand: 0.4.0 — Vorabfassung.** Die Struktur steht und ist geprüft, aber noch nicht an
> genügend echten Einrichtungen erprobt. Rechne in dieser Phase mit Änderungen, die auch
> bestehende Wissensbasen betreffen können. Mit 1.0.0 gilt das Setup als produktiv erprobt.

---

## Loslegen

Du brauchst einen Claude-Zugang, am besten die Desktop-App. Sonst nichts. Du musst vorher
nichts entscheiden und nichts installieren.

### 1 · Ordner anlegen

Lege irgendwo auf deinem Rechner einen leeren Ordner namens `Knowledge Hub` an. Dort
entsteht dein Wissen. Ein zweiter Ordner für große Original-Dateien kommt später dazu —
darum kümmert sich Claude mit dir.

### 2 · Ordner mit Claude verbinden

Öffne die Claude-Desktop-App, starte eine neue Cowork-Aufgabe und füge über
**„Ordner hinzufügen"** deinen Ordner `Knowledge Hub` hinzu.

### 3 · Diesen Text an Claude schicken

```text
Ich möchte mit dir eine persönliche Wissensbasis aufbauen. Die Anleitung dafür liegt
öffentlich auf GitHub unter github.com/dutch-vdl/sb-jumpstart.

Lies dort bitte zuerst README.md, dann docs/tracks.md und danach die vollständige
Anleitung unter plugins/sb/skills/jumpstart/setup-guide.md. Im selben Ordner liegen
user-readme.md (die Erklärung für mich) und die Vorlagen unter templates/.

Richte mich anschließend nach dieser Anleitung ein. Der Ordner Knowledge Hub ist
bereits mit dieser Sitzung verbunden.
```

Das war's. Claude führt dich durch ein Interview und baut die Struktur mit dir zusammen auf.

**Zeitrahmen:** Interview und Grundgerüst rund eine halbe Stunde. Danach kommt das Aufnehmen
von vorhandenem Material — das dauert so lange, wie du Material mitbringst, und muss nicht
am selben Tag passieren.

**Wenn du zwischendurch aufhören musst:** kein Problem. Sag beim nächsten Mal einfach
*„lass uns mein Setup weiterbauen"* — Claude erkennt am angelegten Stand, wo ihr wart.

---

## Was dabei entsteht

Ein Ordner voller einfacher Textdateien, in dem dein Wissen strukturiert liegt: dein Profil,
deine Methoden, wiederverwendbare Dokumente, gesammelte Erkenntnisse. Claude liest das in
jeder Sitzung als Kontext.

Dazu ein paar Regeln, die verhindern, dass daraus mit der Zeit ein Zettelberg wird, und
feste Verfahren für die wiederkehrenden Aufgaben — Material aufnehmen, Quellen ablegen,
wöchentlich aufräumen, Stand sichern.

Es gibt drei Ausbaustufen, von „ein Ordner auf dem Rechner" bis „versioniert und mit
mitlaufenden Verfahren". **Entscheiden musst du das nicht vorab**; Claude leitet die
passende im Gespräch ab, und aufsteigen kannst du jederzeit. Ohne Fachsprache erklärt in
[`docs/tracks.md`](docs/tracks.md).

---

<details>
<summary><b>Was du brauchst — je nach Ausbaustufe</b></summary>

<br>

| | Stufe 1 · Lokal | Stufe 2 · Verteilt | Stufe 3 · Mitlaufend |
|---|---|---|---|
| Claude-Zugang, Desktop-App | ja | ja | ja |
| Ein Ordner auf dem Rechner | ja | ja | ja |
| GitHub-Account | nein | ja | ja |
| Git-Programm (empfohlen: GitHub Desktop) | nein | ja | ja |
| Python 3 auf dem Gerät | nur wenn du die Prüfungen selbst fahren willst | ja | ja |

Fehlt etwas, ist das kein Fehler, sondern ein Argument für die kleinere Stufe.

</details>

<details>
<summary><b>Worauf das aufsetzt — das Open Knowledge Format</b></summary>

<br>

Deine Wissensbasis bekommt **kein Eigenformat**. Sie folgt dem **Open Knowledge Format
(OKF v0.2)** — einer offen dokumentierten Konvention für Wissenssammlungen aus
Markdown-Dateien: ein Verzeichnisbaum als „Bundle", jede Datei ein abgeschlossener Gedanke
mit einem kurzen Kopf aus Metadaten, `index.md` als Inhaltsverzeichnis, `log.md` als
Änderungstagebuch, Verweise untereinander über stabile Pfade.

Dazu ein Satz freiwilliger Felder, die festhalten, woher ein Eintrag stammt, worauf er sich
stützt, wer ihn bestätigt hat und wie lange er gelten soll. Das ist die Grundlage dafür,
dass eine wachsende Basis prüfbar bleibt, statt nur größer zu werden.

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

*Zum Stand der Quellen:* Version 0.2 wurde im Juli 2026 veröffentlicht und ist im
Blogbeitrag dazu vollständig beschrieben; die Spezifikationsdatei im Projekt-Repository trug
zu diesem Zeitpunkt noch die Versionsangabe 0.1. Für die neuen Felder gilt bis auf Weiteres
der Blogbeitrag, für alles Übrige die Spezifikation.

* [OKF v0.2 — Trust Signals (Google-Cloud-Blog)](https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals)
  — die freiwilligen Felder für Herkunft, Belege, Bestätigung, Haltbarkeit und Lebenszyklus.
* [OKF-Spezifikation](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
  — kanonisch; bei Detailfragen gilt sie, nicht dieses Repository.
* [knowledge-catalog auf GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
  — Spec, Beispiel-Bundles und Werkzeuge, unter anderem ein Visualizer, der ein Bundle als
  Graphen rendert.
* [Einführungsartikel im Google-Cloud-Blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/)
  — Motivation und Hintergrund.

</details>

<details>
<summary><b>Was in diesem Repository liegt</b></summary>

<br>

| Pfad | Inhalt |
|------|--------|
| [`docs/tracks.md`](docs/tracks.md) | Die drei Ausbaustufen, ohne Fachsprache. **Fang hier an.** |
| [`docs/skills.md`](docs/skills.md) | Die sechs Verfahren: wann du welches brauchst. |
| [`docs/upgrade.md`](docs/upgrade.md) | Wie du eine neue Fassung dieses Setups übernimmst. |
| [`CHANGELOG.md`](CHANGELOG.md) | Was sich von Fassung zu Fassung geändert hat. |
| `plugins/sb/skills/jumpstart/setup-guide.md` | Die vollständige Anleitung. Richtet sich an Claude, nicht an dich. |
| `plugins/sb/skills/` | Die sechs Verfahren als Textdateien. |
| `docs/versioning.md`, `docs/release-gate.md` | Betriebsdoku für den, der dieses Repo pflegt. |

</details>

---

## Aktualisierungen mitbekommen

Oben rechts auf **Watch → Custom → Releases** stellen. Dann bekommst du eine Mail, sobald
eine neue Fassung erscheint, mit den Änderungen im Klartext.

Zum Übernehmen sagst du Claude:

```text
Prüf mein Setup gegen den neuen Stand.
```

Claude vergleicht deine Fassung mit der neuen, zeigt dir die Unterschiede und arbeitet nach
deiner Freigabe ein, was zu dir passt. **Es wird nie neu aufgesetzt, immer nur die
Differenz** — und was du selbst angepasst hast, wird nicht stillschweigend überschrieben.

## Datenschutz in einem Absatz

Dieses Setup hat **keinen Rückkanal**. Es meldet nichts, misst nichts, sendet nichts. Was in
deinen Ordnern liegt, bleibt in deinen Ordnern. Der Ordner für dein Tagesgeschäft, in dem
echte Namen und Zahlen erlaubt sind, ist von allem ausgenommen, was jemals kopiert wird. Und
wenn du dich für Ausbaustufe 2 entscheidest, liegt deine Wissensbasis auf einem fremden
Server — das ist eine Entscheidung über deine Daten, und Claude weist dich beim Aufsetzen
ausdrücklich darauf hin. Details in [`docs/tracks.md`](docs/tracks.md).
