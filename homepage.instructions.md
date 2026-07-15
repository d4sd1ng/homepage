---
applyTo:
  - "index.html"
  - "**/*.css"
  - "**/*.js"
---

# Nurovelle Homepage Instructions

## Verbindliche Quellen

Vor Änderungen an Homepage-Dateien vollständig lesen:

1. `AGENTS.md`
2. `copilot_homepage_update.json`
3. `nurovelle_homepage_visible_content.md`
4. `styleguide.md`
5. `nurovelle-tokens.css`
6. `nurovelle-animations.css`
7. `shared-header-footer.css`
8. `decision_log.md`
9. `task_contract.md`
10. `changelog.md`

## Ziel

Die bestehende `index.html` kontrolliert an den freigegebenen Homepage-Stand anpassen, ohne vorhandene Funktionalität oder unbeauftragte Bereiche zu verändern.

## Hintergrundsystem

- Hero: Partikelhintergrund hinter dem bestehenden Cube
- Warum Nurovelle: Schwarz
- Der erste Schritt zu Ihrem KI-Projekt: Dunkelgrün
- Konkrete KI-Idee: Schwarz
- Potenzialanalyse: Dunkelgrün
- Formular: Schwarz
- KI-Leistungen: Dunkelgrün
- Vom Geschäftsprozess zur KI-Lösung: Schwarz
- Download-Bereich: Dunkelgrün
- Kontakt: Schwarz
- FAQ: Dunkelgrün
- Footer: Schwarz

Nur bestehende Nurovelle-Farbvariablen verwenden.

## Hero

- bestehenden Cube erhalten
- Partikelanimation hinter dem Cube
- keine freie Ersatzanimation
- keine Conic-/Noise-Maske als Ersatz
- `prefers-reduced-motion` erhalten

## Erster Schritt zu Ihrem KI-Projekt

Genau drei Cards:

1. Prozess klären
2. Daten prüfen
3. Umsetzung planen

Animation:

- Start außerhalb des linken Bildschirmrands
- nacheinander auf Endposition sliden
- Texte während der Bewegung unsichtbar
- Texte erst nach Ankunft einblenden
- Reihenfolge 1, 2, 3
- keine Bewegung von rechts, oben oder unten
- Reduced-Motion-Fallback ohne Slide

## Konkrete KI-Idee

Drei Fotoelemente:

- Prozessautomatisierung
- Datenbasierte Entscheidungshilfe
- Interne Wissenssuche

Regeln:

- rechteckiges Bild 30 % größer
- quadratische Bilder behalten ihre Größe
- grünen Streifen rechts an beiden quadratischen Bildern entfernen
- keine Bilder austauschen
- keine Bildausschnitte frei ändern

## Branchen

Aktuell nicht umsetzen.

- keine Branchencards
- keine alten Branchentexte
- keine Ersatzsektion

## Potenzialanalyse und Formular

Texte exakt aus `nurovelle_homepage_visible_content.md` übernehmen.

Formularlogik vollständig erhalten:

- Pflichtfelder
- Consent
- Datenschutz
- Honeypot
- Submission
- Success
- Error

Keine Feldnamen ändern, wenn die Verarbeitung davon abhängt.

## KI-Leistungen

Genau elf Karten.

Linke Seite:

- Icon im Rahmen
- Trennstrich
- `◎ Einsatzbereiche`
- genau drei Bulletpoints

Rechte Seite:

- Nummer im Rahmen
- Titel
- Untertitel
- Ergebnis-Card
- Ergebnis-Symbol
- Ergebnisüberschrift
- kurzer Ergebnistext

Nicht ergänzen:

- keinen zusätzlichen Beschreibungssatz
- keine zusätzlichen Bulletpoints
- keine zusätzliche Text-Card

Iconpfade:

- `assets/cards/service/icons/1.png`
- `assets/cards/service/icons/2.png`
- `assets/cards/service/icons/3.png`
- `assets/cards/service/icons/4.png`
- `assets/cards/service/icons/5.png`
- `assets/cards/service/icons/6.png`
- `assets/cards/service/icons/7.png`
- `assets/cards/service/icons/8.png`
- `assets/cards/service/icons/9.png`
- `assets/cards/service/icons/10.png`
- `assets/cards/service/icons/11.png`
- Ergebnis: `assets/cards/service/icons/ergebnis.png`

Keine Ersatzicons erzeugen.

## Vom Geschäftsprozess zur KI-Lösung

Sechs Module:

1. Aufgabe erfassen
2. KI-Potenzial bewerten
3. Daten prüfen
4. Prozess modellieren
5. Lösung auswählen
6. Umsetzung strukturieren

Darstellung:

- räumlicher 3D-Pfad
- klare Leserichtung 1 bis 6
- perspektivische Tiefenstaffelung
- Verbindung über Pfadsegmente
- nur Modulbezeichnungen
- keine Erklärungstexte
- keine Bulletpoints
- keine Zusatz-Cards
- kein CTA

Fehlende Assetzuordnung nicht erraten.

## Downloads

Vier Karten:

- Case Study KI-Automatisierung
- ROI-Rechner für KI-Automatisierung
- Prompt Guide
- Checkliste KI-Potenziale

Download-Aktion:

- unten rechts
- als Schrift oder kleine Pill
- kein großer CTA
- kein primärer Goldbutton
- Success und Error ersetzen den Text an derselben Stelle
- Success nur nach echtem Downloadstart

Keine Downloadpfade erfinden.

## Kontakt

- Einleitung oben
- darunter 40/60-Zweispaltenlayout
- links Portraitkarte
- rechts Kontaktkarte
- Mobile: Einleitung, Portraitkarte, Kontaktkarte

Texte exakt aus der Content-Datei übernehmen.

## FAQ

- acht Fragen
- acht Antworten
- Akkordeon/Expander erhalten
- Fragen nicht kürzen
- Kennzahlen kompakt als Fortschrittsanzeigen
- keine großen Kennzahlen-Buttons

## Footer

Enthalten:

- kurze Unternehmensbeschreibung
- Social Icons
- nützliche Links
- Newsletter
- Kontakt
- Rechtliches
- Copyright
- Nach-oben-Button

Sichtbar, aber deaktiviert und grau:

- Aktuelles
- Team
- SEO
- Pakete

Keine nicht vorhandenen Seiten verlinken.

## Prüfung vor Abschluss

- HTML-Tags korrekt geschlossen
- keine doppelten IDs
- keine gebrochenen Assetpfade
- Formularlogik intakt
- keine JavaScript-Fehler
- Desktop geprüft
- Mobile geprüft
- Reduced Motion geprüft
- Browserkonsole geprüft

Abschlussbericht exakt nach `AGENTS.md`.
