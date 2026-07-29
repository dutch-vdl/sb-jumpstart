---
name: weekly-review
description: Wöchentlicher Pflegedurchlauf für die Wissensbasis – Destillat aus dem Workspace, Aktualitätsprüfung nach Haltbarkeit, Aufgaben-Triage, Regel-Ernte aus den Korrekturen der Woche und Konsistenzkontrolle inklusive Prüfskripten. Verwenden bei „Weekly Review", „Wochendurchlauf", „räum die Basis auf", „Pflegedurchlauf", „was ist liegengeblieben" – und proaktiv vorschlagen, wenn seit dem letzten Durchlauf erkennbar mehr als eine Woche vergangen ist.
---

# Weekly Review — der Pflegedurchlauf

## Was dieser Skill tut

Er ist die eine Routine, die Workspace und Wissensbestand verbindet und beide frisch hält.
Rund fünfzehn Minuten, fester Ablauf in fünf Blöcken, als **knapper Bericht mit
Entscheidungspunkten** — kein stiller Umbau.

**Der Durchlauf ersetzt keine Einzelaufnahme.** Er sammelt ein, was liegengeblieben ist;
was während der Woche dokumentierenswert war, wird auch während der Woche angeboten.

## Block 1 — Destillat

Den Workspace sichten: Was hat sich als generalisierbar erwiesen? Kandidatenliste mit
Typ-Vorschlag und **einem Satz Begründung** je Kandidat. Aufnahme nur mit Freigabe und über
die Extrakt-Regel. Danach den Workspace straffen — Erledigtes raus.

**Löschen kannst du nicht.** In verbundenen Ordnern sind `rm` und `rmdir` nicht erlaubt, nur
Verschieben. „Straffen" heißt deshalb: Erledigtes nach `_zu-loeschen/` in der Wurzel
verschieben (der Ordner ist von beiden Prüfungen und von der Versionierung ausgenommen) und
**berichten, was dorthin gewandert ist**. Das endgültige Löschen macht die Person selbst.
Behaupte nie, aufgeräumt zu haben, wenn nur verschoben wurde.

## Block 2 — Aktualität

Nach Haltbarkeit gestaffelt: **Insights** am gründlichsten, **Learning** auf offensichtliche
Veralterung, **Frameworks** in der Regel gar nicht.

Steuerung über den Abschnitt `# Haltbarkeit / Stand`: Geprüft wird der **verfallende
Anteil**, der stabile Kern bleibt unangetastet. Concepts ohne diesen Vermerk, die ihn
bräuchten, als Nachtrag vorschlagen.

## Block 3 — Aufgaben-Triage

Erledigtes raus, Überfälliges nach vorn, Neues aus den Notizen der Woche einsammeln. Dazu
die Marker-Governance anwenden: Unbeschaffbares aktiv verwerfen (mit Vermerk), pausierte
Vorhaben parken, wartende Marker in terminierte Wiedervorlagen umschreiben, gefundene
Originale sofort verankern.

**Jede Aufgabe braucht ein Datum — Aufgaben ohne Datum sind Absichten.**

## Block 4 — Regel-Ernte

Was hat die Nutzung der Woche über die Zusammenarbeit gelehrt? Korrekturen, wiederkehrende
Entscheidungen und Stil-Erkenntnisse als Regel-Kandidaten vorschlagen; wiederholte Abläufe
als Skill-Kandidaten. Eine zweimal angemahnte Regel ist Regelwerk, keine Präferenz.

Aufnahme nur mit Freigabe.

## Block 5 — Konsistenz und Ausbaustufen

* Beide Prüfskripte laufen lassen: `python3 _meta/check_okf.py` und
  `python3 _meta/check_privacy.py`.
* **Entitätenliste pflegen:** neue Kunden, Projekte, Kontakte der letzten Wochen in
  `_meta/privacy-entities.txt` nachtragen. Das ist der feste Termin dafür — ohne ihn
  veraltet die Liste und die Prüfung wird wirkungslos.
* Frontmatter vollständig? Version und `log.md` synchron? Ab Stufe 2 zusätzlich: stimmt der
  Repository-Stand, gibt es ungesicherte Änderungen?
* **Hat sich die berufliche Situation geändert?** Ein Arbeitgeberwechsel ändert die
  Entitätenliste: Der bisherige Arbeitgeber wird vom Klärungsfall (`?Name`) zur Sperre
  (`Name`), der neue umgekehrt zum Klärungsfall. Die bestehenden Karrierestationen und
  `resource`-Pfade bekommen dann `jumpstart-ignore` mit Begründung — sonst blockiert der
  eigene Lebenslauf jede weitere Sicherung. Einmal fragen, nicht jede Woche.
* Offene Ausbaustufen aus `CLAUDE.md` prüfen. Ist die Basis so gewachsen, dass der Aufstieg
  auf die nächste Stufe oder ein Backup der Asset Library sinnvoll wird? Dann **einmalig**
  erinnern und die Entscheidung notieren — nicht jede Woche erneut.

## Optionaler Block 6

Wer die Basis für messbare Ziele nutzt, kann einen Kennzahlen-Puls ergänzen. Rollenabhängig,
gehört nicht in jedes Setup.

## Abschluss

Bericht vorlegen, Entscheidungen einholen, dann Sichern vorschlagen — der Durchlauf ist ein
Sicherungsvorgang, also **ein** Versionsschritt.

---

## Der Termin

Der Durchlauf braucht einen Auslöser, sonst findet er nicht statt. Zwei Wege, Empfehlung
zuerst: eine **geplante Aufgabe**, die wöchentlich feuert (nach dem Anlegen einmal manuell
auslösen, damit die Werkzeugfreigaben sitzen), oder ein **Eintrag in `workspace/TASKS.md`
mit Datum** als Minimum. Fehlt beides, schlag es beim ersten Durchlauf vor.

---

*Bei Widerspruch zwischen diesem Skill und `conventions.md` im Hub gilt `conventions.md`.*

*Status: Entwurf. Offener Kalibrierungspunkt: ob fünf Blöcke in fünfzehn Minuten realistisch
sind oder ob Block 2 und 5 in einen zweiwöchigen Takt gehören.*
