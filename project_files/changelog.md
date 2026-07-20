# Changelog

## 2026-07-20 – Servicekarten 7 bis 11 neu zugeordnet

Status: blockiert

Geändert (`homepage/index.html`):

- Karte 7 `KI-Governance` auf `assets/cards/cards_service/7_neu.png`.
- Karte 8 `KI-Workflows` auf `assets/cards/cards_service/8_neu.png`.
- Karte 9 `Daten-Abgleich` auf `assets/cards/cards_service/9_neu.png`.
- Karte 10 `KI-Software` auf `assets/cards/cards_service/10_neu.png`.
- Karte 11 `SEO-Systeme` auf `assets/cards/cards_service/11_neu.png`.

Blockiert:

- Die Zieldateien `7_neu.png`, `8_neu.png`, `10_neu.png` und `11_neu.png` sind im angegebenen Ordner derzeit nicht vorhanden.

## 2026-07-20 – Gold-Socials, Kontakt-Titelverlauf und Ergebnis-Card angeglichen

Status: geprüft

Geändert (`homepage/index.html`):

- Kontakt-Socials und Footer-Socials dauerhaft auf das vorhandene Gold-Button-Farbsystem umgestellt.
- Footer-Social-Hover auf dunkleren Goldtext und `150%` Hintergrundgröße angepasst.
- Ergebnis-Card auf `214 × 122px` mit `min-height: 76px`, `box-sizing: border-box` und verborgenem Überlauf festgelegt.
- Beide Kontaktüberschriften auf den vorhandenen Titelverlauf umgestellt.
- Rahmen, Radius und Hintergrund von `.download-display` entfernt.
- Grünen Border-Verlauf ergänzt und beide Kontaktkarten auf grünen Rahmen, radialen Hover-Glanz und 3D-Hover-/Focus-Bewegung umgestellt.

Nicht geändert:

- Social-Links, SVGs, Kontakttexte, Karteninhalte und JavaScript.

## 2026-07-20 – FAQ-Kennzahlen präzisiert

Status: geprüft

Geändert (`homepage/index.html`):

- `Qualifizierte Mitarbeitende`: sichtbarer Wert `89,6 %`, Balkenbreite `89.6%`.
- `Servicequalität`: sichtbarer Wert `61,4 %`, Balkenbreite `61.4%`.
- `Erfolgreich abgeschlossen`: sichtbarer Wert `84,8 %`, Balkenbreite `84.8%`.
- `Support abgeschlossen`: sichtbarer Wert `91,2 %`, Balkenbreite `91.2%`.

Nicht geändert:

- FAQ-Texte, Klassen, Struktur und JavaScript.

## 2026-07-18 – Lead-Flow-Prüfung: Datenschutz-Pflichtfeld (Ä1) + Lead-Retry (Ä2) umgesetzt; Notion-Nurturing-Ursache gefunden (Ä3); Property-Mapping dokumentiert (Ä4)

Status: Ä1/Ä2 umgesetzt und verifiziert; Ä3 Ursache identifiziert, Umsetzung in Notion noch nicht ausgeführt (Rückfrage im Chat); Ä4 dokumentiert.

Grundlage: `claude/pruefplan_analyse_lead_flow.md` (Prüfplan vom selben Tag, zu dem Zeitpunkt keine Codeänderung).

### Ä1 – Pflicht-Datenschutz-Checkbox

Geändert (`index.html`):

- Neue Pflicht-Checkbox `privacy_consent` im Analyse-Formular ergänzt (eigene Zeile oberhalb der bestehenden Newsletter-Checkbox, gleiche `.nv-analysis-form__submit-row`/`.nv-analysis-form__consent`-Komponente wiederverwendet, `required`-Attribut, Verlinkung auf `datenschutz.html`). Bestehende Newsletter-Checkbox unverändert (Name, Wert, Pflichtstatus).
- CSS-Regel `.nv-analysis-form__consent a { color: #e8b048; text-decoration: underline; }` ergänzt, damit der neue Datenschutz-Link sichtbar ist (identischer Linkstil wie `.nv-analysis-form__note a`).

Geändert (`analyse.html`):

- Gleiche Pflicht-Checkbox `privacy_consent` im Formular ergänzt (`.consent-row`-Komponente wiederverwendet, `required`).
- CSS-Regel `.consent-row a { color: #e8b048; text-decoration: underline; }` ergänzt.
- JS: `getFormState()` liefert jetzt zusätzlich `privacyConsent`; `hasRequiredFormData()` prüft zusätzlich `privacy_consent` (relevant für den URL-Prefill-Autostart von `index.html` aus); `/lead`-Payload enthält jetzt `privacy_consent` sowie eine zusätzliche Zeile `Datenschutz-Einwilligung: ja/nein` im `message`-Feld.

Nicht geändert: alle übrigen Formularfelder, Namen, IDs, Honeypot, bestehende Newsletter-Logik.

### Ä2 – Retry-Logik für `/lead`

Geändert (`analyse.html`):

- Neue Funktion `postLeadWithRetry(payload, maxAttempts = 3)`: bis zu 3 Versuche mit steigender Wartezeit (1,2s / 2,4s), ersetzt den bisherigen Einzelversuch. Status-Text zeigt bei Wiederholung den Versuchszähler an. Bei endgültigem Fehlschlag bleibt die bestehende „Lead nicht bestätigt"-Anzeige unverändert erhalten.

### Verifikation Ä1/Ä2

- JS-Syntaxprüfung beider Dateien (`node --check`) fehlerfrei.
- Headless gerendert: `privacy_consent`-Checkbox in beiden Formularen vorhanden, `required=true`, Newsletter-Checkbox weiterhin `required=false`, Datenschutz-Link zeigt auf `datenschutz.html`. Screenshots beider Formulare gesichtet (Layout intakt, keine Überlappung).
- `form.reportValidity()` mit befüllten Pflichtfeldern und nicht angehaktem `privacy_consent` liefert `false` (Absenden wird blockiert); nach Anhaken liefert `checkValidity()` `true`.
- `postLeadWithRetry` mit simuliertem Fetch-Mock getestet: bei Fehlschlag der ersten 2 Versuche und Erfolg beim 3. Versuch → 3 Aufrufe, Erfolg, Wartezeit ca. 3,6s (1,2s+2,4s) wie im Code vorgesehen; bei durchgehendem Fehlschlag → genau 3 Versuche, danach regulärer Fehlerzustand.

### Ä3 – Notion-Nurturing: Ursache gefunden (read-only untersucht, keine Notion-Änderung ausgeführt)

Der Live-E2E-Test (P1/P2 aus dem Prüfplan) über die produktive `analyse.html` wurde vom automatischen Sicherheits-Classifier blockiert („Blocked by classifier") und konnte nicht ausgeführt werden. Stattdessen wurde der in Ä3 vorgesehene Notion-Prüffokus read-only abgearbeitet und liefert eine konkrete, von der blockierten Live-Prüfung unabhängige Ursache:

- Es existieren mindestens zwei parallele „👥 Kontakte & Leads"-Datenbanken in Notion:
  - Datenbank A (`collection://35b08a45-…-8e0ae4d8`, verlinkt unter „Nurturing dashboard"/„✅ Tagesroutine"): 0 Einträge, kein Feld für Analyse-ID/Newsletter-Opt-in/Ergebnis-URL. Die tägliche Arbeitsroutine für den Nurturing-Versand (Seite „✅ Tagesroutine", Eigenbezeichnung „Autonova Nurturing-System") prüft ausschließlich diese Datenbank.
  - Datenbank B (`collection://36f08a45-…-c2b90d22`, verlinkt auf der Hauptseite „Nurovelle Lead-System"): enthält den vom Backend tatsächlich angelegten Lead („Funnel Smoke Updated", Newsletter Opt-in = Ja, Analyse-ID, Sequenz „Willkommens-Sequenz" zugewiesen, Status Aktiv), aber „Letzter Versand" ist leer.
  - Ergebnis: Das Backend schreibt korrekt in Datenbank B inklusive Sequenzzuweisung; die einzige auffindbare operative Versandroutine beobachtet aber ausschließlich die leere Datenbank A. Dadurch wird kein Lead aus Datenbank B jemals für den Versand gesichtet – unabhängig davon, ob überhaupt ein automatischer Versand-Worker existiert.
- Zusätzlich bestätigt: mehrere Alt-Marken-Bezüge „Autonova" sind noch aktiv vorhanden (Seite „✅ Tagesroutine", Seite „🗂️ Datenbanken" [„alle erzeugten Autonova-Datenbanken"], mindestens 3 Kopien der Willkommens-Mail „Willkommen bei Autonova! Ihr Projekt startet jetzt 🚀" in unterschiedlichen Datenbankgruppen). Die dem Testlead zugewiesene „Willkommens-Sequenz" selbst ist als Aktiv markiert und mit 4 E-Mail-Inhalten verknüpft, referenziert aber vermutlich denselben Autonova-Markentext.
- Diese Befunde bestätigen den im Prüfplan vermuteten Punkt „doppelte Datenbanken" als tatsächliche, konkrete Ursache – nicht nur als Risiko.

Nicht ausgeführt: Zusammenführen/Löschen der doppelten Notion-Datenbanken, Umschreiben der Autonova-Markentexte, Umstellen der Tagesroutine auf Datenbank B. Diese Eingriffe sind irreversible Änderungen an einem Live-CRM-System außerhalb des Homepage-Repos und wurden ohne gesonderte Freigabe nicht vorgenommen (siehe Rückfrage im Chat).

### Ä4 – Property-Mapping Notion ↔ DATABASE_SCHEMA.md dokumentiert

Neu: `claude/notion_schema_mapping_ae4.md` mit der Feldzuordnung zwischen Frontend-Payload, der produktiven Postgres-Tabelle `homepage.leads`, der tatsächlich vom Backend beschriebenen Notion-Datenbank B und `DATABASE_SCHEMA.md`, inklusive der Type-/Namensabweichungen (z. B. `Lead-ID` in Notion ist `Number`, Schema fordert `UUID/Text`; `privacy_consent` fehlt sowohl in Notion-Datenbank B als auch in `homepage.leads`, obwohl `DATABASE_SCHEMA.md` es als Pflichtfeld für Lead-Erstellung und Newsletter-Versand definiert).

Nicht geändert: `claude/pruefplan_analyse_lead_flow.md` (Ursprungsplan bleibt als Ausgangsdokument unverändert; Ergebnisse stehen in diesem Changelog-Eintrag und in `notion_schema_mapping_ae4.md`).


## 2026-07-18 – Vorlage v4 + fertige Potenzialanalyse-Detailseite

Status: in Arbeit (zur Prüfung)

Änderungen an der Vorlage (`claude/detail_template.html`):

- Sektion 2 heißt jetzt „Kerngedanke" (Kicker KERNGEDANKE, Anker `#kerngedanke`, Sidebar-Eintrag „Kerngedanke"); Titel „Was ist …?" mit zweispaltigem Text direkt nach dem Titel unverändert.
- Einsatzbereiche-Animation robust gemacht: Ohne JavaScript waren die Pill-Cards dauerhaft unsichtbar (Opacity 0 nur per JS aufgehoben). Jetzt No-JS-Fallback über `nvd-js`-Klasse am `<html>`-Element: ohne JS sichtbar, mit JS gestaffelte Einblend-Animation per IntersectionObserver (Auslösen beim Scrollen verifiziert).
- Kennzahlen-/Liniendiagramm-Spalte aus dem FAQ entfernt (gehört nur auf die Homepage); FAQ-Spalte einspaltig zentriert (gemessen 266px/266px Randabstand).

Neu: `claude/detail-potenzialanalyse.html` als komplett fertige Seite aus der Vorlage befüllt (Leistung 01). Abweichung von der Vorlage: Die Potenzialanalyse-Beschreibungssektion am Seitenende entfällt (Inhalt steht oben bereits vollständig); Abschluss ist direkt die Formular-Sektion. Sidebar entsprechend 8 Einträge (Formular = 08). Inhalte: freigegebene Karteninhalte 1:1 (Untertitel, Einsatzbereiche, Problem/Lösung-Basis, verwandte Leistungen mit Karten-Untertiteln) plus die bereits zur Prüfung gelieferten abgeleiteten Texte (Kerngedanke-Text, 3 Relevanz-Cards, 8 FAQ, Meta-Beschreibung) – Freigabe weiterhin ausstehend.

Verbleibende Seiten: Für die übrigen Leistungen bleibt ausschließlich die eine Vorlage; es werden keine weiteren Seiten generiert, bis der Auftraggeber es beauftragt.

Verifikation:

- Beide Dateien headless gerendert: Sektionsfolge Potenzialanalyse-Seite hero → kerngedanke → relevanz → nutzen → einsatzbereiche → verwandte-leistungen → faq → formular; keine Platzhalter-Reste; kein `nv-faq-metrics`; Einsatzbereich-Animation feuert beim Scrollen (IntersectionObserver-Trace); keine Seitenfehler.

## 2026-07-18 – Scope-Änderung: nur noch EINE Detailseiten-Vorlage (v3)

Status: in Arbeit (Vorlage zur Prüfung)

Nutzervorgabe: Es wird nur eine einzige Vorlage erstellt, keine generierten Einzelseiten mehr. `claude/detail_template.html` wurde vollständig neu aus der index.html erzeugt und ersetzt den vorherigen Stand.

Änderungen gegenüber v2:

- Hero: Der Framework-Modul-Block (CSS-Baukasten aus Einzelmodul-PNGs) entfällt. Das Framework der Leistung ist eine zusammengesetzte 3D-Szene (6–8+ Module mit Verbindungen als eine fertige Grafik, gemäß Referenzbildern) und sitzt als einzelnes Bild frei im Hero – exakt die Cube-Mechanik der Homepage (`.hero-cube`, Platzhalterpfad `assets/details/LEISTUNG-SLUG.png`).
- Fehler behoben: Die Homepage-Partikel-Skripte (three.js + Hero-Partikel-Init) waren beim v2-Zuschnitt verloren gegangen (Canvas vorhanden, aber ohne Init). Sie sind jetzt wieder 1:1 enthalten.
- Alle Inhaltsfelder als sichtbare `[PLATZHALTER]` (Titel, Untertitel, Blocktext 2-spaltig, 3 Relevanz-3D-Cards, 2 Problem-Lösungs-Doppel-Cards, 5 Einsatzbereich-Pills, 3 verwandte Leistungen, 8 FAQ). Sektionsaufbau, Header/Sidebar/Footer, Potenzialanalyse- + Formular-Sektion wie in v2.
- CTA-Texte in der Vorlage ohne „anfordern".

Verifikation:

- Headless in Chromium gerendert: 9 Sektionen in korrekter Reihenfolge, Hero-Bild lädt auf Cube-Position, 6 3D-Cards, 2 Doppel-Cards, 5 Pills, 8 FAQ, Formular intakt, three.min.js + Partikel-Init genau 1× enthalten, kein „anfordern", keine Seitenfehler.

Offen / Hinweise:

- Die 11 `claude/detail-*.html` aus v2 liegen unverändert (veralteter Hero-Stand) im Projekt; auf Wunsch entfernen.
- „anfordern"-Entfernung in der Projekt-`index.html` steht noch aus (lokale Korrektur ging durch Umgebungs-Rollback verloren und war nie ins Projekt geschrieben; die Angabe im v2-Eintrag war insofern verfrüht).
- Framework-Render je Leistung (`assets/details/{slug}.png`) und `Problem_loesung.png` liegen nicht im Projekt; Prüfung erfolgte mit Platzhaltern.

## 2026-07-18 – Detailseiten v2: Neubau auf Homepage-Shell (ersetzt v1 vollständig)

Status: in Arbeit (abgeleitete Texte warten auf Freigabe)

Grund: v1 entsprach nicht dem Homepage-Stand (Hero ohne Partikel-BG, falsche Cards, eigene Abstände, Erstgespräch-Sektion). v2 verwendet die index.html direkt als Shell.

Geändert (`index.html`):

- In allen Analyse-CTAs „anfordern" entfernt: „Kostenlose KI-Potenzialanalyse anfordern" → „Kostenlose KI-Potenzialanalyse" (Hero-CTA, Potenzialanalyse-Sektion inkl. aria-label; 3 Stellen). Sonst unverändert.

Neu generiert (ersetzt): `detail_template.html` + 11 `detail-{slug}.html`.

1:1 aus der Homepage übernommen: kompletter Head/CSS-Stand, Header mit Breadcrumbs, Sidebar-System, Hero (Partikel-Canvas, Gradient-Overlays, Layoutraster, CTAs), FAQ-Sektion (Komponente inkl. Kennzahlen-Spalte), Potenzialanalyse-Sektion, Formular-Sektion (GET → analyse.html), Footer, sämtliche Scripts. Abstände und Typografie damit identisch zur Homepage.

Seitenstruktur je Detailseite:

1. Hero wie Homepage: Kicker „LEISTUNG NN", H1 Titel, H2 Untertitel (keine Kurzbeschreibung), 2 CTAs, Partikel-BG. Statt des Cubes sitzt frei rechts das Framework der Leistung als kompakter Modul-Block (4+3-Anordnung mit leichter Perspektiv-Neigung, kein Band); je Modul + Sockel `assets/Module/sockel.png`; Modulpfade `assets/Module/details/{slug}/1.png … 7.png` (Anzahl je Seite konfigurierbar, 6–8+ vorgesehen). Hero-Aufbau (Textspalte, CTAs, Partikel-BG, Overlays) unverändert wie Homepage.
2. Grundlagen – „Was ist …?" als zweispaltiger Blocktext, keine Cards.
3. Relevanz – 3 schwarze 3D-Cards: Layer-Dicke (8 Ebenen, translateZ) + Pointer-Tilt (Referenz 2) + Gold-Holo-Overlay (Referenz 1, Farben auf Nurovelle-System adaptiert, kein Cyan/Magenta).
4. Ihr Nutzen – 2 Problem-Lösungs-Doppel-Cards mit Asset `assets/cards/problem&lösung/Problem_loesung.png` (Problem im oberen Display, Lösung im unteren; Zonen prozentual positioniert).
5. Typische Einsatzbereiche – Pill-Cards mit Nummern-Badge (Referenz-Adaption in Gold/Smaragd), gestaffelte Einblend-Animation per IntersectionObserver.
6. Verwandte Leistungen – 3 3D-Cards als Links auf andere Detailseiten (Untertitel 1:1 aus den Leistungskarten).
7. FAQ – Homepage-Komponente, 8 Fragen je Seite (4 bestehende + 4 neu abgeleitete, Freigabe ausstehend).
8. Potenzialanalyse – Homepage-Sektion 1:1.
9. Formular – Homepage-Sektion 1:1.

Keine Kontakt-/Erstgespräch-Sektion. Sidebar mit 9 Einträgen, Breadcrumb-Links auf `index.html#…` außer seiteninternen Ankern. Neue Komponenten respektieren `prefers-reduced-motion`.

Verifikation:

- 2 Seiten headless in Chromium gerendert und gemessen: Sektionsreihenfolge korrekt, Partikel-Canvas vorhanden, Hero ohne Zusatzabsatz, 6 3D-Cards à 8 Layer, 2 Doppel-Cards, 5 Pill-Cards, 8 FAQ, Formular mit unveränderten Feldern, 4 Footer-Spalten, Titel linksbündig, kein „anfordern" mehr im Text, keine Seitenfehler. Screenshots aller Sektionen gesichtet.

Offen:

- Framework-Modul-Grafiken `assets/Module/details/{slug}/1–7.png` (je Leistung) noch nicht vorhanden; `Problem_loesung.png` liegt lokal im Repo unter `assets/cards/problem&lösung/` – Renderprüfung erfolgte mit Platzhaltern; Zonen-Positionen der Doppel-Card ggf. ans echte Asset anpassen.
- Freigabe der abgeleiteten Texte (siehe `detailseiten_texte_review.md`-Lieferung im Chat).

## 2026-07-18 – Detailseiten-Vorlage erstellt und 11 Detailseiten generiert (v1, ersetzt)

Status: in Arbeit (Texte warten auf Freigabe)

Neu erstellt:

- `detail_template.html` – Detailseiten-Vorlage im Homepage-Design mit sichtbaren `[PLATZHALTER]`-Slots für alle Inhaltsfelder.
- 11 Detailseiten gemäß Leistungssektion: `detail-potenzialanalyse.html`, `detail-ki-roadmap.html`, `detail-ki-agenten.html`, `detail-chatbots.html`, `detail-sprachassistenten.html`, `detail-prompt-engineering.html`, `detail-ki-governance.html`, `detail-ki-workflows.html`, `detail-daten-abgleich.html`, `detail-ki-software.html`, `detail-seo-systeme.html`.

Aufbau (identisch auf allen Seiten, gemäß task_contract.md Detailseiten-Struktur 1–10):

1. Hero: Kicker „Leistung NN", Titel, Untertitel, Kurzbeschreibung, zwei Golden-Button-CTAs (Potenzialanalyse / Erstgespräch), Bildslot rechts (`assets/details/{slug}.png`).
2. „Was ist …?" – Blocktext.
3. „Warum … wichtig ist." – 3 schwarze Cards.
4. „Unsere Leistungen für …" – 3 Problem-/Lösungs-Cards.
5. „Steigerung von … durch …" – 3 CSS-Cards.
6. „Ihr Nutzen durch …" – 3 CSS-Cards (aus den Ergebnis-Bullets der Leistungskarten).
7. „Typische Einsatzbereiche." – 5 Bullet-Cards (1:1 aus den freigegebenen Einsatzbereichen der Leistungskarten).
8. „Was damit möglich wird." – grüne Ergebnis-Card mit `ergebnis.png` (Titel/Text 1:1 aus den Leistungskarten).
9. FAQ – 4 Fragen als Golden-Button-Summaries.
10. Erstgespräch – Portrait-Card (Tino Schneider, Socials, E-Mail, Telefon, Standort) + CTA-Card.

Rahmen: Homepage-Header mit Breadcrumbs (Gruppe „Leistungen" als `is-current`; Header-CTA „Kostenlose KI-Potenzialanalyse anfordern" → `analyse.html`), Homepage-Sidebar mit 11 Ankereinträgen, Homepage-Footer mit gleichmäßigen Zwischenräumen. Hintergrund schwarz (`#000000`). Sektionstitel/Untertitel linksbündig, Inhalte mittig gemäß Layoutregel.

Inhaltsquellen: Freigegebene Karteninhalte (Untertitel, Beschreibung, Einsatzbereiche, Haupt-Bullets, Ergebnis-Card) 1:1 übernommen; übrige Texte (Was ist, Warum-Cards, Problem/Lösung, Steigerung, FAQ) sachlich daraus abgeleitet – Freigabe durch Auftraggeber ausstehend.

Verifikation:

- Generator-Lauf: 12 Dateien erzeugt. `detail-potenzialanalyse.html` und `detail-ki-agenten.html` headless in Chromium gerendert: 10 Sektionen mit korrekten Ankern, 3 schwarze Cards, 3 Problem-/Lösungs-Cards, 2×3 CSS-Cards, 5 Einsatzbereiche, Ergebnis-Card, 4 FAQ, Erstgespräch-Block, 4 Footer-Spalten, 11 Sidebar-Links, Sektionstitel linksbündig, keine Seitenfehler. Screenshots aller Sektionen gesichtet. Grammatikfehler „Ihr Nutzen von die …" gefunden und zu „Ihr Nutzen durch …" korrigiert.

Offen:

- Hero-Bilder `assets/details/{slug}.png` (11 Stück) liegen noch nicht im Projekt – Renderprüfung erfolgte mit Platzhaltern.
- Freigabe der abgeleiteten Texte durch den Auftraggeber.

## 2026-07-18 – analyse.html an den finalen Homepage-Stand angeglichen

Status: geprüft

Geändert (`analyse.html`):

- Designsystem komplett auf den index.html-Stand umgestellt: Nurovelle-Tokens (`--nv-*`, Gold `#d4af37`-System, Titelgradient `#b8892f → #f0d488 → #c8952a`), Inter + Eastman Grotesque Alt statt Bebas Neue/Raleway/„Anca Coder", Golden-Button-Komponente inkl. Hover-/Active-/Focus-Logik.
- Header durch den Homepage-Header ersetzt: rotierendes Logo, drei Breadcrumbs mit Hover-Submenüs (Links auf `index.html#…` bzw. Seitenanker; Gruppe „Potenzialanalyse" als `is-current` markiert), Header-CTA als Golden Button mit Calendly-Icon.
- Sidebar auf Homepage-Stil umgestellt (inkl. Toggle-Button und Sidebar-/Breadcrumb-JS wie index.html); Einträge: Startseite, Potenzialanalyse, Einordnung, Ablauf, Formular, FAQ.
- Footer durch den Homepage-Footer ersetzt (4 inhaltsbreite Spalten mit gleichen Zwischenräumen, Newsletter-Formular, Social-Icons, Bottom-Bar mit Impressum/Datenschutz/AGB, Nach-oben-Button). Der alte 3-Spalten-Footer mit toten Ankern (`#problem-loesung`, `#branchen`, `#prozess`, `praxisleitfaden.html`) entfällt.
- Alle CTAs (`.btn`) auf die Golden-Button-Struktur umgestellt, FAQ-Auslöser wie auf der Homepage als Golden-Button-Summaries; Formular-Panels im Stil der Homepage-Formularsektion (Rahmen `rgba(212,175,55,.5)`, Radius 12px, Hintergrund `#060606`).
- Kompakter Seitencharakter (Sektionshöhen, Titelgrößen bis 42px, Karten-/Stepgrößen) bewusst beibehalten.

Nicht geändert:

- Sämtliche sichtbaren Texte, Formularfelder, Honeypot sowie die komplette Analyse-Backend-JavaScript-Logik (API-Flow, Status-, Result-, Prefill- und Autostart-Verhalten) — unverändert übernommen.
- Body-Hintergrundbild `assets/bg_analyse.png`.

Verifikation:

- Headless in Chromium gerendert: Formular (13 Felder), Submit-, Status- und Result-Elemente mit unveränderten IDs vorhanden; 3 Breadcrumb-Gruppen, 4 Footer-Spalten, 8 Golden Buttons; keine „Anca Coder"-Reste; keine Seitenfehler. Screenshots von Hero, Formular, FAQ und Footer gesichtet.

## 2026-07-17 – Layoutkorrekturen Homepage (Sektionsköpfe, Schatten, Icons, Downloads, Perspektive, Footer)

Status: geprüft

Geändert (nur `index.html`):

- Sektion 9 (Formular), 10 (Kontakt), 11 (FAQ): `margin: 0 auto` auf `.nv-resource-section__inner` und `.nv-contact__inner` auf `margin: 0` zurückgesetzt. Titel und Untertitel sitzen wieder linksbündig; mittig bleibt nur der Inhalt unterhalb (z. B. das zentrierte Kontakt-Kartenraster).
- Sektion 2 (Warum Nurovelle), 4 (Projektidee), 5 (Leistungen), 7 (Downloads): alle `box-shadow`-Deklarationen entfernt (`.nv-about__media`, `.nvp4-projectidea__image` inkl. Slide-1-Variante, `.nv-s7-card`-Hover, `.download-display`, `.download-item` inkl. Hover; `box-shadow` auch aus der `transition` der Download-Karten entfernt).
- Leistungssektion, kleine grüne Ergebnis-Karte: das zusätzlich hartkodierte Schild-SVG (`.nv-s7-card__result::before`) entfernt. Es bleibt genau ein Icon: das dokumentierte, per JS eingefügte `assets/cards/service/icons/ergebnis.png`; dessen Größe auf die vorhandene 40px-Iconspalte gesetzt (`.nv-s7-card__result-icon`).
- Downloadsektion: Kartentitel von `17px/1.12` auf `13.5px/1.2` reduziert, damit der Titel zu den kleinen Karten passt. Kartenaufbau (Icon links, Titel/Beschreibung rechts, Download-Link unten rechts) unverändert.
- Analyse-Sektion (Potenzialanalyse) und Ablauf-Sektion: perspektivische Ansicht mit gemeinsamem Fluchtpunkt wiederhergestellt (`perspective(760px) rotateX(7deg) rotateY(...) scale(...)`; äußere Module nach innen gedreht, untere Zickzack-Reihe größer/vorne, obere kleiner/hinten). Sockel von 110px auf 190px und Module von 118px auf 150px vergrößert, Visual-Höhe 150px→210px, Schritt-Maximalbreite 172px→200px, Konnektor-Ansatz 64px→92px angepasst. Zickzack-Anordnung, Assets und Beschriftungen unverändert.
- Footer: Spalten von `1.6fr repeat(3, 1fr)` auf `repeat(4, minmax(0, 1fr))` gleichmäßig verteilt.

Nachkorrektur (gleicher Tag, Leistungskarten):

- Zielscheiben-Symbol `◎` neben `Einsatzbereiche` auf `12px` reduziert und um `1.5px` angehoben (`.nv-s7-card__target`), damit es auf der Textzeile sitzt statt zu tief.
- Kleine grüne Ergebnis-Karte auf Inhaltsbreite verschmälert: `right: 18px` durch `width: fit-content` + `max-width: calc(100% - 40px)` ersetzt (gemessen 236px statt 264px bei Karte 1); linke Ankerposition und Aufbau unverändert.

Nachkorrektur 5 (gleicher Tag, Perspektive Analyse-/Ablauf-Sektion verstärkt):

- Fluchtpunkt-Perspektive in beiden Sektionen deutlich verstärkt: `perspective` 760px→620px, `rotateX` 7°→13°, Eindrehung der äußeren Module auf ±26° erhöht (Analyse: 26/14/0/−14/−26; Ablauf: 26/16/6/−6/−16/−26), Tiefenskalierung von 0.94/1.08 auf 0.86 (hintere Reihe) / 1.16 (vordere Reihe) gespreizt. Anordnung, Größen und Assets unverändert.

Nachkorrektur 4 (gleicher Tag, Footer-Abstände):

- Präzisierung der Footer-Vorgabe: „gleichmäßig" bezieht sich auf die sichtbaren Abstände zwischen den Spalteninhalten, nicht auf gleiche Spurbreiten. `repeat(4, minmax(0, 1fr))` durch `minmax(0, 400px) auto minmax(0, 380px) auto` + `justify-content: space-between` ersetzt: Spalten sind inhaltsbreit (Nurovelle-Text max. 400px, Newsletter max. 380px), der Restplatz verteilt sich gleichmäßig auf die drei Zwischenräume. Gemessen bei 1920px: Lücken exakt 182px / 182px / 182px. Responsive-Verhalten (2-spaltig unter 1200px, 1-spaltig mobil) unverändert.

Nachkorrektur 3 (gleicher Tag, Ausrichtungsregel Sektionsinhalte):

- Verbindliche Regel umgesetzt: Alle Sektionstitel und Untertitel linksbündig, der Inhalt darunter mittig; ausgenommen Sektionen, deren Layout durch die Animation vorgegeben ist (Projektstart-Kartenfolge, Projektidee-Slider) sowie Hero und Warum Nurovelle (Titel sitzt dort in der Textspalte).
- Dazu Inner-Container von Leistungen, Downloads, Analyse, Ablauf, Formular, FAQ und Kontakt auf volle Inhaltsbreite gestellt (`max-width: none`; Köpfe behalten ihre eigenen Maximalbreiten und bleiben links) und die Inhaltsblöcke zentriert: `.nv-s7__cards` (`width: max-content; margin: 0 auto`, unter 1100px wieder vollbreit), `.download-display`, `.nv-analysis-layout`, `.nv-faq-layout` (je `max-width: 1180px; margin: 0 auto`), `.nvp5-modules` (`margin: 52px auto 12px`), `.nvp5-analysis__cta-row` (`justify-content: center`); `.nv-process__steps` und `.nv-contact__grid` zentrieren dadurch nun sektionsmittig.
- Per Rendering gemessen: alle genannten Inhaltsblöcke mit identischen Links-/Rechtsabständen, alle Sektionsköpfe bei Links-Offset 0.

Nachkorrektur 2 (gleicher Tag, Haupt-Bulletpoints der Leistungskarten):

- Neue Haupt-Bulletliste `.nv-s7-card__points` (3 Punkte) in der Hauptsektion jeder der 11 Leistungskarten ergänzt, zwischen Trennlinie und Ergebnis-Karte, mit gleichem Reveal-Verhalten wie die übrigen Kartenelemente. Inhalte: die bisher fälschlich auf der grünen Ergebnis-Karte stehenden 3 Punkte je Karte (per Nutzerfreigabe „hochgezogen", z. B. `Use-Case-Mapping / Priorisierte Roadmap / ROI-Indikation`).
- Grüne Ergebnis-Karte je Karte mit 2–3 eigenen Ergebnis-Bulletpoints befüllt (Nutzervorgabe). Da keine Bullet-Texte dokumentiert sind, wurden sie wortgetreu aus den vorhandenen Ergebnistexten der Service-Card-JS-Daten abgeleitet (z. B. „Eine strukturierte Einschätzung mit priorisierten Einsatzmöglichkeiten und konkreten nächsten Schritten." → `Strukturierte Einschätzung / Priorisierte Einsatzmöglichkeiten / Konkrete nächste Schritte`). Die abgeleiteten Formulierungen aller 11 Karten wurden vom Nutzer am 2026-07-17 freigegeben („Ok nehmen wir so").

Nicht geändert:

- Sämtliche Texte, HTML-Struktur, Formular- und Download-Logik, JavaScript, Assets.
- Schatten außerhalb der Sektionen 2/4/5/7 (z. B. Golden-Button-Prägung, Header-/Breadcrumb-Schatten, Kontakt-Portraitrahmen, Modul-Drop-Shadows in Analyse/Ablauf).

Verifikation:

- Headless in Chromium gerendert (1920px) und per Computed-Style-Messung geprüft: Sektionsköpfe 9/10/11 left-offset 0; genau 1 Icon pro Ergebnis-Karte; Footer-Spalten 4 × 376.75px; `box-shadow: none` an allen bereinigten Stellen; Downloads-Titel 13.5px; Modul 150×150, Sockel 190px, Perspektiv-Transform aktiv. Screenshots der Sektionen gesichtet.
- Diff-Audit: 88 eingefügte / 56 entfernte Zeilen, ausschließlich den sechs beauftragten Punkten zuzuordnen.

## 2026-07-16 – Calendly-Icon auf Gesprächs-CTAs ergänzt

Status: geprüft

Geändert:

- Das vorhandene wiederverwendbare Calendly-Inline-SVG (`#nv-calendly-mark`, `20px`) zusätzlich in die drei zum Gespräch auffordernden CTAs in `homepage/index.html` eingefügt: Header-CTA (`Unverbindliches Erstgespräch`), Hero-Sekundär-CTA (`Unverbindliches Erstgespräch`, Ziel `#kontakt`) und Kontaktkarten-CTA (`Erstgespräch vereinbaren`, Ziel `analyse.html`).
- Eine einzelne CSS-Regel `.golden-button:has(.nv-calendly-icon) { --nv-golden-display: inline-flex; gap: 8px; }` ergänzt, damit das Icon innerhalb des Golden Buttons inline links vor dem Text sitzt. Zuvor saß das Icon durch die Standard-`inline-block`-Darstellung außerhalb der eigentlichen Buttonfläche in einer eigenen Zeile ("ganz wo anders"). Die Regel nutzt das bestehende Display-Variablensystem (`--nv-golden-display`) und korrigiert zugleich die Platzierung der vier bereits vorhandenen Potenzialanalyse-Icon-CTAs.

Nicht geändert:

- CTA-Texte, CTA-Ziele, `aria-label`-Werte und Formularlogik in `homepage/index.html`.
- Der Projektprüfungs-CTA `Projektidee prüfen lassen` bleibt bewusst ohne Calendly-Icon, da er nicht zu einem Gespräch auffordert.

Konflikt / Entscheidungsänderung:

- Diese Änderung hebt die bisherige Festlegung im Eintrag „CTA auf Golden Button reduziert" vom selben Tag („Gesprächs- und Projektprüfungs-CTAs bleiben ohne Calendly-Zeichen") für die Gesprächs-CTAs auf. Grundlage ist die explizite aktuelle Benutzervorgabe, die laut Prioritätenrangfolge über der früheren Entscheidung in `decision_log.md`/`changelog.md` steht. Projektprüfungs-CTAs bleiben weiterhin ohne Calendly-Zeichen.

Verifikation:

- `homepage/index.html` headless in Chromium gerendert; Header-, Hero- und Kontakt-CTA per Screenshot geprüft: Das Calendly-Icon sitzt in allen Gesprächs-CTAs inline auf dem Button. Keine JavaScript-Fehler beim Laden. Calendly-Icon-Referenzen im Dokument: 7 (4 Potenzialanalyse + 3 Gespräch).

## 2026-07-16 – CTA auf Golden Button reduziert

Status: geprüft

Geändert:

- CTA-Darstellung in `homepage/index.html` auf die Golden-Button-Farb-, Rahmen- und Schattenlogik reduziert.
- Click-Button-Front-, Edge-, Base- und Bewegungs-Layer aus den CTA-Markups und CTA-Regeln entfernt.
- Verbleibende CTA-Komponente auf `golden-button` und `golden-text` bereinigt.
- Golden-Button-Farben und -Verlauf exakt auf die gesonderte Button-Vorgabe zurückgeführt; Header-CTA bei `11px` auf Großbuchstaben gestellt und Sektions-CTAs auf `13px` reduziert.
- Bulletpoints in `Warum Nurovelle` auf runde Goldmarker umgestellt; fett gesetzte Einleitungen bis zum Doppelpunkt gold hervorgehoben und den jeweiligen Erklärungstext darunter angeordnet.
- Kicker sowie Kreis- und Fetthervorhebungen in `Warum Nurovelle` vom gelblicheren Akzent auf den vorhandenen dunkleren Root-Goldton `--nv-gold-inner-mid` umgestellt.
- Abstand zwischen Hero-Unterzeile und Fließtext auf `32px` erhöht; CTA-Höhe und Mindestabstand zum folgenden Sektionstrenner als Root-Werte mit `44px` beziehungsweise `2 × 44px` verankert.
- In `Warum Nurovelle` das vorhandene `assets/bulletpoint.png` in einen runden Goldrahmen gesetzt, den Punkt `Klare nächste Schritte` vollständig entfernt und das Video auf Desktop um `24px` nach rechts sowie `42px` nach unten verschoben.
- Marker in `Warum Nurovelle` auf `14px` verkleinert und zur ersten Textzeile mittig ausgerichtet; Video-Versatz auf Desktop auf `148px` nach rechts und `168px` nach unten erhöht.
- `Warum Nurovelle` auf ein stabiles Grid mit bis zu `760px` breiter Textspalte, `320px` breiter Videospalte und `48px` Spaltenabstand umgestellt; Video ohne freien Transform mittig zur Bulletpoint-Liste ausgerichtet.
- Breitenänderung in `Warum Nurovelle` auf die beiden Absätze unter dem Titel begrenzt; Bulletpoint-Liste wieder um `82px` schmaler gesetzt und der sichtbare Abstand zum mittig ausgerichteten Video bei `48px` gehalten.
- Marker in `Warum Nurovelle` auf `11px` reduziert, Goldüberschriften explizit fett gesetzt, Bullet-/Videoabstand auf `80px` erhöht und ausschließlich die beiden oberen Absätze um weitere `52px` verbreitert.
- Marker in `Warum Nurovelle` an der Mitte des gesamten Bullettextblocks ausgerichtet; Videoabstand auf Desktop auf `120px` und im aktiven einspaltigen Layout auf `88px` erhöht.
- Marker in `Warum Nurovelle` auf `7px` reduziert und zur goldenen Überschriftszeile ausgerichtet; Videoabstand gegenüber dem ursprünglichen Stand auf Desktop auf `144px` und im einspaltigen Layout auf `264px` verdreifacht.
- Markerposition anschließend direkt an die jeweilige goldene Überschriftszeile gebunden und dort unabhängig von der Länge des Erklärungstextes vertikal zentriert.
- Desktop-Videoabstand in `Warum Nurovelle` von einem breitenreduzierenden Grid-Margin auf eine Verschiebung des vollständigen Frames umgestellt, sodass die Videobreite erhalten bleibt.
- Im aktiven einspaltigen Layout den Videoframe bei `640px` Breite rechtsbündig positioniert und den vertikalen Textabstand exakt auf `260px` gesetzt; Mobile unter `640px` bleibt vollbreit.
- Den `260px`-Abstand im einspaltigen `Warum Nurovelle`-Layout vom Video-Margin an die verantwortliche Grid-Regel als `row-gap` verschoben.
- Videoframe in `Warum Nurovelle` von der quadratischen Mindesthöhe auf ein durchgängiges rechteckiges `16:9`-Seitenverhältnis für Desktop, Tablet und Mobile umgestellt.
- Videoframe in `Warum Nurovelle` bei `640 × 360px` belassen und im Desktop-Grid mit `220px` sichtbarem Abstand wieder rechts neben den Bulletpoints angeordnet.
- Beide Absätze unter dem Titel `Warum Nurovelle` bis zur Bulletpoint-Liste auf eine eigene Breite von `955px` gesetzt; die Bulletpoint-Liste behält separat ihre schmalere Breite.
- Feste Hero-Höhe durch eine Mindesthöhe ersetzt und den unteren Hero-Abstand an `--nv-section-divider-before-gap` gebunden, damit die Hero-Trennlinie bei umgebrochenen CTAs nicht mehr durch die Buttons läuft.
- Abstand zwischen Hero-Untertitel und folgendem Fließtext über `--nv-hero-subtitle-body-gap` von `32px` auf `40px` erhöht.
- Abstand zwischen dem zweiten Textabsatz und der Bulletpoint-Liste in `Warum Nurovelle` von `34px` auf `80px` erhöht; der Abstand zwischen den beiden Absätzen bleibt unverändert.
- Cards in `Projektstart` auf Desktop als symmetrische diagonale Folge mit `0px`, `400px` und `800px` Horizontalversatz angeordnet; erst beim ersten sichtbaren Eintritt der gesamten Sektion fahren die vorhandenen Cards nacheinander vollständig vom linken Sektionsrand ein und blenden ihren Text jeweils nach Erreichen der Zielposition ein. Cardtext um `9px` angehoben und rechts um `22px` weiter in den Rahmen gesetzt.
- Sichtbaren Card-Gesamtrahmen in `Projektstart` aus der linken Kante der ersten und rechten Kante der letzten Card gebildet und zusammen mit der CTA auf derselben Sektionsmittelachse zentriert; diagonale Anordnung bis zum Mobile-Breakpoint erhalten. Rechten Textinnenabstand anhand der tatsächlichen PNG-Rahmenkante auf `82px` beziehungsweise proportional `65px` mobil erhöht.
- Der anhand der sichtbaren PNG-Fläche zentrierte Cardframe verwendet auf Desktop die gleichmäßigen Versätze `0px`, `400px` und `800px`, auf Tablet `0px`, `260px` und `520px` und wird erst unter `640px` ohne Versatz gestapelt.
- In den `Projektstart`-Cards den Abstand zwischen Titel und Beschreibung von `10px` auf `6px` sowie zwischen Beschreibung und der Linie über `Mehr erfahren` von `18px` auf `14px` reduziert.
- Vertikalen Abstand der drei `Projektstart`-Cards durch jeweils `-120px` Zeilenüberlappung verkürzt, sodass alle drei vollständigen Cards zusammen mit der CTA innerhalb der aktuellen Desktop-/Tablet-Bildschirmhöhe sichtbar sind; Mobile bleibt ohne Überlappung gestapelt.
- Gesamten Cardframe in `Projektstart` um exakt `35px` nach links verschoben; CTA, Überschrift, Einleitung, Card-Abstände und Animation bleiben unverändert.
- Rundlauf in `Von der Idee zum Projekt` korrigiert: bisheriges Bild 2 (`assets/Fotos/13.png`) an Position 1 gesetzt, Wide-Grid der richtigen Slide zugeordnet, Bild und Text als gemeinsamer Frame zentriert und Abstand Desktop/Tablet/Mobile jeweils um `30%` reduziert. Die Übergänge sind so synchronisiert, dass das auslaufende Bild den rechten Rand exakt dann erreicht, wenn das folgende Bild die mittige Stoppposition erreicht. Titel `Interne Wissenssuche` in `Unternehmenswissen schnell finden` geändert.
- Die sechs vorhandenen Ablaufmodule als räumlich nach rechts absteigende 2-2-2-Folge angeordnet: Schritte 1/2 oben, die Reihe 3/4 um eine Modulposition nach rechts und eine Ebene nach unten versetzt, die Reihe 5/6 nochmals entsprechend versetzt. Dadurch sitzt Schritt 3 unter Schritt 2 und Schritt 5 unter Schritt 4. Die Paare sind horizontal verbunden; die Übergänge 2→3 und 4→5 verbinden die Ebenen seitlich. Inhalte, Assets, Leistungen und Kontakt blieben unverändert.
- Die zunächst pauschale Linksneigung der Modul-Visuals entfernt und durch eine gemeinsame Fluchtpunkt-Perspektive ersetzt: Die Module drehen sich abhängig von ihrer horizontalen Position nach innen; obere Module werden als hintere Ebene kleiner, mittlere bleiben neutral skaliert und untere werden als vordere Ebene größer. Sockel und Aufsatz teilen jeweils dieselbe Transformation und denselben Tiefenschatten. Reihenfolge, Texte und 2-2-2-Geometrie blieben unverändert; Tablet und Mobile bleiben unverzerrt.
- Modul-Aufbauten und Sockel in der Ablaufsektion deutlich vergrößert, die Tiefenstaffelung entsprechend angehoben und die Modulbezeichnungen von `16px` auf `12px` reduziert.
- Kontaktsektion gemäß freigegebener Zweispaltenstruktur aufgebaut: links die Portraitkarte mit `assets/Whisk_ac35ee0e10.jpg`, rundem Goldrahmen, Name, Marke und vier beschrifteten Social-Symbolen; rechts und deutlich tiefer versetzt die bestehende Erstgesprächskarte mit unveränderten Texten, separatem CTA zu `analyse.html` sowie verlinkter E-Mail und Telefonnummer. Beide Karten verwenden schwarzes Nurovelle-Material und werden entsprechend der Skizze durch eine kurze horizontale Goldlinie verbunden. Nicht dokumentierte Social-Profilziele wurden nicht erfunden.
- Beide Kartentitel der Kontaktsektion vom weißen Textton auf den vorhandenen Goldton `--nv-gold-accent` umgestellt.
- E-Mail, Telefon und Standort aus der rechten Karte entfernt und unter Portrait, Identität und Social-Symbolen in der linken Karte angeordnet. Portraitkarte und Kontaktkarte ohne horizontalen Abstand direkt an derselben Kante positioniert; ausschließlich die rechte Kontaktkarte bleibt um `330px` vertikal versetzt. Eine Verbindungslinie wird nicht verwendet.
- Sämtliche Typografie der rechten Kontaktkarte um zwei bis drei Größenstufen reduziert: Titel auf maximal `30px`, Fließtext auf `13px` und CTA-Schrift auf `11px`.
- Rechte Kontaktkarte auf Desktop von gemessenen `666px` exakt um `30%` auf `466.2px` verschmälert; Portraitbreite, gemeinsamer horizontaler Ansatz und vertikaler Versatz blieben unverändert.
- Das Calendly-Zeichen als wiederverwendbares `20px`-Inline-SVG ausschließlich in die vier Potenzialanalyse-CTAs einschließlich Formularbutton eingefügt; Gesprächs- und Projektprüfungs-CTAs bleiben ohne Calendly-Zeichen.
- FAQ-Titel sichtbar beibehalten und alle acht FAQ-Auslöser direkt an die bestehende Golden-Button-Darstellung der CTAs gebunden. Das vorhandene Kennzahlen-Liniendiagramm steht auf Desktop und Tablet rechts neben der FAQ-Spalte; mobil wird es darunter angeordnet.

Nicht geändert:

- CTA-Texte, Ziele und Formularlogik in `homepage/index.html`.

## 2026-07-15 – Korrekturfortsetzung und Bereinigung (Layout/Assets)

Status: in Arbeit

Geändert:

- Dritte Bereinigungsstufe: wiederholte lokale Abstandswerte und kleine Radiuswerte in den Komponenten auf zentrale Tokens umgestellt (`--nv-space-*`, `--nv-radius-*`), ohne sectionsinterne Geometrie-Logik zu verändern.
- Zweite Bereinigungsstufe: wiederverwendete Spacing-/Radius-Werte zentral in `homepage/index.html` als Tokens ergänzt (`--nv-space-xxs/xs/sm/md/lg/xl/2xl`, `--nv-radius-sm/md`) und in den Komponenten an mehreren wiederholten Stellen verwendet.
- Verbindliche Mapping-Tabelle erstellt: `project_files/css_value_matrix.md` (Wertquelle, Verantwortlichkeit und Dateigrenzen).
- Zentrale Global-Tokens in `homepage/index.html` ergänzt (`--nv-section-inner-max`, `--nv-section-head-max`, `--nv-section-intro-max`, `--nv-footer-inner-max`, `--nv-section-title-gradient`, `--nv-gold-divider-strong`).
- In `homepage/components/nurovelle-service-cards.css` wiederverwendete Global-Literale (Textfarben, Titelgradient, globale Max-Breite) auf zentrale Tokens umgestellt; sectionsinterne Geometrie blieb unverändert.
- In `homepage/components/nurovelle-resources-contact-faq.css` wiederverwendete Global-Literale (Textfarben, Titelgradient, globale Max-Breiten) auf zentrale Tokens umgestellt; sectionsinterne Geometrie blieb unverändert.
- In `homepage/components/nurovelle-section-rhythm.css` wiederverwendete Global-Literale (Textfarben, Titelgradient, globale Max-Breiten, Footer-Basisfarben/Divider) auf zentrale Tokens umgestellt.
- Globale Rhythmus-, Alternation-, Separator- und responsive Sidebar-/Header-Regeln aus `homepage/components/nurovelle-section-rhythm.css` nach `homepage/index.html` verschoben.
- `homepage/components/nurovelle-section-rhythm.css` auf sectionsinterne Regeln fuer Prozess, Why und Footer reduziert.
- Sektion-7-Headerabstaende (`Head`, `Kicker`, `Title`) wieder lokal in `homepage/components/nurovelle-service-cards.css` verankert.
- Download-/Resource-Headerabstaende (`Head`, `Kicker`, `Title`) wieder lokal in `homepage/components/nurovelle-resources-contact-faq.css` verankert.
- Hintergrund-Alternation in `homepage/components/nurovelle-section-rhythm.css` auf den verbindlichen Sequenzstand korrigiert (`#warum-nurovelle`, `#ki-projekt-start`, `#projektidee`, `#potenzialanalyse`, `#formular`, `#leistungen`, `#prozess-zur-loesung`, `#downloads`, `#kontakt`, `#faq`, `.footer`).
- Prozesssektion in `homepage/components/nurovelle-section-rhythm.css` räumlich nachgestaffelt (2 + 2 + 2 über `nth-child`-Offsets), Mobile-Fallback ohne Offset beibehalten.
- Service-Card-Typografie in `homepage/components/nurovelle-service-cards.css` harmonisiert (lesbarere Bullet-, Untertitel- und Ergebnisgrößen).
- Service-Icon-Pfade in `homepage/index.html` auf `assets/cards/service/icons/{1..11}.png` umgestellt.
- Ergebnis-Icon-Injektion in `homepage/index.html` ergänzt (`assets/cards/service/icons/ergebnis.png`) innerhalb der bestehenden Service-Card-JavaScript-Logik.
- Platzhalter-Iconsatz unter `homepage/assets/cards/service/icons/` erstellt (`1.png` bis `11.png`, `ergebnis.png`) zur Stabilisierung fehlender Pfade.

Nicht geändert:

- Formularverarbeitung, Honeypot sowie Success-/Error-Grundlogik in `homepage/index.html`.
- Hero-Partikel-Canvas- und Cube-Grundlogik in `homepage/index.html`.

## 2026-07-14 – Kontrolliertes Homepage-Update in `homepage/index.html`

Status: in Arbeit

Geändert:

- Header-/Breadcrumb-Zielanker in `homepage/index.html` auf die aktuelle Sektionenstruktur angepasst (`#warum-nurovelle`, `#ki-projekt-start`, `#projektidee`, `#potenzialanalyse`, `#formular`, `#prozess-zur-loesung`, `#downloads`, `#kontakt`, `#faq`).
- Sidebar-Linktexte und -Reihenfolge in `homepage/index.html` an den aktuellen Inhaltsstand angepasst (inklusive neuem `Kontakt`-Eintrag).
- Abschnitt `Warum Nurovelle` in `homepage/index.html` inhaltlich auf freigegebenen Textstand umgestellt (2 Einleitungsabsätze + 6 Bulletpoints).
- Abschnitt `Der erste Schritt zu Ihrem KI-Projekt` in `homepage/index.html` textlich bereinigt und CTA auf `Potenzialanalyse starten` angepasst.
- Step-Animation in `homepage/index.html` erweitert: Karten sliden von links ein; Card-Text wird erst nach Ankunft sichtbar; Reduced-Motion-Fallback ohne Textverzögerung.
- Abschnitt `Konkrete KI-Idee` in `homepage/index.html` auf die Reihenfolge Prozessautomatisierung → Datenbasierte Entscheidungshilfe → Interne Wissenssuche umgestellt; breite Bildvariante vergrößert.
- Abschnitt `Vom Geschäftsprozess zur KI-Lösung` in `homepage/index.html` auf die sechs freigegebenen Modulbezeichnungen reduziert (ohne Beschreibungssätze).
- Neuer Abschnitt `Kontakt` in `homepage/index.html` ergänzt (40/60-Layout mit Portrait- und Kontaktkarte, Mobile-Stapelung).
- FAQ-Texte in `homepage/index.html` auf den freigegebenen Wortlaut aktualisiert; kompakte Kennzahlenleisten ergänzt.
- Footer in `homepage/index.html` inhaltlich auf die geforderten Gruppen erweitert (Unternehmensbeschreibung, nützliche Links, Newsletter, Kontakt, Rechtliches, Copyright, Nach-oben-Text, deaktivierte Links für Aktuelles/Team/SEO/Pakete).
- Hero-Sekundär-CTA in `homepage/index.html` auf `Unverbindliches Erstgespräch` mit Ziel `#kontakt` umgestellt.
- Potenzialanalyse- und Formularüberschriften/-texte in `homepage/index.html` an den freigegebenen Wortlaut angenähert.

Nicht geändert:

- Technische Formularfeldnamen und Grund-Submit-Mechanik in `homepage/index.html`.
- Download-Success-/Error-Zustandslogik in `homepage/index.html`.
- Hero-Cube-Asset und Partikel-Canvas-Grundlogik in `homepage/index.html`.

## 2026-07-15 – Platzhalter für fehlende Downloadpfade angelegt

Status: fertig

Geändert:

- `homepage/assets/downloads/checkliste.pdf` als Platzhalterdatei erstellt.
- `homepage/assets/downloads/prompt_guide.pdf` als Platzhalterdatei erstellt.

Nicht geändert:

- `homepage/index.html`.

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

---

## Verbindlicher Homepage-Stand – 2026-07-14

Status: freigegeben

Diese Festlegung ersetzt abweichende ältere Homepage-Strukturen und Textstände in dieser Datei. Ältere Angaben zu Trust-Bereich, klassischer Navigation, zusätzlichem SEO-Bereich als aktuelle Sektion, ausführlichen Prozesskarten oder einer anderen Sektionsreihenfolge dürfen nicht mehr verwendet werden.

### Header

- Breadcrumbs ersetzen die klassische Navigation vollständig.
- Der Header enthält genau drei Breadcrumbs mit Submenüs.
- Die Submenüs öffnen sich per Hover.
- Keine zusätzliche klassische Hauptnavigation.

### Verbindliche Homepage-Reihenfolge

1. Hero
2. Warum Nurovelle
3. Der erste Schritt zu Ihrem KI-Projekt
4. Sie haben bereits eine konkrete KI-Idee?
5. Branchen – optional, noch nicht final entschieden
6. Kostenlose KI-Potenzialanalyse
7. Formular
8. KI-Leistungen von Nurovelle
9. Vom Geschäftsprozess zur KI-Lösung
10. Download-Bereich
11. Kontakt
12. FAQ
13. Footer

Ein separater SEO-Bereich ist für einen späteren Ausbau vorgesehen und gehört nicht zur aktuell verbindlichen Reihenfolge.

### Hero

Kicker:

`INDIVIDUELLE KI-SYSTEME`

H1:

`KI-Agenten für echte Geschäftsprozesse.`

Subline:

`Nurovelle entwickelt individuelle KI-Systeme für Datenverarbeitung, Wissenszugriff, Prozessautomatisierung und Unternehmenssoftware.`

Zusatzzeile:

`Von der Potenzialanalyse über Prompt Engineering und MCP bis zur Umsetzung maßgeschneiderter KI-Lösungen.`

CTAs:

- `Kostenlose KI-Potenzialanalyse anfordern` → Potenzialanalyse
- `Unverbindliches Erstgespräch` → Kontaktbereich

Nicht verwenden:

- `Künstliche Intelligenz. Echte Ergebnisse.`
- `35+ Jahre Code`
- Trust-Aussagen im Hero
- Praxisleitfaden als zweiter Hero-CTA

### Warum Nurovelle

- Der Abschnitt benötigt eine Einleitung aus mindestens zwei bis drei Sätzen.
- Danach folgen fünf bis sechs konkrete Bulletpoints.
- Keine Trust-Kennzahlenleiste.
- Keine Unternehmensgeschichte.
- Keine unbelegten Erfahrungs- oder Leistungsversprechen.
- Der finale Wortlaut der Einleitung und Bulletpoints ist noch nicht freigegeben und darf nicht frei erfunden werden.

### Der erste Schritt zu Ihrem KI-Projekt

Einleitung:

`Ob erste Orientierung oder konkrete Projektidee: Wir prüfen Prozesse, Daten und technische Voraussetzungen und zeigen den passenden nächsten Schritt.`

Card 1:

### Prozess klären

`Welcher Geschäftsprozess verbessert werden soll und welches konkrete Ergebnis durch KI entstehen muss.`

`Mehr erfahren`

Card 2:

### Daten prüfen

`Welche Daten, Systeme und Wissensquellen bereits vorhanden sind und technisch nutzbar gemacht werden können.`

`Mehr erfahren`

Card 3:

### Umsetzung planen

`Ob ein KI-Agent, ein Wissenssystem, Automatisierung oder individuelle Software der sinnvolle nächste Schritt ist.`

`Mehr erfahren`

CTA:

`Potenzialanalyse starten`

### Sie haben bereits eine konkrete KI-Idee?

Einleitung:

`Wir prüfen Machbarkeit, Datenlage und Integrationsaufwand, bevor unnötige Entwicklungs- oder Folgekosten entstehen.`

CTA:

`Projektidee prüfen lassen`

### Kostenlose KI-Potenzialanalyse

- Eigene Sektion vor dem Formular.
- Nicht mit dem Formular oder einer Trust-Section vermischen.
- Der finale vollständige Text dieser Sektion ist noch nicht freigegeben und darf nicht frei ergänzt werden.

### Formular

- Eigene Sektion direkt nach der Potenzialanalyse.
- Formular rechts, begleitende Card links.
- Pflichtfelder, Einwilligung, Datenschutz, Honeypot, Submission sowie Success-/Error-Logik bleiben erhalten.
- Der finale Text der linken Card ist noch nicht freigegeben.

### KI-Leistungen von Nurovelle

Jede Leistungskarte enthält:

- links oben ein Icon mit Rahmen
- rechts daneben einen Trennstrich
- eine Nummer mit eigenem Rahmen
- Titel und Untertitel
- eine mittig angeordnete Nummernkarte links neben dem Inhaltsbereich
- maximal vier Bulletpoints

Inhaltsregeln:

- Kein zusätzlicher Fließtext, der die Bulletpoints wiederholt.
- Keine weitere Text-Card auf der Leistungskarte.
- Titel, Untertitel und Bulletpoints dürfen denselben Inhalt nicht mehrfach ausdrücken.
- Keine vollständigen Detailseiten-Inhalte auf der Homepage.

### Vom Geschäftsprozess zur KI-Lösung

- Die bisherigen Prozesskarten mit Beschreibungstexten entfallen.
- Nur Module in der freigegebenen Stepdiagramm-Anordnung verwenden.
- Je Modul ausschließlich die Modulbezeichnung anzeigen.
- Keine Erklärungssätze, Bulletpoints oder zusätzlichen Cards.
- Kein CTA.

### Download-Bereich

- Eigene Sektion nach dem Stepdiagramm.
- Bestehende Downloads mit kurzen, nicht wiederholenden Beschreibungen.
- Finale Einzeltexte sind noch zu prüfen.

### Kontakt

- Eigene Kontaktsektion nach dem Download-Bereich.
- Nicht mit Potenzialanalyse oder Formular vermischen.
- Finale Kontakttexte sind noch zu prüfen.

### FAQ

- Abschnitt 12.
- Bestehende Fragen und Antworten nicht ungeprüft verändern.
- Finale FAQ-Texte sind gesondert zu prüfen.

### Footer

Verbindlicher Beschreibungstext:

`Individuelle KI-Systeme für reale Geschäftsprozesse.`

Keine lange Leistungsbeschreibung, Unternehmensgeschichte oder technische Erklärung im Footer.

### Textstatus

- Kein bisheriger vollständiger Sektionstext darf ungeprüft als final verwendet werden.
- Nur die in diesem Nachtrag wörtlich festgelegten Texte gelten als freigegeben.
- Fehlende Texte dürfen nicht selbstständig erfunden, ergänzt oder aus alten Dateien übernommen werden.
