# Nurovelle Homepage – Todo

Stand: 2026-08-30  
Status: in Arbeit

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
- [ ] `nurovelle-tokens.css` liegt doppelt (`project_files/` und `homepage/`) und lief inhaltlich auseinander; eine der beiden zur alleinigen Quelle machen und die andere daraus erzeugen — offen
- [ ] sieben Gold-SVG-Wortmarken unter `homepage/assets/hero/` sind in keinem Commit und deshalb live nicht abrufbar; einchecken oder verwerfen — offen

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

- [ ] Exo 2 und Inter als Webfont in die Website einbinden (self-hosted, OFL-Dateien liegen unter `/usr/local/share/fonts/nurovelle/`) — offen
- [ ] Produktionscode auf `--font-display` prüfen: Stellen finden, die noch fest Tapera, Eastman Grotesque oder einen alten Stack setzen — offen
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
- [ ] Meta Title / Description / Canonical / OG prüfen — offen
- [ ] Impressum und Datenschutz verlinken/testen — offen

## Assets

- [ ] `assets.md` gegen den realen Projektordner physisch abgleichen — offen
- [ ] Download-Dateiendungen und endgültige Dateinamen prüfen — offen
- [ ] Analyse-Grafiken `assets/analyse/1.png` bis `8.png` auf finalen Nurovelle-Stil prüfen — offen
- [ ] Hero-/Detailseiten-Assets auf Transparenz und Stilkonstanz prüfen — offen
- [ ] **Unbenannte Moduldateien `from - NN.png` benennen** — offen
  - Neun Dateien in `homepage/assets/Module/`: `from - 5`, `- 16`, `- 51`, `- 70`, `- 86`, `- 87`, `- 89`, `- 90`, `- 92`. Vier lagen schon vorher im Projekt, fünf kamen am 2026-11-14 aus dem Sicherungszweig dazu.
  - Der Nutzer hat am 2026-11-14 bestätigt: Das sind Module, nur noch nicht benannt. Sie bleiben liegen, bis die Motive zugeordnet sind.
- [ ] **Drei namenlose Fotos zuordnen oder verwerfen** — offen
  - `homepage/assets/Fotos/Kein Titel (927 x 1200 px)/1.png` und `/2.png`, dazu `homepage/assets/Fotos/Kein Titel (927 x 1200 px)-(1)/2.png`. Je 927 x 1200 px, zusammen 3,5 MB.
  - Ordner- und Dateinamen stammen aus einem Export ohne gesetzten Titel.
- [ ] **Analyse-Hero auf `analyse_detail_page` umstellen** — offen
  - Der Nutzer hat die Analysegrafik lokal in `analyse_detail_page.png` und `analyse_detail_page.webp` umbenannt, damit sie namentlich zu `chatbot_detail_page.png` und `daten_detail_page.png` passt. Beide Dateien sind am 2026-11-14 noch nicht im Repository und live 404.
  - Bestätigt: die WebP ist dieselbe Grafik wie die PNG.
  - Sobald die Dateien eingecheckt sind: `homepage/analyse.html` Zeile 803, Hero-Verweis von `assets/detail_pages_grafics/sockel_loaded_analyse.png` auf das Projektmuster umstellen, `<picture><source srcset="…webp" type="image/webp" /><img src="…png" alt="Ablauf der KI-Potenzialanalyse" width="…" height="…" /></picture>`, Masse aus der tatsächlichen Datei. Es ist die einzige Referenz auf den alten Namen.
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
  - **Noch offen:** In der Anleitung steht `alt="Ablauf"`. Das ist für eine Hero-Grafik kein sinnvoller Alternativtext und muss je Seite durch eine Beschreibung des Motivs ersetzt werden.
  - Vorhandene Grafiken in `assets/detail_pages_grafics/`: `betreuung`, `büro`, `chatbot`, `daten`, `gouvernance`, `handwerk`, `ki_agenten`, `ki_roadmap`, `ki_software`, `prompt_engineering`, `prozessautomation`, `seo`, `sprachassistent`, jeweils als `<name>_detail_page.png`, vier davon zusätzlich als `.webp`.
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
