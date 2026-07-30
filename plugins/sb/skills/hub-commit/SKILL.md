---
name: hub-commit
description: Den Stand der Wissensbasis sichern – Änderungen sichten, Versionsschritt bestimmen, Änderungshistorie schreiben, Format- und Datenschutzprüfung als Sperre, bei Git-Betrieb zusätzlich Commit mit Conventional-Commits-Nachricht. Verwenden bei „sichere den Stand", „commit", „einchecken", „Stand festhalten", „Version hochzählen", „Release" – und immer dann, wenn eine Arbeitssitzung an der Wissensbasis zu Ende geht und die Änderungen festgehalten werden sollen.
---

# Hub-Commit — den Stand sichern

## Was dieser Skill tut

Er schließt eine Arbeitssitzung an der Wissensbasis ab: Er bestimmt genau **einen**
Versionsschritt, schreibt die Änderungshistorie, lässt die Prüfungen laufen und — ab
Ausbaustufe 2 — committet.

Die Regel dahinter: **ein Sicherungsvorgang = ein Versionsschritt.** Während der Arbeit wird
nie vorgebumpt.

## Ablauf

**1. Stufe feststellen.** `setup_track` im Frontmatter der Wurzel-`index.md`. Bei `lokal`
entfallen die Schritte 2, 7 und 8.

**2. Realen Stand einlesen (ab Stufe 2).** Version, letzte Commits, geänderte Dateien
frisch aus dem Repository lesen — **nicht dem Sitzungskontext trauen**. Wer parallel an
mehreren Geräten oder in mehreren Sitzungen arbeitet, hat sonst regelmäßig einen falschen
Ausgangspunkt. Bei Abweichung zwischen lokalem Stand und Remote: erst klären, dann sichern.

**3. Änderungen sichten.** Was hat sich geändert, was davon soll in den Stand? Inzidentelle
Dateien — Editor-Verzeichnisse, temporäre Dateien, Betriebssystem-Müll — werden
aussortiert, nicht mitgenommen.

**4. Versionsschritt bestimmen.** Die Sprunghöhe richtet sich nach der **größten**
Änderungsklasse im Batch: **MAJOR** bei strukturellem Umbau oder grundlegender
Neubewertung, sonst **MINOR** bei additiver Erweiterung, sonst **PATCH** bei Korrektur,
Präzisierung oder Metadaten. Den Vorschlag mit einem Satz begründen.

**5. Version und Historie setzen.** `version` in der Wurzel-`index.md`, dazu **ein**
`log.md`-Eintrag im Format `## JJJJ-MM-TT — vX.Y.Z`, neueste zuerst. Mehrere Änderungen
werden zu Bullets unter *einer* Versionsüberschrift, nicht zu mehreren Einträgen.

**6. Prüfungen als Sperre.**

```
python3 _meta/check_okf.py
python3 _meta/check_privacy.py
```

**Bei hartem Formatverstoß oder einem Datenschutz-Treffer: stoppen, melden, nicht sichern.**
Das ist keine Empfehlung. Datenschutz-Treffer werden entfernt oder abstrahiert; wer einen
bewusst freigibt, schreibt `jumpstart-ignore` **mit Begründung** daneben.

**Weiche Hinweise sperren nicht.** Ein überschrittenes `stale_after` oder ein fehlendes
`generated` ist ein Pflegebefund, kein Formatfehler — er gehört in den Weekly Review, nicht
in den Abbruch. Wer weiche Hinweise wie Sperren behandelt, gewöhnt sich an, Prüfungen zu
übergehen; dann wirkt auch die harte nicht mehr.

**7. Commit vorschlagen (ab Stufe 2).** Nachricht nach Conventional Commits:
`typ(scope): kurzbeschreibung`. Nur die gewünschten Dateien stagen. **Explizite Freigabe
einholen**, dann committen.

**8. Push bleibt beim Menschen.** Ein Klick im Git-Werkzeug. So liegt nie ein Zugangs-Token
in der Claude-Umgebung. **Lokal wird nicht getaggt** — das Tag setzt die GitHub Action beim
Push aus dem `version`-Feld; es erscheint lokal beim nächsten Abgleich.

## Zwei Fallstricke

* **Version ohne Log oder Log ohne Version** ist ein harter Verstoß und wird vom Prüfskript
  gefunden. Beides gehört in denselben Schritt.
* **Historie säubern heißt Repository neu anlegen.** Ist versehentlich etwas Vertrauliches
  eingecheckt worden, genügt ein Force-Push nicht — alte Tags halten die Commits
  erreichbar. Deshalb wird **vor** dem Commit geprüft, nicht danach.

---

*Bei Widerspruch zwischen diesem Skill und `conventions.md` im Hub gilt `conventions.md`.*

*Status: Entwurf. Offener Kalibrierungspunkt: ob Schritt 4 die Sprunghöhe zuverlässig
trifft — im Zweifel lieber nachfragen als raten.*
