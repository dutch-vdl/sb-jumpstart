# Release-Gate — Prüfung vor jeder Veröffentlichung

*Interne Betriebsanleitung für den Betreiber des Jumpstart-Repos. Nicht Teil dessen, was
Anwender bekommen.*

## Einmalig vor der ersten Veröffentlichung

Eine Checkliste, die genau einmal abgearbeitet wird:

1. **Platzhalter ersetzen.** In `README.md` steht `<DEIN-GITHUB-NAME>` im Startprompt. Ohne
   Ersetzung schickt jeder Empfänger Claude auf eine Adresse, die es nicht gibt.
2. **Repository anlegen**, öffentlich, ohne Beschreibung und ohne Topics. Keine
   Lizenzdatei — ohne sie gilt das volle Urheberrecht: ansehbar, nicht freigegeben.
3. **Support-Kanäle abschalten:** Issues, Discussions, Wiki, Projects unter Settings →
   General. Das ist der wirksamste Einzelhebel gegen ungewollten Support-Aufwand.
4. **Actions-Berechtigungen** auf „Read and write permissions" setzen, sonst kann der
   Release-Workflow kein Tag schreiben.
5. **Hauptbranch `main`**, sonst greift der Workflow nicht.
6. **Eigene Entitätenliste anlegen** unter `_meta/privacy-entities.txt` — mit den echten
   Namen. Sie ist gitignored und darf nie eingecheckt werden. Vorher prüfen, dass die
   `.gitignore`-Zeile wirklich greift: `git status --ignored`.
7. **Hook aktivieren:** `git config core.hooksPath .githooks`.
8. **Ersten Release fahren** und im Browser prüfen, dass Tag und Release erschienen sind.

## Warum es das gibt

Der Jumpstart wird aus einer produktiven, vertraulichen Wissensbasis weiterentwickelt. Der
Rückfluss-Job liest dafür ausgerechnet die Änderungshistorie — die Datei mit der höchsten
Dichte an Kunden-, Arbeitgeber- und Mandatsnamen im ganzen Bestand. Ohne feste Vorkehrung
ist ein Leck keine Möglichkeit, sondern eine Frage der Zeit.

## Die tragende Regel: abstrahieren statt übernehmen

Sie steht vor jeder Prüfung, weil eine Prüfung nur findet, was schon geschrieben wurde.

**Aus dem Hub wird nie übernommen, sondern immer neu formuliert.** Der Rückfluss-Job
liefert Regelvorschläge, keine Textstellen. Kein Kopieren von Passagen, kein Übertragen von
Beispielen, keine Zitate — auch nicht aus scheinbar harmlosen Abschnitten.

Was in den Jumpstart geht, ist die abstrahierte Mechanik. Ein Verfahren, das für einen
bestimmten Kunden entstanden ist, wird zur allgemeinen Regel für die Klasse von Fällen, für
die es gilt. Ein Fehler, der einmal Geld gekostet hat, wird zur Warnung ohne den Vorfall.

**Die Faustregel für jede einzelne Passage:**

> Ergibt sie ohne den konkreten Fall immer noch Sinn? Dann muss der konkrete Fall raus.
> Trägt sie ohne ihn nicht mehr? Dann gehört sie gar nicht ins Paket.

Der zweite Teil ist der wichtigere. Er ist der Grund, warum ein Scanner allein nicht
reicht: Eine Fallbeschreibung ohne jeden Namen kann eindeutig zuzuordnen sein. Branche plus
Größenordnung plus Zeitpunkt genügen oft.

## Der Ablauf vor jedem Release

1. **Diff sichten.** Was hat sich seit dem letzten Release geändert? Jede geänderte Passage
   einzeln gegen die Faustregel halten.
2. **Datenschutzprüfung laufen lassen:**
   ```
   python3 _meta/check_privacy.py
   ```
   Bei Treffern: entfernen oder abstrahieren. Ein Treffer, der bewusst bleiben soll, bekommt
   `jumpstart-ignore` **mit Begründung** in derselben Zeile. Ohne Begründung ist die
   Freigabe wertlos, weil sie später niemand beurteilen kann.
3. **Formatprüfung laufen lassen:**
   ```
   python3 _meta/check_okf.py
   ```
4. **Version setzen** an allen drei Dateiorten und Changelog-Eintrag mit
   Migrationshinweis schreiben. Den Abgleich nicht von Hand prüfen:
   ```
   python3 _meta/check_release.py
   ```
   Das Skript prüft `VERSION`, die Kopie im Plugin, das Versionsfeld im Manifest, dass der
   Marketplace **kein** eigenes Versionsfeld führt, dass der Quellpfad existiert, und dass
   der Changelog-Eintrag vollständig ist und seine Klasse zum Sprung passt. Details in
   `docs/versioning.md`.
5. **Freigabe einholen.** Kein Release läuft automatisch durch. Der Job schlägt vor, ein
   Mensch entscheidet.
6. **Commit und Push.** Der `pre-commit`-Hook prüft ein zweites Mal — als Sicherung, nicht
   als Ersatz für die Schritte davor. Beim Push erzeugt die Automatik Tag **und**
   GitHub-Release; die Release-Beschreibung ist der Changelog-Abschnitt. Der Release ist es,
   der die Benachrichtigung bei den Anwendern auslöst — ein reines Tag tut das nicht.

## Die Entitätenliste

Liegt unter `_meta/privacy-entities.txt`, steht in der `.gitignore` und wird **niemals**
eingecheckt. Sie ist selbst das Leck, das sie verhindern soll.

Aufzunehmen sind mindestens: Arbeitgeber und Stationen, Kunden und Mandate, Produkt- und
Projektnamen, Personennamen aus dem beruflichen Umfeld, Gerätenamen, der eigene
Benutzername, Repository-Koordinaten und Projektkennungen in Musterform.

Kurzschreibungen wie Drei-Buchstaben-Kürzel gehören mit führendem `=` in die Liste, damit
sie nur bei exakter Schreibweise und an Wortgrenzen anschlagen — sonst schlägt jedes zweite
deutsche Wort an.

Die Liste wächst mit. Der feste Termin dafür ist der Konsistenz-Block des wöchentlichen
Durchlaufs: neue Kunden, neue Projekte, neue Kontakte nachtragen.

## Wenn doch etwas durchgerutscht ist

Ein einmal veröffentlichter Commit bleibt über die Historie erreichbar. Ein Force-Push
genügt nicht — alte Tags halten die Commits am Leben. Die saubere Reparatur ist, das
Repository zu löschen und neu anzulegen; die eingeladenen Personen müssen dann neu
eingeladen werden.

Genau deshalb wird **vor** dem Commit geprüft und nicht danach.

## Was das Gate nicht leistet

Es senkt das Risiko erheblich. Es beseitigt es nicht. Der Scanner findet bekannte Namen und
formhafte Muster; die Faustregel fängt die umschriebenen Fälle, aber nur, wenn sie
angewandt wird. Ein Release, bei dem der Diff nicht gelesen wurde, ist ungeprüft — auch
wenn beide Skripte grün melden.
