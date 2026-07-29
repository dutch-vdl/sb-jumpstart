# Arbeitsregeln für dieses Repository

**Wer hier richtig ist:** Diese Datei richtet sich an den **Betreuer** dieses Repositorys —
an die Person, die den SB Jumpstart weiterentwickelt und veröffentlicht.

**Wer hier falsch ist:** Wenn du gerade dabei bist, dir eine eigene Wissensbasis
einzurichten, ist das hier **nicht** deine Anleitung. Deine steht in `README.md` und in
`plugins/sb/skills/jumpstart/setup-guide.md`. Die `CLAUDE.md`, die deine Wissensbasis später
selbst steuert, entsteht während der Einrichtung aus einer Vorlage — sie hat mit dieser Datei
nichts zu tun.

## Was dieses Repository ist

Ein **Bauplan zur Weitergabe**, kein Wissensbestand. Es enthält eine Anleitung, Vorlagen,
zwei Prüfskripte und sechs Verfahren als Plugin. Es enthält **keine** Inhalte, die aus einer
persönlichen oder vertraulichen Wissensbasis stammen.

Daraus folgt der wichtigste Unterschied zum Alltag in einer Wissensbasis: Hier wird nicht
gesammelt, sondern **abstrahiert und ausgeliefert**.

## Die vier Regeln

**1. Abstrahieren statt übernehmen.** Erkenntnisse aus einer privaten Wissensbasis fließen
nur **neu formuliert** hier ein, nie als Textübernahme. Ein Verfahren für einen bestimmten
Fall wird zur allgemeinen Regel für die Klasse von Fällen.

*Faustregel für jede Passage:* Ergibt sie ohne den konkreten Fall noch Sinn, muss der Fall
raus. Trägt sie ohne ihn nicht mehr, gehört sie gar nicht ins Paket.

**2. Vorlage über Kopie, nie umgekehrt.** Die Schutzskripte liegen zweimal: als ausgelieferte
Vorlage unter `plugins/sb/skills/jumpstart/templates/` und als aktive Betriebskopie unter
`_meta/` beziehungsweise `.githooks/`. Wird an einer Vorlage etwas korrigiert, muss die Kopie
nachgezogen werden — sonst arbeitet dieses Repository mit einem älteren Schutzstand als dem,
den es weitergibt. `_meta/check_release.py` erzwingt den Gleichstand byteweise.

**3. Keine Formatprüfung auf dieses Repository.** `check_okf.py` prüft Wissensbasen. Dieses
Repository ist keine (kein Wurzel-`index.md`, kein `log.md`). Das Skript liegt hier
ausschließlich als Vorlage und läuft beim Anwender, nicht hier.

**4. Reihenfolge des Release-Gates einhalten.** Der vollständige Ablauf steht in
`docs/release-gate.md`, die Versionslogik in `docs/versioning.md`. Kurzfassung: Diff gegen
die Abstraktionsregel lesen, `python3 _meta/check_privacy.py`, Version an allen drei
Dateiorten setzen, Changelog-Eintrag mit Migrationsabschnitt schreiben,
`python3 _meta/check_release.py`, Freigabe einholen, committen und pushen. Tag und
GitHub-Release erzeugt die Automatik aus `VERSION`.

## Was nicht ins Repository gehört

* `_meta/privacy-entities.txt` — die Entitätenliste. Sie versammelt genau das, was nicht nach
  außen darf, und ist selbst das Leck, das sie verhindern soll. Steht in `.gitignore`, wird
  **niemals** eingecheckt und **niemals** zwischen Geräten übertragen; auf einem zweiten Gerät
  wird sie neu getippt.
* Verzeichnislistings, Snapshots oder Dateilisten aus einer privaten Wissensbasis — Dateinamen
  verraten, was die Abstraktionsregel aus den Inhalten entfernt.
* Kundennamen, Kennzahlen Dritter, Personennamen, Konditionen — in keiner Datei, auch nicht in
  Datei- und Ordnernamen, auch nicht in Beispielen. Beispiele verwenden erfundene Platzhalter.

## Betrieb

Kein Git-Token in der Arbeitsumgebung. Commit und Tag laufen lokal, der **Push bleibt beim
Betreuer**. Änderungen ohne Versionssprung (etwa an dieser Datei) lösen bewusst keinen Release
aus — die Automatik reagiert nur auf `VERSION`.
