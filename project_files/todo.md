# Nurovelle Homepage – Todo

Stand: 2026-11-15  
Status: in Arbeit

Zuletzt am 2026-11-15 vollstaendig gegen den tatsaechlichen Projektstand geprueft. Punkte, die sich dabei als erledigt oder als ueberholt herausgestellt haben, sind entsprechend gekennzeichnet.

## Zweck dieser Datei

Hier stehen ausschließlich **offene oder laufende Aufgaben**.

Keine abgeschlossenen historischen Entscheidungen, Designregeln oder Projektbeschreibungen hier duplizieren.

## Dokumentation

- [x] Projectfiles nach eindeutiger Zuständigkeit konsolidieren — fertig
- [x] `project_overview.md` als einzige Projekt-/Strukturquelle erstellen — fertig
- [x] `task_contract.md` auf reine Arbeitsregeln reduzieren — fertig
- [x] `styleguide.md` als einzige Designquelle konsolidieren — fertig
- [x] `architecture.md` anlegen — fertig
- [x] `assets.md` aus bestehender Assetliste konsolidieren — fertig
- [x] Implementation Brief als aktive Quelle entfernen — fertig
- [x] `nurovelle-tokens.css` auf Styleguide-Hoheit umstellen — fertig
- [ ] `decision_log.md` künftig bei jeder neuen Freigabe unmittelbar aktualisieren — offen
- [ ] `changelog.md` bei jeder tatsächlichen Änderung unmittelbar aktualisieren — offen
- [ ] `nurovelle-tokens.css` liegt doppelt und laeuft auseinander — **am 2026-11-15 nachgemessen**: `homepage/nurovelle-tokens.css` 5037 Bytes, `project_files/nurovelle-tokens.css` 4442 Bytes, **84 abweichende Zeilen**. Ausgeliefert wird die Fassung unter `homepage/`. Eine der beiden zur alleinigen Quelle machen und die andere daraus erzeugen — offen
- [x] sieben Gold-SVG-Wortmarken unter `homepage/assets/hero/` — **ueberholt**, am 2026-11-15 geprueft: In `homepage/assets/hero/` liegt keine einzige SVG-Datei. Vorhanden sind drei PNG (`Nurovelle_schrift_gold.png`, `nurovelle_logo_gold.png`, `round.png`), und alle drei sind eingecheckt. Der Punkt beschreibt einen Zustand, den es nicht mehr gibt.

## Zahlung / Stripe

- [ ] **Preis-IDs fehlen.** Für alle acht Produkte in `NUROVELLE_STRIPE_PRODUKTE` steht `preis: null`. Vorliegend sind nur die `prod_`-IDs; ein Checkout braucht die `price_`-ID. Zu holen im Stripe-Dashboard unter Produktkatalog → Produkt → Abschnitt Preise (kein API-Schlüssel nötig) — offen
- [ ] **Test oder Live klären.** Test- und Livemodus führen getrennte Produkte und Preise. Eine `price_`-ID aus dem Livemodus funktioniert mit dem hinterlegten `pk_test`-Schlüssel nicht — offen
- [ ] **Bezeichnungen bestätigen**, besonders bei den beiden Deep-Einträgen: welcher ist der Aktionspreis bis 31.12.2026, welcher der reguläre ab 01.01.2027 — offen
- [ ] `homepage/stripe-config.js` in den Seiten einbinden, in denen bezahlt werden soll; welche Seiten das sind, ist nicht entschieden — offen
- [ ] Bezahlflow (Produkte, Preise, Checkout, Server-Endpunkt) festlegen und freigeben — offen
- [ ] Live-Betrieb: Publishable Key des Livemodus liegt nicht vor; `homepage/stripe-config.js` steht auf `test` — offen

## Homepage – Inhalte

- [ ] finalen Text für „Warum Nurovelle“ freigeben — offen
- [ ] finalen vollständigen Text der Potenzialanalyse-Sektion freigeben — offen
- [ ] finalen Text der linken Formular-Card freigeben — offen
- [ ] Download-Beschreibungen final prüfen — offen
- [ ] Kontakttexte final prüfen — offen
- [ ] FAQ gegen aktuellen freigegebenen Stand prüfen — offen

## Homepage – Design / Komponenten

- [x] Exo 2 und Inter als Webfont einbinden (self-hosted) — **fertig**, am 2026-11-15 geprueft: `homepage/assets/fonts/fonts.css` deklariert Exo 2 und Inter, acht `woff2`-Dateien liegen daneben, 34 Seiten binden die Datei ein. `analyse.html` war die letzte Ausnahme und ist am 2026-11-14 von Google Fonts auf lokal umgestellt. Keine Seite laedt noch von `fonts.googleapis.com`.
- [ ] Produktionscode auf alte Schriftstacks pruefen — **praezisiert am 2026-11-15**, nichts davon ist live wirksam:
  - `Tapera` und `Coder Pro`: kommen im Projekt nicht mehr vor.
  - `Eastman Grotesque`: zehn `font-family`-Fundstellen, ausschliesslich in `homepage/xcomponents/` (`nurovelle-service-cards.css`, `nurovelle-resources-contact-faq.css`, `nurovelle-section-rhythm.css`). Dieser Ordner ist im Deploy per `--exclude='xcomponents/'` ausgeschlossen und wird von keiner Seite eingebunden. Entscheidung noetig: Ordner loeschen oder bereinigen.
  - `Bebas Neue` und `Raleway`: in `assets/fonts/fonts.css` deklariert und in `xcomponents/nurovelle-tilt-card.css` gesetzt. In `datenschutz.html` werden sie nur im Rechtstext genannt, nicht gesetzt. Entscheidung noetig: Deklaration aus `fonts.css` entfernen oder die vier `woff2`-Dateien behalten.
  - `Roboto`: nur in `homepage/stripe-sample-code/public/style.css`, also im Beispielcode.
- [ ] **Goldwort-Regel: Entscheidung steht aus** — blockiert
  - `styleguide.md` Zeile 106: auf der Website trägt die Überschrift den Goldverlauf über den **kompletten** Text, „und so bleibt es".
  - Diese Datei verlangte bisher das Gegenteil: genau ein tragendes Wort je Überschrift.
  - Beides kann nicht gelten. Der Nutzer hat am 2026-11-13 entschieden, die Frage vorerst offen zu lassen.
  - Aktueller Produktionsstand: alle `h1`/`h2` tragen über `nurovelle.css` den vollen Goldverlauf. Ausnahme sind die drei am 2026-11-13 ergänzten Abschnitte `#fallbeispiel` auf `detail_datenabgleich`, `detail_prozessautomatisierung` und `detail_prompt-engineering`; dort trägt genau ein Wort den Verlauf, auf ausdrückliche Vorgabe des Nutzers.
  - Nach der Entscheidung ist entweder `styleguide.md` nachzuziehen oder sind die drei Abschnitte auf Vollgold umzustellen. „Nurovelle" bleibt in jedem Fall gold.
- [ ] finale Divider-Variante live prüfen und freigeben — offen
- [ ] Hero-Orb / Cube-Entstehung live prüfen — offen
- [ ] Board-/Stepdiagramm-Darstellung live prüfen — offen
- [ ] CTA-System im realen Produktionscode vollständig gegen Styleguide prüfen — offen
- [ ] Mobile Layout vollständig prüfen — offen

## Homepage – Technik

- [ ] reale Projektstruktur gegen `architecture.md` prüfen — offen
- [ ] Breadcrumb-Header mit genau drei Bereichen und Hover-Submenüs prüfen — offen
- [ ] Sidebar/Hamburger auf Desktop und Mobile prüfen — offen
- [ ] Potenzialanalyse-/Formularflow vollständig testen — offen
- [ ] Notion-/Lead-/Nurturing-Integration im realen Flow prüfen — offen
- [ ] Downloadziele und Success-/Error-Verhalten prüfen — offen
- [ ] Meta Title / Description / Canonical / OG — **am 2026-11-15 geprueft, eine Luecke**: 24 von 25 Seiten haben Description, Canonical und sieben oder mehr `og:`-Angaben. **`analyse.html` hat kein `rel="canonical"`, keine einzige `og:`-Angabe und kein `rel="icon"`.** Die uebrigen Seiten sind vollstaendig.
- [x] Impressum und Datenschutz verlinken — **fertig**, am 2026-11-15 geprueft: `impressum.html`, `datenschutz.html` und `agb.html` sind von allen 25 Seiten verlinkt. `cookie-hinweis.html` nur von sieben; ob das so gewollt ist, ist nicht entschieden.

## Assets

- [ ] `assets.md` gegen den realen Projektordner physisch abgleichen — offen
- [ ] Download-Dateiendungen und endgültige Dateinamen prüfen — offen
- [ ] Analyse-Grafiken auf finalen Nurovelle-Stil pruefen — **Pfad korrigiert am 2026-11-15**: Der Ordner `assets/analyse/` existiert nicht. Gemeint ist `homepage/assets/Module/analyse/`, dort liegen `1.png`, `2.png`, `2.webp`, `3.png`, `4.png`, also vier Motive statt acht.
- [ ] Hero-/Detailseiten-Assets auf Transparenz und Stilkonstanz prüfen — offen
- [ ] **Neu benannte Modulgrafiken einbinden** — offen
  - Am 2026-11-15 benannt und bisher auf keiner Seite verwendet: `seo.png`, `web.png`, `data.png`, `ausschuss.png`, `google.svg`, `datenaufbereitung.png`, `datenschutz.png`, `sicherung.png`, `api2.png`, `mitarbeiterfreigabe.png`.
  - Wo sie eingesetzt werden, ist nicht entschieden.
- [x] **Analyse-Hero auf `analyse_detail_page` umstellen** — **fertig** am 2026-11-14. Hero in `analyse.html` nutzt `<picture>` mit `analyse_detail_page.webp` und `.png`, 1672 x 941. `sockel_loaded_analyse.png` ist geloescht.
- [ ] Workflow-Modultabelle gegen tatsächlich vorhandene Modulassets prüfen — offen

## Detailseiten

- [ ] endgültige Liste aller Leistungsdetailseiten gegen den zuletzt erarbeiteten Contentstand prüfen — offen
- [ ] gemeinsame Detailseiten-Struktur final gegen die zuletzt erarbeiteten Seiten prüfen — offen
- [ ] Texte jeder Detailseite vollständig freigeben — offen
- [ ] Framework je Detailseite mit mindestens der freigegebenen Anzahl Module/Schritte prüfen — offen
- [ ] Hero-Visual je Detailseite zuordnen — offen
- [ ] **Hero-Grafik je Detailseite einsetzen, beim Durchgehen der jeweiligen Seite** — offen
  - 14 Seiten haben an der Hero-Stelle einen leeren Platzhalter `<div class="visual-card visual-card--empty" aria-hidden="true">` mit einer Einsetz-Anleitung im HTML-Kommentar. **Es ist nichts kaputt**: Der Pfad steht nur im Kommentar und wird nie angefordert.
  - Betroffen: `detail_roadmap`, `detail_prompt-engineering`, `paket-buero`, `potenzialanalyse-deep`, `detail_workflows`, `detail_seo`, `paket-betreuung`, `detail_ki-software`, `detail_ki-agenten`, `detail_ki-sicherheit`, `detail_automationen`, `detail_warum-nurovelle`, `paket-handwerk`, `detail_sprachassistenten`.
  - Der Ordner in der Anleitung war falsch. Er stand auf `assets/Module/Ablauf/` und ist am 2026-11-14 auf `assets/detail_pages_grafics/` korrigiert, wo die Hero-Grafiken der Detailseiten liegen.
  - Welche Grafik auf welche Seite gehört, ist nicht entschieden. Der Nutzer klärt das bei der jeweiligen Seite, nicht pauschal.
  - `width="620" height="507"` ist am 2026-11-14 aus der Anleitung entfernt. Die Zahlen stammten aus `assets/Module/Ablauf/lösung_wählen.png`, das tatsächlich 620 x 507 misst, und passten zu keiner Hero-Grafik; zwölf von vierzehn sind 1672 x 941, dazu `ki_roadmap` 1659 x 948, `ki_software` 1912 x 823 und `seo` 1774 x 887. Beim Einsetzen werden die echten Masse der jeweiligen Datei eingetragen.
  - `alt="Ablauf"` ist am 2026-11-15 durch den Platzhalter `alt="BESCHREIBUNG"` ersetzt, zusammen mit einem Hinweis im Kommentar. Beim Einsetzen werden `DATEI` und `BESCHREIBUNG` ersetzt: Dateiname ohne Endung und ein Alternativtext, der das Motiv beschreibt.
  - Vorhandene Grafiken in `assets/detail_pages_grafics/`: `analyse`, `betreuung`, `büro`, `chatbot`, `daten`, `governance`, `handwerk`, `ki_agenten`, `ki_roadmap`, `ki_software`, `prompt_engineering`, `prozessautomatisierung`, `seo`, `sprachassistent`, jeweils als `<name>_detail_page.png`, fuenf davon zusaetzlich als `.webp`.
- [ ] verwandte Leistungen je Seite final zuordnen — offen
- [ ] FAQ je Detailseite final prüfen — offen
- [ ] Kontakt-/Erstgesprächskomponente final prüfen — offen
- [ ] alle Detailseiten responsiv testen — offen

## Launch

- [ ] finale Korrektur lesen — offen
- [ ] alle Links testen — offen
- [ ] Formular testen — offen
- [ ] Potenzialanalyse testen — offen
- [ ] Downloads testen — offen
- [ ] CTAs testen — offen
- [ ] Detailseiten testen — offen
- [ ] Desktop testen — offen
- [ ] Tablet testen — offen
- [ ] Smartphone testen — offen
- [ ] rechtliche Seiten vor Veröffentlichung prüfen — offen
