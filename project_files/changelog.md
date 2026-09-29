# Changelog

## 2026-09-29 – Divider und Footer-Abstand in analyse.html korrigiert

Status: fertig

Geändert:

- `homepage/analyse.html`: normale Section-Divider auf `0.8px` und den Homepage-Goldverlauf gesetzt.
- `homepage/analyse.html`: Footer-Abschlussdivider explizit über `.footer::before` sichtbar abgesichert.
- `homepage/analyse.html`: Abstand zwischen Footer-Titel und folgendem Inhalt auf `var(--nv-space-md)` gesetzt.
- Keine weiteren Inhalte oder Layoutbereiche verändert.

## 2026-09-29 – Hero-Titel und Definition-Cards in analyse.html korrigiert

Status: fertig

Geändert:

- `homepage/analyse.html`: Hero-Titel in zwei feste Zeilen aufgeteilt.
- `homepage/analyse.html`: Desktop-Hero-Spalten so angepasst, dass die erste Titelzeile nicht intern umbrechen kann.
- `homepage/analyse.html`: die beiden Definition-Cards auf `max-width: 1200px` gesetzt und horizontal zentriert.
- Keine weiteren Inhalte oder Sektionen verändert.

## 2026-09-29 – Grüne 3D-Bullets aus index.html in analyse.html übernommen

Status: fertig

Geändert:

- `homepage/analyse.html`: normale Bulletpoints verwenden jetzt exakt `assets/bulletpoint.png` wie auf `index.html`.
- Betroffen: `.label-list`, `.dot-list` und `.card-bullets`.
- Der bestehende grüne Rand `#55863f` und die runde Darstellung wurden übernommen.
- Nummerierte Punkte `01–08` im Leistungsumfang bleiben unverändert.

## 2026-09-29 – Hero-Bildpfad in analyse.html korrigiert

Status: fertig

Geändert:

- `homepage/analyse.html`: Hero-Bildpfad von `assets/Module/detail_pages_grafics/Analyse_detail _final.png` auf den tatsächlich vorhandenen Pfad `assets/detail_pages_grafics/Analyse_detail _final.png` korrigiert.
- Keine weiteren Inhalte oder Layoutregeln verändert.

## 2026-09-29 – Doppelten Footer-Divider in analyse.html entfernt

Status: fertig

Geändert:

- `homepage/analyse.html`: lokale `.footer { border-top: ... }`-Regeln entfernt.
- `homepage/analyse.html`: lokale `.footer-bottom { border-top: ... }`-Regeln entfernt.
- Der Footer verwendet damit nur noch den gemeinsamen Divider aus `shared-header-footer.css` über `.footer::before`.
- Keine Footer-Inhalte oder Abstände verändert.

## 2026-09-29 – Hero-Titel analyse.html zweizeilig festgelegt

Status: fertig

Geändert:

- `homepage/analyse.html`: Hero-Titel mit festem Zeilenumbruch nach „Ihrem“.
- Darstellung: „Wo lohnt sich KI in Ihrem“ / „Unternehmen wirklich?“.
- Keine weiteren Inhalte oder Layoutregeln verändert.

## 2026-09-29 – analyse.html auf Homepage-Breite und Shared Header/Footer umgestellt

Status: fertig

Geändert:

- `homepage/analyse.html`: globalen `body { zoom: 0.8; }`-Hack entfernt.
- `homepage/analyse.html`: Contentbreite auf `1560px` und Seiten-Gutter auf das aktuelle `index.html`-System `clamp(19.2px, 4.8vw, 96px)` angeglichen.
- `homepage/analyse.html`: `nurovelle-tokens.css` und `shared-header-footer.css` eingebunden.
- `homepage/analyse.html`: drei nachträgliche lokale Header-Override-Blöcke entfernt, damit der Shared Header die maßgebliche CSS-Quelle ist.
- `homepage/analyse.html`: Section-Abstände vereinheitlicht und alte Verschiebungs-Hacks (`translateY`, große künstliche Bottom-Margins) neutralisiert.
- Formularstruktur, Pflichtfelder, Honeypot sowie API-/Success-/Error-Logik nicht verändert.

## 2026-09-29 – Zwei CTAs in Leistungssektion ergänzt

Status: fertig

Geändert:

- `homepage/index.html`: unter den 11 Leistungs-Cards in Sektion 5 zwei Golden-CTAs ergänzt.
- CTA 1: `Potenzialanalyse starten` → `#potenzialanalyse`.
- CTA 2: `Erstgespräch vereinbaren` → `#kontakt`.
- Bestehenden Golden-CTA-Stil verwendet; keine Card-Struktur oder übrigen Sektionen verändert.

## 2026-09-28 – Hover-State am Analyseformular-CTA ergänzt

Status: fertig

Geändert:

- `homepage/index.html`: der Submit-Button `.nv-aform__submit` übernimmt jetzt denselben Hover- und Focus-State wie die bestehenden Golden-CTAs.
- `homepage/index.html`: Active-State für `.nv-aform__submit` ergänzt.
- Keine Formularinhalte, Größen oder Abstände verändert.

## 2026-09-28 – Service-Card-Wappen mit echter Goldumrandung

Status: fertig

Geändert:

- `homepage/index.html`: das Wappen/Result-Icon in den Service-Cards verwendet jetzt eine echte durchgehende `1.6px` Gold-Border.
- Die bisherige Konstruktion aus goldener Außenform und schwarzer Innenform wurde entfernt.
- `box-sizing: border-box` hält die vorhandene Icon-Gesamtgröße unverändert.
- Keine Card-Größen, Texte, Abstände oder Positionen verändert.

## 2026-09-28 – Ablaufpfeile horizontal ausgerichtet

Status: fertig

Geändert:

- `homepage/index.html`: die wechselnden `rotate(36deg)`-/`rotate(-36deg)`-Regeln der Ablaufpfeile entfernt.
- Alle fünf Pfeile verwenden jetzt dieselbe bereits vorhandene Position `top: 42px; left: 88%` ohne Rotation.
- Keine Grafikgrößen, Texte oder sonstigen Abstände geändert.

## 2026-09-28 – Service-Card-Divider ausgerichtet und Ablaufgrafiken vereinheitlicht

Status: fertig

Geändert:

- `homepage/index.html`: horizontalen Divider unter dem Service-Card-Iconrahmen mittig zwischen Iconrahmen und „Einsatzbereiche“ gesetzt (`margin: 14px 0`).
- `homepage/index.html`: alle sechs Ablaufgrafiken auf denselben bereits vorhandenen Skalierungswert `0.58` gesetzt.
- Unterschiedliche Odd-/Even-Skalierung der Ablaufgrafiken entfernt.
- Keine Texte, Pfeile, Grafikquellen, Card-Größen oder übrigen Abstände verändert.

## 2026-09-28 – Abschnitts- und Footer-Divider vereinheitlicht

Status: fertig

Geändert:

- `homepage/index.html`: Abschnitts-Divider von 1.6px auf 0.8px reduziert.
- `homepage/index.html`: FAQ-Divider direkt vor dem Footer entfernt, damit dort nicht zwei Divider übereinander liegen.
- `homepage/index.html`: oberer Footer-Divider auf volle Breite gesetzt (`left: 0; right: 0`) und auf 0.8px reduziert.
- `homepage/index.html`: internen Divider von `.footer-bottom` entfernt.
- `homepage/shared-header-footer.css`: Footer-Divider und `.footer-bottom` synchron angepasst.
- Keine Inhalte, Abstände oder Spalten des Footers verändert.

## 2026-09-28 – Ablauf-Titel getrennt und Prozessgrafiken halbiert

Status: fertig

Geändert:

- `homepage/index.html`: Ablauf-Headline nach „Vom Geschäftsprozess“ getrennt; „zur KI-Lösung“ steht vollständig in der zweiten Zeile.
- `homepage/index.html`: bestehende Skalierung der sechs Ablaufgrafiken inklusive Sockel exakt halbiert (`1 → 0.5`, `0.86 → 0.43`, `1.16 → 0.58`).
- Grafik-Containerhöhen, Beschriftungen, Pfeile, CTA-Abstände und übrige Sektionseinstellungen nicht verändert.

## 2026-09-28 – Service-Card-Divider im geschlossenen Zustand vollständig verborgen

Status: fertig

Geändert:

- `homepage/index.html`: linker kurzer Divider, vertikaler Divider und rechter horizontaler Divider erhalten im geschlossenen Zustand zusätzlich `visibility: hidden`.
- Hover, Focus und `.is-active` setzen die drei Divider explizit auf `visibility: visible` und `opacity: 1`.
- Keine Card-Positionen, Texte, Größen oder Grid-Werte geändert.

## 2026-09-28 – Service-Card-Divider-Fix in aktuellen Refactor-Branch übernommen

Status: fertig

Geändert:

- `homepage/index.html`: die bereits auf `fix/service-card-dividers` vorhandene Divider-Logik in den aktuellen Branch `refactor/shared-header-footer-tokens` übernommen.
- Geschlossene Leistungskarten: linker kurzer Divider, vertikaler Divider und rechter horizontaler Divider sind jetzt `opacity: 0`.
- Geöffnete Leistungskarten: alle drei Divider werden bei Hover, Focus oder `.is-active` mit `opacity: 1` eingeblendet.
- Die drei Divider verwenden 1.6px in der Karten-CSS, damit sie unter dem vorhandenen `zoom: 0.65` sichtbar bleiben.
- Keine Card-Positionen, Texte oder sonstigen Bereiche verändert.

## 2026-09-28 – Erste Header-Basisregeln aus index.html entfernt

Status: fertig

Geändert:

- `homepage/index.html`: ausschließlich die bereits 1:1 in `shared-header-footer.css` vorhandenen Basisregeln für `.site-header`, `.site-header::after` und die Desktop-Basisregel von `.header-inner` entfernt.
- Responsive `.header-inner`-Regeln, Logo-, Breadcrumb-, CTA-, Footer-, globale CTA- und Token-Regeln unverändert gelassen.
- `homepage/shared-header-footer.css` in diesem Schritt nicht verändert.

## 2026-09-28 – Footer-Divider an Abschnittssystem angepasst

Status: fertig

Geändert:

- `homepage/index.html`: den vollbreiten `border-top` des Footers entfernt.
- `homepage/index.html`: Footer-Divider als eingerückten 1.6px-Verlauf mit `left: 7%` / `right: 7%` und Glow umgesetzt, analog zu den übrigen Abschnitts-Dividern.
- `homepage/shared-header-footer.css`: dieselbe Footer-Divider-Regel synchron übernommen.
- Keine Footer-Inhalte, Abstände oder Spalten verändert.

## 2026-09-28 – Shared Header/Footer Stylesheet in index.html eingebunden

Status: fertig

Geändert:

- `homepage/index.html`: `shared-header-footer.css` direkt nach `nurovelle-tokens.css` eingebunden.
- Noch keine Header- oder Footer-Regeln aus dem Inline-CSS entfernt.
- `homepage/shared-header-footer.css` nicht verändert; der vollständige Header-Regelsatz wurde zuvor gegen `index.html` abgeglichen und stimmt regelweise inklusive doppelter Responsive-Selektoren überein.

## 2026-09-28 – Header-Abhängigkeiten in Produktions-Tokens ergänzt

Status: fertig

Geändert:

- `homepage/nurovelle-tokens.css`: die aktuell in `index.html` verwendeten Header-/CTA-Abhängigkeitswerte ergänzt, damit die spätere schrittweise Auslagerung in `shared-header-footer.css` ohne Wertverlust möglich ist.
- `--header-height` und `--page-gutter` auf die aktuell tatsächlich in `index.html` verwendeten Werte gesetzt.
- Logo-Größen, Gold-/CTA-Materialwerte und die vom Header-CTA benötigten Shadow-Werte aus `index.html` übernommen.
- `homepage/index.html` und `homepage/shared-header-footer.css` nicht verändert.

## 2026-09-25 – Analyse-Regler und Consent-Cards korrigiert

Status: fertig

Geändert:

- `homepage/index.html`: Desktop-Schieberegler auf `calc(100% - 80px)` gekürzt.
- Datenschutz- und Newsletter-Card explizit auf jeweils eigene Grid-Zeile und volle Formularbreite gesetzt.
- Keine zusätzlichen CSS-Override-Blöcke angelegt.

## 2026-09-25 – Schieberegler im Richtwert-Rechner gekürzt

Status: fertig

Geändert:

- `homepage/index.html`: ausschließlich die drei Desktop-Schieberegler in „Richtwert berechnen“ deutlich gekürzt (`calc(100% - 72px)` statt `calc(100% - 24px)`).
- Mobile Regel bleibt unverändert bei `width: 100%`.

## 2026-09-25 – Tiefenstaffelung der Ablaufmodule korrigiert

Status: fertig

Geändert:

- `homepage/index.html`: perspektivische Odd/Even-Tiefenstaffelung (`0.86` / `1.16`) der sechs Ablaufmodule wiederhergestellt.
- Nur die vertikale Modulposition zum Sockel wurde auf den Wert des ersten Moduls (`--nv-module-top: 13.6px`) vereinheitlicht; die individuellen Perspektivwinkel bleiben erhalten.

## 2026-09-25 – Paket-Hinweis an Card-Grid ausgerichtet

Status: fertig

Geändert:

- `homepage/index.html`: Hinweistext unter den drei Automationspaketen auf dieselbe maximale Breite und horizontale Zentrierung wie das bestehende Paket-Card-Grid gesetzt.
- `homepage/index.html`: Beträge in den Paket-Cards rechtsbündig angeordnet; die zugehörigen Preisbeschreibungen stehen links.
- `homepage/index.html`: die drei Range-Balken in „Richtwert berechnen“ um 24px gekürzt; Card-Breite, Spalten, Texte, Werte und Auswahlfelder unverändert.
- `homepage/index.html`: Datenschutz- und Newsletter-Card im Analyseformular untereinander über die volle Formularbreite angeordnet.
- `homepage/index.html`: alle sechs Ablaufmodule erhalten dieselbe Skalierung und vertikale Position zum Sockel wie das erste Modul „Aufgabe erfassen“.

Nicht geändert:

- Paket-Cards, Texte, Section-Layout, Header, Footer, übrige Homepage-Bereiche und JavaScript.

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
