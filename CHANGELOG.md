# Änderungen am SB Jumpstart

Neueste zuerst. Jeder Eintrag hat dieselbe Form, weil der Upgrade-Skill ihn liest.
Aufbau und Regeln der Einträge stehen in [docs/versioning.md](docs/versioning.md);
`_meta/check_release.py` erzwingt sie.


**Zur 0.x-Linie:** Alles unterhalb von 1.0.0 ist Vorabfassung. Die Struktur steht, aber sie
ist noch nicht an genügend echten Einrichtungen erprobt. Rechne in dieser Phase mit
Änderungen, die auch bestehende Wissensbasen betreffen können. Mit 1.0.0 gilt das Setup als
produktiv erprobt.

---

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
