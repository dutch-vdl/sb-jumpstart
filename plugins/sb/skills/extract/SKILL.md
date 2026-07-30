---
name: extract
description: Ein Originaldokument (Präsentation, PDF, Tabelle, Transkript, Konzept, Arbeitsmappe) als Deliverable-Concept in die Wissensbasis aufnehmen – nach der verbindlichen Extrakt-Regel mit mechanischer Vertraulichkeitsprüfung und ausgeschriebenem Methodenkern, inklusive Ablage des Originals und Verlinkung. Verwenden bei „extrahiere", „nimm das in mein Wissen auf", „neues Deliverable", „archivier das Dokument", „mach ein Concept daraus" – und immer dann, wenn jemand eine Arbeitsdatei hochlädt oder referenziert, deren Wissen dauerhaft erhalten bleiben soll.
---

# Extract — Original zu Wissen destillieren

## Was dieser Skill tut

Er verwandelt ein konkretes Arbeitsdokument in ein wiederverwendbares Wissensdokument. Das
Original wandert in die Asset Library, in den Wissensbestand kommt ein Extrakt: entkernt um
alles Vertrauliche, angereichert um den übertragbaren Methodenkern.

**Der Leitsatz:** Der Extrakt beantwortet *„wie geht man vor"*, nicht *„was war im Fall X
konkret"*. Das Konkrete bleibt im Original und ist über den Verweis erreichbar — es geht
kein Zugriff verloren, nur die Kopie im Bestand.

## Ablauf

**1. Einordnen.** Worum handelt es sich, welcher Typ passt (meist `Deliverable`), wo im
Bestand gehört es hin? Vorher kurz prüfen, ob es das Concept schon gibt — dann aktualisieren
statt neu anlegen.

**2. Original ablegen.** In die Asset Library, nach dem dort geltenden Ordnerschema.
**Der Dateiname wird mitgeprüft** — kein vertraulicher Inhalt im Namen.

**3. Vertraulichkeitsprüfung — mechanisch, immer, fünf Fragen.** Enthält der Entwurf
Konditionen (Preise, Sätze, Margen)? Kennzahlen Dritter (Umsätze, Budgets, Performance)?
Technische Interna (Architektur, Zugänge, Sicherheitsstand)? Interne Strategie
(Selbstkritik, Wettbewerbsbewertungen)? Personennamen Dritter?

Die *Prüfung* ist verpflichtend, die *Entkernung* nur bei Treffer. Nicht auf Gefühl
verlassen — die Liste abfragen. Treffer bleiben im Original; im Extrakt steht ein kursiver
Hinweis, was ausschließlich dort zu finden ist. Personennamen werden **nicht gestrichen,
sondern durch die Rolle ersetzt** („der Product Owner", „die Architektin").

**Stammt das Material vom eigenen Arbeitgeber, ist Frage 4 der kritische Punkt** — und
zugleich der, an dem die maschinelle Prüfung strukturell nicht helfen kann: Der eigene
Arbeitgeber steht als Klärungsfall (`?Name`) auf der Entitätenliste, nicht als Sperre.
Beantworte Frage 4 für dieses Material **einzeln und sichtbar**, nicht pauschal mit den
übrigen vier, und setze danach den Vermerk `jumpstart-checked: <Begründung>` ins
Frontmatter des Extrakts. Ohne diesen Vermerk meldet die Datenschutzprüfung die Datei als
offene Klärung.

**4. Methodenkern ausschreiben.** Der eigentliche Wert. Vorgehen, Gliederungen,
Entscheidungsbäume, Bewertungsraster, Argumentationsfiguren, Einwand-Antwort-Paare,
Reihenfolge-Logiken. **Ausformuliert, nicht als Stichwortliste.** Vom Anlassfall abgelöst
und auf die Klasse von Fällen gehoben, für die er gilt.

Testfrage: *Brauche ich das noch, wenn ich morgen in einem anderen Kontext vor einer
ähnlichen Aufgabe stehe?*

**Prinzip: nicht kürzen, sondern umschichten.** Der vertrauliche Anteil schrumpft, der
methodische wächst. Schrumpft ein Extrakt beim Entkernen substanziell, war er kein
Wissensdokument, sondern eine Kopie — dann sagen und neu ansetzen.

**5. Aufbau schreiben.** Frontmatter mit `type`, `generated`, `resource` und
Herkunftsfeldern — zitiert der Extrakt fremdes Material, kommt es als `sources`-Eintrag dazu,
nicht als Linkliste im Body. Dann: `# Überblick` ·
`# Struktur / Gliederung` (Gliederungen sind Methode, kein Geheimnis) ·
`# Wiederverwendbare Inhalte` (der Kern) · `# Tragfähigkeit` · `# Als Vorlage nutzbar für` ·
`# Original`.

`# Tragfähigkeit` ist **Pflicht**: Trägt der Kern, oder ist er nur flüssig formuliert? Fakt
und Einschätzung getrennt — was das Original belegt, was es behauptet, was in seiner
Kategorie üblich ist. „Trägt uneingeschränkt" ist eine gültige Antwort; Weglassen ist keine.
Ohne diesen Abschnitt verleiht der Extrakt schwachem Material die Autorität eines
Wissensbestands. Das trifft besonders KI-erzeugtes Material.

**Ist das Original ein Modell-Dialog**, sind die Runden die Gliederung, die auslösenden
Fragen der Methodenkern und die Ergebnistexte das Anlassmaterial. Die Rolle ist die des
Auftraggebers, nicht die des Autors — im Frontmatter vermerken.

**6. Verlinken.** Aus dem passenden Index und den verwandten Concepts heraus, bundle-relativ
mit führendem `/`.

**7. Framework-Check.** Trägt der Methodenkern erkennbar über den Anlassfall hinaus?
Dann vorschlagen, ihn **zusätzlich** als eigenständiges `Framework` zu generalisieren; das
Deliverable bleibt als Beleg verlinkt. Das ist der Schritt, der aus einem Archiv eine
Wissensbasis macht — nicht überspringen, nur weil er Arbeit macht.

**8. Vorlegen.** Zur Freigabe, nicht direkt schreiben. Bei mehreren Dokumenten gebündelt.

**9. Datenschutzprüfung.** Vor dem Sichern `python3 _meta/check_privacy.py` laufen lassen.
Treffer werden entfernt oder abstrahiert, nicht weggeklickt.

## Kein Version-Bump in-session

Der Extrakt wird geschrieben, die Version steigt erst beim Sichern.

---

*Bei Widerspruch zwischen diesem Skill und `conventions.md` im Hub gilt `conventions.md`.*

*Status: Entwurf. Nach den ersten Durchläufen prüfen, ob Schritt 4 ausführlich genug
ausfällt — die häufigste Schwäche ist ein Methodenkern, der nur benannt statt ausgeschrieben
wird.*
