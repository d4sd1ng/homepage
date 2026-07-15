# AGENTS.md

## Geltungsbereich

Diese Datei gilt global für das gesamte Repository.

## Arbeitsgrundsatz

Ändere ausschließlich, was ausdrücklich beauftragt wurde.

Keine freie Interpretation.
Keine stillen Zusatzänderungen.
Keine Umstrukturierung ohne Auftrag.
Keine Kürzung oder Erweiterung von Texten ohne Freigabe.
Keine Layoutänderung ohne Auftrag.
Keine Änderung vorhandener Entscheidungen.

## Pflichtprüfung vor jeder projektbezogenen Änderung

Vor jeder Änderung müssen diese Dateien vollständig geprüft werden:

1. `project_overview.md`
2. `task_contract.md`
3. `decision_log.md`
4. `todo.md`
5. `nurovelle-tokens.css`
6. vorhandene CSS-Referenzen
7. `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`
8. `changelog.md`
9. `styleguide.md`
10. `nurovelle_homepage_visible_content.md`
11. `copilot_homepage_update.json`

Bei Widersprüchen gilt diese Reihenfolge:

1. aktuelle ausdrückliche Benutzervorgabe
2. `task_contract.md`
3. `decision_log.md`
4. `project_overview.md`
5. `todo.md`
6. eigene Vorschläge nur nach Freigabe

## Verbindliches Vorgehen

1. Bestehende Zieldatei vollständig lesen.
2. Relevante Pflichtdateien vollständig lesen.
3. Bestehende IDs, Klassen, Hooks, Assetpfade und Logik erfassen.
4. Auftrag exakt gegen die Dokumentation abgleichen.
5. Nur ausdrücklich beauftragte Stellen ändern.
6. Keine unbekannten Entscheidungen selbst treffen.
7. Bestehende Funktionalität erhalten.
8. Diff vollständig prüfen.
9. HTML, CSS und JavaScript auf Folgefehler prüfen.
10. `changelog.md` nur mit tatsächlich ausgeführten Änderungen aktualisieren.
11. Abschlussbericht mit exakter Änderungsliste ausgeben.

## Strikte Verbote

- keine Texte kürzen
- keine Texte ergänzen
- keine Texte umformulieren
- keine IDs umbenennen
- keine Assetpfade verändern
- keine Assets austauschen
- keine Sections hinzufügen
- keine freigegebenen Sections entfernen
- keine neuen Farben oder Verläufe
- keine neuen Schriften
- keine neuen Buttonvarianten
- keine neuen globalen Overrides
- keine neuen `!important`-Regeln
- keine funktionierende JavaScript-Logik ersetzen
- keine Formularlogik beschädigen
- keine Success-, Error-, Consent- oder Honeypot-Logik entfernen
- keine alten Inhalte ungeprüft übernehmen
- keine fehlenden Links, Dateipfade oder Assets erfinden
- keine stillen Fallbacks einbauen

## Typografie

Verbindlich:

- Headlines und große Titel: `Eastman Grotesque Alt`
- Fließtext, Navigation, Buttons, Formulare, Cards und Footer: `Inter`

Nicht neu verwenden:

- Tapera
- Bebas Neue
- Anca Coder
- Coder Pro
- Raleway
- Roboto

## Statuswerte

Nur diese Statuswerte verwenden:

- offen
- in Arbeit
- fertig
- geprüft
- freigegeben
- blockiert

## Abschlussbericht

Nach jeder Änderung ausgeben:

### GEÄNDERT

- exakte Dateien
- exakte Bereiche
- exakte Texte
- exakte CSS-Klassen
- exakte JavaScript-Bereiche

### NICHT GEÄNDERT

- bewusst unberührte Komponenten
- erhaltene Assetpfade
- erhaltene technische Logik

### OFFEN

- fehlende eindeutige Assetzuordnungen
- fehlende reale Links
- fehlende Downloadpfade
- dokumentierte Konflikte

### GETESTET

- HTML-Struktur
- CSS
- JavaScript
- Formular
- Desktop
- Mobile
- Reduced Motion
- Browserkonsole
