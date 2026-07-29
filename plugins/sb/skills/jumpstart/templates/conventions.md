---
type: Reference
title: Konventionen
description: Arbeitsregeln dieser Wissensbasis – Typ-Vokabular, Ordnerlogik, Extrakt-Regel und Versionierung.
tags: [meta, konventionen]
timestamp: <JJJJ-MM-TT>T00:00:00Z
---

# Aufbau

Diese Wissensbasis folgt dem Open Knowledge Format (OKF v0.1): ein Verzeichnisbaum aus
Markdown-Dateien mit YAML-Frontmatter. Jedes inhaltliche Dokument („Concept") hat ein
Pflichtfeld `type`. Die Dateinamen `index.md` (Inhaltsverzeichnis) und `log.md`
(Änderungshistorie) sind reserviert.

Hauptstränge: <aus Interview 1.1, je eine Zeile mit einem Satz Zweck>.

# Namensregeln

Ordner- und Dateinamen in englischem kebab-case (klein, mit Bindestrich) für Portabilität.
Anzeigename und Inhalt in <Sprache> über das Frontmatter-Feld `title` und den Body.

Auslieferbare Artefakte tragen von Anfang an ihren endgültigen Klarnamen — keine
Arbeits-Suffixe wie `-v2`, `-final`, `-neu` im Dateinamen, da diese sonst zum sichtbaren
Namen werden. Nach einer Umbenennung Referenzen per Sweep prüfen und das Ergebnis melden.

Frontmatter-Werte, die einen Doppelpunkt enthalten (etwa ein `title` der Form „Thema:
Untertitel"), in Anführungszeichen setzen — sonst bricht der YAML-Parser.

# Typ-Vokabular

| type | Verwendung |
|------|------------|
| `Framework` | Erklärt eine Strategie oder Vorgehensweise. Langlebigste Kategorie. |
| `Learning` | Guide zu einem Thema. Mittlere Haltbarkeit, kann veralten. |
| `Insight` | Externes Erkenntnismaterial: Studien, Marktdaten, Reports. Kürzeste Haltbarkeit. |
| `Deliverable` | Markdown-Extrakt eines Originals aus der Asset Library, plus Verweis darauf. |
| `Project` | Ein eigenes Vorhaben. |
| `Profile` | Verdichtetes Profil. Zwei Ausprägungen, zwei Dateien: das **Personenprofil** (Kompetenzen, Domänen, Arbeitsstil) und das **Zusammenarbeits-Profil** (`profile/zusammenarbeit.md`, wie Claude arbeiten soll). Unterschieden über `title` und `tags`. |
| `Person` | Eine relevante Person. |
| `Reference` | Meta- oder Nachschlage-Dokument. |

Das Vokabular ist erweiterbar. Neue Typen hier ergänzen, damit sie konsistent bleiben. Ein
Typ, der nur einmal vorkommt, ist meist keiner.

# Wissenskategorien & Haltbarkeit

Drei Kategorien wiederverwendbaren Wissens, nach Haltbarkeit absteigend: **Framework >
Learning > Insight.** Alle drei tragen ein `timestamp`. Die Aktualitätsprüfung im
wöchentlichen Durchlauf skaliert umgekehrt zur Haltbarkeit: Insights werden am häufigsten
geprüft und ausgemistet, Learning periodisch gesichtet, Frameworks am seltensten angefasst.

**Pro-Concept-Haltbarkeitsvermerk** (empfohlen für `Insight`, optional für `Learning`).
Mischt ein Concept einen dauerhaften Methodenkern mit verfallenden Bestandteilen — konkrete
Zahlen, Marktstände, Details einer Benutzeroberfläche —, trägt es einen Abschnitt
`# Haltbarkeit / Stand`, der beides trennt: den **stabilen Kern** (was übertragbar bleibt)
und den **verfallenden Anteil** (was mit Datum veraltet). Geprüft wird dann gezielt der
verfallende Teil; der stabile Kern bleibt unangetastet.

**Quellen ohne klassisches Original.** Erkenntnisse aus reinen Web-Quellen haben kein
Original zum Ablegen. Regel: `date` ist das **Publikationsdatum** der Quelle (ist der Tag
unbekannt, mindestens `JJJJ-MM`), `resource` zeigt auf einen **Erfassungs-Extrakt** in der
Asset Library, die Quell-URLs stehen in `source` und in einem Abschnitt `# Citations`. So
zeigt `resource` nie auf eine URL, die in einem Jahr tot ist.

# Frontmatter-Standard

Pflicht: `type`. Empfohlen: `title`, `description`, `tags`, `timestamp`. Bei `Deliverable`
zusätzlich `resource` (Verweis auf das Original als `asset:/pfad`) sowie Herkunftsfelder wie
`source_station`, `client`, `date`.

Cross-Links zwischen Concepts als bundle-relative Links mit führendem `/` — die bleiben
beim Verschieben stabil.

# Asset Library & Deliverables

Große Binärdateien (Präsentationen, PDFs, Bilder) liegen **nicht** im Wissensbestand,
sondern in einer separaten Asset Library: <Lage relativ zum Hub, z. B. „Nachbarordner
`Knowledge Asset Library`" oder „Ordner `Assets` im selben Cloud-Verzeichnis">.

**Der Ort wird relativ beschrieben, nie als absoluter Pfad.** Zwei Gründe: Absolute Pfade
sind gerätespezifisch und auf einem zweiten Gerät falsch, und sie schlagen als „Lokaler
Benutzerpfad" in der Datenschutzprüfung an — sie enthalten den Benutzernamen. Wer hier einen
Pfad wie `/Users/…` einträgt, blockiert jede weitere Sicherung, ohne dass die Fehlermeldung
den Grund nennt. Dieselbe Regel gilt für `resource`-Felder; die verwenden ohnehin `asset:/…`
relativ zur Library-Wurzel.

**Ordnerschema:** pro Arbeitgeber, Station oder Großprojekt ein Ordner in
Großbuchstaben-Kürzel; übergreifende Wissenskategorien als Buckets in Kleinschreibung
(`frameworks/`, `learning/`, `insights/`, `personal/`); `TBD/` für noch Unsortiertes.

**Wenn ein Ordnerkürzel schutzbedürftig wird.** Sprechende Kürzel sind im Alltag praktisch,
verankern aber einen Namen im `resource`-Feld jedes zugehörigen Concepts. Wird der Name
später schutzbedürftig — typischerweise nach einem Arbeitgeberwechsel —, ist das kein Fall
für Handarbeit, sondern ein Ablauf in vier Schritten:

1. Neues, neutrales Kürzel festlegen (Branche plus Jahr statt Marke, etwa `PHARMA-2024`).
2. Ordner in der Asset Library umbenennen.
3. **Referenz-Sweep über den gesamten Bestand:** alle `resource`-Felder und alle Fließtext-
   Verweise auf das alte Kürztel suchen und ersetzen. Der Sweep ist derselbe wie bei einer
   Datei-Umbenennung, nur auf `resource` ausgedehnt.
4. Prüfskripte laufen lassen und das Ergebnis melden — ein übersehener Verweis ist ein toter
   Link, kein stiller Fehler.

**Zwei-Schichten-Prinzip.** Wissensschicht: Jede Originaldatei bekommt ein
`Deliverable`-Concept — ein Markdown-Extrakt des wiederverwendbaren Inhalts plus Metadaten.
Originalschicht: Die Datei selbst bleibt in der Asset Library. Verknüpft wird über
`resource:` als Pfad relativ zur Library-Wurzel mit Präfix `asset:/…`.

**Keine Verzeichnislistings der Asset Library in den Bestand.** Dateilisten verraten über
die Namen genau das, was die Extrakt-Regel aus den Inhalten entfernt.

# Extrakt-Regel — verbindlich

**Geltungsbereich:** Schritt 1 gilt für **jede Datei im Bestand** — Concepts jedes Typs,
`log.md`, Meta- und Hilfsdateien, **auch Datei- und Ordnernamen**. Schritt 2 gilt für
`Deliverable`-Concepts.

Zwei getrennte Schritte mit verschiedenen Zwecken: **Schritt 1 schützt, Schritt 2
verbessert.**

**Leitsatz:** Der Extrakt beantwortet **„wie geht man vor"**, nicht **„was war im Fall X
konkret"**. Das Konkrete bleibt im Original und ist über `resource:` erreichbar — es geht
kein Zugriff verloren, nur die Kopie im Bestand.

## Schritt 1 — Vertraulichkeitsprüfung (immer durchführen)

Die **Prüfung** ist ausnahmslos verpflichtend; die **Entkernung** nur bei Treffer. Grund:
„Anonymisiere bei sensiblen Inhalten" verlangt eine Selbsteinschätzung, die beim Schreiben
regelmäßig ausbleibt. Eine mechanische Checkliste löst aus, wo Intuition versagt. Fünf
Fragen, dreißig Sekunden. Enthält der Entwurf …

1. **Konditionen?** Preise, Stundensätze, Margen, Vertrags- und Lizenzstaffeln — eigene wie
   fremde.
2. **Kennzahlen Dritter?** Umsätze, Nutzerzahlen, Budgets, Performance-Daten.
3. **Technische Interna?** Systemarchitektur, Tech-Stack, Zugänge, Schnittstellen,
   Sicherheitsstand.
4. **Interne Strategie?** Selbstkritik des Arbeitgebers, Wettbewerbsbewertungen,
   Sprechregeln, Pipeline-Bewertungen.
5. **Personennamen Dritter?**

Kein Treffer → weiter mit Schritt 2. Treffer → die betroffene Passage bleibt im Original,
im Extrakt steht ein kursiver Hinweis, welche Inhalte ausschließlich dort zu finden sind.

Personennamen sind der Sonderfall: Sie werden nicht gestrichen, sondern **durch die Rolle
ersetzt** („der Product Owner", „die Architektin"). Ausnahme: Personen im eigenen
Karrierekontext.

## Schritt 2 — Methodenkern ausschreiben (Qualitätsstandard)

Unabhängig von Vertraulichkeit. Ein Extrakt ist erst fertig, wenn der übertragbare Kern
**ausformuliert** ist — nicht bloß als Stichwort benannt:

* Vorgehen, Gliederungen, Entscheidungsbäume, Bewertungsraster, Argumentationsfiguren.
* Einwand-Antwort-Paare, Praxisregeln, Reihenfolge-Logiken („warum zuerst X, dann Y").
* Generalisierung: der Kern wird bewusst **vom Anlassfall abgelöst** und auf die Klasse von
  Fällen gehoben, für die er gilt.

**Testfrage:** *Brauche ich das noch, wenn ich morgen in einem anderen Kontext vor einer
ähnlichen Aufgabe stehe?*

## Aufbau des Extrakts

1. Frontmatter inkl. `resource` und Herkunftsfeldern.
2. `# Überblick` — worum ging es, welcher Dokumenttyp, welche Rolle; plus ein Satz, worin
   der übertragbare Gehalt liegt. Bei Treffer in Schritt 1: kursiver Hinweis.
3. `# Struktur / Gliederung` — Gliederungen sind Methode, kein Geheimnis; bleiben erhalten.
4. `# Wiederverwendbare Inhalte` — **der Kern. Ausformuliert, nicht als Stichwortliste.**
5. `# Tragfähigkeit` — **Pflichtabschnitt.** Trägt der Methodenkern, oder ist er nur
   flüssig formuliert? Fakt und Einschätzung getrennt: Was das Original belegt, was es
   behauptet, was in seiner Kategorie üblich ist. „Trägt uneingeschränkt" ist eine gültige
   Antwort — ein leerer Abschnitt ist ein Signal, ein fehlender nicht.
6. `# Als Vorlage nutzbar für`
7. `# Original` — Verweis, Format, Vertraulichkeitsvermerk.

**Prinzip: nicht kürzen, sondern umschichten.** Ein bereinigter Extrakt ist selten kürzer
als vorher — der vertrauliche Anteil schrumpft, der methodische wächst. Schrumpft ein
Extrakt beim Entkernen substanziell, war er kein Wissensdokument, sondern eine Kopie.

**Warum `# Tragfähigkeit` Pflicht ist.** Ein Extrakt schreibt den Methodenkern aus und
verleiht ihm damit die Autorität eines Wissensbestands — auch dann, wenn der Kern dünn ist.
Ohne festen Ort für diese Einschätzung wächst die Basis in die Breite, ohne dass
Qualitätsunterschiede sichtbar bleiben. Das trifft besonders KI-erzeugtes Material, das
flüssig wirkt und deshalb überschätzt wird.

## Dialogverläufe als Original

Ein exportierter Modell-Dialog hat weder Gliederung noch einen Verfasser im üblichen Sinn.
Er lässt sich trotzdem sauber abbilden: Die **Runden** sind die Gliederung, die
**auslösenden Fragen** sind der Methodenkern — sie sind das Übertragbare, nicht die
Antworten —, und die **Ergebnistexte** sind Anlassmaterial. Die Rolle ist die des
Auftraggebers, nicht die des Autors; das gehört im Frontmatter erkennbar vermerkt, damit
später niemand den Text für eigene Urheberschaft hält. `# Tragfähigkeit` ist hier besonders
wichtig, weil Modellantworten formal immer belastbar aussehen.

# Elevation-Kaskade

Trägt der Methodenkern eines `Deliverable` erkennbar über den Anlassfall hinaus, wird
vorgeschlagen, ihn **zusätzlich** als eigenständiges `Framework` zu generalisieren; das
Deliverable bleibt als Beleg verlinkt. Für `Insight` gilt dasselbe eine Stufe später: Ein
Insight, das sich über mehrere Quellen hinweg bestätigt, wird als Elevation-Kandidat
markiert.

Ohne diese Kaskade wächst die Basis in die Breite und nicht in die Reife.

# Marker-Governance

Offene Punkte werden als **Marker** geführt — Platzhalter für fehlende Fakten, ausstehende
Anreicherungen, offene Entscheidungen. Ein Marker ist nur so lange nützlich, wie er zu einer
Handlung führen kann. Vier Regeln:

* **Unbeschaffbares aktiv verwerfen** — mit Vermerk „aktiv verworfen, nicht vergessen",
  damit die Entscheidung nachvollziehbar bleibt und die Lücke nicht erneut als Aufgabe
  auftaucht.
* **Pausierte Vorhaben parken** — `status: pausiert (seit MM/JJJJ)` plus Parkvermerk; ihre
  offenen Fragen fallen bis zur Wiederaufnahme aus dem wöchentlichen Check.
* **Wartende Marker terminieren** — steht nur noch eine Bestätigung aus, wird der Marker zum
  Wiedervorlagepunkt mit Datum.
* **Gefundenes sofort verankern** — ist eine gesuchte Originaldatei lokalisiert, wandert der
  Verweis unmittelbar ins Concept, damit dieselbe Suche sich nicht wiederholt.

# Betriebsumgebung

<NUR STUFE 2/3:>

* **Der Wissensbestand bleibt lokal, nicht in einem Cloud-Ordner.** Zwei
  Synchronisationssysteme auf demselben Verzeichnis erzeugen Konfliktkopien und beschädigen
  die Git-Verwaltungsdaten; das Remote-Repository *ist* bereits die Cloud-Schicht. Die
  **Asset Library** dagegen gehört bewusst in die Cloud.
* **Das Remote ist die verbindliche Fassung.** Lokale Kopien sind gleichberechtigte Klone:
  vor der Arbeit pullen, nach dem Sichern pushen.
* **Tags vergibt die Automatik.** Die GitHub Action `.github/workflows/auto-tag.yml` setzt
  beim Push das Tag aus dem `version`-Feld der Wurzel-`index.md`. Lokal wird nicht getaggt.
  So gilt „Version ≡ getaggter Commit" unabhängig davon, wer committet.
* **Git-Historie säubern heißt Repository neu anlegen.** Ein Force-Push genügt nicht — alte
  Tags halten die Commits erreichbar.

<ALLE STUFEN:>

* **Geplante Aufgaben einmal manuell auslösen.** Nach dem Anlegen oder Ändern eines
  geplanten Jobs einmal „jetzt ausführen", damit die Werkzeug-Freigaben gespeichert sind und
  automatische Läufe nicht auf Bestätigungen warten.

# Versionierung (Semantic Versioning, sinngemäß)

Die inhaltliche Reife der Wissensbasis wird als `MAJOR.MINOR.PATCH` geführt:

* **MAJOR** — struktureller Umbau oder grundlegende Neubewertung, die den bisherigen Stand
  ablöst.
* **MINOR** — additive Erweiterung: ein neues Concept, ein neuer Abschnitt. Bestehendes
  bleibt gültig.
* **PATCH** — Korrektur, Präzisierung, Metadaten.

**Bump-Kopplung:** Die Version wird **genau einmal pro Sicherungsvorgang** erhöht. Änderungen
einer Session werden gebündelt; der `log.md`-Eintrag darf mehrere Bullets unter *einer*
Versionsüberschrift tragen. Die Sprunghöhe richtet sich nach der **größten** Änderungsklasse
im Batch. Während der Arbeit wird **nicht** vorgebumpt.

Die Version lebt synchron in der Wurzel-`index.md` (Feld `version`) und in `log.md`
(`## JJJJ-MM-TT — vX.Y.Z`, neueste zuerst)<, ab Stufe 2 zusätzlich als Git-Tag `vX.Y.Z`>.
Getrennt davon steht `okf_version` (Version des Formats) sowie `setup_version` und
`setup_track` (Herkunft aus dem Jumpstart).

Die Konformität prüft `python3 _meta/check_okf.py`. Details und bewusste Abweichungen vom
Standard stehen in `okf-conformance.md`.

<!-- JUMPSTART-VORLAGE — Hinweisblock beim Anlegen entfernen.
     Das Regelwerk der Basis. Anders als CLAUDE.md darf diese Datei lang sein: Sie ist
     Nachschlagewerk, nicht Session-Kontext. Typ-Vokabular und Ordnerlogik aus dem
     Interview anpassen; die Extrakt-Regel im Wortlaut übernehmen.
     Alle <spitzen Klammern> sind aus dem Interview zu füllen. -->
