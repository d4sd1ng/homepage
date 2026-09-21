# Changelog

## 2026-09-21 – Analyse-Datei: Hero-Viewport und Sektionsabstände

Status: geprüft

Geändert:

- `homepage/analyse_bereinigt_hero_viewport_typo_fix (1).html`: Hero-Mindesthöhe an vorhandenen Body-Zoom angepasst; Einstiegskarten schließen den ersten Desktop-Viewport ab.
- Hero-Mindesthöhe zusätzlich um die Divider-Höhe (2 CSS-Pixel) reduziert, damit die Linie innerhalb des ersten Desktop-Viewports sichtbar ist.
- `.section-divider`: vorhandenen Goldverlauf der Sektionslinien übernommen; doppelte Pseudo-Divider ersetzt, vorhandene FAQ-Trennung als Divider-Element erhalten.
- Sektionsabstände sowie Kicker-/Titel-/Untertitel-/Inhaltsabstände vereinheitlicht; konkurrierende Höhenregeln entfernt, Inhaltssektionen dürfen bei Platzbedarf wachsen.
- `main h2`: Schriftgröße um 2 CSS-Pixel erhöht.

Nicht geändert:

- Texte, IDs, Assetpfade, Schriftfamilien, Header, Footer und JavaScript einschließlich Formular-/API-Logik.


## 2026-09-06 – Bildregeln für Social-/Content-Posts

Status: fertig

Geändert:

- `styleguide.md`: neuer Abschnitt 17a „Bildstil für Social-Media- und
  Content-Posts" – keine Personen-/Hände-/Schreibtischfotografie in
  generierten Post-Bildern, Verweis auf die bereits freigegebene
  Modulwelt aus Abschnitt 14 als Standardmotiv für Abläufe/Fähigkeiten,
  Warnhinweis zur bekannten Hologramm-Falle bei abstrakt beschriebenen
  Datenverbindungs-Motiven.
- `styleguide.md`, Abschnitt 17a: Absatz „Richtungsreferenzen" ergänzt –
  verweist auf die neuen Bilder in `austausch/an-team/vorlagen/nurovelle/`
  (`1.png`–`16.png`, `reference_posting_*.png`) als Stimmungsreferenz,
  nicht als fertige Assets; haelt zwei erkennbare Richtungen fest
  (Server-/Rechenzentrums-Fotografie mit Workflow-Panels und
  Dashboard-Requisiten; dunkle Wuerfel-/Modul-Cluster mit goldener
  Kantenbeleuchtung und Zahnraedern als Ausfuehrung von Abschnitt 14).
- `decision_log.md`: passender Eintrag ergänzt.

Nicht geändert:

- Abschnitt 17 (Website-Assets) und alle übrigen Abschnitte bleiben
  unverändert.
- Die bestehende VERBOTEN-Liste in Judes eigenem Rollentext (u.a.
  „Platinen") ist NICHT Teil dieser Änderung und wurde hier bewusst
  nicht in den Styleguide übernommen, da sie nie freigegeben war und
  echten Assets widerspricht (siehe `decision_log.md`).

## 2026-08-29 – Homepage-Abstände, Kartenflächen, FAQ und Analyse-Header

Status: fertig

Geändert:

- `homepage/index.html`: Hero-Kicker auf Weiß gesetzt, Subtitle-/Body-Abstand und CTA-/Statistikabstand korrigiert.
- `homepage/index.html`: Kartenflächen und Ergebnisrahmen auf `--color-emerald` vereinheitlicht; Kartenrahmen erscheint beim gemeinsamen `is-visible`-Reveal.
- `homepage/index.html`: Deep-Potenzialanalyse-Text erweitert, CTA näher an den Text gesetzt und FAQ-Elemente auf gleiche Spaltenbreite gestreckt.
- `homepage/analyse.html`: Header-CTA durch `Erstgespräch vereinbaren` mit Calendly-Link ersetzt.

Nicht geändert:

- Bestehende Formular-, API-, Lead-, Newsletter- und Notion-Integrationen.
- Bestehende IDs, Assetpfade, Kartenlinks und JavaScript-Logik.

## 2026-08-30 – Stripe-Testkonfiguration angelegt

Status: fertig

Geändert:

- `homepage/stripe-config.js`: neu angelegt. Setzt `window.NUROVELLE_STRIPE_PUBLISHABLE_KEY` (Publishable Key des Testmodus) und `window.NUROVELLE_STRIPE_MODE` (`test`) nach der bestehenden `window.NUROVELLE_*`-Konvention aus `analyse.html`. Reine Konfiguration, keine Bezahllogik.
- `architecture.md`: Abschnitt „Stripe-Konfiguration" ergänzt.
- `todo.md`: Abschnitt „Zahlung / Stripe" mit drei offenen Punkten ergänzt.

Nicht geändert:

- HTML-Seiten unter `homepage/`: die Datei ist in keiner Seite eingebunden.
- Layout, Texte, Farben, Fonts, Assets, Formular- und Analyse-Logik.
- `.github/workflows/deploy.yml`: der rsync-Ausschluss betrifft keine `.js`-Dateien, die Datei wird ohne Anpassung mit ausgerollt.

Anmerkung: Der Publishable Key ist für den Browser bestimmt und deshalb öffentlich; der Secret Key (`sk_...`) gehört nicht in dieses Repository.

## 2026-08-14 – Goldwort-Regel nach Medium getrennt, ein Goldverlauf für Dokumente

Status: fertig

Geändert:

- `styleguide.md`: Goldwort-Regel nach Medium getrennt (Website: ganze Überschrift; alles andere: ein tragendes Wort). Neuer Abschnitt „Goldverlauf in Dokumenten" mit dem dreistufigen Verlauf und der Begründung, warum der siebenstufige Website-Verlauf dort nicht taugt.
- `decision_log.md`: Eintrag zur Goldwort-Regel entsprechend präzisiert, zweiter Eintrag zum Dokumentverlauf ergänzt.

Nicht geändert:

- `--gold-1` in den 14 HTML-Dateien: der Website-Verlauf bleibt unverändert.
- Produktionscode, Farben, Komponenten, Assets.

Anmerkung: Die Vorlagen für Briefkopf, Angebot, Projektvertrag, AVV und E-Mail-Signatur liegen ausserhalb dieses Repos unter `Jude/data/marke/`. Sie verwenden den dreistufigen Dokumentverlauf.


## 2026-08-14 – Fontsystem auf Exo 2 + Inter, Goldwort-Regel, Regeln für das Agenten-Team

Status: fertig

Geändert:

- `decision_log.md`: fünf neue Entscheidungen aufgenommen (Exo 2 + Inter als Fontsystem, Goldwort-Regel, Wortmarke immer gold, keine Platzhalterwerte, Lesezugriff des Agenten-Teams, Newsletter ohne Gestaltung). Der Eintrag vom 2026-07-31 (Tapera + Inter) ist als abgelöst gekennzeichnet, nicht entfernt.
- `styleguide.md`: Abschnitt 4 auf Exo 2 + Inter umgestellt, Liste abgelöster Fontstacks entfernt; Abschnitt 3 um die Goldwort-Regel ergänzt.
- `nurovelle-tokens.css` (in `project_files/`): `--font-display` von Tapera auf Exo 2 umgestellt.
- `homepage/nurovelle-tokens.css`: `--font-display` und `--font-technical` von Eastman Grotesque Alt auf Exo 2 umgestellt. Die beiden Dateien waren inhaltlich auseinandergelaufen.
- `task_contract.md`: Abschnitte „Platzhalter" und „Agenten-Team" ergänzt.
- `todo.md`: Webfont-Einbindung, Prüfung des Produktionscodes auf alte Fontstacks, Umsetzung der Goldwort-Regel, doppelte Tokens-Datei und nicht eingecheckte Gold-SVGs als offen aufgenommen.

Nicht geändert:

- `index.html` und übriger Produktionscode
- Farben, Abstände, Komponenten und Layout
- Assets im Repo
- `project_overview.md` und `architecture.md`

Anmerkung: Die Schriftdateien selbst liegen ausserhalb des Repos unter `/usr/local/share/fonts/nurovelle/` (Exo 2 und Inter, variable TrueType, jeweils mit OFL-Lizenztext). Die Einbindung als Webfont steht noch aus und ist in `todo.md` geführt.

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

## 2026-08-14 – Projectfiles entflechtet und konsolidiert

Status: fertig

Geändert:

- `project_overview.md`: auf Projektumfang, Conversion-Pfade, Homepage-Struktur und Projektziel reduziert; Stand 2026-07-14 übernommen.
- `task_contract.md`: auf reine Arbeits-, Änderungs- und Dokumentationsregeln reduziert.
- `styleguide.md`: als alleinige Designquelle konsolidiert; Tapera + Inter, Nurovelle-Materialsprache, Goldsystem, Metallic-Gold-Verlauf, CTA-, Card-, Download-, Hero- und Bildregeln zusammengeführt.
- `architecture.md`: neu als alleinige technische Architektur- und Integrationsquelle angelegt.
- `assets.md`: aus vorhandener Assetliste als alleinige Asset-/Pfadquelle konsolidiert.
- `todo.md`: auf ausschließlich offene/laufende Aufgaben reduziert.
- `decision_log.md`: auf Entscheidungen mit Verweisen zur jeweils zuständigen aktiven Datei reduziert.
- `nurovelle-tokens.css`: Designhoheit vom alten Implementation Brief auf `styleguide.md` umgestellt; Fontsystem auf Tapera + Inter synchronisiert; Metallic-Gold- und CTA-Materialtokens aufgenommen.
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`: als aktive Quelle stillgelegt und auf Archiv-/Weiterleitungsfunktion reduziert.

Nicht geändert:

- `index.html`
- produktive Homepage
- `shared-header-footer.css`
- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`
- reale Backend-/API-Systeme
- reale Notion-/Mail-/Lead-Integrationen
- Assetdateien selbst
