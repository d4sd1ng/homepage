# NUROVELLE HOMEPAGE IMPLEMENTATION BRIEF

Status: konsolidierte Arbeitsfassung für HTML/CSS/JS-Umsetzung; CTA-/Formular-/Success-Logik final festgelegt; Bestandscode und Rechts-/Analyse-Seiten ergänzt; Assetliste und Modultabelle sind Referenzanlagen, aber nicht mehr kritische Freigabeblocker  
Stand: 2026-06-30  
Zweck: Diese Datei ist die **eine Haupt-Brief-Datei** für den HTML-Programmierer. Sie wird zusammen mit genau zwei Anlagen übergeben: **Assetliste** und **Workflow-Modultabelle**.

---

## 0. Übergabepaket

Die vollständige Übergabe besteht aus genau diesen drei Teilen:

1. `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`  
   Haupt-Brief. Enthält Seitenstruktur, Inhalte, Designregeln, technische Regeln, CTA-Logik, SEO, Interaktionen und Umsetzungsvorgaben.

2. Assetliste  
   Separate Referenzanlage mit aktuell bekannten Bild-, Icon-, Mockup- und Download-Pfaden. Die Assetliste ist **nicht aktuell** und wird ab diesem Stand **nicht mehr als kritischer Freigabeblocker** bewertet. Sie dient der Pfad- und Asset-Orientierung, ersetzt aber keine Prüfung im realen Projektordner.

3. `workflow_module_table.xlsx`  
   Separate Referenzanlage für Workflow-/Modul-Assets. Die Modultabelle ist **nicht aktuell** und wird ab diesem Stand **nicht mehr als kritischer Freigabeblocker** bewertet. Sie dient der Orientierung für verfügbare Module und spätere Zuordnung, nicht als finale Umsetzungspflicht.

Es werden keine weiteren Übergabedateien benötigt. Assetliste und Modultabelle bleiben Anlagen, blockieren die HTML-Übergabe aber nicht mehr allein durch fehlende Aktualität.

---

## 0.1 Verbindlichkeit

Diese Datei beschreibt die Umsetzung der Startseite und der technischen Basis für Folgeausbau.  
Die Assetliste und die Modultabelle werden **nicht vollständig in diese Datei kopiert**. Sie sind Referenzanlagen, aber nicht mehr kritische Blocker, weil beide nicht aktuell sind.

Regel für den Programmierer:

- Inhalte, Layoutlogik und Interaktionen aus dieser Datei übernehmen.
- Asset-Dateinamen und Assetpfade aus der Assetliste nur als Referenz übernehmen und gegen den realen Projektordner prüfen.
- Modul-/Workflow-Zuordnungen aus der Modultabelle nur als Referenz behandeln, nicht als finale Pflichtzuordnung.
- Keine zusätzlichen Layoutideen ergänzen.
- Keine Sections hinzufügen.
- Keine Inhalte kürzen.
- Keine Farbstile ändern.
- Keine Assets neu interpretieren.

---

## 0.2 Was gebaut wird

Gebaut wird:

- eine responsive Nurovelle-Startseite
- vorhandener Header
- vorhandene Sidebar
- vorhandener Footer
- Hero-Bereich
- Sections 2 bis 8 gemäß dieser Datei
- keine zusätzliche Formular-/Kontaktsektion auf der Startseite
- Potenzialanalyse-Seite `analyse.html` mit bestehendem Formular- und API-Flow
- Success-/Error-Zustand in `analyse.html`, keine separate `danke.html`
- Downloadbereich mit später verlinkbaren Assets
- Leistungs-Cards mit Hover/Tap-Interaktion
- SEO-/OG-Grunddaten
- saubere Anker- und CTA-Logik

---

## 0.3 Was nicht gebaut wird

Nicht bauen:

- keine neue Markenlogik
- kein neues Farbsystem
- kein neuer Header
- kein neuer Footer
- keine neue Sidebar
- kein neues Formular
- kein Loginbereich
- kein Kundenportal
- kein Blogsystem
- keine neue Download-Detailseitenstruktur
- keine Detailseiten-Inhalte in dieser Startseitenumsetzung
- keine zusätzlichen Trust-Sections
- keine Faktenbox in „Warum Nurovelle“
- keine generischen KI-Roboter
- keine fremden Dashboard-Szenen

---

## 0.4 Technische Zielstruktur

Empfohlene einfache Dateistruktur für die Umsetzung:

```text
/
├── index.html
├── assets/
│   ├── images/
│   ├── icons/
│   ├── downloads/
│   └── og/
├── css/
│   └── styles.css
└── js/
    └── main.js
```

Falls ein bestehendes Projekt bereits eine andere Struktur hat, darf diese übernommen werden. Die IDs, CTA-Ziele und Komponentenlogik aus dieser Datei bleiben verbindlich.

---

## 0.5 Pflicht-IDs und Anker

Diese IDs müssen existieren:

| Bereich | ID | Zweck |
|---|---|---|
| Hero | `#hero` | Startbereich |
| Erster Schritt | `#ki-projekt-start` | Einstiegserklärung |
| Potenzialanalyse | `#potenzialanalyse` | Analyse-Angebot |
| Projektidee | `#projektidee` | konkrete Idee prüfen |
| Leistungen | `#leistungen` | 11 Leistungs-Cards |
| Prozess/Roadmap | `#prozess-zur-loesung` | Geschäftsprozess zu KI-Lösung |
| Warum Nurovelle | `#warum-nurovelle` | Glaubwürdigkeit ohne Trust-Box |
| Downloads | `#downloads` | Downloadbereich |
| Potenzialanalyse / Anfrage | `analyse.html` | aktuelle Analyse-Seite mit Formular und API-Flow |

CTA-Regel:

- alle Potenzialanalyse- und Anfrage-CTAs immer zu `analyse.html`
- Download-CTAs bleiben bei `#downloads` oder `praxisleitfaden.html`
- kein zusätzlicher Kontakt-/Formularbereich auf der Startseite
- kein zusätzlicher Roadmap-CTA

---

## 0.6 Design-Tokens für CSS

Diese Werte sind als CSS-Variablen anzulegen oder äquivalent im bestehenden CSS-System abzubilden.

```css
:root {
  --color-black: #050706;
  --color-matte-black: #080B09;
  --color-deep-green: #0A1913;
  --color-emerald: #112A20;
  --color-teal-dark: #163A35;
  --color-text-light: #F5F7F4;
  --color-text-muted: #B9C3BD;

  --gold-1: linear-gradient(135deg, #AE8625, #F7EF8A, #D2AC47, #EDC967);
  --gold-2: linear-gradient(135deg, #DFBD69, #926F34);
  --gold-3: linear-gradient(135deg, #F9F295, #E0AA3E, #FAF398, #B88A44);
  --gold-text-alt: linear-gradient(135deg, #C5A059 0%, #FDF0CD 50%, #D4AF37 100%);

  --bg-green-1: linear-gradient(135deg, #0A1913 0%, #112A20 50%, #1D4234 100%);
  --bg-green-2: linear-gradient(180deg, #071412 0%, #163A35 100%);

  --radius-card: 18px;
  --radius-button: 999px;
  --max-width: 1200px;
  --section-padding-desktop: 120px 24px;
  --section-padding-tablet: 88px 24px;
  --section-padding-mobile: 64px 18px;
}
```

Nicht verwenden:

- Cyan
- Blau als Hauptfarbe
- Violett
- Bronze
- Kupfer
- Neon-Look

---

## 0.7 Web-Typografie

| Element | Schrift | Desktop | Mobile | Regel |
|---|---:|---:|---:|---|
| H1 | Bebas Neue | 64–88 px | 42–56 px | All Caps möglich, Goldverlauf erlaubt |
| Section-H2 | Bebas Neue | 44–60 px | 34–42 px | Goldverlauf oder hell auf dunkel |
| H3 / Card-Titel | Anca Coder / Coder Pro | 18–24 px | 17–21 px | technische Labels / Cards |
| Body | Raleway oder Roboto | 17–19 px | 16–18 px | gut lesbar, keine zu engen Zeilen |
| Label / Zahlen | Anca Coder / Coder Pro | 12–15 px | 12–14 px | technische Akzente |
| Button | Raleway oder Roboto | 15–17 px | 15–16 px | klar, klickbar |

Fallbacks:

```css
font-family: 'Bebas Neue', Impact, sans-serif;
font-family: 'Anca Coder', 'Coder Pro', monospace;
font-family: 'Raleway', 'Roboto', Arial, sans-serif;
```

---

## 0.8 Responsive Breakpoints

| Breakpoint | Regel |
|---|---|
| ab 1200 px | Desktop-Layout mit maximaler Breite `1200px` |
| 900–1199 px | Tablet: Grids auf 2 Spalten reduzieren |
| unter 900 px | Hero und Text/Bild-Sektionen stapeln |
| unter 640 px | Cards einspaltig, CTAs untereinander, ausreichende Tap-Flächen |

Mobile Mindestregeln:

- Buttons mindestens 44 px Höhe.
- Keine abgeschnittenen Card-Inhalte.
- Leistungs-Cards per Tap öffnen.
- Ein geöffneter Card-Zustand reicht; beim Öffnen einer anderen Card schließt die vorherige.

---

## 0.9 Komponentenregeln

### Buttons

Primärbutton:

- Goldverlauf 3
- dunkle Schrift oder sehr dunkles Grün/Schwarz
- runde Pill-Form
- klarer Hover-Zustand

Sekundärbutton:

- transparenter Hintergrund
- Goldrahmen
- helle Schrift
- Hover: dezente goldene Fläche oder Goldglow

### Cards

- dunkle matte Fläche
- dezenter grüner Rahmen oder dunkler Glasrahmen
- kein Goldrahmen um alle Cards, außer explizit angegeben
- Gold nur für Akzente, Trennlinien, Hover, CTA, Highlights
- keine langen Fließtexte in Leistungs-Cards

### Section-Hintergründe

- Wechsel aus mattem Schwarz und sehr dunklem Petrol/Grün
- keine bunten Verläufe
- keine hellen Vollflächen
- keine Stockfoto-Optik

---

## 0.10 Header / Footer / Sidebar

Header, Footer und Sidebar werden aus dem vorhandenen Bestand übernommen.

Umsetzungsregel:

- bestehendes Markup übernehmen
- bestehende Navigation übernehmen
- bestehendes Verhalten übernehmen
- nur Links/Anker an diese Datei anpassen
- keine neue Navigation konzipieren
- keine neue Sidebar-Logik erfinden

Wenn der vorhandene Code nicht verfügbar ist, darf der Programmierer **nicht frei neu entwerfen**, sondern muss dies als fehlende Quelle markieren.

---

## 0.11 Formular / Kontakt

Es wird kein zusätzlicher Formular-/Kontaktbereich auf der Startseite gebaut. Die Potenzialanalyse läuft über `analyse.html`.

Verbindlich:

- Zielseite: `analyse.html`
- keine neuen Felder
- Formular in `analyse.html`logik aus `analyse.html` übernehmen
- keine neue Inhaltsplanung
- bestehende Formularverarbeitung/API-Logik aus `analyse.html` übernehmen
- nach erfolgreichem Absenden Success-/Error-Zustand in `analyse.html` verwenden; keine separate `danke.html` erstellen

Technisch zu prüfen:

- Pflichtfelder funktionieren
- Datenschutz-/Einwilligungshinweis bleibt sichtbar
- Fehlermeldungen sind mobil lesbar
- Erfolgsmeldung oder Weiterleitung funktioniert

Wenn die bestehende Formularlogik nicht verfügbar ist, muss sie als fehlende Quelle markiert werden. Nicht frei neu konzipieren.

---

## 0.11.1 Bestandscode- und Seitenquellen

Die vorhandenen HTML-Dateien sind technische Quellen. Wichtig: `index.html` ist **alter Stand** und darf nicht als finale Startseitenstruktur übernommen werden. `analyse.html` ist als aktuelle Analyse-Seite/Formularbasis vorhanden. Die Rechtsseiten und `praxisleitfaden.html` sind als vorhandene Zielseiten zu berücksichtigen.

### `index.html`

Verwendung:

- alter Startseitenbestand / technische Referenz
- Referenz für vorhandene Header-, Sidebar- und Footer-Strukturen
- Referenz für bestehende CSS-/JS-Muster und vorhandene Klassenlogik
- Referenz für bestehende Navigations- und Linkmuster

Nicht verbindlich:

- `index.html` ist **nicht** die finale Startseitenstruktur.
- Alte Startseiten-Sections, alte Trust-Elemente, alte Texte und alte CTA-Anker aus `index.html` dürfen nicht automatisch übernommen werden.
- Bei Konflikt gilt diese Brief-Datei, nicht der alte `index.html`-Stand.

Verbindlich aus `index.html` nur als Referenz:

- Header-/Sidebar-/Footer-Mechanik darf technisch wiederverwendet werden.
- Bestehende Klassen, IDs und Layoutlogik dürfen als technische Basis dienen, sofern sie der Brief-Vorgabe nicht widersprechen.
- Inline-CSS darf technisch ausgelagert werden, aber ohne freie Designänderung.
- Links, die auf nicht vorhandene Zielseiten zeigen, als Zielpfade markieren und nicht frei neu benennen.

### `analyse.html`

Verwendung:

- aktuelle Seite für die KI-Potenzialanalyse
- aktuelle Formularstruktur
- aktuelle Pflichtfelder und optionale Felder
- aktuelle Datenschutz-/Einwilligungslogik
- aktueller API-Flow für Analyse, Antworten, Score, Report und Lead-Erfassung
- aktuelle Success-/Error-Ausgabe auf der Seite

Verbindlich:

- Formular in `analyse.html`logik aus `analyse.html` übernehmen.
- API-Endpunkte nicht ohne Freigabe ändern.
- Pflichtfelder nicht entfernen.
- Datenschutz-/Einwilligungshinweis nicht entfernen.
- Honeypot-Feld nicht entfernen.
- Success-/Error-Zustände technisch prüfen.

### Umgang mit Bestandscode

Der Programmierer darf den Bestand technisch bereinigen, bündeln oder in separate Dateien auslagern, zum Beispiel:

- CSS aus Inline-Styles in eine CSS-Datei verschieben
- JavaScript aus Inline-Scripts in eine JS-Datei verschieben
- wiederkehrende Header-/Footer-Strukturen zentralisieren

Dabei gilt:

- keine Layoutänderung ohne Freigabe
- keine Textkürzung ohne Freigabe
- keine neue Navigationslogik ohne Freigabe
- keine neuen Formularfelder in `analyse.html` ohne Freigabe ohne Freigabe
- keine Farbstiländerung ohne Freigabe

### Bekannte Bestandscode-Hinweise

- `shared-header-footer.css` liegt vor und ist als gemeinsame Header-/Footer-/Sidebar-CSS-Referenz zu verwenden.
- Beide HTML-Dateien verwenden Assetpfade unter `assets/...`. Diese Pfade müssen im realen Projektordner geprüft werden; die Assetliste ist nur Referenz, weil sie nicht aktuell ist.
- Mehrere Detailseiten-Links sind im Bestand bereits angelegt, die Detailseiten selbst sind aber nicht Bestandteil dieser Startseiten-Umsetzung, sofern sie nicht separat beauftragt werden.
- Impressum, Datenschutz, AGB, Cookie-Hinweis, Analyse-Hinweise und Praxisleitfaden liegen als HTML-Zielseiten vor.

---

## 0.12 Assetliste – Verwendung

Datei: `asset_liste_v34.md`

Die separate Assetliste ist Bestandteil der Übergabe, aber **nicht aktuell**. Sie wird deshalb ab diesem Stand **nicht mehr als kritischer Blocker** bewertet.

Verwendung:

- Referenz für bekannte Assetpfade
- Referenz für Hero-, Grid-, Prozess-, Card-, Icon- und Detailseitenpfade
- Orientierung für vorhandene Ordnerlogik

Regel:

- Assetliste nicht als vollständig final behandeln.
- Assetpfade gegen den echten Website-Projektordner prüfen.
- Fehlende Assets als fehlend markieren, nicht frei neu erfinden.
- Keine neue Asset-Systematik ohne Freigabe anlegen.
- Die HTML-Umsetzung darf wegen nicht aktueller Assetliste nicht pauschal als blockiert bewertet werden.

---

## 0.13 Workflow-Modultabelle – Verwendung

Datei: `workflow_module_table.xlsx`

Die separate Workflow-Modultabelle ist Bestandteil der Übergabe, aber **nicht aktuell**. Sie wird deshalb ab diesem Stand **nicht mehr als kritischer Blocker** bewertet.

Verwendung:

- Referenz für vorhandene Workflow-/Modul-Ideen
- Referenz für Modulnamen und spätere Zuordnung
- Orientierung für spätere Workflow-Darstellungen

Regel:

- Modultabelle nicht in den Brief kopieren.
- Tabelle als Referenzanlage mitgeben.
- Keine Module erfinden.
- Keine Modulbilder austauschen, wenn später ein geprüftes Bild vorhanden ist.
- Die HTML-Umsetzung darf wegen nicht aktueller Modultabelle nicht pauschal als blockiert bewertet werden.

---

## 0.14 Definition of Done für diese Übergabe

Die Startseite gilt als umgesetzt, wenn:

- alle Sections 1–9 vorhanden sind
- Header, Sidebar, Footer übernommen sind
- alle CTAs korrekt verlinken
- Downloadbereich vorhanden ist
- kein zusätzlicher Startseiten-Kontaktbereich gebaut wird und alle Potenzialanalyse-CTAs auf `analyse.html` zeigen
- Success-/Error-Zustand in `analyse.html` vorhanden ist
- Leistungs-Cards auf Desktop per Hover funktionieren
- Leistungs-Cards auf Mobile per Tap funktionieren
- SEO-/OG-Daten gesetzt sind
- Impressum und Datenschutz erreichbar sind
- Desktop, Tablet und Mobile geprüft sind
- keine Platzhaltertexte mehr sichtbar sind
- keine nicht freigegebenen Assets als finale Assets verwendet werden

---

## 0.15 Übergabeprüfung 2026-06-30

Geprüfter Übergabeumfang laut Vorgabe:

1. Haupt-Brief: `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`
2. Assetliste: `asset_liste_v34.md` – vorhanden, aber nicht aktuell; Referenzanlage, kein kritischer Blocker
3. Modultabelle: `workflow_module_table.xlsx` – vorhanden, aber nicht aktuell; Referenzanlage, kein kritischer Blocker

Zusätzlich vorhandene technische Quellen/Zielseiten:

- `index.html` – alter Startseitenstand / technische Referenz, nicht finale Zielstruktur
- `analyse.html` – aktuelle Analyse-Seite/Formularbasis
- `shared-header-footer.css` – gemeinsame Header-/Footer-/Sidebar-CSS-Referenz
- `impressum.html`
- `datenschutz.html`
- `agb.html`
- `cookie-hinweis.html`
- `analyse-rechtliche-hinweise.html`
- `praxisleitfaden.html`

Diese Dateien sind keine neue Konzeptübergabe und ersetzen nicht die 3-teilige Übergabestruktur. Sie klären aber bisher offene Bestandspunkte.

### Prüfergebnis

| Bereich | Ergebnis | Konsequenz |
|---|---|---|
| Haupt-Brief | vorhanden und konsolidiert | dient als zentrale Arbeitsanweisung |
| `index.html` | vorhanden und lesbar | alter technischer Referenzstand; nicht als finale Startseitenstruktur übernehmen |
| `analyse.html` | vorhanden und lesbar | aktuelle Analyse-Seite/Formularbasis mit Formularstruktur, API-Flow, Success-/Error-Zuständen |
| `asset_liste_v34.md` | vorhanden | nicht aktuell; Referenz für Pfade, aber kein kritischer Blocker |
| `workflow_module_table.xlsx` | vorhanden | nicht aktuell; Referenz für Module, aber kein kritischer Blocker |
| `shared-header-footer.css` | vorhanden | gemeinsame CSS-Referenz für Header, Footer, Sidebar, Responsive-Verhalten |
| Impressum / Datenschutz / AGB / Cookie / Analyse-Hinweise | vorhanden | Zielseiten sind vorhanden, Inhalte vor Veröffentlichung juristisch prüfen |
| Praxisleitfaden | vorhanden | Zielseite vorhanden; finaler Downloadinhalt/Datei kann später ergänzt werden |
| Assetpfade im HTML | aus HTML/Assetliste ersichtlich | gegen echten Projektordner prüfen; fehlende Assets nicht frei erfinden |

### Verbindlicher Status nach Ergänzung

Diese Datei ist weiterhin die eine Haupt-Brief-Datei. Die Übergabe bleibt strukturell:

1. `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`
2. `asset_liste_v34.md` als Referenzanlage
3. `workflow_module_table.xlsx` als Referenzanlage

Der alte `index.html`-Stand ist nur technische Referenz. `analyse.html`, die Rechtsseiten, `praxisleitfaden.html` und `shared-header-footer.css` liegen vor. Assetliste und Modultabelle sind nicht aktuell und blockieren die Übergabe nicht mehr als kritische Punkte.

---

## 0.16 Prüfbefund: verbleibende Entscheidungen nach Korrektur

Nach Korrektur gilt: Abweichungen aus `index.html` sind primär Altbestand und nicht automatisch Ziel-Widerspruch. Der Programmierer darf alte Inhalte aus `index.html` nicht als Freigabe interpretieren.

| Bereich | Status | Konsequenz |
|---|---|---|
| `index.html` | alter Stand | nur technische Referenz; alte Trust-Section, 35+ Jahre Aussage und alte Startseitenstruktur nicht automatisch übernehmen |
| `analyse.html` | vorhanden / aktuelle Analyse-Seite | Formular, API-Flow, Success-/Error-Logik als Grundlage verwenden |
| CTA-Ziel | final festgelegt | alle Potenzialanalyse-CTAs führen zu `analyse.html`; kein zusätzlicher `analyse.html`-Bereich auf der Startseite |
| Assetliste | vorhanden, aber nicht aktuell | Referenz, kein kritischer Blocker; echte Assets im Projektordner prüfen |
| Modultabelle | vorhanden, aber nicht aktuell | Referenz, kein kritischer Blocker; konkrete Workflow-Zuordnung später prüfen |
| Rechtsseiten | vorhanden | vor Veröffentlichung juristisch prüfen lassen |

### Aktueller Freigabestatus

Nicht mehr kritisch:

- fehlende Assetliste
- fehlende Modultabelle
- fehlende `shared-header-footer.css`
- fehlendes Impressum
- fehlender Datenschutz
- fehlender Praxisleitfaden
- fehlende rechtliche Zusatzseiten

Noch zu entscheiden:

1. Kein offener CTA-Blocker mehr: Potenzialanalyse-CTAs führen final zu `analyse.html`.
2. Kein zusätzlicher Kontakt-/Formularanker auf der Startseite.
3. Ob die Rechtsseiten inhaltlich vor Veröffentlichung juristisch geprüft werden müssen.
4. Welche im realen Projektordner fehlenden Assets nachgeliefert oder ersetzt werden.

---

## 1. Projektziel

Nurovelle wird als technische B2B-Homepage für individuelle KI-Lösungen positioniert.

Die Startseite soll klar erklären:

- was Nurovelle anbietet
- für wen das Angebot geeignet ist
- wie Besucher ohne konkrete KI-Idee starten
- wie Besucher mit konkreter Projektidee starten
- welche Leistungen angeboten werden
- wie aus einem Geschäftsprozess eine KI-Lösung wird
- warum Nurovelle glaubwürdig ist
- welche Downloads verfügbar sind
- wie Besucher Kontakt aufnehmen oder die KI-Potenzialanalyse starten

Hauptziel der Startseite:

- Besucher zur KI-Potenzialanalyse, zum Erstgespräch oder zur Projektidee-Prüfung führen.

---

## 2. Verbindliche Designregeln

### Stil

- dunkler technischer Premium-Look
- schwarze / dunkelgrüne / petrolfarbene Flächen nach bestehender Designlogik
- Gold mit Verlauf für Akzente, Rahmen, CTA, aktive Zustände
- kein Bronze
- kein Kupfer
- keine blauen Hauptfarben
- keine violetten Hauptakzente
- keine generischen KI-Roboter
- keine Stockfoto-Optik
- keine überladenen Dashboard-Szenen

### Schriften

- Bebas Neue: große Titel, Hero, Section-Titel
- Anca Coder / Coder Pro: technische Labels, kleine Akzente, Zahlen
- Raleway / Roboto: Fließtext, Navigation, normale UI-Texte

### Inhaltsregeln

- keine Trust-Section
- keine Trust-Elemente im Hero
- keine Faktenbox in „Warum Nurovelle“
- keine langen Texte auf Leistungs-Cards
- Leistungs-Cards nur mit Stichpunkten / Bulletpoints
- Texte in Grafiken nach Möglichkeit per HTML/CSS setzen
- Header, Footer, Seitenleiste und Formular werden 1:1 aus der aktuellen/alten Homepage übernommen

---

## 3. Finale Seitenstruktur

1. Hero
2. Der erste Schritt zu Ihrem KI-Projekt
3. Kostenlose KI-Potenzialanalyse
4. Sie haben bereits eine konkrete KI-Idee?
5. KI-Leistungen von Nurovelle
6. Vom Geschäftsprozess zur KI-Lösung
7. Warum Nurovelle
8. Download-Bereich
9. Analyse-Seite / Formularweiterleitung
10. Success-/Error-Zustand in `analyse.html`

Bestandsbereiche:

- Header: 1:1 übernehmen
- Footer: 1:1 übernehmen
- Seitenleiste: 1:1 übernehmen
- Analyse-/Formularflow: aus `analyse.html` übernehmen; auf Startseite kein zusätzlicher Formularbereich

---

## 4. CTA- und Linklogik

### Anfrage-CTAs

Alle Potenzialanalyse-, Anfrage- und Erstgespräch-CTAs führen final zu `analyse.html`. Es gibt keinen zusätzlichen `analyse.html`-Formularbereich auf der Startseite.

- Kostenloses Erstgespräch vereinbaren → `analyse.html`
- KI-Potenzialanalyse durchführen → `analyse.html`
- Projektidee prüfen lassen → `analyse.html`
- Section 6 CTA „KI-Potenzialanalyse durchführen“ → `analyse.html`

### Download-CTAs

Download-CTAs führen direkt zum Downloadbereich oder zur Praxisleitfaden-Seite.

- Praxisleitfaden / Downloads → `#downloads`

### Nicht verwenden

- kein eigener Roadmap-CTA
- kein CTA „Nächsten Umsetzungsschritt planen“
- kein zusätzlicher Formularaufbau auf der Startseite
- kein zusätzlicher Kontakt-/Formularbereich auf der Startseite

---

## 5. Section 1 – Hero

### H1

```text
KI-Agenten für echte Geschäftsprozesse.
```

### Subline

```text
Nurovelle entwickelt individuelle KI-Systeme für Datenverarbeitung, Wissenszugriff, Prozessautomatisierung und Unternehmenssoftware.
```

### Zusatzzeile

```text
Von der Potenzialanalyse über Prompt Engineering und MCP bis zur Umsetzung maßgeschneiderter KI-Lösungen.
```

### CTAs

- Kostenloses Erstgespräch vereinbaren → `analyse.html`
- KI-Potenzialanalyse durchführen → `analyse.html`

### Hero-Regeln

- keine Trust-Elemente
- keine Badge-Leiste
- keine zusätzlichen Fakten
- Hero-Text nicht mehr ändern

---

## 6. Section 2 – Der erste Schritt zu Ihrem KI-Projekt

### Titel

```text
Der erste Schritt zu Ihrem KI-Projekt
```

### Text

```text
Ein KI-Projekt beginnt nicht mit der Auswahl eines Tools. Es beginnt mit der Frage, welcher Prozess verbessert, welche Daten nutzbar gemacht und welches Ergebnis erreicht werden soll.

Nurovelle prüft, wo KI-Agenten, Automatisierung, Wissenssysteme oder individuelle Software tatsächlich Mehrwert schaffen. Dabei geht es nicht um allgemeine KI-Ideen, sondern um konkrete Geschäftsprozesse, technische Machbarkeit und eine realistische Umsetzung.

So entsteht aus einer ersten Idee ein belastbarer nächster Schritt: vom Erstgespräch über die Potenzialanalyse bis zur Entwicklung eines Prototyps oder einer fertigen Lösung.
```

### CTA

- Kostenloses Erstgespräch vereinbaren → `analyse.html`

### Layout

- links: drei bestehende schwarze Glaskarten horizontal
- rechts: Textblock
- Cards-Reihenfolge: 2, 1, 3
- grüner Rahmen stärker
- goldener Bodenschatten unter den Cards
- kein Goldrahmen um Cards
- keine neue Bildgenerierung
- Card-Texte später per CSS/HTML, nicht fest im Bild

---

## 7. Section 3 – Kostenlose KI-Potenzialanalyse

### Titel

```text
Kostenlose KI-Potenzialanalyse
```

### Text

```text
Finden Sie heraus, wo KI in Ihrem Unternehmen sinnvoll ansetzen kann.

Nurovelle analysiert, welche Abläufe, Daten, Dokumente oder Wissensquellen sich für KI-Agenten, Automatisierung, Chatbots oder individuelle Softwarelösungen eignen. Dabei geht es nicht um theoretische Möglichkeiten, sondern um konkrete Einsatzbereiche mit erkennbarem Nutzen.

Sie erhalten eine Einschätzung, welche Potenziale vorhanden sind, welche Voraussetzungen bestehen und welcher nächste Schritt für Ihr Unternehmen sinnvoll ist.

Bei erkennbarem Potenzial kann daraus im nächsten Schritt eine vertiefende Analyse, eine technische Roadmap, ein Prototyp oder die direkte Umsetzung entstehen.
```

### CTA

- KI-Potenzialanalyse durchführen → `analyse.html`

### Regel

- keine eigene bezahlte Potenzialanalyse-Section auf der Startseite
- vertiefende Analyse nur dezent erwähnen
- spätere Angebotsseite möglich

---

## 8. Section 4 – Sie haben bereits eine konkrete KI-Idee?

### Titel

```text
Sie haben bereits eine konkrete KI-Idee?
```

### Text

```text
Wenn Sie bereits wissen, welcher Prozess verbessert, welche Datenquelle nutzbar gemacht oder welche interne Aufgabe unterstützt werden soll, ist der nächste Schritt keine allgemeine Orientierung.

Nurovelle prüft mit Ihnen, ob die Idee technisch realistisch ist, welche Systeme, Daten oder Schnittstellen benötigt werden und welcher Umsetzungsweg sinnvoll ist.

So wird aus einer ersten Idee ein konkreter Projektansatz für KI-Agenten, Automatisierung, Datenverarbeitung oder individuelle Software.
```

### CTA

- Projektidee prüfen lassen → `analyse.html`

---

## 9. Section 5 – KI-Leistungen von Nurovelle

### Section-Titel

```text
KI-Leistungen von Nurovelle
```

### Funktionsregel

Normalzustand:

- Icon
- Überschrift

Hover/Tap-Zustand:

- Bausteine
- Anwendungen
- Kostenfaktor / Nutzen

Desktop:

- Hover öffnet vollständige Card.

Mobile:

- Tap öffnet vollständige Card.
- zweiter Tap oder Tap auf andere Card schließt vorherige Card.

### Asset-Schema

Haupticons:

- `service_01.svg` bis `service_11.svg`

Nutzen-Line-Icons:

- `benefit_01.svg` bis `benefit_11.svg`

Empfohlene Haupticon-Dateinamen:

- `service_01_potenzialanalyse.svg`
- `service_02_beratung_roadmap.svg`
- `service_03_ki_agenten.svg`
- `service_04_chatbots.svg`
- `service_05_sprachassistenten.svg`
- `service_06_prompt_engineering.svg`
- `service_07_sicherheit_governance.svg`
- `service_08_automatisierung_workflows.svg`
- `service_09_dokumente_daten_abgleich.svg`
- `service_10_ki_software_integration.svg`
- `service_11_seo_sichtbarkeit.svg`

Empfohlene Nutzenicon-Dateinamen:

- `benefit_01_klarheit.svg`
- `benefit_02_plan.svg`
- `benefit_03_entlastung.svg`
- `benefit_04_antworten.svg`
- `benefit_05_dialog.svg`
- `benefit_06_qualitaet.svg`
- `benefit_07_kontrolle.svg`
- `benefit_08_ablauf.svg`
- `benefit_09_datenqualitaet.svg`
- `benefit_10_integration.svg`
- `benefit_11_sichtbarkeit.svg`

---

### 01 — KI-Potenzialanalyse

Bausteine:

- Prozessprüfung
- Datenlage
- Aufgabenanalyse
- KI-Eignung
- nächster Schritt

Anwendungen:

- unklare KI-Einstiege
- manuelle Abläufe
- wiederkehrende Aufgaben
- Daten- und Dokumentenprozesse
- Automatisierungsideen

Kostenfaktor / Nutzen:

- klare Prioritäten
- weniger Fehlentscheidungen
- bessere Investitionsgrundlage

---

### 02 — KI-Beratung & KI-Roadmap

Bausteine:

- Use-Case-Bewertung
- Priorisierung
- Umsetzungsplan
- Technologieauswahl
- Roadmap

Anwendungen:

- KI-Strategie
- Projektplanung
- Entscheidungsgrundlagen
- Technologieauswahl
- Umsetzungsreihenfolge

Kostenfaktor / Nutzen:

- weniger Aktionismus
- klarere Budgetplanung
- strukturierter Projektstart

---

### 03 — KI-Agenten

Bausteine:

- Agentenlogik
- Tool-Anbindung
- MCP
- API-Zugriff
- Aufgabensteuerung

Anwendungen:

- interne Assistenz
- Recherche
- Aufgabenweitergabe
- Prozessunterstützung
- Systemzugriffe

Kostenfaktor / Nutzen:

- weniger Vorarbeit
- weniger Suchaufwand
- weniger manuelle Übergaben

---

### 04 — Chatbots

Bausteine:

- Dialoglogik
- Antwortsteuerung
- Datenanbindung
- Prompt-Struktur
- Qualitätsregeln

Anwendungen:

- Kundenfragen
- interne Rückfragen
- Servicefälle
- FAQ-Bereiche
- Mitarbeiterassistenz

Kostenfaktor / Nutzen:

- schnellere Antworten
- weniger Standardanfragen
- geringerer Supportaufwand

---

### 05 — Sprachassistenten

Bausteine:

- Spracheingabe
- Sprachausgabe
- Dialogführung
- Systemanbindung
- Assistenzlogik

Anwendungen:

- telefonische Anfragen
- mobile Nutzung
- interne Assistenz
- Serviceprozesse
- sprachbasierte Erfassung

Kostenfaktor / Nutzen:

- weniger Bedienaufwand
- schnellere Erfassung
- bessere Erreichbarkeit

---

### 06 — Prompt Engineering

Bausteine:

- Prompt-Standards
- Rollenlogik
- Ausgabeformate
- Qualitätsprüfung
- Vorlagen

Anwendungen:

- wiederkehrende KI-Aufgaben
- Textprozesse
- Analyseprozesse
- interne Vorlagen
- Assistenzsysteme

Kostenfaktor / Nutzen:

- weniger Nacharbeit
- bessere Ergebnisqualität
- einheitliche KI-Ausgaben

---

### 07 — KI-Sicherheit & Governance

Bausteine:

- Zugriffsrechte
- Rollenmodelle
- Datenfreigaben
- Prüflogik
- Qualitätskontrolle

Anwendungen:

- interne KI-Nutzung
- sensible Dokumente
- Systemzugriffe
- Freigabeprozesse
- KI-Agenten mit Datenzugriff

Kostenfaktor / Nutzen:

- weniger Risiko
- mehr Kontrolle
- klare Verantwortlichkeiten

---

### 08 — KI-Automatisierung & Workflows

Bausteine:

- Workflow-Logik
- Aufgabenketten
- Freigaben
- Statusmeldungen
- Reporting

Anwendungen:

- wiederkehrende Abläufe
- Freigabeprozesse
- Statusberichte
- Aufgabensteuerung
- operative Abstimmung

Kostenfaktor / Nutzen:

- weniger Abstimmung
- kürzere Durchlaufzeiten
- bessere Prozessübersicht

---

### 09 — Dokumente, Daten & Abgleich

Bausteine:

- Datenaufbereitung
- Datenabgleich
- Dokumentenprüfung
- Eingabemasken
- Anonymisierung

Anwendungen:

- Tabellen
- Listen
- Formular in `analyse.html`e
- Stammdaten
- Richtlinien / Verfahrensanweisungen

Kostenfaktor / Nutzen:

- weniger Prüfaufwand
- weniger Doppelarbeit
- bessere Datenqualität

---

### 10 — Individuelle KI-Software & Integration

Bausteine:

- interne Tools
- Dashboards
- Prototypen / MVPs
- API-Anbindungen
- MCP / Azure / Low-Code

Anwendungen:

- eigene Anwendungen
- Systemintegration
- interne Workflows
- Schnittstellen
- spezielle Unternehmensprozesse

Kostenfaktor / Nutzen:

- weniger Tool-Brüche
- bessere Systemverbindung
- passgenaue Umsetzung

---

### 11 — SEO & Sichtbarkeit

Bausteine:

- Keyword-Recherche
- Content-Struktur
- technische SEO-Prüfung
- OnPage-Optimierung
- interne Verlinkung

Anwendungen:

- Website-Sichtbarkeit
- Leistungs-Detailseiten
- Download-Seiten
- Ratgeber-Struktur
- lokale Suchanfragen

Kostenfaktor / Nutzen:

- bessere Auffindbarkeit
- weniger Anzeigenabhängigkeit
- qualifiziertere Anfragen

---

## 10. Section 6 – Vom Geschäftsprozess zur KI-Lösung

### Titel

```text
Vom Geschäftsprozess zur KI-Lösung
```

### Text

```text
Nicht jede Aufgabe braucht einen KI-Agenten. Manchmal ist ein Chatbot sinnvoll, manchmal ein Datenabgleich, eine Eingabemaske, ein Workflow oder eine individuelle Softwarelösung.

Deshalb beginnt die Roadmap mit der Geschäftsaufgabe: Was soll einfacher, schneller, prüfbarer oder besser steuerbar werden? Danach werden KI-Eignung, Datenlage, Prozesslogik und technische Voraussetzungen bewertet.

Das Ergebnis ist ein klarer Umsetzungsplan: welche Lösung sinnvoll ist, was dafür benötigt wird und welcher erste Baustein den größten Nutzen bringt.
```

### CTA

- KI-Potenzialanalyse durchführen → `analyse.html`

### Roadmap-Grafik

Die bestehende Grafik „So läuft die Zusammenarbeit“ wird wiederverwendet.

Keine neue Grafik erstellen.

Sechs Stationen:

1. Geschäftsaufgabe bestimmen
2. KI-Eignung prüfen
3. Datenlage bewerten
4. Prozesslogik klären
5. Lösungstyp festlegen
6. Umsetzung planen

Regel:

- kein eigener Roadmap-CTA
- CTA verweist auf Potenzialanalyse

---

## 11. Section 7 – Warum Nurovelle

### Titel

```text
Warum Nurovelle
```

### Text

```text
Nurovelle verbindet technisches Prozessverständnis mit praktischer Softwareentwicklung und moderner KI-Umsetzung.

Die technische Prägung begann früh – mit ersten eigenen Codezeilen auf dem C64. Beruflich liegt der Schwerpunkt seit 2013 in der Entwicklung digitaler Lösungen, ergänzt durch Agentur- und Kundenprojekte seit 2015.

Dadurch entstehen keine isolierten KI-Tools, sondern Lösungen, die zu realen Geschäftsprozessen passen: verständlich geplant, technisch sauber aufgebaut und auf konkrete Umsetzung ausgerichtet.
```

### Regeln

- keine separate Trust-Section
- keine Faktenbox
- keine Aussage „35 Jahre Programmiererfahrung“
- keine konfliktbehafteten biografischen Details
- Portrait oder technisches Visual optional als Mischsektion

---

## 12. Section 8 – Download-Bereich

### ID

`#downloads`

### Inhalte

- Praxisleitfaden
- Whitepaper
- Miniguides
- Checklisten

### Darstellungsregel

- kurze Titel
- kurze Bulletpoints
- Mockup / Vorschaubild je Asset
- Download-CTA je Asset
- keine langen Beschreibungstexte

### Nicht jetzt

- keine Download-Detailseiten
- keine Ratgeberstruktur
- keine Blog-Struktur
- keine langen SEO-Texte

Diese Punkte kommen später mit dem Detailseiten-/SEO-Projekt.

---

## 13. Analyse-/Formularlogik

### ID

`analyse.html`

### Regel

- keine Formular-/Kontaktsektion auf der Startseite übernehmen oder neu bauen; `analyse.html` ist Zielseite und Formularbasis
- keine neuen Formularfelder in `analyse.html` ohne Freigabe
- keine neue Formularstruktur in `analyse.html` ohne Freigabe
- keine neue Inhaltsplanung

Technisch nur:

- übernehmen
- responsive prüfen
- Funktion testen

---

## 14. Success-/Error-Zustand

Finale Entscheidung:

- Es wird keine separate `danke.html` erstellt.
- Nach dem Absenden der Potenzialanalyse bleibt der Nutzer auf `analyse.html`.
- `analyse.html` zeigt den vorhandenen Success-/Error-Zustand.
- Der vorhandene Analyse-Flow aus `analyse.html` bleibt Grundlage für Formular, API-Flow, Ergebnislink, Fehlermeldung und Statusausgabe.
- Keine neue Danke-Seite, keine zusätzliche Success-Seite und kein zusätzlicher Startseiten-Formularbereich.

Der Programmierer prüft nur:

- ob der Success-Zustand in `analyse.html` sichtbar und verständlich ist,
- ob der Error-Zustand in `analyse.html` sichtbar und verständlich ist,
- ob Pflichtfelder, Honeypot, API-Timeout und Statusmeldungen technisch funktionieren,
- ob Datenschutzlink und rechtliche Hinweise erreichbar sind.

---

## 15. SEO Startseite

### Meta Title

```text
Nurovelle | KI-Agenten, Automatisierung & KI-Potenzialanalyse
```

### Meta Description

```text
Nurovelle entwickelt KI-Agenten, Chatbots, Sprachassistenten, Automatisierung und individuelle KI-Software für reale Geschäftsprozesse. Jetzt KI-Potenzialanalyse durchführen.
```

### H1

```text
KI-Agenten für echte Geschäftsprozesse.
```

### Primäre Keywords

- KI-Agenten
- KI-Automatisierung
- KI-Potenzialanalyse
- KI-Beratung
- individuelle KI-Software

### Sekundäre Keywords

- Chatbots
- Sprachassistenten
- Prompt Engineering
- Prozessautomatisierung
- Datenverarbeitung
- Dokumentenautomatisierung
- KI-Sicherheit
- SEO & Sichtbarkeit

### Detailseiten-SEO

Nicht jetzt ausarbeiten.

Detailseiten sind ein eigener großer Block und werden später beim Aufbau der Detailseiten bearbeitet.

Vorgesehene spätere Detailseiten:

- `/ki-potenzialanalyse`
- `/ki-beratung-roadmap`
- `/ki-agenten`
- `/chatbots`
- `/sprachassistenten`
- `/prompt-engineering`
- `/ki-sicherheit-governance`
- `/ki-automatisierung-workflows`
- `/dokumente-daten-abgleich`
- `/ki-software-integration`
- `/seo-sichtbarkeit`

---

## 16. Open Graph / Social Preview

### OG Title

```text
Nurovelle | KI-Agenten für echte Geschäftsprozesse
```

### OG Description

```text
KI-Potenzialanalyse, KI-Agenten, Automatisierung, Chatbots, Sprachassistenten, SEO und individuelle KI-Software für Unternehmen.
```

### OG Image

```text
og-nurovelle-homepage.jpg
```

### LinkedIn-Vorschautext

```text
Nurovelle entwickelt KI-Agenten, Automatisierung und individuelle KI-Software für reale Geschäftsprozesse – inklusive Potenzialanalyse, Beratung, Umsetzung und SEO-Sichtbarkeit.
```

Regel:

- keine zusätzliche Social-Section
- kein neuer Homepage-Block
- nur Metadaten + Vorschaubild technisch setzen

---

## 17. Responsive- und Funktionsprüfung

### Desktop

- Header korrekt
- Sidebar korrekt
- Hero sichtbar
- Leistungs-Cards nicht überladen
- Downloads erreichbar
- Formular in `analyse.html`bereich 1:1 übernommen
- Hover-Cards funktionieren

### Tablet

- Section-Abstände sauber
- Leistungs-Cards lesbar
- Hover/Tap-Logik verständlich
- keine abgeschnittenen Inhalte

### Smartphone

- Sidebar-Verhalten prüfen
- Cards per Tap öffnen
- CTA-Buttons gut erreichbar
- Formular in `analyse.html` vollständig nutzbar
- Downloadbereich nicht zu lang

### Funktionstest

- Anfrage-CTAs führen zu `analyse.html`
- Download-CTAs führen zu `#downloads` oder `praxisleitfaden.html`
- Section 6 CTA führt zu `analyse.html`
- Formular in `analyse.html` funktioniert
- Success-/Error-Zustand in `analyse.html` funktioniert
- Impressum erreichbar
- Datenschutz erreichbar
- Downloads funktionieren

---

## 18. Nicht ändern / nicht neu bauen

- Header nicht neu konzipieren
- Footer nicht neu konzipieren
- Seitenleiste nicht neu konzipieren
- Formular in `analyse.html` nicht neu konzipieren
- keine Trust-Section hinzufügen
- keine Faktenbox in Warum Nurovelle hinzufügen
- keine neuen Formularfelder in `analyse.html` ohne Freigabe
- keine Blog-Struktur im Launch
- keine Detailseiten jetzt ausarbeiten
- keine Roadmap-CTA als eigenen Einstieg
- keine 10 Leistungs-Cards; final sind 11 Cards
- keine langen Texte auf Leistungs-Cards
- keine KI-generierten Neuinterpretationen bestehender Assets

---

## 19. Umsetzungsschritte

1. Bestandsbereiche übernehmen
   - Header 1:1
   - Footer 1:1
   - Seitenleiste 1:1
   - Analyse-/Formularlogik aus `analyse.html`

2. Assets einbinden
   - service_01 bis service_11
   - benefit_01 bis benefit_11
   - Download-Mockups / Vorschaubilder
   - og-nurovelle-homepage.jpg

3. Startseiten-Sections umsetzen
   - Hero
   - Section 2 bis 7
   - Download-Bereich
   - Analyse-/Formularlogik aus `analyse.html` als Bestandsübernahme

4. Interaktionen umsetzen
   - Leistungs-Cards Desktop: Hover
   - Leistungs-Cards Mobile: Tap
   - Anfrage-CTAs → `analyse.html`
   - Download-CTAs → `#downloads` oder `praxisleitfaden.html`
   - Section 6 CTA → KI-Potenzialanalyse

5. Tests
   - Desktop
   - Tablet
   - Smartphone
   - Links
   - Downloads
   - Formular in `analyse.html`
   - Success-/Error-Zustand in `analyse.html`
   - Impressum / Datenschutz

---

## 20. Offene Punkte nach Startseiten-Brief

Nur noch diese Punkte sind später offen:

- Asset-Liste final mit echten Dateinamen abgleichen
- technische Einbindung
- responsive Prüfung
- Funktionsprüfung
- später: Detailseiten / SEO-Seiten als eigenes größeres Projekt


## Designentscheidung – Alternativer Gold-Textverlauf

Zusätzlich zu den bestehenden Goldverläufen wird folgender Verlauf als alternative Text-Variante aufgenommen.

**Alternative für Titel/Text-Highlights:**
- Dark Tone: `#C5A059` (Muted Bronze)
- Bright Accent: `#FDF0CD` (Warm Champagne)
- Mid Tone: `#D4AF37` (Metallic Gold)

```css
h1, h2 {
  background: linear-gradient(135deg, #C5A059 0%, #FDF0CD 50%, #D4AF37 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}
```

**Verwendung:** Alternative für Titel oder hochwertige Text-Highlights, wenn Verlauf 2 zu kräftig wirkt.



## Content-Dokumente – Typografie- und Farbsystem

Diese Regeln gelten für Content-Dokumente, Guides, PDFs, Arbeitsdokumente und Download-Dokumente. Website-Gradienten gelten nicht automatisch für Content-Dokumente.

| Elementtyp | Schrift | Stil / Gewicht | Farbe / Mapping |
|---|---|---|---|
| Title / H1 | Bebas Neue | Bold, All Caps, ca. 26 pt | Gold Gradient / Fallback Gold `#D4AF37` |
| Section Header / H2 | Plus Jakarta Sans | Semi-Bold, ca. 18 pt | Deep Emerald Green `#112A20` |
| Sub-Header / H3 | Plus Jakarta Sans | Medium, ca. 14 pt | Muted Matte Gold `#B38F4D` |
| Small Header / H4 | Plus Jakarta Sans | Bold, All Caps, ca. 10.5 pt | Deep Emerald Green `#112A20` |
| Column Header | Inter | Bold, All Caps, ca. 10 pt | White Text `#FFFFFF` auf Emerald Block `#112A20` |
| Text / Body | Inter | Regular, 10.5 pt, Line Space 1.4 | Dark Charcoal `#2A2A2A` |
| Bulletpoint-Header | Plus Jakarta Sans | Semi-Bold, 12 pt | Deep Emerald Green `#112A20` |
| Bulletpoints / Lists | Inter | Regular, 10.5 pt | Text: Charcoal `#2A2A2A`; Bullet Dot: Emerald |
| Numbering / # | Inter | Regular, 10.5 pt | Text: Charcoal `#2A2A2A`; Numbers: Matte Gold |
| Hervorhebung Normal | Inter | Italic / Medium, 10.5 pt | Deep Emerald Green `#112A20` |
| Hervorhebung Extrem | Inter | Extra-Bold, 10.5 pt | Dark Bronze-Gold `#A37A3E` |

### Verbindliche Dokument-Regeln

- H1 nutzt Bebas Neue in Versalien.
- H2, H3, H4 und Bulletpoint-Header nutzen Plus Jakarta Sans.
- Fließtext, Listen, Nummerierungen und Hervorhebungen nutzen Inter.
- Farbverläufe werden in Content-Dokumenten nur für H1 beziehungsweise Titel eingesetzt.
- H2 und H4 bleiben Deep Emerald `#112A20`.
- H3 bleibt Matte Gold `#B38F4D`.
- Fließtext bleibt Dark Charcoal `#2A2A2A`.

---

## 21. Nachtrag 2026-06-30 – Aktueller Asset-Status

### Hero-Formen

Die Hero-Formen sind nicht final abgeschlossen.

Falls weiter daran gearbeitet wird:

- keine neue Designsprache
- keine frei erfundenen Formen
- nur vorhandene Formen aus der freigegebenen Übersicht
- eine Form je Datei in hoher Auflösung
- freischwebend
- keine Plattform, kein Sockel, keine Bodenplatte
- technische Nodes und Linien im Raum um das Objekt
- dezentes Smaragdgrün ergänzen
- Gold nur als Eck-/Knotenhighlight

### 3D-Icons

Es liegen 3D-Icon-Formen vor, aber noch kein final geprüfter Nurovelle-Farbtest.

Nächster Schritt:

- ein Icon als Farbtest in Photoshop CS6 umfärben
- keine Stiländerung
- keine Veredelung
- keine Serienentscheidung vor Prüfung

### Asset-Liste

Die Assetliste bleibt als separate Referenzanlage Bestandteil der Übergabe. Sie wird nicht vollständig in diese Hauptdatei kopiert. Sie ist nicht aktuell und deshalb kein kritischer Blocker; Dateinamen und Pfade müssen gegen den echten Projektordner geprüft werden.


---

## 22. Übergabe-Checkliste für den Programmierer

Vor Umsetzung prüfen:

- [ ] Hauptdatei gelesen
- [x] Assetliste `asset_liste_v34.md` vorhanden – Referenz, nicht aktuell
- [x] Modultabelle `workflow_module_table.xlsx` vorhanden – Referenz, nicht aktuell
- [x] `index.html` als alter Referenzstand vorhanden
- [x] `analyse.html` als Bestandscode-Quelle vorhanden
- [x] bestehender Header-Code aus `index.html` vorhanden
- [x] bestehender Sidebar-Code aus `index.html` vorhanden
- [x] bestehender Footer-Code aus `index.html` vorhanden
- [x] bestehender Formular-/Analyse-Code aus `analyse.html` vorhanden
- [x] `shared-header-footer.css` vorhanden
- [ ] finale Assetpfade im realen Projektordner prüfen

Während Umsetzung:

- [ ] keine neuen Sections ergänzen
- [ ] keine Texte kürzen
- [ ] keine Farbvarianten erfinden
- [ ] keine Assets neu interpretieren
- [x] CTA-Ziel final: Potenzialanalyse-CTAs führen zu `analyse.html`
- [ ] mobile Tap-Logik für Cards umsetzen

Nach Umsetzung testen:

- [ ] Desktop
- [ ] Tablet
- [ ] Smartphone
- [ ] alle CTA-Links
- [ ] Formular
- [x] keine separate `danke.html`; Success-/Error-Zustand in `analyse.html`
- [ ] Downloads
- [ ] Impressum
- [ ] Datenschutz
- [ ] Ladezeit
- [ ] keine sichtbaren Platzhalter

---

## 23. Bekannte Grenzen dieser Übergabe

Diese Punkte sind keine neuen Konzeptfragen, sondern reine Quellen-/Bestandsfragen:

- `asset_liste_v34.md` liegt vor, ist aber nicht aktuell. Sie dient als Referenz, nicht als kritischer Blocker.
- `workflow_module_table.xlsx` liegt vor, ist aber nicht aktuell. Sie dient als Referenz, nicht als kritischer Blocker.
- Echte Assetpfade müssen im realen Website-Projektordner geprüft werden.
- Konkrete Workflow-Modulzuordnungen werden später anhand der tatsächlichen Seiten-/Workflow-Planung geprüft.
- Header-/Footer-/Sidebar-Markup kann aus dem Altbestand technisch referenziert werden, aber `index.html` ist nicht die finale Startseitenstruktur.
- Formular in `analyse.html`verarbeitung kommt aus `analyse.html`.
- `shared-header-footer.css` liegt vor und ist nicht mehr als fehlende Datei zu behandeln.

Diese Punkte blockieren die Übergabe nicht mehr pauschal. Sie sind bei der Umsetzung als Prüfhinweise zu behandeln.
