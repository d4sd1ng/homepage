# Aktueller Homepage-Ausführungsstand

Status: in Arbeit
Stand: 2026-07-31

Diese Datei dokumentiert den aktuellen freigegebenen Stand aus der laufenden Umsetzung. Sie dient als direkte Aktualisierung für die weitere Arbeit an der Nurovelle-Homepage, bis die bestehenden Hauptdokumente vollständig nachgezogen sind.

## Vorrangregel

Die aktuelle ausdrücklich freigegebene Benutzervorgabe überschreibt ältere Reihenfolgen in Brief, Overview oder Zwischenständen.

Für die aktuelle Umsetzung gilt deshalb nicht mehr die alte Reihenfolge „Potenzialanalyse vor Projektidee“, sondern die unten dokumentierte Reihenfolge.

## Aktuelle Startseiten-Reihenfolge

1. Hero
2. Warum Nurovelle (`warum-nurovelle`)
3. Der erste Schritt zu Ihrem KI-Projekt (`ki-projekt-start`)
4. Sie haben bereits eine konkrete KI-Idee? (`projektidee`)
5. KI-Leistungen von Nurovelle (`leistungen`)
6. Kompetenzen (`kompetenzen`)
7. Kostenlose KI-Potenzialanalyse (`potenzialanalyse`)
8. Vom Geschäftsprozess zur KI-Lösung (`prozess-zur-loesung`)
9. Kontakt (`kontakt`)
10. Download-Bereich (`downloads`)
11. FAQ (`faq`)
12. Footer

Prozess, Kontakt, Downloads, FAQ und Footer sind am 2026-07-31 aus `index1.html` portiert worden.


## Aktuelle Divider-Abfolge

1. Nach Hero: Divider A – SVG-Schräg-Divider / Separator
2. Nach Section 2 „Der erste Schritt zu Ihrem KI-Projekt“: Divider B normal
3. Nach Section 3 „Sie haben bereits eine konkrete KI-Idee?“: Divider B reverse
4. Nach Section 4 „Kostenlose KI-Potenzialanalyse“: Divider C zur nächsten Trennung

## Bedeutung für die Umsetzung

- Projektidee steht vor Potenzialanalyse.
- Potenzialanalyse kommt eine Sektion später.
- Divider A, B normal, B reverse und C werden als Live-Übersicht verwendet.
- Diese Abfolge ist noch keine finale Auswahl einer einzigen Divider-Variante.
- Finale Divider-Entscheidung bleibt nach Sichtprüfung offen.

## Weiterhin verbindlich

- keine zusätzlichen Sections ohne Auftrag
- keine Textkürzung ohne Auftrag
- keine Layoutänderung ohne Auftrag
- keine neuen Farben
- keine Demo-Farben aus Referenzen
- keine Bild-, GIF- oder Video-Divider
- keine Verzerrung von Text, Cards, CTAs oder Hero-Visuals
- alle Potenzialanalyse-, Anfrage- und Erstgespräch-CTAs führen zu `analyse.html`
- Download-CTAs führen zu `#downloads` oder `praxisleitfaden.html`

## Noch offen

- bestehende Hauptdateien vollständig nachziehen:
  - `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`
  - `project_overview.md`
  - `decision_log.md`
  - `task_contract.md`
  - `todo.md`
  - `changelog.md`

## Gestaltungsstand (2026-07-31)

- Typo-Rollensystem aktiv: 17 Rollen als `--t-<rolle>` / `--w-<rolle>` in `:root`. Kicker/Titel/Subtitle/Fließtext einheitlich 16/600, 100/800, 24/600, 20/400 über alle elf Abschnitte.
- Zwei Flächenfarben im Wechsel: `#050505` dunkel, `#010603` grün. Karte auf dunkel `#17251d`, Karte auf grün `#1a1a1a`.
- Alle Goldrahmen über `--gold-3` mit Doppel-Hintergrund-Technik.
- `body { zoom: 0.8 }`: Werte im Stylesheet sind CSS-Pixel, gerendert wird das 0.8-fache.
- Abschnitte auf Viewporthöhe (`calc(125vh - var(--header-height))`), Inhalt vertikal zentriert. Ausnahmen: `leistungen` und `potenzialanalyse` dürfen scrollen.
- Analyse- und Kontaktformular unverändert, Auto-Lead-Anbindung intakt.
