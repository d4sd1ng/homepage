# Changelog

## 2026-07-11 – Sektion 2 mit drei Glaskarten implementiert

Status: fertig

Geändert:

- `index.html`: neue Sektion `#ki-projekt-start` direkt nach dem Hero eingefügt.
- Sektion 2 gemäß Brief umgesetzt: drei Glaskarten links, Textblock rechts, CTA zu `analyse.html`.
- Kartenreihenfolge verbindlich als 2, 1, 3 umgesetzt.
- Responsive Darstellung für Desktop, Tablet und Mobile ergänzt.
- Kartenassets unter `assets/cards/section2/` abgelegt.

Nicht geändert:

- Hero
- Header, Sidebar und Footer
- bestehende nachfolgende Sections
- Inhalte der drei Kartenbilder

## 2026-07-07 – Hero-Orb-Originalvorgabe gesichert

Status: fertig

Geändert:

- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`: Hero-Orb-Abschnitt mit der Originalvorgabe aus dem Chat ersetzt.
- `styleguide.md`: Hero-Animation konkretisiert: Orb kommt hinter den Cube; Originalvorgabe ist SCSS/HAML-Partikel-Orb.
- `nurovelle-animations.css`: bestehende `.nv-hero-orb`-/Conic-Umsetzung als rekonstruierte Adaption gekennzeichnet, nicht als Original.
- `nurovelle-hero-orb-original.scss`: Original-SCSS separat gesichert.
- `nurovelle-hero-orb-original.haml`: Original-HAML separat gesichert.

Nicht geändert:

- `index.html`
- Homepage-Layout
- bestehender Cube
- Produktions-CSS-Verhalten auf der Website

## 2026-07-07 – Divider-Diagonal-Originalreferenz gesichert

Status: fertig

Geändert:

- `nurovelle-divider-diagonal-original-reference.txt`: vom Nutzer gelieferte Diagonal-Section-/Divider-Referenz unverändert gesichert.
- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`: Variante C als technische Prüfvariante mit Originalreferenz, übernehmbarem Kern und ausgeschlossenen Demo-Bestandteilen dokumentiert.
- `styleguide.md`: Divider-Regeln ergänzt: `skewY()` nur auf Hintergrund-/Pseudo-Elemente, Content bleibt unverzerrt.
- `nurovelle-animations.css`: bestehende Divider-C-CSS als Nurovelle-Adaption gekennzeichnet, nicht als Originalcode.

Nicht geändert:

- `index.html`
- Homepage-Layout
- produktive Section-Divider auf der Website
- Hero-/Cube-Animation
- CTA-Buttons

## 2026-07-07 – SVG-Divider-Originalreferenz gesichert

Status: fertig

Geändert:

- `nurovelle-divider-svg-original-reference.txt`: vom Nutzer gelieferte SVG-Separator-/Divider-Referenz unverändert gesichert.
- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`: Variante A als SVG-Schräg-Divider / Separator mit Originalreferenz, übernehmbarem Kern und ausgeschlossenen Demo-Bestandteilen dokumentiert.
- `styleguide.md`: Divider als verbindlicher Homepage-Bestandteil festgehalten; finale Divider-Form bleibt Prüfentscheidung zwischen SVG-Separator und Diagonal-/Skew-Varianten.
- `nurovelle-animations.css`: Nurovelle-Adaption für SVG-Separator ergänzt, nicht als Originalcode gekennzeichnet.

Nicht geändert:

- `index.html`
- Homepage-Layout
- produktive Section-Divider auf der Website
- Hero-/Cube-Animation
- CTA-Buttons


## 2026-07-07 – Pure-CSS-Angled-Divider-Originalreferenz ergänzt

Status: fertig

Geändert:

- `nurovelle-divider-pure-css-angled-original-reference.scss` als unveränderte Originalreferenz gespeichert.
- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md` um Divider-Variante B mit technischer Einordnung ergänzt.
- `styleguide.md` um Regeln für Variante B ergänzt.
- `decision_log.md` um die Entscheidung zur gesicherten Variante-B-Referenz ergänzt.
- `nurovelle-animations.css` Abschnitt 7B als Nurovelle-Adaption mit Fallback-/Support-Logik ergänzt.
- `todo.md` um Vergleich der Pure-CSS-Angled-Sections gegen SVG- und Skew-Variante ergänzt.

Nicht geändert:

- `index.html`
- produktive Homepage-Struktur
- finale Divider-Auswahl

## 2026-07-07 – CTA-Originalreferenzen und Board-Option gesichert

Status: fertig

Geändert:

- `nurovelle-button-original-references.md`: neue Originalreferenzdatei für Arrow-Reveal, Press-Button und Golden-Button-Farblogik erstellt.
- `nurovelle-section-board-codepen-reference.md`: externe CodePen-Option für Section-/Board-Komponente dokumentiert.
- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`: CTA-System neu eingeordnet und Board-Option ergänzt.
- `styleguide.md`: CSS-first-Regel und Prüfkomponentenliste ergänzt.
- `decision_log.md`: Entscheidung zur Button-Originalreferenz und Board-Prüfoption ergänzt.
- `todo.md`: Prüfpunkte für Navigation, Burger, Breadcrumbs, Social Buttons, Hero, Divider, Cards, Board und CTA-System ergänzt.

Nicht geändert:

- `index.html`
- produktive Homepage
- finale CTA-Auswahl
- finale Board-/Section-Auswahl
- finale Divider-Auswahl

## 2026-07-07 – 8 Zusatzdateien in Projektfiles übernommen

Status: fertig

Geändert:

- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`: vollständiges Referenzarchiv für die 8 zuvor separat erzeugten Dateien ergänzt.
- `styleguide.md`: Regel ergänzt, dass die Einzeldateien nicht als eigenständige aktive Designquellen gelten.
- `decision_log.md`: Entscheidung zur Konsolidierung der Zusatzdateien dokumentiert.
- `task_contract.md`: Arbeitsregel gegen verstreute Referenzdateien ergänzt.
- `project_overview.md`: CSS-/Interaktionsreferenzen als konsolidierte Projektgrundlage aufgenommen.
- `todo.md`: Konsolidierung abgeschlossen und offene Prüfaufgaben ergänzt.

Übernommen:

1. `nurovelle_cta_button_preview.html`
2. `nurovelle-hero-orb-original.scss`
3. `nurovelle-hero-orb-original.haml`
4. `nurovelle-divider-diagonal-original-reference.txt`
5. `nurovelle-divider-svg-original-reference.txt`
6. `nurovelle-divider-pure-css-angled-original-reference.scss`
7. `nurovelle-button-original-references.md`
8. `nurovelle-section-board-codepen-reference.md`

Nicht geändert:

- `index.html`
- produktive Homepage
- finale Divider-Auswahl
- finale CTA-Auswahl
- finale Hero-Orb-/Cube-Entstehungslogik
