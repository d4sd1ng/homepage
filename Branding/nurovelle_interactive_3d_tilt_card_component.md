# Nurovelle Interactive 3D Tilt Card Component

Status: Styleguide-Erweiterung / Web-Komponente

Diese Komponente beschreibt eine interaktive 3D-Tilt-Card fuer Web-Oberflaechen, Previews und Control-Panel-nahe Asset-Vorschauen.

Sie ist keine native LinkedIn-Interaktion. Fuer LinkedIn wird daraus nur eine statische Ableitung verwendet.

---

## 1. Komponentenname

Primaer:

- `interactive_3d_tilt_card`

Statische LinkedIn-Ableitung:

- `static_3d_depth_card`

---

## 2. Einsatzbereich

### Erlaubt fuer

- Homepage
- interaktive Landingpage-Elemente
- Atomizer-/Creator-Preview
- Control-Panel-Vorschau
- Web-Leadmagnet-Module

### Nicht direkt erlaubt fuer

- finalen LinkedIn-Export als interaktive Card
- statische PDF-Ausgabe mit Hover-Abhaengigkeit

LinkedIn darf nur die statische Ableitung nutzen:

- Tiefenwirkung
- dunkle Karte
- Grid-/Rasterstruktur
- Gold-/Smaragd-Akzente
- Schatten
- keine echte Cursor-Interaktion

---

## 3. Visuelle Grundidee

Die Card wirkt wie ein dunkles technisches Objekt mit leichter Tiefe.

Sie nutzt:

- 3D-Tilt bei Hover
- dunklen Nurovelle-Hintergrund
- feines technisches Raster
- Gold-/Kupfer-Akzente
- ruhige Smaragd-/Emerald-Akzente nur dezent
- leichten Glow
- erhabenen Text

Nicht erlaubt:

- Knallgruen
- Neon-Gruen
- blaue Akzente
- bunte SaaS-Gradienten
- generische Gaming-Card-Optik
- ueberladene Spiegelungen

---

## 4. Typografie

Die Komponente verwendet die fuehrenden Homepage-Schriften:

- Titel: `Bebas Neue`
- technische Labels / kleine Uppercase-Labels: `Anca Coder`, Fallback `monospace`
- Fliesstext: `Raleway`

Keine eigene Font-Logik in der Komponente.

---

## 5. Farbrollen

Die Komponente verwendet die Nurovelle-Farbrollen aus der Homepage:

- dunkle Basisflaeche
- Schwarzgruen / Deep Dark
- Gold-/Kupfer-Verlauf
- helles Weiss / Creme fuer Text
- gedimmter Text fuer Nebeninformationen
- Smaragd / Emerald nur als ruhiger Sekundaerakzent

Keine festen neuen Hexwerte innerhalb der Komponente, wenn der Homepage-Styleguide die Rolle bereits definiert.

---

## 6. Interaktionsregeln

Die Web-Variante darf:

- sich per `rotateX` / `rotateY` neigen
- auf Cursorposition reagieren
- ein dezentes Licht-/Glow-Overlay verschieben
- ein technisches Raster im Hintergrund zeigen

Die Web-Variante darf nicht:

- Inhalt verschieben, sodass Lesbarkeit leidet
- Motion zu stark einsetzen
- mehr als eine dominante Glow-Quelle haben
- Performance durch zu feine Trap-Grids unnoetig belasten

---

## 7. Technische Parameter

Empfohlene Ausgangswerte:

- Cursor-Trap-Grid: `N = 7`
- maximale Neigung: ca. `25deg`
- Perspektive: ca. `65em`
- Kartenformat: `2 / 3`
- Border-Radius: ca. `1.25em`
- Hintergrundraster: klein und subtil

Groesseres Cursor-Trap-Grid bedeutet:

- genauere Interaktion
- mehr HTML-Elemente
- mehr CSS-Regeln

---

## 8. HTML-Struktur

Empfohlene Struktur:

```html
<section class="nv-tilt-scene" style="--n: 7">
  <div class="nv-tilt-grid" aria-hidden="true">
    <!-- 49 trap elements for N=7 -->
  </div>

  <article class="nv-tilt-card">
    <div class="nv-tilt-card__text">
      <p class="nv-tilt-card__kicker">FORMAT LABEL</p>
      <h2>HEADLINE</h2>
      <p>Kurzer Bodytext.</p>
    </div>
  </article>
</section>
```

---

## 9. Statische LinkedIn-Ableitung

Name:

- `static_3d_depth_card`

Sie simuliert:

- Tiefenwirkung
- Schatten
- dunkle technische Karte
- Rasterstruktur
- Gold-/Kupfer-Akzent
- dezenten Smaragd-/Emerald-Akzent

Sie nutzt keine:

- Hover-Regeln
- Cursor-Traps
- CSS-`:has()`-Interaktion
- beweglichen Overlays

---

## 10. Geeignet fuer LinkedIn-Visual-Komponenten

Die statische Ableitung ist geeignet fuer:

- text_card
- metric_card
- quote_card
- myth_fact_card
- framework_card
- process_diagram mit maximal 5 Schritten

Weniger geeignet fuer:

- grosse Tabellen
- sehr textlastige Checklisten
- mehrspaltige Vergleichstabellen mit vielen Zellen

---

## 11. No-Gos

Nicht erlaubt:

- grelles Gruen
- Neon-Gruen
- Blau als Akzent
- mehrere konkurrierende Glows
- billige Gaming-Optik
- starke Verzerrung von Text
- Hover-Interaktion als Voraussetzung fuer Informationsverstaendnis
- erfundene Kennzahlen, Diagrammwerte oder Zitate
