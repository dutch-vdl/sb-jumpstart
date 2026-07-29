# Dein Second Brain — was das ist und wie du damit arbeitest

*Diese Datei liegt in deinem Wissens-Ordner, damit du jederzeit nachlesen kannst, wie dein
Setup funktioniert. Du musst nichts davon auswendig können — Claude kennt die Regeln und
hält sie für dich ein.*

## Was ist ein Second Brain?

Ein Second Brain ist ein „zweites Gehirn": ein Ort, an dem dein Wissen dauerhaft gesammelt
wird, damit du es nicht im Kopf behalten musst. Das Besondere an diesem Setup: Es ist nicht
nur eine Ablage für dich, sondern vor allem ein **Gedächtnis für Claude**. Wenn du mit
Claude arbeitest, liest Claude zuerst in diesem Ordner nach, wer du bist, was du kannst,
woran du arbeitest und wie du gern zusammenarbeitest. Dadurch musst du nicht in jedem
Gespräch bei null anfangen — und die Zusammenarbeit wird mit der Zeit besser, weil das
Gedächtnis mitwächst.

## Die Bausteine

**Der Hub** (dein Ordner `Knowledge Hub`) ist der Ordner, in dem du gerade liest. Er
enthält dein gesammeltes Wissen als einfache Textdateien (Markdown, Endung `.md`). Warum
Textdateien und keine App? Weil Text das haltbarste Format überhaupt ist: Du kannst diese
Dateien in zwanzig Jahren noch mit jedem Computer öffnen, du bist von keinem Anbieter
abhängig, und jede KI kann sie lesen. Du kannst sie mit jedem Texteditor öffnen — oder mit
einem hübscheren Programm wie Obsidian, das ist aber optional.

**Die Asset Library** (dein Ordner `Knowledge Asset Library`) ist ein zweiter Ordner für
die großen Original-Dateien: Präsentationen, PDFs, Bilder. Die Arbeitsteilung: Das Original
liegt in der Asset Library, und im Hub liegt eine Textzusammenfassung mit dem Hinweis, wo
das Original zu finden ist. So bleibt der Hub schlank, und trotzdem geht nichts verloren.

**Der Workspace** ist ein Unterordner im Hub für dein Tagesgeschäft: Notizen,
Aufgabenliste, laufende Vorgänge. Hier darf es schnell und unordentlich zugehen — das ist
dein Schmierzettel. Der Rest des Hubs ist die gute Stube: Dort landet nur, was aufgeräumt,
durchdacht und dauerhaft wertvoll ist. Ohne diese Trennung verwandelt sich jedes
Wissenssystem mit der Zeit in einen Zettelberg.

**Die Regel-Dateien:** Ganz oben im Hub liegen drei besondere Dateien. `CLAUDE.md` ist die
Bedienungsanleitung für Claude — dort steht, was Claude in jedem Gespräch beachten muss.
`conventions.md` sind die Spielregeln deiner Wissensbasis. `okf-conformance.md` beschreibt
das Dateiformat und sagt, wie die kleinen Prüfprogramme aufgerufen werden; die liegen im
Unterordner `_meta`. Alle drei sind beim Setup gemeinsam mit dir entstanden und wachsen mit.

Daneben liegen zwei Dateien, die du selbst nie anfassen musst: `index.md` ist das
Inhaltsverzeichnis und trägt die Versionsnummer, `log.md` ist das Änderungstagebuch.

## Die wichtigsten Spielregeln

**Claude liest frei, schreibt aber nur mit deiner Erlaubnis.** Claude nutzt dein Wissen
automatisch als Hintergrund, ohne jedes Mal zu fragen. Aber bevor etwas dauerhaft
gespeichert oder verändert wird, legt Claude dir einen Vorschlag vor, und du sagst ja oder
nein. Nichts verändert sich hinter deinem Rücken.

**Dein Wissen hat Versionsnummern.** Deine Wissensbasis trägt eine Versionsnummer, die bei
jeder Sicherung einen Schritt hochzählt, und eine Datei namens `log.md` führt Tagebuch
darüber, was sich wann geändert hat. Das klingt technisch, hat aber einen einfachen Nutzen:
Du kannst jederzeit nachvollziehen, wie dein Wissen entstanden ist. Wie groß der Schritt
ist, hängt davon ab, was passiert ist — eine Korrektur zählt kleiner als ein neues
Dokument, ein Umbau zählt am größten.

**Vertrauliches bleibt vertraulich.** Wenn du beruflich mit Kunden- oder Firmendaten
arbeitest, gilt: Echte Namen und sensible Zahlen bleiben in deinen privaten Ordnern. Sobald
ein Text nach draußen geht, prüft Claude anhand einer festen Checkliste, ob etwas
anonymisiert werden muss. Auch das musst du dir nicht merken.

## Datenschutz — was mit deinen Daten passiert

Wenn du beruflich arbeitest, landen in deiner Wissensbasis früher oder später Dinge, die
nicht jeden angehen: Kundennamen, Zahlen, interne Vorgänge. Deshalb hier klar, was gilt.

**Niemand außer dir bekommt etwas davon zu sehen.** Dieses Setup hat keinen Rückkanal. Es
meldet nichts an denjenigen, von dem du es bekommen hast, es misst nichts, es sendet
nichts. Was in deinen Ordnern liegt, bleibt in deinen Ordnern.

**Dein Schmierzettel bleibt draußen.** Der `workspace/`-Ordner, in dem echte Namen und
Zahlen erlaubt sind, ist von allem ausgenommen, was jemals irgendwohin kopiert wird. Auch
die großen Originaldateien in der Asset Library bleiben, wo sie sind.

**Eine mechanische Prüfung, keine Selbsteinschätzung.** Beim Aufsetzen legst du gemeinsam
mit Claude eine Liste deiner schützenswerten Namen an — Kunden, Arbeitgeber, Kontakte,
Projektkennungen. Ein kleines Prüfprogramm durchsucht damit deine Dateien, bevor etwas
gesichert wird, und findet zusätzlich Muster wie Mailadressen, Beträge oder
Kontoverbindungen. Diese Liste wird selbst nie irgendwohin kopiert — sie wäre sonst genau
das Problem, das sie verhindern soll.

**Wenn du dich für Git entscheidest, ist das eine Entscheidung über deine Daten.** Ab
Ausbaustufe 2 liegt deine Wissensbasis auf einem fremden Server. Das kann völlig in Ordnung
sein — aber wenn du mit Kundendaten arbeitest, kann es auch vertraglich heikel sein.
Claude weist dich beim Aufsetzen darauf hin und empfiehlt dann ein privates Repository.
Diese Entscheidung kann dir niemand abnehmen, und dieses Setup ist keine Rechtsberatung.

**Und die ehrliche Nebenbemerkung:** Wenn du mit Claude arbeitest, werden deine Inhalte bei
einem Anbieter verarbeitet. Das gilt für jede Nutzung eines KI-Assistenten und ändert sich
durch dieses Setup nicht. Es soll nur nicht unerwähnt bleiben.

## Wie du im Alltag damit arbeitest

Der Alltag ist unspektakulär. Du verbindest den Hub-Ordner mit deiner Claude-Sitzung und
arbeitest einfach — schreibst Texte, bereitest Termine vor, denkst laut nach. Claude zieht
sich den passenden Kontext von selbst aus dem Hub. Und wenn etwas entsteht, das dauerhaft
wertvoll ist, fragt Claude von sich aus: „Sollen wir das aufnehmen?"

Zwei kleine Routinen halten das System gesund:

**Das Sichern.** Wenn sich Änderungen angesammelt haben, sagst du sinngemäß „sichere den
Stand". Claude zeigt dir, was sich geändert hat, schlägt die neue Versionsnummer vor, und
nach deinem Okay wird gespeichert und ins Tagebuch eingetragen.

**Das Weekly Review.** Einmal pro Woche, etwa eine Viertelstunde, gehst du mit Claude
durch: Was aus dem Schmierzettel-Workspace ist so gut, dass es aufgeräumt ins dauerhafte
Wissen wandern soll? Was ist veraltet und kann raus? Welche Aufgaben sind liegengeblieben?
Und was hat die Woche über eure Zusammenarbeit gelehrt — welche Korrektur von dir sollte
zur festen Regel werden, welcher wiederholte Ablauf zur festen Routine? Claude bereitet das
als kurzen Bericht vor, du entscheidest. Diese Viertelstunde ist der Unterschied zwischen
einem lebendigen Second Brain und einem digitalen Dachboden.

## Die Verfahren, die Claude für dich kennt

Für die wiederkehrenden Aufgaben gibt es feste Verfahren — Claude improvisiert nicht jedes
Mal neu, sondern arbeitet einen erprobten Ablauf ab. Sechs sind dabei:

* **Einrichten** — das, was beim Aufsetzen gelaufen ist. Brauchst du nicht wieder.
* **Dokument aufnehmen** — aus einer Präsentation, einem Konzept oder einer Auswertung wird
  wiederverwendbares Wissen. Sag: „Nimm das in mein Wissen auf."
* **Externe Quelle aufnehmen** — eine Studie, ein Report, Marktdaten. Sag: „Nimm die Studie
  auf."
* **Weekly Review** — der Pflegedurchlauf einmal pro Woche. Sag: „Lass uns das Weekly Review
  machen."
* **Stand sichern** — Änderungen festhalten und die Version hochzählen. Sag: „Sichere den
  Stand."
* **Setup aktualisieren** — wenn es eine neue Fassung gibt. Sag: „Prüf mein Setup gegen den
  neuen Stand."

**Du musst dafür nichts installieren und nichts auswendig lernen.** Die Verfahren sind
Textdateien; Claude schlägt das passende nach, wenn du in normalen Worten sagst, was du
willst. Wenn dir jemand eine Installation eingerichtet hat, kannst du sie zusätzlich mit
einem Schrägstrich-Befehl aufrufen — bequemer, aber nicht nötig.

Was jedes Verfahren genau tut und wo die Abgrenzung zum nächsten liegt, steht ausführlich in
`docs/skills.md` des Jumpstart-Pakets.

## Deine Ausbaustufe

Dieses Setup gibt es in drei Ausprägungen — **Lokal**, **Verteilt** und **Mitlaufend**. Sie
unterscheiden sich nicht darin, wie dein Wissen aufgebaut ist, sondern nur darin, womit du
arbeitest und wie Neuerungen an diesem Setup bei dir ankommen. Deine Stufe steht im
Frontmatter der Datei `index.md` im Feld `setup_track`; welche Stufe was bedeutet, steht
kurz in `docs/tracks.md` des Jumpstart-Pakets.

Ein Aufstieg ist jederzeit möglich, und Claude erinnert dich von selbst daran, sobald es
sich lohnt. Was bewusst noch fehlt, steht in `CLAUDE.md` unter „Ausbaustufen".

## Aktualisierungen

Dieses Setup wird weiterentwickelt. Wenn eine neue Fassung erscheint, bekommst du eine
Benachrichtigung. Du sagst dann Claude „prüf mein Setup gegen den neuen Stand" — Claude
vergleicht deine Fassung mit der neuen, zeigt dir die Unterschiede und arbeitet nach deiner
Freigabe ein, was zu dir passt. Du musst nie neu aufsetzen und übernimmst nur, was du
willst.

## Was du davon hast

Nach ein paar Wochen merkst du den Effekt: Claude schreibt Texte, die nach dir klingen.
Vorbereitungen gehen schneller, weil dein Kontext schon da ist. Gute Ideen aus alten
Projekten sind wieder auffindbar, statt in irgendeiner Präsentation von vor drei Jahren zu
schlummern. Und mit jeder Korrektur, die du Claude gibst, merkt sich das System die Regel
dahinter.

Ein letzter Rat: Fang klein an und lass das System im Gebrauch wachsen. Drei gepflegte
Dokumente sind mehr wert als dreißig leere Ordner. Wenn nach ein paar Wochen ein Ordner
ungenutzt bleibt — weg damit. Dein Second Brain soll sich deiner Realität anpassen, nicht
umgekehrt.
