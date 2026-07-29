<!-- JUMPSTART-VORLAGE — Hinweis für Claude, beim Anlegen entfernen.
     Wird als workspace/README.md abgelegt. Unterstruktur an den Beruf der Person anpassen. -->
# Workspace — Regeln

Dies ist der Arbeitsraum für laufende Vorgänge, **nicht** der Wissensbestand.

## Was hier gilt

* **Klarnamen und Zahlen sind erlaubt.** Dieser Ordner ist nicht versioniert und verlässt
  den Wissensbestand nicht.
* **Kein Frontmatter-Zwang, keine Freigabe-Pflicht.** Hier zählt Arbeitsgeschwindigkeit.
  Claude darf frei schreiben.
* **Nichts verlässt den Workspace unanonymisiert.** Alles, was in den Wissensbestand oder
  nach außen geht, läuft vorher durch die Extrakt-Regel aus `conventions.md`.
* **Arbeitsstand, kein Archiv.** Verallgemeinerbares wird im Weekly Review destilliert und
  gehoben, Erledigtes gelöscht. Ein Workspace, der nur wächst, ist kaputt.

## Struktur

* `TASKS.md` — offene Punkte, Zusagen, Wiedervorlagen. Jede Aufgabe braucht ein Datum;
  Aufgaben ohne Datum sind Absichten.
* `meetings/JJJJ-MM-TT-thema.md` — Notizen zu Terminen.
* <weitere Ordner je nach Beruf>

Vorlagendateien bekommen einen Unterstrich als Präfix (`_vorlage-meeting.md`), damit sie in
der Sortierung oben stehen und nicht mit echten Vorgängen verwechselt werden.

## Hinweis bei Mehrgeräte-Betrieb (Stufe 2 und 3)

Der Workspace ist von der Versionierung ausgenommen und existiert damit auf jedem Gerät
verschieden. Er wird **nicht** synchronisiert. Was geräteübergreifend verfügbar sein soll,
muss in den Wissensbestand.
