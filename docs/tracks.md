# Welche Ausbaustufe passt zu mir?

*Kurzfassung für dich als Mensch. Die ausführliche Anleitung ist an Claude gerichtet — du
musst sie nicht lesen.*

Das Setup gibt es in drei Ausprägungen. Sie unterscheiden sich **nicht** darin, wie dein
Wissen aufgebaut ist — Ordner, Dokumenttypen, Regeln und Versionsnummern sind überall
gleich. Sie unterscheiden sich nur darin, **womit du arbeitest** und **wie Neuerungen an
diesem Setup bei dir ankommen**.

Wenn du unsicher bist: Nimm Stufe 1. Aufsteigen kannst du jederzeit, und Claude erinnert
dich von selbst daran, sobald es sich lohnt.

---

## Stufe 1 — Lokal

**Für dich, wenn** du an einem Rechner arbeitest und mit Git bisher nichts zu tun hattest.

Dein Wissen liegt in einem ganz normalen Ordner. Kein Zusatzwerkzeug, keine Installation
— und du musst nichts eintippen. Deine Wissensbasis bekommt trotzdem von Anfang an eine Versionsnummer
und ein Änderungstagebuch — das ist eine Zeile Text pro Sicherung und der Grund, warum du
später mühelos aufsteigen kannst, wenn du willst.

**Aktualisierungen:** Du bekommst eine Mail, wenn es eine neue Fassung gibt, und sagst
Claude „prüf mein Setup gegen den neuen Stand". Claude holt sich den neuen Stand selbst von
der Adresse, die in deiner Wissensbasis vermerkt ist, zeigt dir was sich geändert hat und
arbeitet es nach deiner Freigabe ein. Herunterladen musst du nichts.

**Was du dafür brauchst:** einen Claude-Zugang, am besten die Desktop-App, und einen
leeren Ordner. Sonst nichts. Einen GitHub-Account brauchst du nur, wenn du über neue
Fassungen benachrichtigt werden willst — zum Lesen der Anleitung nicht.

*Kleingedrucktes:* Zur Wissensbasis gehören zwei kleine Prüfprogramme, die Formatfehler und
versehentlich hineingeratene Namen finden. Sie brauchen Python. Ob das auf deinem Rechner
nötig ist oder ob Claude sie an seinem Ende ausführt, klärt Claude beim Aufsetzen mit dir —
und wenn Python fehlt, ist das kein Hindernis für den Start.

**Deine Daten:** bleiben auf deinem Rechner. Nichts wird hochgeladen, nichts geteilt.

---

## Stufe 2 — Verteilt

**Für dich, wenn** du an mehreren Geräten arbeitest und Git schon kennst oder es dir
zutraust.

Dein Wissen liegt in einem eigenen Repository. Damit arbeitest du am Laptop weiter, was du
am Rechner begonnen hast, und jede Änderung ist nachvollziehbar. Der Preis dafür ist eine
Handvoll neuer Handgriffe: pullen vor der Arbeit, sichern nach der Arbeit, pushen mit einem
Klick. **Holen und Hochladen bleiben bewusst bei dir** — beides braucht deine
Zugangsdaten, und die sollen nicht in einer KI-Umgebung liegen. Alles dazwischen übernimmt
Claude.

**Aktualisierungen:** wie bei Stufe 1 — Mail, dann „prüf mein Setup gegen den neuen
Stand".

**Was du dafür brauchst:** zusätzlich einen GitHub-Account und ein Git-Programm auf jedem
Gerät. Empfohlen: **GitHub Desktop** — es ist auf Klicken ausgelegt statt auf Befehle und
bringt Git gleich mit, sodass du nichts separat installieren musst. Jedes andere
Git-Programm geht auch, wenn du eins gewohnt bist.

Ein Programm brauchst du hier wirklich, nicht nur der Bequemlichkeit halber: Den letzten
Schritt — das Hochladen — machst du bewusst selbst, damit keine Zugangsdaten in einer
KI-Umgebung liegen. Ohne Programm könntest du diesen Schritt nicht ausführen.

Dazu **Python 3** auf jedem Gerät, auf dem die Sperre vor dem Speichern laufen soll. Wenn
du GitHub Desktop installierst, ist das der zweite und letzte Handgriff dieser Art.

**Deine Daten — hier wird es wichtig:** Ab dieser Stufe liegt deine Wissensbasis auf
einem fremden Server. Das ist der eigentliche Unterschied zu Stufe 1, und es ist eine
Entscheidung über deine Daten, nicht nur über deinen Komfort. Wenn du beruflich mit
Kundendaten arbeitest, kann das vertraglich heikel sein — Geheimhaltungsvereinbarungen,
Vorgaben deines Arbeitgebers, Regeln zur Auftragsverarbeitung. Nimm in dem Fall auf jeden
Fall ein **privates** Repository, und wenn du unsicher bist, bleib bei Stufe 1. Claude
weist dich beim Aufsetzen darauf hin, kann dir die Entscheidung aber nicht abnehmen und
ersetzt keine Rechtsberatung.

Zusätzlich kannst du dir eine Sperre einrichten, die einen Speichervorgang abbricht, sobald
darin ein Name aus deiner Schutzliste auftaucht. Claude erklärt dir das beim Aufsetzen; es
ist ein einmaliger Befehl.

**Eine Warnung, die zählt:** Lege deinen Wissens-Ordner in dieser Stufe **nicht** in einen
Cloud-Ordner wie iCloud oder Dropbox. Zwei Synchronisationssysteme auf demselben Verzeichnis
beschädigen sich gegenseitig. Das Repository ist bereits deine Cloud.

---

## Stufe 3 — Mitlaufend

**Für dich, wenn** du Stufe 2 fährst und die Weiterentwicklung dieses Setups automatisch
mitnehmen willst.

Hier wird das Jumpstart-Repository direkt als Quelle eingebunden. Neue oder verbesserte
Verfahren kommen an, ohne dass du etwas herunterlädst. Du entscheidest weiterhin, ob du eine
Neuerung übernimmst — automatisch ist die Lieferung, nicht der Umbau deiner Basis.

**Zwei Einschränkungen, die du kennen solltest.** Die automatische Aktualisierung ist bei
eigenen Quellen wie dieser standardmäßig **ausgeschaltet** und muss einmalig eingeschaltet
werden — sonst passiert nichts, ohne dass es auffällt. Und über diesen Weg kommen nur die
**Verfahren**; die Regeldateien und Prüfskripte in deiner eigenen Wissensbasis fasst kein
Update an. Dafür brauchst du wie alle anderen den Befehl „prüf mein Setup gegen den neuen
Stand".

**Was du dafür brauchst:** alles aus Stufe 2, plus einmalig zwei Handgriffe — die
Plugin-Quelle hinzufügen und die automatische Aktualisierung einschalten. Claude führt dich
durch beides.

Falls du sowohl die Desktop-App als auch die Kommandozeilen-Fassung von Claude benutzt:
Das sind zwei getrennte Installationen. Du richtest die Quelle dann zweimal ein, einmal je
Umgebung.

**Deine Daten:** wie Stufe 2. Zusätzlich kommen Aktualisierungen automatisch bei dir an —
die Richtung bleibt aber einseitig: Es fließt etwas zu dir hin, nie etwas von dir weg.

---

## Aufsteigen und absteigen

Der Wechsel zwischen den Stufen ist vorgesehen und kostet wenig, weil die inhaltliche
Struktur identisch bleibt. Deine aktuelle Stufe steht in deiner Wissensbasis vermerkt;
Claude weiß also, was es dir anbieten darf und was nicht.

Der typische Weg: Man startet lokal, merkt nach ein paar Wochen, dass man an zwei Geräten
arbeitet, und steigt auf Stufe 2. Umgekehrt geht es auch — wer feststellt, dass er den
Git-Anteil nie benutzt, kann ihn abschalten, ohne etwas zu verlieren.

## Was in keiner Stufe passiert

Dieses Setup hat keinen Rückkanal. Es meldet nichts an denjenigen, von dem du es bekommen
hast, es misst nichts, es sendet nichts. Was in deinen Ordnern liegt, bleibt in deinen
Ordnern — unabhängig davon, welche Stufe du fährst.
