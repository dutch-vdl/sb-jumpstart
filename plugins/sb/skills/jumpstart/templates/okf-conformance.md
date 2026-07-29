---
type: Reference
title: OKF-Konformität & Kontrolle
description: Regeln des Open Knowledge Format v0.1, bewusste Abweichungen dieser Basis und das Prüfskript.
tags: [meta, okf, konformität]
timestamp: <JJJJ-MM-TT>T00:00:00Z
---

# Abgrenzung

Hier stehen die **OKF-Standard-Regeln** (extern, nicht von uns gesetzt) sowie die Stellen,
an denen diese Basis bewusst davon abweicht. Die **eigenen Festlegungen** — Typ-Vokabular,
Ordnerlogik, Extrakt-Regel, Versionierung — stehen getrennt in `conventions.md`.

Bei Detailfragen zur Konformität gilt die Spezifikation, nicht diese Datei. Quellen am
Ende.

# Die Regeln des Formats

* **Bundle.** Die Wissensbasis ist ein Verzeichnisbaum („Bundle") aus Markdown-Dateien.
  Die Wurzel des Bundles ist der Bezugspunkt für alle bundle-relativen Pfade.
* **Concept.** Ein Concept ist **genau eine Datei**. Der Pfad ist seine Identität — wer
  eine Datei verschiebt, ändert die Identität und muss die Verweise nachziehen.
* **Frontmatter.** Jedes Concept beginnt mit einem YAML-Block zwischen `---`-Zeilen.
  Einziges Pflichtfeld ist `type`. Alle weiteren Felder sind frei; empfohlene Felder stehen
  in `conventions.md`.
* **Reservierte Dateinamen.** `index.md` ist das Inhaltsverzeichnis eines Ordners, `log.md`
  die Änderungshistorie. Beide sind keine Concepts und tragen kein `type`.
* **Cross-Linking.** Verweise zwischen Concepts als bundle-relative Links mit führendem
  `/`. Sie bleiben stabil, unabhängig davon, wo das Bundle im Dateisystem liegt.
* **Konformität.** Ein Bundle ist konform, wenn jedes Concept ein gültiges Frontmatter mit
  `type` trägt und die reservierten Dateinamen ihrer Rolle entsprechen.

# Bewusste Abweichungen

<Jede Abweichung mit Begründung eintragen. Startbestand:>

* **`log.md`-Überschriften tragen zusätzlich die Version.** Format
  `## JJJJ-MM-TT — vX.Y.Z` statt des reinen Datums. Grund: Die Version ist bei uns an den
  Sicherungsvorgang gekoppelt; die Historie soll ohne Zweitquelle lesbar sein.
* **Die Wurzel-`index.md` trägt Frontmatter.** Der Standard sieht für `index.md` kein
  Frontmatter vor. Wir brauchen die Wurzeldatei als Träger von `version`, `okf_version`,
  `setup_version` und `setup_track`. Für `index.md` **unterhalb** der Wurzel gilt die
  Standardregel unverändert — kein Frontmatter, und das Prüfskript wertet einen Verstoß
  hart.
* **`workspace/` ist vom Format ausgenommen.** Die operative Schicht ist bewusst kein
  Wissensbestand: kein Frontmatter, keine Versionierung, vom Prüfskript übersprungen.
* <Weitere Abweichungen hier ergänzen, jeweils mit Grund. Eine Abweichung ohne Begründung
  ist ein Fehler, kein Merkmal.>

# Prüfskript

```
python3 _meta/check_okf.py
```

Aufruf aus der Wurzel der Wissensbasis. Nur Standardbibliothek, keine Installation nötig.

**Harte Verstöße** (Exit-Code 1, es wird nicht gesichert):

* fehlendes oder nicht geschlossenes Frontmatter in einem Concept
* fehlendes Pflichtfeld `type`
* `index.md` außerhalb der Wurzel mit Frontmatter
* Wurzel-`index.md` ohne `version`
* `version` in der Wurzel-`index.md` weicht vom jüngsten `log.md`-Eintrag ab

**Weiche Hinweise** (Exit-Code 0, aber sichtbar):

* toter bundle-relativer Link
* Concept ohne `timestamp`

Übersprungen werden `.git`, `.github`, `_meta`, `workspace`, der Skill-Ordner und
Editor-Verzeichnisse. `CLAUDE.md`, `README.md` und `log.md` in der Wurzel tragen bewusst
kein Frontmatter und werden nicht geprüft.

# Quellen

1. [OKF-Spezifikation v0.1 — SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
2. [knowledge-catalog — OKF (GitHub)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
3. [„How the Open Knowledge Format can improve data sharing" — Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/)

<!-- JUMPSTART-VORLAGE — Hinweisblock beim Anlegen entfernen.
     Diese Datei hält die EXTERNEN Format-Regeln fest. Eigene Festlegungen gehören nach
     conventions.md. Der Abschnitt "Bewusste Abweichungen" ist der eigentliche Zweck:
     Er macht Standardtreue prüfbar statt behauptet.
     Alle <spitzen Klammern> sind aus dem Interview zu füllen. -->
