# Versionierung und Releases des Jumpstart

*Betriebsanleitung für den Betreiber des Repos. Anwender brauchen davon nur den Abschnitt
„Was ein Anwender davon merkt".*

## Zwei Versionslinien, die nichts miteinander zu tun haben

Das ist die Unterscheidung, an der man sonst hängenbleibt:

* Die **Setup-Version** (`VERSION` in diesem Repo) misst die Reife des **Bauplans** — der
  Anleitung, der Vorlagen, der Skills, der Prüfskripte.
* Die **Basis-Version** (`version` in der Wurzel-`index.md` eines Anwenders) misst die Reife
  **seines Wissens**.

Sie laufen unabhängig. Jemand kann bei Setup 1.4.0 stehen und seine Basis auf 2.31.0 haben.
Im Hub des Anwenders wird die Setup-Version als `setup_version` mitgeführt, damit der
Upgrade-Skill weiß, wo er ansetzt.

## Was welcher Sprung bedeutet

Semantic Versioning, übertragen auf einen Bauplan. Maßstab ist immer: **Was kostet es einen
bestehenden Hub, das zu übernehmen?**

**MAJOR** — bestehende Hubs können nicht ohne Handarbeit folgen. Ordnerlogik geändert, ein
Pflichtfeld eingeführt oder entfernt, eine Regel gestrichen, auf der andere aufbauen, eine
Ausbaustufe umgebaut. Ein MAJOR **muss** einen Migrationshinweis tragen, der Schritt für
Schritt ausführbar ist. Ohne den ist es kein MAJOR, sondern ein Bruch.

**MINOR** — additive Erweiterung. Neue Regel, neuer Skill, neue Vorlage, neuer Abschnitt.
Bestehende Hubs bleiben ohne Änderung gültig; wer die Neuerung nicht übernimmt, verliert
nichts.

**PATCH** — Korrektur, Präzisierung, Formulierung, Metadaten. Nichts, was jemand aktiv
nachziehen müsste.

Die Sprunghöhe richtet sich nach der **größten** Änderungsklasse im Release. Ein Release mit
einer Korrektur und einer neuen Regel ist MINOR.

**Sicherheitsrelevante Korrekturen** sind eine Ausnahme von der Gelassenheit: Sie können
PATCH sein und trotzdem im Changelog als *dringend* markiert werden. Der Upgrade-Skill legt
sie dann nicht als *optional* vor, sondern als *empfohlen* mit Begründung.

## Wo die Version steht

Vier Orte, und jeder hat genau einen Zweck:

| Ort | Zweck |
|-----|-------|
| `VERSION` (Repo-Wurzel) | Die maßgebliche Angabe. Eine Zeile, von Mensch und Skript ohne Parser lesbar. |
| `plugins/sb/VERSION` | Kopie **innerhalb** des Plugins. Notwendig, weil bei installierten Plugins nur der Plugin-Ordner beim Anwender landet — ohne diese Kopie findet der Upgrade-Skill bei Stufe 3 keine Version. |
| `plugins/sb/.claude-plugin/plugin.json` → `version` | Steuert die Update-Erkennung der Plugin-Mechanik. Ohne Änderung dieses Feldes bekommt niemand ein Update, egal wie viele Commits gepusht werden. |
| Git-Tag `vX.Y.Z` + GitHub-Release | Der Anker der Historie **und** der Auslöser der Benachrichtigung. |

**Nicht** in `.claude-plugin/marketplace.json`. Die Dokumentation rät ausdrücklich davon ab,
`version` an beiden Stellen zu führen: Der Wert aus `plugin.json` gewinnt kommentarlos, ein
im Marketplace gepflegter Wert täuscht also ein Release vor, das niemanden erreicht.

Der Abgleich der drei Dateiorte wird nicht per Sorgfalt sichergestellt, sondern von
`_meta/check_release.py` erzwungen.

## Das Changelog

`CHANGELOG.md`, neueste zuerst. Jeder Eintrag hat dieselbe Form, weil der Upgrade-Skill ihn
lesen muss:

```markdown
## v1.2.0 — 2026-08-14

**Klasse:** MINOR
**Betrifft:** alle Stufen
**Dateien:** templates/conventions.md, plugins/sb/skills/weekly-review/SKILL.md

### Was sich ändert
Zwei bis fünf Sätze in Prosa. Was ist neu, warum, was wird dadurch besser.

### Migration
Was ein bestehender Hub tun muss. Bei PATCH oft „nichts". Bei MINOR die Ergänzung,
die übernommen werden kann. Bei MAJOR eine ausführbare Schrittfolge.
```

Die Felder im Einzelnen:

* **Klasse** — `MAJOR`, `MINOR` oder `PATCH`. Bei sicherheitsrelevanten Korrekturen
  zusätzlich `dringend`.
* **Betrifft** — `alle Stufen` oder eine Aufzählung (`Stufe 2, Stufe 3`). Der Upgrade-Skill
  blendet damit aus, was für den jeweiligen Anwender nicht gilt.
* **Dateien** — Pfade relativ zur Repo-Wurzel. Damit erkennt der Upgrade-Skill, ob die
  betroffene Datei im Hub des Anwenders überhaupt existiert und ob sie dort individuell
  angepasst wurde.
* **Migration** — der Teil, der zählt. Ein Eintrag ohne Migrationsabschnitt gilt als
  unfertig; `check_release.py` beanstandet ihn.

## Der Release-Ablauf

1. **Änderungen abschließen.** Rückfluss-Vorschläge eingearbeitet, Formulierungen fertig.
2. **Klasse bestimmen** nach der größten Änderung im Batch.
3. **Version setzen** — an allen drei Dateiorten gleichzeitig.
4. **Changelog-Eintrag schreiben**, vollständig, mit Migrationsabschnitt.
5. **Release-Gate fahren** (siehe `release-gate.md`): Diff gegen die Abstraktionsregel
   lesen, `check_privacy.py`, `check_okf.py` — und `check_release.py` für die
   Versionskonsistenz.
6. **Freigabe einholen.** Kein Release läuft automatisch durch.
7. **Committen und pushen.** Der Rest passiert in der Automatik.

Beim Push auf den Hauptbranch setzt `.github/workflows/release.yml` das Tag `vX.Y.Z` aus
`VERSION` und erzeugt daraus einen **GitHub-Release**, dessen Beschreibung der zugehörige
Changelog-Abschnitt ist.

**Warum ein Release und nicht nur ein Tag:** Die Benachrichtigung, die Anwender abonnieren
(„Watch → Custom → Releases"), hängt am Release, nicht am Tag. Ein reines Tag erzeugt keine
Mail. Das ist die Stelle, an der die Benachrichtigungskette sonst still bricht.

## Was ein Anwender davon merkt

* Er hat einmalig „Watch → Custom → Releases" gesetzt und bekommt bei jedem Release eine
  Mail mit den Änderungen im Klartext.
* Er sagt Claude „prüf mein Setup gegen den neuen Stand". Der Upgrade-Skill vergleicht seine
  `setup_version` mit `VERSION`, liest die Changelog-Einträge dazwischen, filtert auf seine
  Stufe und legt eine Entscheidungsliste vor.
* Bei Stufe 3 kommen die **Skills** zusätzlich über die Plugin-Mechanik — aber nur die.
  Vorlagen und Regelwerk in seinem Hub fasst kein Plugin-Update an; dafür braucht es den
  Upgrade-Skill genauso wie bei Stufe 1 und 2.

## Was bewusst nicht automatisiert ist

Kein automatisches Release, keine automatische Übernahme beim Anwender. Beides ist eine
Entscheidung, die ein Mensch trifft — auf der Seite, die veröffentlicht, und auf der, die
übernimmt.
