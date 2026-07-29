---
name: jumpstart-upgrade
description: Eine bestehende Wissensbasis auf eine neuere Fassung des Setups heben – Versionsdifferenz bestimmen, Änderungen aus dem Changelog gegen den eigenen Bestand halten, gebündelt zur Freigabe vorlegen und einarbeiten. Verwenden bei „prüf mein Setup gegen den neuen Stand", „gibt es eine neuere Version", „Setup aktualisieren", „Upgrade fahren" – und immer dann, wenn jemand eine Release-Benachrichtigung bekommen hat oder wissen will, ob seine Basis noch aktuell ist.
---

# Jumpstart-Upgrade — bestehende Basis nachziehen

## Was dieser Skill tut

Er hebt eine bereits eingerichtete Wissensbasis auf eine neuere Fassung des Setups —
**ohne Neuaufbau**. Es wird nur die Differenz eingearbeitet, und nur das, was zur Stufe und
zur tatsächlichen Arbeitsweise der Person passt.

## Ablauf

**1. Eigenen Stand feststellen.** Im Frontmatter der Wurzel-`index.md` stehen
`setup_version` und `setup_track`. Fehlen sie, ist die Basis vor Einführung dieser Felder
entstanden — dann den Stand aus `log.md` und der vorhandenen Struktur abschätzen und die
Felder im Zuge des Upgrades ergänzen.

**2. Neuen Stand feststellen.** Die Version steht in der Datei `VERSION` im
Wurzelverzeichnis des Setup-Pakets. Sind beide gleich, ist nichts zu tun — das sagen und
aufhören.

**3. Changelog lesen.** Alle Einträge zwischen der eigenen und der neuen Version. Jeder
Eintrag trägt einen Migrationshinweis. Einträge, die nur eine andere Stufe betreffen,
werden übersprungen — einem Stufe-1-Nutzer wird keine Marketplace-Aktualisierung
vorgeschlagen.

**4. Gegen den eigenen Bestand halten.** Für jede Änderung prüfen: Ist die betroffene Datei
oder Regel überhaupt vorhanden? Wurde sie seit dem Aufsetzen individuell angepasst? **Eine
eigene Anpassung wird nicht stillschweigend überschrieben.** Bei Konflikt beide Fassungen
zeigen und entscheiden lassen.

**5. Gebündelt vorlegen.** Eine Liste mit je einer Zeile: was ändert sich, warum, welche
Datei. Klassifiziert nach *empfohlen*, *optional* und *betrifft dich nicht*. Dann Freigabe
einholen — einzeln oder als Ganzes.

**6. Einarbeiten**, `setup_version` (und bei Stufenwechsel `setup_track`) setzen,
`log.md`-Eintrag schreiben, Prüfskripte laufen lassen, sichern.

## Leitplanken

* **Nur mit Freigabe.** Auch ein reines Setup-Upgrade ist ein Schreibzugriff auf den
  Wissensbestand.
* **Kein Zwang zur Vollständigkeit.** Wer eine Neuerung nicht will, bekommt sie nicht.
  `setup_version` wird trotzdem gesetzt, mit einer Notiz in `log.md`, was bewusst
  ausgelassen wurde — sonst wird dieselbe Änderung beim nächsten Upgrade erneut
  vorgeschlagen.
* **Datenschutzteile sind keine Option.** Sicherheitsrelevante Nachträge — Prüfskripte,
  Ausschlüsse in der `.gitignore`, Regeln zur Vertraulichkeit — werden als *empfohlen*
  vorgelegt und mit einem Satz begründet, warum ein Auslassen riskant ist.
* **Ein Versionsschritt.** Das gesamte Upgrade ist ein Sicherungsvorgang, nicht mehrere.

---

*Bei Widerspruch zwischen diesem Skill und `conventions.md` im Hub gilt `conventions.md`.*

*Status: Entwurf, noch nie gegen ein echtes Versions-Delta gelaufen. Beim ersten
tatsächlichen Upgrade prüfen, ob Schritt 4 den Konfliktfall sauber erkennt.*
