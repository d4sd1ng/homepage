# Asset-Liste – Nurovelle Homepage

Status: aktualisierte Assetliste nach neuem Homepage-Aufbau  
Grundlage: aktuelle Benutzervorgabe zur Projektstruktur  
Hinweis: Diese Liste beschreibt die Zielstruktur für den HTML-Programmierer. Sie ersetzt die alte V34-Zuordnung als aktuelle Asset-Referenz. Die tatsächliche physische Vollständigkeit der Dateien muss im finalen Projektordner geprüft werden.

---

## 1. Projektwurzel

| Pfad / Datei | Verwendung | Status / Hinweis |
|---|---|---|
| `index.html` | Startseite | Hauptdatei der Homepage |
| `css/styles.css` | zentrale CSS-Datei | Alle finalen Styles hier bündeln |
| `js/main.js` | zentrale JavaScript-Datei | Alle finalen Interaktionen hier bündeln |

---

## 2. Assets-Ordner – Hauptstruktur

```text
assets/
├── images/
├── icons/
├── downloads/
├── og/
├── ablauf/
├── analyse/
├── cards/
├── hero/
└── module/
```

---

## 3. Kontaktbild / Portrait

| Asset | Pfad | Verwendung | Hinweis |
|---|---|---|---|
| Kontaktbild | `assets/images/contact.png` | Kontakt-/CTA-Bereich, Portraitkarte oder Kontaktmodul | Vorgabe: `contact.png 342`; Größe/Endmaß im Projekt prüfen |

---

## 4. Icons

### 4.1 Branchenicons

| Bereich | Dateien | Pfad | Verwendung |
|---|---|---|---|
| Branchenicons | `icon1.png` bis `icon9.png` | `assets/icons/icons_branche/` | Icons für 9 Branchenbereiche |

### 4.2 Serviceicons

| Bereich | Dateien | Pfad | Verwendung |
|---|---|---|---|
| Serviceicons | `icon1.png` bis `icon9.png` | `assets/icons/icons_service/` | Icons für 9 Servicebereiche |

### 4.3 Vorteile-Icons

| Bereich | Dateien | Pfad | Verwendung |
|---|---|---|---|
| Vorteile-Icons | `icon1.png` bis `icon5.png` | `assets/icons/icons_vorteile/` | Icons für Nutzen-/Vorteilebereiche |

---

## 5. Downloads

| Download | Pfad | Verwendung | Hinweis |
|---|---|---|---|
| Case Study KI-Automatisierung | `assets/downloads/CASE_STUDY_KI_AUTOMATISIERUNG` | Download-Bereich | Dateiendung im Projekt prüfen, z. B. `.pdf` |
| ROI Guide KI-Automatisierung Nurovelle | `assets/downloads/ROI_GUIDE_KI_AUTOMATISIERUNG_NUROVELLE` | Download-Bereich | Dateiendung im Projekt prüfen, z. B. `.pdf` |
| Prompt Guide | `assets/downloads/prompt_guide` | Download-Bereich | Dateiendung im Projekt prüfen, z. B. `.pdf` |
| Checkliste | `assets/downloads/checkliste` | Download-Bereich | Dateiendung im Projekt prüfen, z. B. `.pdf` |

Regel:

- Download-CTAs führen laut finaler Brief-Entscheidung zu `#downloads` oder `praxisleitfaden.html`.
- Keine zusätzliche Download-Logik ohne Freigabe.
- Dateiendungen und endgültige Dateinamen im Projektordner prüfen.

---

## 6. Open Graph

| Asset | Pfad | Verwendung |
|---|---|---|
| Open-Graph-Bild | `assets/og/og.png` | Social Preview / OG Image |

---

## 7. Ablaufgrafiken

| Asset | Pfad | Verwendung | Hinweis |
|---|---|---|---|
| Ablauf Desktop | `assets/ablauf/all.png` | Desktop-Ablaufgrafik | ersetzt alte Einzel-/Desktop-Zuordnung, sofern im Brief so verwendet |
| Ablauf Mobile 1 | `assets/ablauf/1.png` | mobiler Ablauf | Mobile Schrittgrafik |
| Ablauf Mobile 2 | `assets/ablauf/2.png` | mobiler Ablauf | Mobile Schrittgrafik |
| Ablauf Mobile 3 | `assets/ablauf/3.png` | mobiler Ablauf | Mobile Schrittgrafik |
| Ablauf Mobile 4 | `assets/ablauf/4.png` | mobiler Ablauf | Mobile Schrittgrafik |
| Ablauf Mobile 5 | `assets/ablauf/5.png` | mobiler Ablauf | Mobile Schrittgrafik |
| Ablauf Mobile 6 | `assets/ablauf/6.png` | mobiler Ablauf | Mobile Schrittgrafik |
| Ablauf Mobile 7 | `assets/ablauf/7.png` | mobiler Ablauf | Mobile Schrittgrafik |

---

## 8. Analyse-Seite

| Asset | Pfad | Verwendung | Hinweis |
|---|---|---|---|
| Analysegrafik 1 | `assets/analyse/1.png` | Analyse-Seite | Farbliche Anpassung noch erforderlich |
| Analysegrafik 2 | `assets/analyse/2.png` | Analyse-Seite | Farbliche Anpassung noch erforderlich |
| Analysegrafik 3 | `assets/analyse/3.png` | Analyse-Seite | Farbliche Anpassung noch erforderlich |
| Analysegrafik 4 | `assets/analyse/4.png` | Analyse-Seite | Farbliche Anpassung noch erforderlich |
| Analysegrafik 5 | `assets/analyse/5.png` | Analyse-Seite | Farbliche Anpassung noch erforderlich |
| Analysegrafik 6 | `assets/analyse/6.png` | Analyse-Seite | Farbliche Anpassung noch erforderlich |
| Analysegrafik 7 | `assets/analyse/7.png` | Analyse-Seite | Farbliche Anpassung noch erforderlich |
| Analysegrafik 8 | `assets/analyse/8.png` | Analyse-Seite | Farbliche Anpassung noch erforderlich |

Regel:

- `analyse.html` ist laut finaler Entscheidung die aktuelle Formular-/Analysegrundlage.
- Alle Potenzialanalyse-CTAs führen zu `analyse.html`.
- Success-/Error-Zustand bleibt in `analyse.html`.
- Keine separate `danke.html` erforderlich.
- Hinweis zur Anpassung: Nur die Analysegrafiken `assets/analyse/1.png` bis `assets/analyse/8.png` sind farblich noch an das finale Nurovelle-Design anzupassen.

---

## 9. Cards

### 9.1 Servicekarten

| Bereich | Dateien | Pfad | Verwendung |
|---|---|---|---|
| Servicekarten | `1.png` bis `9.png` | `assets/cards/cards_service/` | Kartenhintergründe für 9 Servicebereiche |

### 9.2 Branchenkarten

| Bereich | Dateien | Pfad | Verwendung |
|---|---|---|---|
| Branchenkarten | `1.png` bis `9.png` | `assets/cards/cards_branche/` | Kartenhintergründe für 9 Branchenbereiche |

### 9.3 Problem-Lösung-Karte

| Asset | Pfad | Verwendung |
|---|---|---|
| Problem-/Lösung-Card | `assets/cards/cards_problem_loesung/best_card_single 470x360.png` | Problem-/Lösungskarten |

---

## 10. Hero

| Asset | Pfad | Verwendung |
|---|---|---|
| Hero-Bild / Würfel | `assets/hero/1.png` | Hero-Visual |
| Hero Grid | `assets/hero/bg_grid.png` | technischer Hero-Hintergrund |
| Logo | `assets/hero/nurovelle_logo.png` | Header-Logo |

---

## 11. Module

### 11.1 Container

| Bereich | Dateien | Pfad | Verwendung |
|---|---|---|---|
| Container-Module | `container1.png` bis `container6.png` | `assets/module/container/` | Workflow-/Modulvisuals |

### 11.2 Displays

| Asset | Pfad | Verwendung |
|---|---|---|
| Tablet | `assets/module/displays/tablet.png` | Display-Modul |
| Monitor | `assets/module/displays/monitor.png` | Display-Modul |
| Handy | `assets/module/displays/handy.png` | Display-Modul |


### 11.3 Weitere Modulbilder

| Bereich | Dateien | Pfad | Verwendung |
|---|---|---|---|
| Weitere Modul-Assets | `10.png` bis `40.png` | `assets/module/` | übrige Workflow-/Modulvisuals nach Modultabelle oder Seitenbedarf |

Regel:

- `container1.png` bis `container6.png` bleiben im Ordner `assets/module/container/`.
- `tablet.png`, `monitor.png` und `handy.png` bleiben im Ordner `assets/module/displays/`.
- Die zusätzlichen Modulbilder laufen direkt unter `assets/module/` als `10.png` bis `40.png`.
- Es erfolgt keine Umbenennung der Container- oder Display-Dateien auf fortlaufende Nummern.

---

## 12. Section-Hintergrund

| Asset | Pfad | Verwendung | Hinweis |
|---|---|---|---|
| Section Background | `assets/sections_bg.png` | allgemeiner Section-Hintergrund | Schreibweise final bestätigt: `sections_bg.png` |

---

## 13. Aktualisierte Zielstruktur

```text
index.html
assets/
├── images/
│   └── contact.png
├── icons/
│   ├── icons_branche/
│   │   ├── icon1.png
│   │   ├── icon2.png
│   │   ├── icon3.png
│   │   ├── icon4.png
│   │   ├── icon5.png
│   │   ├── icon6.png
│   │   ├── icon7.png
│   │   ├── icon8.png
│   │   └── icon9.png
│   ├── icons_service/
│   │   ├── icon1.png
│   │   ├── icon2.png
│   │   ├── icon3.png
│   │   ├── icon4.png
│   │   ├── icon5.png
│   │   ├── icon6.png
│   │   ├── icon7.png
│   │   ├── icon8.png
│   │   └── icon9.png
│   └── icons_vorteile/
│       ├── icon1.png
│       ├── icon2.png
│       ├── icon3.png
│       ├── icon4.png
│       └── icon5.png
├── downloads/
│   ├── CASE_STUDY_KI_AUTOMATISIERUNG
│   ├── ROI_GUIDE_KI_AUTOMATISIERUNG_NUROVELLE
│   ├── prompt_guide
│   └── checkliste
├── og/
│   └── og.png
├── ablauf/
│   ├── all.png
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   ├── 6.png
│   └── 7.png
├── analyse/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   ├── 6.png
│   ├── 7.png
│   └── 8.png
├── cards/
│   ├── cards_service/
│   │   ├── 1.png
│   │   ├── 2.png
│   │   ├── 3.png
│   │   ├── 4.png
│   │   ├── 5.png
│   │   ├── 6.png
│   │   ├── 7.png
│   │   ├── 8.png
│   │   └── 9.png
│   ├── cards_branche/
│   │   ├── 1.png
│   │   ├── 2.png
│   │   ├── 3.png
│   │   ├── 4.png
│   │   ├── 5.png
│   │   ├── 6.png
│   │   ├── 7.png
│   │   ├── 8.png
│   │   └── 9.png
│   └── cards_problem_loesung/
│       └── best_card_single 470x360.png
├── hero/
│   ├── 1.png
│   ├── bg_grid.png
│   └── nurovelle_logo.png
├── module/
│   ├── container/
│   │   ├── container1.png
│   │   ├── container2.png
│   │   ├── container3.png
│   │   ├── container4.png
│   │   ├── container5.png
│   │   └── container6.png
│   ├── displays/
│   │   ├── tablet.png
│   │   ├── monitor.png
│   │   └── handy.png
│   ├── 10.png
│   ├── 11.png
│   ├── 12.png
│   ├── 13.png
│   ├── 14.png
│   ├── 15.png
│   ├── 16.png
│   ├── 17.png
│   ├── 18.png
│   ├── 19.png
│   ├── 20.png
│   ├── 21.png
│   ├── 22.png
│   ├── 23.png
│   ├── 24.png
│   ├── 25.png
│   ├── 26.png
│   ├── 27.png
│   ├── 28.png
│   ├── 29.png
│   ├── 30.png
│   ├── 31.png
│   ├── 32.png
│   ├── 33.png
│   ├── 34.png
│   ├── 35.png
│   ├── 36.png
│   ├── 37.png
│   ├── 38.png
│   ├── 39.png
│   └── 40.png
└── sections_bg.png
css/
└── styles.css
js/
└── main.js
```

---

## 14. Prüfhinweise für den HTML-Programmierer

- Diese Assetliste ist die aktuelle Zielstruktur.
- Alte Pfade aus früheren HTML-Ständen dürfen nicht blind übernommen werden.
- `index.html` aus dem Bestand ist alter Referenzstand, nicht finale Zielstruktur.
- `analyse.html` ist die aktuelle Grundlage für Analyseformular, API-Flow und Success-/Error-Zustände.
- Assetdateien müssen im echten Projektordner physisch geprüft werden.
- Fehlende Dateiendungen bei Downloads sind vor Verlinkung zu ergänzen.
- Nur die Analysegrafiken `assets/analyse/1.png` bis `8.png` müssen farblich noch an das finale Nurovelle-Design angepasst werden.
- Schreibweise final: `assets/sections_bg.png`. Im Code einheitlich genau so verwenden.
- Modul-Assets: Container bleiben `assets/module/container/container1.png` bis `container6.png`; Displays bleiben `assets/module/displays/tablet.png`, `monitor.png`, `handy.png`; weitere Modulbilder liegen direkt unter `assets/module/10.png` bis `assets/module/40.png`.
