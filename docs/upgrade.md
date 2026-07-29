# Eine neue Fassung übernehmen

*Für dich als Anwender. Du brauchst dafür nichts zu können — der Ablauf ist ein Satz.*

## Wie du mitbekommst, dass es etwas Neues gibt

Stell dieses Repository oben rechts auf **Watch → Custom → Releases**. Dann bekommst du
eine Mail, sobald eine neue Fassung erscheint, mit den Änderungen im Klartext.

Ohne diese Einstellung erfährst du nichts — GitHub benachrichtigt nicht von selbst.

## Wie du sie übernimmst

Sag Claude in einer Sitzung mit verbundenem Wissens-Ordner:

> Prüf mein Setup gegen den neuen Stand.

Was dann passiert:

1. Claude liest, auf welcher Fassung du stehst — das steht im Kopf deiner `index.md` als
   `setup_version`.
2. Claude liest, was seither dazugekommen ist, und blendet aus, was nur andere
   Ausbaustufen betrifft.
3. Du bekommst eine Liste, sortiert nach **empfohlen**, **optional** und **betrifft dich
   nicht**. Jede Zeile sagt, was sich ändert und warum.
4. Du entscheidest — einzeln oder im Ganzen. Danach arbeitet Claude ein, was du freigegeben
   hast, und trägt die neue Fassung ein.

## Drei Zusagen

**Es wird nie neu aufgesetzt.** Nur die Differenz wird eingearbeitet. Dein Wissen bleibt
unangetastet.

**Was du selbst angepasst hast, wird nicht überschrieben.** Hast du eine Regel für dich
umformuliert und kommt an derselben Stelle eine Änderung, siehst du beide Fassungen und
entscheidest.

**Du musst nichts übernehmen.** Wenn du eine Neuerung nicht willst, bekommst du sie nicht.
Claude notiert, was du bewusst ausgelassen hast — damit dieselbe Sache dir nicht beim
nächsten Mal erneut vorgelegt wird.

Eine Ausnahme davon gibt es: Änderungen, die den Schutz deiner Daten betreffen, werden
immer als **empfohlen** vorgelegt, mit einem Satz dazu, was ein Auslassen riskiert. Auch
die kannst du ablehnen — aber nicht, ohne es gelesen zu haben.

## Wenn du bei Ausbaustufe 3 bist

Dann kommen die **Verfahren** automatisch über die Plugin-Quelle, sofern du die
automatische Aktualisierung eingeschaltet hast. Alles andere — Regeldateien, Vorlagen,
Prüfprogramme in deinem Ordner — kommt trotzdem nur über den Satz oben. Das Plugin fasst
deine Wissensbasis nicht an.

## Wenn etwas schiefgeht

Der Upgrade ist ein normaler Sicherungsvorgang: Er landet in deinem Änderungstagebuch und
bekommt eine eigene Versionsnummer. Wenn dir etwas nicht gefällt, siehst du in `log.md`
genau, was geändert wurde — und bei Ausbaustufe 2 und 3 kannst du jeden Stand über die
Versionsverwaltung wiederherstellen.
