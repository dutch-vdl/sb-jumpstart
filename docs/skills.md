# Die Skills — was sie tun und wann du sie brauchst

Ein Skill ist ein festes Verfahren für eine wiederkehrende Aufgabe, aufgeschrieben als
Textdatei. Claude liest es und arbeitet es ab, statt jedes Mal neu zu improvisieren. Das ist
der ganze Zauber — es steckt keine Software dahinter.

## Du musst nichts installieren

**Skills funktionieren in allen drei Ausbaustufen**, auch ohne Installation. Sie sind
Markdown-Dateien; Claude kann sie im Paket nachschlagen und ausführen. Sag einfach, was du
willst — „nimm dieses Dokument in mein Wissen auf" —, und Claude schlägt das passende
Verfahren nach.

Was eine Installation zusätzlich bringt, ist der Kurzaufruf mit Schrägstrich (`/sb:extract`)
und das automatische Auslösen im passenden Moment. Für Ausbaustufe 3 kommt das ohnehin über
die Plugin-Quelle. Bequemlichkeit, kein Funktionsunterschied.

---

## `jumpstart` — die Wissensbasis einrichten

**Wann:** Einmal, ganz am Anfang. Danach nie wieder.

**Was passiert:** Ein kurzes Interview zu deinen Lebens- und Arbeitsbereichen, deiner
Arbeitsweise und deiner Vertraulichkeitslage. Daraus leitet Claude deine Ausbaustufe ab und
legt Ordnerstruktur, Regeldateien und Prüfskripte an. Anschließend bringst du vorhandenes
Material mit, das gemeinsam aufgenommen wird, und ihr richtet die Routinen ein.

**Dauer:** Interview und Grundgerüst rund eine halbe Stunde. Das Aufnehmen von Material
dauert so lange, wie du Material hast.

**Sag zum Beispiel:** „Richte mir nach dieser Anleitung mein Second Brain ein."

---

## `extract` — ein Dokument zu Wissen machen

**Wann:** Immer, wenn du eine Datei hast, aus der dauerhaft etwas erhalten bleiben soll —
eine Präsentation, ein Konzept, eine Auswertung, ein Gesprächsprotokoll.

**Was passiert:** Das Original wandert in deine Asset Library. In deine Wissensbasis kommt
ein Extrakt: alles Vertrauliche entfernt, dafür der übertragbare Kern ausgeschrieben — also
das Vorgehen, die Gliederung, die Entscheidungslogik, die Argumente. Claude prüft dabei
mechanisch eine feste Liste ab: Preise und Konditionen, fremde Kennzahlen, technische
Interna, interne Strategie, Namen Dritter. Namen werden nicht gelöscht, sondern durch die
Rolle ersetzt.

**Der Maßstab:** Der Extrakt beantwortet „wie geht man vor", nicht „was war bei diesem
Kunden konkret". Wenn beim Entkernen fast nichts übrig bleibt, war es kein Wissensdokument,
sondern eine Kopie — dann sagt Claude das.

**Sag zum Beispiel:** „Nimm das in mein Wissen auf." · „Mach ein Concept daraus."

---

## `insight` — eine externe Quelle aufnehmen

**Wann:** Wenn du eine Studie, einen Report, Marktdaten oder einen Fachartikel hast, auf den
du später zurückgreifen willst.

**Was passiert:** Claude prüft, ob du das Thema schon hast und ob die neue Quelle die alte
ersetzt. Zahlen werden mit Fundstelle übernommen und nie gerundet. Und das Dokument bekommt
einen Haltbarkeitsvermerk, der trennt, was dauerhaft gilt, und was mit dem Datum veraltet —
das macht die spätere Pflege überhaupt erst möglich.

**Abgrenzung zu `extract`:** Fremdes Material kommt hierher, eigene Arbeitsdokumente zu
`extract`.

**Sag zum Beispiel:** „Nimm die Studie auf." · „Leg das als Insight ab."

---

## `weekly-review` — der Pflegedurchlauf

**Wann:** Einmal pro Woche, rund eine Viertelstunde. Das ist die Routine, die den
Unterschied macht zwischen einer lebendigen Wissensbasis und einem digitalen Dachboden.

**Was passiert:** Fünf Blöcke. Was aus deinem Schmierzettel-Workspace ist gut genug, um
aufgeräumt ins dauerhafte Wissen zu wandern? Was ist veraltet? Welche Aufgaben sind
liegengeblieben? Was hat die Woche über eure Zusammenarbeit gelehrt — welche Korrektur
sollte zur Regel werden? Und zuletzt die Kontrolle: Prüfskripte, Vollständigkeit, und die
Pflege deiner Schutzliste um neue Kunden und Projekte.

Du bekommst einen kurzen Bericht mit Entscheidungspunkten. Umgebaut wird nichts ohne dein
Ja.

**Sag zum Beispiel:** „Lass uns das Weekly Review machen."

---

## `hub-commit` — den Stand sichern

**Wann:** Am Ende einer Arbeitssitzung, in der sich etwas geändert hat.

**Was passiert:** Claude sichtet die Änderungen, schlägt die neue Versionsnummer vor —
klein bei einer Korrektur, größer bei einem neuen Dokument, am größten bei einem Umbau —,
schreibt den Eintrag ins Änderungstagebuch und lässt beide Prüfungen laufen. Schlägt eine
an, wird **nicht** gesichert.

**Ab Ausbaustufe 2** kommt der Commit dazu. Den letzten Schritt, das Hochladen, machst du
selbst mit einem Klick — bewusst, damit keine Zugangsdaten in einer KI-Umgebung liegen.

**Bei Ausbaustufe 1** endet der Skill nach den Prüfungen und dem Tagebucheintrag — der
Commit entfällt, die Prüfungen nicht. Schlägt eine an, wird auch hier nicht gesichert. Die
Mechanik ist dieselbe, nur ohne Werkzeug darunter.

**Sag zum Beispiel:** „Sichere den Stand."

---

## `jumpstart-upgrade` — dein Setup aktualisieren

**Wann:** Wenn du eine Benachrichtigung über eine neue Fassung bekommen hast, oder wenn du
wissen willst, ob deine Basis noch aktuell ist.

**Was passiert:** Claude vergleicht deine Setup-Version mit der neuen, liest die
Änderungsliste dazwischen und hält jede Änderung gegen deine tatsächliche Basis. Änderungen,
die nur eine andere Ausbaustufe betreffen, fallen raus. Was du selbst angepasst hast, wird
**nicht** stillschweigend überschrieben — bei Konflikt siehst du beide Fassungen.

Du bekommst eine Liste, sortiert nach *empfohlen*, *optional* und *betrifft dich nicht*, und
entscheidest einzeln oder im Ganzen. Es wird nie neu aufgesetzt, immer nur die Differenz
eingearbeitet.

**Sag zum Beispiel:** „Prüf mein Setup gegen den neuen Stand."

---

## Zwei Regeln, die für alle Skills gelten

**Die Regeln deiner Wissensbasis gewinnen.** Steht in einem Skill etwas anderes als in
deiner `conventions.md`, gilt deine `conventions.md`. Skills führen aus, sie regieren nicht.

**Geschrieben wird nur mit deiner Freigabe.** Jeder Skill legt vor, bevor er etwas dauerhaft
verändert. Das gilt auch dann, wenn du ihn ausdrücklich aufgerufen hast.

## Und wenn ein Skill nicht passt

Alle Skills tragen einen Vermerk, dass sie noch nicht eingeschliffen sind, plus eine Liste
offener Punkte am Ende. Das ist Absicht: Ein Verfahren, das erst zweimal gelaufen ist, sollte
nicht so tun, als wäre es erprobt. Wenn dir etwas auffällt, sag es Claude — daraus wird eine
Regel, und aus der Regel die nächste Fassung.
