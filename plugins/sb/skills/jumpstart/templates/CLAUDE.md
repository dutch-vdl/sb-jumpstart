<!-- JUMPSTART-VORLAGE — Hinweis für Claude, beim Anlegen entfernen.
     Diese Datei wird jede Session zuerst gelesen. Halte sie kurz.
     Alles in <spitzen Klammern> ist aus dem Interview zu füllen.
     Stufenabhängige Blöcke sind markiert; nicht zutreffende ersatzlos streichen. -->

# Knowledge Hub — Bedienungsanleitung für Claude

Dies ist die persönliche Wissensbasis von **<Name>** (Open Knowledge Format v0.1). Sie
dient als Kontext für die Zusammenarbeit.

## 0 · Nicht verhandelbar (immer, ohne Ausnahme)

Diese Regeln gelten vorrangig vor allem Übrigen. Bei Konflikt gewinnt dieser Block.

* **MUSS – Kontext vor Handlung:** Vor der **ersten inhaltlichen Aktion** in einer Session
  `conventions.md` lesen<und, sobald vorhanden, das Zusammenarbeits-Profil>. Kein
  Losarbeiten ohne diesen Schritt.
* **MUSS – Sprache und Register:** <Sprache>, im Register <Register aus dem Interview>.
* **MUSS – Vorschlag vor großer Aktion:** Vor Schreibzugriffen auf den Wissensbestand,
  Massen- oder Strukturänderungen erst einen **Vorschlag zur Prüfung** vorlegen.
  Zurückgeschrieben wird **nur mit ausdrücklicher Freigabe**.
* **MUSS – Vertraulichkeit:** <Nur bei Bedarf aus Interview 1.3:> In ausgehenden Dokumenten
  Namen Dritter und sensible Kennzahlen anonymisieren. Klarnamen bleiben in den privaten
  Ablagen.
* **MUSS – Nichts verlässt den Rechner ohne Zustimmung:** Inhalte aus dieser
  Wissensbasis werden nicht an Dritte ausgeleitet, nicht in fremde Ablagen kopiert und
  nicht veröffentlicht, ohne dass <Name> dem im Einzelfall ausdrücklich zustimmt. Das
  gilt auch für scheinbar harmlose Nebenwege — Beispiele in ausgehenden Texten,
  Screenshots, Auszüge in Chats.
* **MUSS – Fakt vs. Einschätzung:** Beides klar trennen; bei Unsicherheit über Fakten zur
  Person **nachfragen statt raten**.
* **MUSS – Versionierung:** Die `version` **nur beim Sichern** erhöhen — nie in-session
  vorbumpen.
* <Persönliche No-Gos aus Interview 1.6, je als eigene NIE-Zeile.>

## Bei Session-Start

1. `index.md` lesen (Überblick, `version`, `setup_track`) sowie — verpflichtend gemäß
   Block 0 — `conventions.md`.
2. Die für die Aufgabe relevanten Concepts als Kontext heranziehen. Navigation über die
   `index.md`-Dateien der Ordner (Progressive Disclosure), statt alles zu laden.
3. Ergänzendes Regelwerk bei Formatfragen: `okf-conformance.md`.

## Nutzen (Standard)

Die Basis **automatisch** als Kontext nutzen. Lesen erfordert keine Rückfrage.

## Arbeitsregeln

* **Bestandsabgleich vor nicht-trivialen Aufgaben.** Erst über Dateinamen und Titel der
  Wissensordner suchen (billig), dann die ein bis drei einschlägigen Treffer vollständig
  lesen. Den Befund **sichtbar machen** — auch ein „nichts Einschlägiges gefunden" ist eine
  bewusste Aussage, keine Auslassung.
* **Konventions-Selbstcheck.** Neue Artefakte vor der Vorlage unaufgefordert gegen
  `conventions.md` halten; Abweichungen als Entscheidungsliste ausweisen.
* **Machbarkeit vor Bau.** Bei technischen Lösungen erst Dokumentation und Machbarkeit
  klären, dann bauen.
* **Entscheidungsformate.** Entscheidungsfragen gebündelt als nummerierte oder gebuchstabte
  Optionen mit klarer Empfehlung vorlegen, damit Kurzfreigaben möglich sind.
* <NUR STUFE 2/3:> **Realen Stand einlesen.** Vor Aussagen über den Stand der Basis und vor
  jedem Schreibzugriff Version, letzte Commits und betroffene Dateien frisch einlesen statt
  dem Session-Kontext zu trauen.

## Operative Schicht: `workspace/`

`workspace/` ist der Arbeitsraum für laufende Vorgänge — **kein Teil des Wissensbestands**,
nicht versioniert<, gitignored>, vom Prüfskript ausgenommen. Dort gelten eigene Regeln
(`workspace/README.md`): Klarnamen und Zahlen erlaubt, kein Frontmatter, freies Schreiben
**ohne** Freigabe-Pflicht. Die Freigabe-Regel aus Block 0 gilt unverändert für den
Wissensbestand; Wissen wandert nur destilliert (Extrakt-Regel) und mit Freigabe vom
Workspace in den Bestand.

## Anreichern (nur mit Freigabe)

Schreibe **nicht** automatisch zurück. Wenn dauerhaft dokumentierenswertes Wissen entsteht,
**frage aktiv nach**, ob wir es aufnehmen. Typische Auslöser:

* Arbeit an einem neuen Projekt → neues `Deliverable` (Original in die Asset Library).
* Neue oder ausgebaute Methodennutzung → `Framework`.
* Wiederverwendbarer Guide oder Learning → `Learning`.
* Neue Erkenntnis über Kompetenzen, Arbeitsstil oder Domänen → Profil-Update.
* Relevante externe Studie oder Marktdaten → `Insight`.

Neue Concepts gemäß `conventions.md` einordnen (Typ-Vokabular, Ordnerlogik, Asset Library).

## Lern-Mechaniken

* **Selbstlernen nach Korrektur.** Nach einer Korrektur die zugrunde liegende Regel
  dauerhaft festhalten — Stil- und Verhaltensregeln im Zusammenarbeits-Dokument,
  Inhaltliches im passenden Cluster. Eine zweimal angemahnte Regel ist Regelwerk, keine
  Präferenz.
* **Muster-Ernte.** Wiederkehrende Entscheidungen und Ablauf-Muster als Regel-Kandidaten
  vormerken und im Weekly Review gebündelt vorschlagen — nicht einzeln nachfragen.
* **Skill-Reife.** Wiederholt sich ein Ablauf zum dritten Mal, vorschlagen, ihn als Skill
  zu formalisieren.

## Sichern und Versionierung

Ein Sicherungsvorgang = ein Versionsschritt. Änderungen werden während der Session
gesammelt, **nicht** einzeln vorgebumpt. Ablauf beim Sichern:

1. Nächste `version` bestimmen: Sprunghöhe = **größte** Änderungsklasse im Batch — MAJOR
   (struktureller Umbau, grundlegende Neubewertung), sonst MINOR (additive Erweiterung),
   sonst PATCH (Korrektur, Präzisierung, Metadaten).
2. `version` in der Wurzel-`index.md` setzen und **einen** `log.md`-Eintrag anlegen
   (neueste zuerst; mehrere Änderungen als Bullets unter *einer* Versionsüberschrift).
3. Beide Prüfskripte ausführen — in **allen** Stufen:
   `python3 _meta/check_okf.py` und `python3 _meta/check_privacy.py`.
   Bei einem harten Verstoß oder einem Datenschutz-Treffer wird **nicht** gesichert:
   stoppen, melden, entfernen oder abstrahieren.
4. <NUR STUFE 2/3:> Commit nach Conventional Commits (`typ(scope): kurzbeschreibung`), nur
   die gewünschten Dateien stagen. **Bei hartem Verstoß aus Schritt 3: stoppen, melden,
   nicht committen.** Das Tag setzt die GitHub Action beim Push; lokal wird nicht getaggt.
   **Der Push bleibt bei <Name>** — es liegt kein Zugangs-Token in der Claude-Umgebung.

## Die beiden Routinen

Beide sind hier in Kurzform verankert, damit sie **auch ohne installierte Verfahren**
verfügbar sind. Die ausführlichen Abläufe stehen im Jumpstart-Paket; bei Widerspruch gilt
das Paket.

**Sichern** — siehe Abschnitt oben.

**Weekly Review** (wöchentlich, rund fünfzehn Minuten, als knapper Bericht mit
Entscheidungspunkten — kein stiller Umbau). Fünf Blöcke:

1. **Destillat.** `workspace/` sichten: Was hat sich als generalisierbar erwiesen?
   Kandidaten mit Typ-Vorschlag und einem Satz Begründung; Aufnahme nur mit Freigabe und
   über die Extrakt-Regel. Danach den Workspace straffen.
2. **Aktualität.** Insights am gründlichsten, Learning auf offensichtliche Veralterung,
   Frameworks in der Regel nicht. Gesteuert über den Abschnitt `# Haltbarkeit / Stand`:
   geprüft wird der verfallende Anteil, nicht das ganze Dokument.
3. **Aufgaben-Triage.** Erledigtes raus, Überfälliges nach vorn, Neues einsammeln,
   Marker-Governance anwenden. Jede Aufgabe braucht ein Datum.
4. **Regel-Ernte.** Was hat die Woche über die Zusammenarbeit gelehrt? Korrekturen und
   wiederkehrende Entscheidungen als Regel-Kandidaten, wiederholte Abläufe als
   Skill-Kandidaten. Aufnahme nur mit Freigabe.
5. **Konsistenz und Ausbaustufen.** Beide Prüfskripte laufen lassen. Entitätenliste um neue
   Kunden, Projekte und Kontakte ergänzen — das ist der feste Termin dafür. Frontmatter
   vollständig, Version und Log synchron? Offene Ausbaustufen prüfen und **einmalig**
   erinnern, wenn eine reif ist.

Der Durchlauf ersetzt keine Einzelaufnahme — er sammelt ein, was liegengeblieben ist. Er
endet mit einem Sicherungsvorgang, also **einem** Versionsschritt.

## Ausbaustufen (bewusst noch nicht umgesetzt)

<Aus Phase 1 übernehmen, z. B.:>

* Aufstieg auf Stufe <2/3> — noch nicht nötig, weil <Grund>. Prüfen, sobald <Auslöser>.
* Backup oder Cloud-Sync der Asset Library — noch offen.
* Aufgeschobene Skill-Kandidaten: <Liste>.

Claude erinnert von selbst daran, spätestens im Weekly Review, sobald die Basis spürbar
gewachsen ist (Richtwert: ab etwa zwanzig Concepts oder nach einigen Wochen Nutzung).

## Herkunft

Diese Basis wurde mit dem SB Jumpstart aufgesetzt. Drei Felder im Frontmatter der
Wurzel-`index.md` halten das fest: `setup_version` (welche Fassung), `setup_track` (welche
Ausbaustufe) und `setup_source` (woher — die Adresse, unter der neue Fassungen liegen).

Bei einer neuen Fassung prüft der Upgrade-Skill die Differenz gegen diese Quelle und legt
sie zur Freigabe vor. Ohne `setup_source` findet er nichts; das Feld ist kein Schmuck.
