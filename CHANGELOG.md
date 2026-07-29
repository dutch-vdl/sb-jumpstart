# Änderungen am SB Jumpstart

Neueste zuerst. Jeder Eintrag hat dieselbe Form, weil der Upgrade-Skill ihn liest.
Aufbau und Regeln der Einträge stehen in [docs/versioning.md](docs/versioning.md);
`_meta/check_release.py` erzwingt sie.


**Zur 0.x-Linie:** Alles unterhalb von 1.0.0 ist Vorabfassung. Die Struktur steht, aber sie
ist noch nicht an genügend echten Einrichtungen erprobt. Rechne in dieser Phase mit
Änderungen, die auch bestehende Wissensbasen betreffen können. Mit 1.0.0 gilt das Setup als
produktiv erprobt.

---

## v0.2.0 — 2026-07-29

**Klasse:** MINOR, **dringend**
**Betrifft:** alle Stufen
**Dateien:** plugins/sb/skills/jumpstart/templates/check_privacy.py, plugins/sb/skills/jumpstart/templates/check_okf.py, plugins/sb/skills/jumpstart/templates/pre-commit, plugins/sb/skills/jumpstart/templates/index.md, plugins/sb/skills/jumpstart/templates/CLAUDE.md, plugins/sb/skills/jumpstart/templates/privacy-entities.example.txt, plugins/sb/skills/jumpstart/setup-guide.md, plugins/sb/skills/jumpstart-upgrade/SKILL.md, docs/tracks.md, docs/skills.md, docs/upgrade.md, docs/release-gate.md, docs/versioning.md, README.md, _meta/check_privacy.py, _meta/check_release.py, .githooks/pre-commit

### Was sich ändert

Ergebnis eines Durchlaufs aus Anwendersicht über alle drei Ausbaustufen. Drei Fehler waren
so schwer, dass sie den Zweck des Setups untergraben haben.

**Die Datenschutzprüfung war vor dem Sichern umgehbar.** Sie las den Inhalt vom
Datenträger statt aus dem, was tatsächlich zum Sichern vorgemerkt war. Eine Datei mit einem
schützenswerten Namen, die danach im Arbeitsverzeichnis bereinigt wurde, passierte die
Prüfung — gesichert wurde die unbereinigte Fassung. Das war genau der Weg, den die Prüfung
absichern soll, und es geschah lautlos. Behoben: Geprüft wird jetzt der vorgemerkte Stand.

**Die Prüfung konnte an der eigenen Wissensbasis scheitern.** Die Anleitung verlangte den
eigenen Namen und den eigenen Arbeitgeber auf der Schutzliste — beide stehen aber
zwangsläufig im eigenen Profil und in den Regeldateien. Wer sich daran hielt, konnte nie
sichern. Behoben: Die eigene Person und der eigene Arbeitgeber gehören ausdrücklich **nicht**
auf die Liste; sie sind Karrierekontext, nicht Schutzgegenstand.

**Die Wissensbasis wusste nicht, woher sie stammt.** Ohne diese Angabe fand der
Aktualisierungs-Ablauf keine Quelle. Neu ist ein Feld `setup_source` im Kopf der
Wissensbasis; das Aktualisieren holt den neuen Stand selbst und verlangt keinen Download
mehr.

**Weiter behoben:** Nicht aufgelöste Konfliktmarker gelten jetzt als harter Verstoß statt
unbemerkt in der Historie zu landen. Fehlt Python, bricht die Sicherung mit der richtigen
Begründung ab statt mit einer falschen. Windows-Benutzerpfade werden erkannt. Die Anleitung
enthält einen Selbsttest für die Sperre, den tatsächlich häufigsten Konfliktfall bei zwei
Geräten, und keine unersetzten Platzhalter mehr. Widersprüchliche Aussagen dazu, ob eine
Prüfung in Ausbaustufe 1 blockiert, sind vereinheitlicht: Sie tut es, in allen Stufen.

**Am eigenen Repository:** Die Schutzskripte liegen zweimal — als ausgelieferte Vorlage und
als Kopie, mit der sich dieses Repository selbst absichert. Die Kopie war beim Beheben der
Lücke oben nicht mitgezogen worden; das Repository arbeitete also mit dem Stand weiter, den
es gerade als fehlerhaft ausgeliefert hatte. Die Release-Prüfung vergleicht beide Orte jetzt
byteweise und verweigert die Freigabe bei Abweichung. Außerdem lief bisher die Formatprüfung
für Wissensbasen gegen dieses Repository, das keine ist — sie gehört nicht in diesen Ablauf
und ist dort entfernt.

### Migration

**Für bestehende Wissensbasen — dringend, in dieser Reihenfolge:**

1. Beide Prüfprogramme unter `_meta/` durch die neuen Fassungen ersetzen. Ohne diesen
   Schritt bleibt die Sicherung umgehbar.
2. `pre-commit` unter `.githooks/` ersetzen, falls die Sperre genutzt wird. Danach der
   Selbsttest: eine Testdatei mit einem Namen aus der eigenen Liste anlegen und committen
   wollen — der Commit muss abbrechen.
3. Aus `_meta/privacy-entities.txt` den eigenen Namen und den eigenen Arbeitgeber
   entfernen, falls sie dort stehen.
4. Im Kopf der Wurzel-`index.md` das Feld
   `setup_source: "https://github.com/dutch-vdl/sb-jumpstart"` ergänzen und
   `setup_version` auf `0.2.0` setzen.

Die Schritte 1 bis 3 betreffen die Sicherheit und sollten nicht aufgeschoben werden.

## v0.1.0 — 2026-07-29

**Klasse:** MINOR
**Betrifft:** alle Stufen
**Dateien:** keine

### Was sich ändert

Erste Fassung. Der SB Jumpstart ist ein Bauplan, mit dem Claude eine persönliche
Wissensbasis von Grund auf einrichtet: ein kurzes Interview, ein Grundgerüst aus
Markdown-Dateien, ein Regelwerk und feste Verfahren für die wiederkehrenden Aufgaben. Der
Anwender braucht dafür einen Claude-Zugang und einen leeren Ordner — sonst nichts.

**Enthalten:**

* **Eine Anleitung in sieben Phasen**, die sich an Claude richtet und nicht an den
  Anwender — vom Interview über das Grundgerüst und das Regelwerk bis zur ersten Befüllung
  mit vorhandenem Material und den Routinen.
* **Drei Ausbaustufen** — *Lokal* (ein Ordner, kein Zusatzwerkzeug), *Verteilt* (eigenes
  Repository, mehrere Geräte), *Mitlaufend* (Verfahren kommen als Plugin nach). Die Stufe
  wird nicht abgefragt, sondern aus der Situation abgeleitet; der Aufstieg ist jederzeit
  möglich, und im Zweifel gewinnt die kleinere.
* **Vollständige Vorlagen** für den Wissensbestand: Bedienungsanleitung, Konventionen,
  Format-Regeln, Inhaltsverzeichnis, Änderungstagebuch, Workspace-Regeln. Keine leeren
  Gerüste — die Regeln sind ausformuliert, nur das Persönliche wird im Interview gefüllt.
* **Zwei Prüfprogramme.** Eines prüft die Formattreue (Frontmatter, Pflichtfelder,
  Versionskonsistenz), das andere findet Namen und Muster, die nicht nach außen dürfen —
  gegen eine lokale Liste, die selbst nie versioniert wird. Beide kommen mit Python ohne
  Zusatzpakete aus.
* **Sechs Verfahren:** Einrichten, Dokumente zu wiederverwendbarem Wissen destillieren,
  externe Quellen aufnehmen, wöchentlicher Pflegedurchlauf, Stand sichern, Setup
  aktualisieren. Sie funktionieren in allen Stufen — auch ohne Installation, weil es
  Textdateien sind.
* **Datenschutz als Konstruktionsprinzip:** kein Rückkanal, nichts verlässt den eigenen
  Rechner ohne ausdrückliche Zustimmung, und die Wahl der Ausbaustufe wird ausdrücklich als
  Entscheidung über die eigenen Daten behandelt statt als Komfortfrage.

**Bewusst offen:** Wie weit die Prüfprogramme im Alltag lokal laufen müssen, hängt von der
Umgebung ab — das klärt Claude beim Aufsetzen. Und alle Verfahren tragen einen
Reifevermerk: Ein Ablauf, der erst zweimal gelaufen ist, sollte nicht so tun, als wäre er
erprobt.

### Migration

Entfällt — Erstveröffentlichung. Wer neu aufsetzt, folgt der `README.md`.
