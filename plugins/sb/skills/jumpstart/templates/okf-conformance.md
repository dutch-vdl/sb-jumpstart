---
type: Reference
title: OKF-Konformität & Kontrolle
description: Regeln des Open Knowledge Format v0.2, bewusste Abweichungen dieser Basis und das Prüfskript.
tags: [meta, okf, konformität]
generated: { by: human:<vorname-nachname>, at: <JJJJ-MM-TT>T00:00:00Z }
---

# Abgrenzung

Hier stehen die **OKF-Standard-Regeln** (extern, nicht von uns gesetzt) sowie die Stellen,
an denen diese Basis bewusst davon abweicht. Die **eigenen Festlegungen** — Typ-Vokabular,
Ordnerlogik, Extrakt-Regel, Versionierung — stehen getrennt in `conventions.md`.

Bei Detailfragen zur Konformität gilt die Spezifikation, nicht diese Datei. Quellen am
Ende — dort steht auch, welche Fassung derzeit maßgeblich ist.

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

# Trust-Signale (v0.2)

v0.2 ist ein **additives** Update: `type` bleibt das einzige Pflichtfeld, alle neuen Felder
sind freiwillig. Sie beantworten vier Fragen, die eine wachsende Basis irgendwann stellt —
woher kommt das, wer steht dafür ein, gilt es noch, und wo im Lebenszyklus steht es.

| Feld | Frage | Form |
|------|-------|------|
| `generated` | Wer hat es erzeugt, wann? | `{ by: human:<kennung>, at: <ISO-8601> }`; Akteure als `human:<id>` oder `agent:<id>` |
| `sources` | Worauf stützt es sich? | Liste mit `id`, `title`, `resource`; optional `author`, `last_modified` |
| `verified` | Wer hat es bestätigt? | Liste aus `{ by: <akteur>, at: <ISO-8601> }` |
| `stale_after` | Bis wann gilt es? | absolutes Datum `JJJJ-MM-TT` |
| `status` | Wo im Lebenszyklus? | genau einer von `draft`, `stable`, `deprecated` |

Aus `verified` ergibt sich die Vertrauensstufe eines Concepts: kein Eintrag heißt
**ungeprüft**, ein reiner Maschinen-Akteur **maschinell bestätigt**, mindestens ein
`human:`-Eintrag **von einem Menschen geprüft**. Ungeprüft ist kein Mangel — es ist der
Normalzustand frisch geschriebener Concepts und nur dann ein Befund, wenn das Concept
gleichzeitig sein `stale_after` überschritten hat.

**Der fünfte Baustein bleibt draußen.** v0.2 kennt zusätzlich eine *Attested Computation* —
einen Concept-Typ, der eine ausgeführte Berechnung samt Quittung und maschinellem Prüfer
belegt. Er ist für Datenplattformen gebaut, in denen Zahlen aus Abfragen entstehen. In einer
persönlichen Wissensbasis gibt es diesen Fall nicht; der Erklärungsaufwand wäre größer als
der Nutzen. Wer ihn braucht, findet ihn in der Spezifikation.

# Was gegenüber v0.1 umbenannt wurde

* `timestamp` → `generated.at` (plus `generated.by`, das es vorher nicht gab).
* Die Body-Sektion `# Citations` → das Frontmatter-Feld `sources`.

Beides ist rückwärtskompatibel: Eine v0.1-Basis bleibt gültig, ein v0.2-Leser fällt auf die
alte Form zurück. Der Grund, trotzdem umzustellen: In der alten Form steht die Herkunft im
Fließtext und ist nur von Menschen lesbar. In der neuen steht sie im Frontmatter und ist
maschinell prüfbar — genau der Unterschied, der eine Basis ab einigen hundert Dateien noch
kontrollierbar hält.

# Was ausdrücklich kein Verstoß ist

Fehlende optionale Felder. Unbekannte `type`-Werte. Eigene Felder über den Standard hinaus —
sie müssen von Werkzeugen unverändert durchgereicht werden. Ein Concept ohne `verified`.
Ein toter Cross-Link: Er kann auf Wissen zeigen, das noch nicht geschrieben ist, und ist
deshalb ein Hinweis, kein Fehler.

# Bewusste Abweichungen

<Jede Abweichung mit Begründung eintragen. Startbestand:>

* **`log.md`-Überschriften tragen zusätzlich die Version.** Format
  `## JJJJ-MM-TT — vX.Y.Z` statt des reinen Datums. Grund: Die Version ist bei uns an den
  Sicherungsvorgang gekoppelt; die Historie soll ohne Zweitquelle lesbar sein.
* **Die Wurzel-`index.md` trägt Frontmatter.** Der Standard erlaubt dort nur `okf_version`.
  Wir brauchen die Wurzeldatei zusätzlich als Träger von `version`, `setup_version`,
  `setup_source` und `setup_track`. Für `index.md` **unterhalb** der Wurzel gilt die
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
* nicht aufgelöste Merge-Konfliktmarker

**Weiche Hinweise** (Exit-Code 0, aber sichtbar):

* toter bundle-relativer Link
* Concept ohne `generated`
* Concept trägt noch das alte `timestamp` statt `generated`
* `generated` ohne `by` oder ohne `at`
* `status` mit einem Wert außerhalb von `draft`, `stable`, `deprecated`
* `stale_after` in unlesbarem Datumsformat
* `stale_after` überschritten — das Concept braucht eine Re-Verifikation

Die harten Kriterien prüfen **Konformität**, die weichen prüfen **Pflegezustand**. Deshalb
blockieren die weichen nichts: Ein überschrittenes Verfallsdatum ist kein Formatfehler, und
ein Sicherungsvorgang, der daran scheitert, würde nur dazu führen, dass die Prüfung
umgangen wird.

Übersprungen werden `.git`, `.github`, `_meta`, `workspace`, der Skill-Ordner und
Editor-Verzeichnisse. `CLAUDE.md`, `README.md` und `log.md` in der Wurzel tragen bewusst
kein Frontmatter und werden nicht geprüft.

# Quellen

**Stand der Spezifikation (bitte beim Lesen prüfen):** v0.2 wurde im Juli 2026 im
Google-Cloud-Blog veröffentlicht und ist dort mit allen Feldern beschrieben. Die
Spezifikationsdatei im Projekt-Repository trug zum Zeitpunkt dieser Fassung noch die
Versionsangabe 0.1 — der Blogbeitrag ist bis auf Weiteres die maßgebliche Quelle für die
Trust-Signale. Sobald `SPEC.md` nachgezogen ist, gilt wieder die Spezifikation, und diese
Datei ist gegen sie abzugleichen.

1. [OKF v0.2 adds trust signals — Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals)
2. [OKF-Spezifikation — SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
3. [knowledge-catalog — OKF (GitHub)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
4. [„How the Open Knowledge Format can improve data sharing" — Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/)

<!-- JUMPSTART-VORLAGE — Hinweisblock beim Anlegen entfernen.
     Diese Datei hält die EXTERNEN Format-Regeln fest. Eigene Festlegungen gehören nach
     conventions.md. Der Abschnitt "Bewusste Abweichungen" ist der eigentliche Zweck:
     Er macht Standardtreue prüfbar statt behauptet.
     Der Abschnitt "Quellen" trägt einen Stand-Vermerk — beim nächsten Wartungsdurchlauf
     prüfen, ob die Spezifikationsdatei inzwischen auf v0.2 steht, und ihn dann streichen.
     Alle <spitzen Klammern> sind aus dem Interview zu füllen. -->
