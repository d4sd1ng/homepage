# NUROVELLE – CSS-Animationen und Interaktionen

Status: zusammengestellte Arbeitsreferenz  
Stand: 2026-07-05  
Zweck: zentrale Sammlung der bisher genannten und festgelegten CSS-/UX-Animationen für Homepage und Detailseiten.

Diese Datei ist **keine neue Designfreigabe**. Sie sammelt nur die bisher besprochenen Animationslogiken, damit sie nicht erneut aus Chatverläufen rekonstruiert werden müssen.

---

## 1. Grundregeln

Verbindlich:

- Umsetzung bevorzugt mit HTML/CSS/JS.
- Keine Bildgenerierung für kontrollierbare UI-Komponenten.
- Keine Demo-Farben aus Referenzen übernehmen.
- Keine Demo-Texte übernehmen.
- Keine externen Fonts nur wegen einer Animation importieren.
- Keine externen Scripts wie Prefixfree übernehmen.
- Keine React- oder Styled-Components-Pflicht.
- Mobile-Zustände müssen per Tap/Focus funktionieren.
- Tastaturbedienung, Focus-State und `prefers-reduced-motion` berücksichtigen.

Nicht verwenden:

- Cyan
- Blau als Hauptfarbe
- Violett
- Neon
- Bronze
- Kupfer
- Gaming-/Comic-Buttonwirkung
- Casino-/Spielautomatwirkung

---

## 2. Gemeinsame Design-Tokens

```css
:root {
  --nv-black: #050706;
  --nv-matte-black: #080B09;
  --nv-deep-green: #0A1913;
  --nv-emerald: #112A20;
  --nv-teal-dark: #163A35;
  --nv-text-light: #F5F7F4;
  --nv-text-muted: #B9C3BD;

  --nv-gold-dark: #a54e07;
  --nv-gold-mid: #b47e11;
  --nv-gold-light: #fef1a2;
  --nv-gold-core: #bc881b;
  --nv-gold-border: #a55d07;
  --nv-gold-inner-dark: #8b4208;
  --nv-gold-inner-mid: #b17d10;
  --nv-gold-highlight: #fae385;
  --nv-gold-text-dark: rgb(120, 50, 5);
  --nv-gold-gradient: linear-gradient(160deg, #a54e07, #b47e11, #fef1a2, #bc881b, #a54e07);
  --nv-gold-soft: linear-gradient(135deg, #F9F295, #E0AA3E, #FAF398, #B88A44);

  --nv-radius-card: 18px;
  --nv-radius-button: 999px;
  --nv-ease-premium: cubic-bezier(0.23, 1, 0.32, 1);
  --nv-ease-press: cubic-bezier(.2, .8, .2, 1);
}
```

---

## 3. CTA-Button – Arrow-Reveal zu Gold-Fill

Ursprung: vom Nutzer gelieferte Buttonlogik mit einfahrendem Pfeil, ausfahrendem Pfeil, Textverschiebung und expandierender Kreisfläche.  
Übernommen wird nur die Logik, nicht `greenyellow`, Demo-Text oder React-Struktur.

### HTML

```html
<a class="nv-btn nv-btn-arrow" href="analyse.html">
  <svg class="nv-btn__arrow nv-btn__arrow--in" viewBox="0 0 24 24" aria-hidden="true">
    <path d="M16.1716 10.9999L10.8076 5.63589L12.2218 4.22168L20 11.9999L12.2218 19.778L10.8076 18.3638L16.1716 12.9999H4V10.9999H16.1716Z"></path>
  </svg>
  <span class="nv-btn__text">KI-Potenzialanalyse durchführen</span>
  <span class="nv-btn__fill" aria-hidden="true"></span>
  <svg class="nv-btn__arrow nv-btn__arrow--out" viewBox="0 0 24 24" aria-hidden="true">
    <path d="M16.1716 10.9999L10.8076 5.63589L12.2218 4.22168L20 11.9999L12.2218 19.778L10.8076 18.3638L16.1716 12.9999H4V10.9999H16.1716Z"></path>
  </svg>
</a>
```

### CSS

Siehe Datei `nurovelle-animations.css`, Abschnitt `1. CTA BUTTON: ARROW-REVEAL + GOLD-FILL LOGIK`.

---

## 4. CTA-Button – Press-Button / haptische Absenkung

Ursprung: vom Nutzer gelieferte Buttonlogik mit oberer Buttonfläche, Unterseite und Basis.  
Übernommen wird nur die Press-Logik, nicht Demo-Türkis oder Demo-Grün.

### HTML

```html
<button class="nv-press-button" type="button">
  <span class="nv-press-button__top">Kostenlose Analyse starten</span>
  <span class="nv-press-button__bottom" aria-hidden="true"></span>
  <span class="nv-press-button__base" aria-hidden="true"></span>
</button>
```

### CSS

Siehe Datei `nurovelle-animations.css`, Abschnitt `2. CTA BUTTON: PRESS-BUTTON / HAPTISCHE ABSENKUNG`.

---

## 5. Golden-Button-Farblogik

Vom Nutzer gelieferte Farb-/Materiallogik. Sie dient als Grundlage für hochwertige Goldwirkung, Lichtkante und Innenkante.

```css
:root {
  --nv-gold-dark: #a54e07;
  --nv-gold-mid: #b47e11;
  --nv-gold-light: #fef1a2;
  --nv-gold-core: #bc881b;
  --nv-gold-border: #a55d07;
  --nv-gold-inner-dark: #8b4208;
  --nv-gold-inner-mid: #b17d10;
  --nv-gold-highlight: #fae385;
  --nv-gold-text-dark: rgb(120, 50, 5);
  --nv-gold-gradient: linear-gradient(160deg, #a54e07, #b47e11, #fef1a2, #bc881b, #a54e07);
}
```

Regeln:

- Kein Demo-Text „Golden Button“.
- Kein `role="button"` auf echtem `<button>`.
- Keine Casino-/Spielautomatwirkung.
- Gold darf hochwertig wirken, aber nicht billig glänzen.

---

## 6. Downloadbutton → größerer Danke-/Bestätigungsbutton

Gesuchte Referenzseite wurde nicht wiedergefunden. Die Interaktionslogik ist trotzdem festzuhalten.

### Verhalten

Startzustand:

- Downloadbutton / Anfragebutton

Nach erfolgreicher Aktion:

- Button transformiert in größere Bestätigungsfläche
- Text wechselt zu `Danke`, `Download startet`, `Download bereit` oder `Anfrage erhalten`
- Success-Zustand darf nur nach echter erfolgreicher Aktion gesetzt werden
- Fehler dürfen keinen Danke-Zustand auslösen

### HTML

```html
<button class="nv-download-confirm" type="button" data-download-button>
  <span class="nv-download-confirm__idle">Praxisleitfaden herunterladen</span>
  <span class="nv-download-confirm__success">Danke – Download startet</span>
</button>
```

### JS-Minimalbeispiel

```js
const button = document.querySelector('[data-download-button]');

button?.addEventListener('click', async () => {
  // Hier reale Download-/Formularlogik ausführen.
  // Nur bei Erfolg:
  button.classList.add('is-success');
});
```

### CSS

Siehe Datei `nurovelle-animations.css`, Abschnitt `3. DOWNLOADBUTTON TRANSFORMIERT ZU GROESSEREM DANKE-BUTTON`.

---

## 7. Breadcrumb – Chevron-/Pfeil-Segmente

Ursprung: vom Nutzer gelieferte CSS-Breadcrumb-Referenz.  
Übernommen wird die Chevron-/Pfeil-Logik mit `::after`; ausgeschlossen sind Demo-Farben, Google-Font-Import, Prefixfree-Script und Nummernzwang.

### HTML

```html
<nav class="nv-breadcrumb" aria-label="Breadcrumb">
  <a href="/">Start</a>
  <a href="/leistungen.html">Leistungen</a>
  <span aria-current="page">KI-Potenzialanalyse</span>
</nav>
```

### CSS

Siehe Datei `nurovelle-animations.css`, Abschnitt `4. BREADCRUMB: CHEVRON / PFEIL-SEGMENTE`.

---

## 8. Hero-Animation – Orb hinter Cube / Cube-Entstehung

Status: **Originalvorgabe aus Chat gesichert.**  
Einsatz: **hinter den bestehenden Hero-Cube / Würfel.**  
Nicht als Conic-/Noise-Mask interpretieren. Nicht frei umbauen.

### Originalvorgabe SCSS

```scss
// best in chrome
$total: 300; // total particles
$orb-size: 100px;
$particle-size: 2px;
$time: 14s; 
$base-hue: 0; // change for diff colors (180 is nice)

html, body {
  height: 100%;
}

body {
  background: black;
  overflow: hidden; // no scrollbars.. 
}

.wrap {
  position: relative;
  top: 50%;
  left: 50%;
  width: 0; 
  height: 0; 
  transform-style: preserve-3d;
  perspective: 1000px;
  animation: rotate $time infinite linear; // rotate orb
}

@keyframes rotate {
  100% {
    transform: rotateY(360deg) rotateX(360deg);
  }
}

.c {
  position: absolute;
  width: $particle-size;
  height: $particle-size;
  border-radius: 50%;
  opacity: 0; 
}

@for $i from 1 through $total {
  $z: (random(360) * 1deg); // random angle to rotateZ
  $y: (random(360) * 1deg); // random to rotateX
  $hue: ((40/$total * $i) + $base-hue); // set hue
  
  .c:nth-child(#{$i}){ // grab the nth particle
    animation: orbit#{$i} $time infinite;
    animation-delay: ($i * .01s); 
    background-color: hsla($hue, 100%, 50%, 1);
  }

  @keyframes orbit#{$i}{ 
    20% {
      opacity: 1; // fade in
    }
    30% {
      transform: rotateZ(-$z) rotateY($y) translateX($orb-size) rotateZ($z); // form orb
    }
    80% {
      transform: rotateZ(-$z) rotateY($y) translateX($orb-size) rotateZ($z); // hold orb state 30-80
      opacity: 1; // hold opacity 20-80
    }
    100% {
       transform: rotateZ(-$z) rotateY($y) translateX( ($orb-size * 3) ) rotateZ($z); // translateX * 3
    }
  }
}
```

### Originalvorgabe HAML

```haml
%div.wrap
  -300.times do
    %div.c
```

### Einordnungsregeln

- Diese Animation ist die Hero-Orb-Quelle hinter dem Cube.
- Der Code ist SCSS/HAML, nicht direktes Produktions-CSS.
- Die bestehende `.nv-hero-orb`-/Conic-Mask-Rekonstruktion ist davon zu unterscheiden.
- Eine Nurovelle-Adaption darf erst nach gesonderter Freigabe entstehen.
- Bei Adaption dürfen nur projektkonforme Farben eingesetzt werden: Schwarz, sehr dunkles Petrol/Smaragd, Gold-Akzente.
- Keine cyan/blauen/violetten Demo-Farben übernehmen.
- Der Cube selbst darf dadurch nicht unkontrolliert bewegt werden.
- `prefers-reduced-motion` ist bei Produktionsumsetzung zu berücksichtigen.


## 9. Divider-Varianten

Status: muss live gesehen werden.


### Aktuelle Divider-Abfolge für die Live-Übersicht

Stand: 2026-07-10.

Für die aktuelle Startseitenprüfung gilt folgende Abfolge:

1. Hero → Section 2: Divider A – SVG-Schräg-Divider / Separator.
2. Section 2 „Der erste Schritt zu Ihrem KI-Projekt“ → Section 3 „Sie haben bereits eine konkrete KI-Idee?“: Divider A erneut.
3. Section 3 „Sie haben bereits eine konkrete KI-Idee?“ → Section 4 „Kostenlose KI-Potenzialanalyse“: Divider B normal.
4. Section 4 „Kostenlose KI-Potenzialanalyse“ → Section 5 „KI-Leistungen von Nurovelle“: Divider B reverse.
5. Section 5 „KI-Leistungen von Nurovelle“ → Section 6 „Vom Geschäftsprozess zur KI-Lösung“: Divider C.

Diese Abfolge dient der Live-Übersicht über die Varianten A, B und C. Variante A wird bewusst zweimal hintereinander gezeigt, damit ihre Wirkung über aufeinanderfolgende Sections beurteilt werden kann. Die Abfolge ist noch keine finale Auswahl einer einzigen Divider-Variante.

### Variante A – SVG-Schräg-Divider / Separator

Status: technische Prüfvariante, nicht final als konkrete Form freigegeben. Divider selbst sind verbindlich vorgesehen.

Quelle:

- Nutzerreferenz aus dem Chat vom 2026-07-07.
- Original separat gesichert in `nurovelle-divider-svg-original-reference.txt`.

Übernehmbarer technischer Kern:

- Section enthält einen absolut positionierten `.separator` am unteren Rand.
- Das SVG nutzt `width="100%"`, `viewBox="0 0 100 100"` und `preserveAspectRatio="none"`.
- Zwei Pfade bilden eine schräge Hauptfläche und eine zweite Tiefen-/Akzentfläche.
- Mobile darf mit versetztem, breiterem und leicht rotiertem SVG geprüft werden.
- `overflow-x: hidden` ist als Schutz gegen horizontales Scrollen erlaubt, muss aber kontrolliert eingesetzt werden.

Nicht übernehmen:

- Demo-Grün `#5FC18B`, `#44A36F`, `#308355`.
- Demo-Klassen wie `.section-one` / `.section-two` als Produktionsstruktur.
- Demo-Texte und Beispielinhalte.

Nurovelle-Adaption:

Siehe Datei `nurovelle-animations.css`, Abschnitt `7A. DIVIDER A: SVG-SCHRÄG-DIVIDER / SEPARATOR`. Diese CSS-Klasse ist eine Nurovelle-Adaption der Technik, nicht die Originalreferenz.

### Variante B – Pure-CSS-Angled-Sections mit `clip-path`, CSS-Trigonometrie und Fallbacks

Status: technische Prüfvariante, nicht final freigegeben. Divider selbst sind verbindlich vorgesehen.

Quelle:

- Nutzerreferenz aus dem Chat vom 2026-07-07.
- Original separat gesichert in `nurovelle-divider-pure-css-angled-original-reference.scss`.

Übernehmbarer technischer Kern:

- Section-Kanten werden direkt über `clip-path: polygon(...)` schräg angeschnitten.
- Winkel wird als SCSS-Wert gesetzt und mit Guardrails begrenzt.
- `@property` registriert `--angle`, `--space` und `--hypot` als Fallback-Werte.
- `@supports (z-index: tan(0deg))` erlaubt progressive Enhancement mit CSS-Trigonometrie.
- `@supports (rotate: atan2(1vh, 1vw))` kann als zusätzliche Viewport-/Support-Prüfung dienen.
- Wechselnde Section-Richtung über Paritätsflag (`--p`) ist als Prüfmechanik möglich.
- Schattenkante per `section::after` kann als dezenter Tiefeneffekt geprüft werden.

Nicht übernehmen:

- Demo-Fonts wie Ubuntu / Trebuchet.
- Pastell-/Demo-Verläufe, Support-Infoboxen, Code-Demo, Footer-Lochmuster, Link-XOR-Effekt.
- Transformierte Headlines außerhalb der finalen Nurovelle-Typografie.
- Beispieltexte, Referenzlinks oder Playground-/Support-Demo-Inhalte.

Nurovelle-Adaption:

Siehe Datei `nurovelle-animations.css`, Abschnitt `7B. DIVIDER B: PURE-CSS-ANGLED-SECTIONS MIT FALLBACKS`. Diese CSS-Klasse ist eine Nurovelle-Adaption der Technik, nicht die Originalreferenz.

### Variante C – Diagonal Box / SkewY + Clip-Path

Status: technische Prüfvariante, nicht final freigegeben.

Quelle:

- Nutzerreferenz aus dem Chat vom 2026-07-07.
- Original separat gesichert in `nurovelle-divider-diagonal-original-reference.txt`.

Übernehmbarer technischer Kern:

- Section-Hintergrund wird über ein `::before`-/`:before`-Pseudo-Element schräg gestellt.
- `skewY(var(--angle))` wirkt nur auf das Hintergrundelement, nicht auf Content.
- Content bleibt horizontal, lesbar und im sicheren Inhaltsbereich.
- Winkel und Sicherheitsabstände werden über CSS-Variablen berechnet.
- `tan()` / `--skew-padding` / `--clip-padding` sind als Berechnungslogik prüfbar.
- `clip-path` ist als ergänzende Variante prüfbar.

Nicht übernehmen:

- Demo-Farben wie Violett, Pink, Cyan oder Blau.
- Playground-Controls.
- Demo-Texte, fremde Links und Demo-SVGs.
- transformierter Content wie `h1 { transform: skewY(...) }`.
- externe Fonts oder Beispielseitenstruktur.

Nurovelle-Adaption:

Siehe Datei `nurovelle-animations.css`, Abschnitt `8. DIVIDER C: DIAGONAL BOX / SKEWY + CLIP-PATH`. Diese CSS-Klasse ist eine Nurovelle-Adaption der Technik, nicht die Originalreferenz.

---

## 10. Card-Animation – Frosted-Glass / Overlay-Reveal

Ursprung: CodePen-Option für Cards.  
Übernommen wird die Logik: Card-Grundzustand, einfahrende Info-Fläche, Blur-/Overlay-Wirkung, Hover/Tap.

### HTML

```html
<article class="nv-reveal-card">
  <div class="nv-reveal-card__media" aria-hidden="true"></div>
  <div class="nv-reveal-card__base">
    <h3>KI-Agenten</h3>
  </div>
  <div class="nv-reveal-card__info">
    <h3>KI-Agenten</h3>
    <span class="nv-reveal-card__accent" aria-hidden="true"></span>
    <p>Agentenlogik, Tool-Anbindung, MCP, API-Zugriff und Aufgabensteuerung.</p>
  </div>
</article>
```

### CSS

Siehe Datei `nurovelle-animations.css`, Abschnitt `9. CARD: FROSTED-GLASS / OVERLAY REVEAL`.

Mobile-Regel:

- JS setzt `.is-open`.
- Beim Öffnen einer anderen Card schließt die vorherige.

---

## 11. Social-Icon-Animation

Status: bestimmt als CSS/SVG-Umsetzung.  
Regeln:

- Nur Symbol sichtbar.
- Keine Textlabels sichtbar.
- `aria-label` Pflicht.
- Keine Bildgenerierung.
- Farben Nurovelle-kompatibel.

### HTML

```html
<div class="nv-socials">
  <a class="nv-social" href="#" aria-label="LinkedIn">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="..."></path></svg>
  </a>
</div>
```

### CSS

Siehe Datei `nurovelle-animations.css`, Abschnitt `10. SOCIAL ICONS: SYMBOL ONLY, HOVER/FOKUS`.

---

## 12. Section-/Board-Prüfvariante

Ursprung: CodePen-Option für Section/Board.  
Status: Prüfvariante, nicht finale Pflicht.

Übernommen werden kann:

- Board-Struktur
- seitliche Icon-Navigation
- Grid-/Panel-Flächen
- aktive Zustände
- Hover-Highlights

Ausgeschlossen:

- Demo-Logo
- Demo-Farben
- Demo-Texte
- Finanz-/Wallet-/Profit-Inhalte
- externe Avatar-/Bild-URLs
- `arial-label`-Fehler; korrekt ist `aria-label`

### CSS

Siehe Datei `nurovelle-animations.css`, Abschnitt `11. BOARD-/DASHBOARD-SECTION ALS PRUEFVARIANTE`.

---

## 13. Mobile-Interaktion für Cards

```js
const cards = document.querySelectorAll('.nv-reveal-card');

cards.forEach((card) => {
  card.addEventListener('click', () => {
    cards.forEach((other) => {
      if (other !== card) other.classList.remove('is-open');
    });
    card.classList.toggle('is-open');
  });
});
```

---

## 14. Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .001ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: .001ms !important;
  }
}
```

---

## 15. Statusübersicht

| Komponente | Status |
|---|---|
| CTA-Button-Animation | bestimmt |
| Golden-Button-Farblogik | aufgenommen |
| Downloadbutton zu Danke-Button | aufgenommen / Referenzseite noch nicht gefunden |
| Breadcrumb-Ausführung | bestimmt |
| Social Buttons | bestimmt |
| Card-Overlay | Prüfvariante |
| Board-/Section-Komponente | Prüfvariante |
| Divider | verbindlich vorgesehen / finale Variante live prüfen |
| Hero-Animation | live prüfen |

---

## 16. Zugehörige CSS-Datei

Die direkt verwendbaren CSS-Snippets liegen zusätzlich in:

```text
nurovelle-animations.css
```

---

## 17. CTA-Button-System – Originalreferenzen vom 2026-07-07

Status: Originalreferenzen gesichert, Produktionsadaption separat.  
Originaldatei:

```text
nurovelle-button-original-references.md
```

### 17.1 Arrow-Reveal als Startlogik

Ursprung: vom Nutzer gelieferter React-/styled-components Button mit Klasse `.animated-button`.

Übernommen wird nur die Interaktionslogik:

- rechter Pfeil startet sichtbar rechts (`arr-1`)
- linker Pfeil startet außerhalb links (`arr-2`)
- Hover: rechter Pfeil fährt raus, linker Pfeil fährt rein
- Text verschiebt sich von links nach rechts
- Kreisfläche wächst aus der Mitte und füllt den Button
- Active-State skaliert den Button leicht herunter

Nicht übernehmen:

- `greenyellow`
- Demo-Text `Modern Button`
- React-/styled-components-Pflicht
- Demo-Klassen als finale öffentliche API

### 17.2 Press-Button als haptische Logik

Ursprung: vom Nutzer gelieferter React-/styled-components Button mit `.button`, `.button-top`, `.button-bottom`, `.button-base`.

Übernommen wird nur die Logik:

- Button besteht aus Top-, Bottom- und Base-Ebene
- `.button-top` senkt sich bei `:active`
- `.button-bottom` verändert Radius und Tiefe
- `.button-base` bildet die ruhende Schattenbasis

Nicht übernehmen:

- Demo-Türkis / Demo-Grün
- Demo-Text `Button`
- React-/styled-components-Pflicht

### 17.3 Golden-Button-Farblogik

Ursprung: vom Nutzer gelieferter Golden-Button-Code.

Übernommen wird die Farblogik:

- `#a54e07`
- `#b47e11`
- `#fef1a2`
- `#bc881b`
- `#a55d07`
- `#8b4208`
- `#b17d10`
- `#fae385`
- `rgb(120, 50, 5)`
- `linear-gradient(160deg, #a54e07, #b47e11, #fef1a2, #bc881b, #a54e07)`

Nicht übernehmen:

- Demo-Text `Golden Button`
- `role="button"` auf echtem `<button>`
- Casino-/Spielautomatwirkung

### 17.4 Systemlogik

Die Zielrichtung ist:

```text
Arrow-Reveal / Circle-Fill als Start-CTA-Logik
+ Press-Button als haptische Klick-/Active-Logik
+ Golden-Button-Farblogik als Nurovelle-Materialbasis
```

Diese Kombination ist eine Nurovelle-Adaption. Sie darf nicht als unveränderter Originalcode bezeichnet werden.

---

## 18. Section-/Board-CodePen als Option

Status: externe Prüfoption, nicht final.  
Quelle: `https://codepen.io/josephrexme/pen/oNNpZYJ`  
Original-/Quellenhinweis:

```text
nurovelle-section-board-codepen-reference.md
```

Einordnung:

- Option für eine Section-/Board-Komponente.
- Keine 1:1-Übernahme.
- Keine Produktionsfreigabe.
- Nur nach visueller Prüfung und Nurovelle-Adaption verwenden.

Übernehmbar nach Prüfung:

- Board-/Panel-Struktur
- seitliche Icon-Navigation
- aktive Zustände
- Hover-/Focus-Zustände
- technische Dashboard-/Board-Anmutung

Nicht übernehmen:

- Demo-Logo
- Demo-Farben
- Demo-Texte
- Finanz-/Wallet-Inhalte
- externe Avatar-/Bild-URLs
- `arial-label`; korrekt ist `aria-label`

---

## 99. Übernommene Zusatzdateien / Originalreferenz-Archiv

Status: übernommen in Projektfiles  
Datum: 2026-07-07  
Zweck: Die zuvor separat erzeugten 8 Zusatzdateien werden hier als Projektbestandteil gesichert. Diese Anhänge sind Referenz-/Archivmaterial, nicht automatisch Produktionscode.

Regeln:

- Originalcode bleibt nachvollziehbar erhalten.
- Nurovelle-Adaptionen müssen getrennt von Originalreferenzen bleiben.
- Keine Demo-Farben, Demo-Texte, externen Fonts, externen Scripts oder React-/Styled-Components-Pflichten übernehmen.
- `index.html` wird dadurch nicht geändert.
- Finale Nutzung einzelner Varianten erst nach Sichtprüfung und Freigabe.


### 99.x – CTA-Button-Preview HTML

Ursprüngliche Zusatzdatei: `nurovelle_cta_button_preview.html`  
Status: in Projektfiles übernommen / Original- oder Arbeitsreferenz

```html
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Nurovelle CTA Button Preview</title>
  <style>
    :root {
      --nv-black: #050706;
      --nv-matte-black: #080B09;
      --nv-deep-green: #0A1913;
      --nv-emerald: #112A20;
      --nv-teal-dark: #163A35;
      --nv-text-light: #F5F7F4;
      --nv-text-muted: #B9C3BD;

      --nv-gold-dark: #a54e07;
      --nv-gold-mid: #b47e11;
      --nv-gold-light: #fef1a2;
      --nv-gold-core: #bc881b;
      --nv-gold-border: #a55d07;
      --nv-gold-inner-dark: #8b4208;
      --nv-gold-inner-mid: #b17d10;
      --nv-gold-highlight: #fae385;
      --nv-gold-text-dark: rgb(120, 50, 5);
      --nv-gold-gradient: linear-gradient(160deg, #a54e07, #b47e11, #fef1a2, #bc881b, #a54e07);
      --nv-gold-soft: linear-gradient(135deg, #F9F295, #E0AA3E, #FAF398, #B88A44);

      --nv-radius-card: 18px;
      --nv-radius-button: 999px;
      --nv-ease-premium: cubic-bezier(0.23, 1, 0.32, 1);
      --nv-ease-press: cubic-bezier(.2, .8, .2, 1);
    }

    * { box-sizing: border-box; }

    html,
    body {
      min-height: 100%;
      margin: 0;
      background: var(--nv-black);
      color: var(--nv-text-light);
      font-family: Arial, sans-serif;
    }

    body {
      display: grid;
      place-items: center;
      padding: 32px;
    }

    .cta-preview {
      display: flex;
      flex-wrap: wrap;
      gap: 18px;
      align-items: center;
      justify-content: center;
      max-width: 1100px;
    }

    .nv-download-confirm {
      --btn-width: 220px;
      position: relative;
      display: inline-grid;
      place-items: center;
      min-width: var(--btn-width);
      min-height: 50px;
      padding: 0 28px;
      border: 1px solid var(--nv-gold-border);
      border-radius: var(--nv-radius-button);
      color: var(--nv-gold-highlight);
      background: rgba(5,7,6,.72);
      box-shadow: 0 0 0 1px rgba(250,227,133,.14), 0 12px 28px rgba(0,0,0,.35);
      cursor: pointer;
      overflow: hidden;
      font: inherit;
      font-weight: 800;
      letter-spacing: .02em;
      text-transform: uppercase;
      transition: min-width .45s var(--nv-ease-premium), min-height .45s var(--nv-ease-premium), border-radius .45s var(--nv-ease-premium), color .35s ease, background .35s ease, box-shadow .35s ease, transform .18s ease;
      -webkit-tap-highlight-color: transparent;
    }

    .nv-download-confirm::before {
      content: "";
      position: absolute;
      inset: auto 0 0 0;
      height: 0%;
      background: var(--nv-gold-gradient);
      transition: height .5s var(--nv-ease-premium);
      z-index: 0;
    }

    .nv-download-confirm__idle,
    .nv-download-confirm__loading,
    .nv-download-confirm__success {
      position: relative;
      z-index: 1;
      transition: opacity .25s ease, transform .35s var(--nv-ease-premium);
    }

    .nv-download-confirm__loading,
    .nv-download-confirm__success {
      position: absolute;
      opacity: 0;
      transform: translateY(18px) scale(.96);
    }

    .nv-download-confirm__success {
      color: var(--nv-black);
      font-weight: 800;
    }

    .nv-download-confirm:hover,
    .nv-download-confirm:focus-visible {
      outline: none;
      box-shadow: 0 0 0 1px rgba(250,227,133,.26), 0 16px 34px rgba(0,0,0,.42);
    }

    .nv-download-confirm:active { transform: scale(.975); }

    .nv-download-confirm.is-loading {
      min-width: 250px;
      color: var(--nv-gold-highlight);
      border-radius: 18px;
      box-shadow: 0 15px 36px rgba(0,0,0,.40), 0 0 0 1px rgba(250,227,133,.22);
    }

    .nv-download-confirm.is-loading::before {
      height: 38%;
      animation: nv-loading-fill 1s var(--nv-ease-premium) infinite alternate;
    }

    .nv-download-confirm.is-loading .nv-download-confirm__idle {
      opacity: 0;
      transform: translateY(-18px) scale(.96);
    }

    .nv-download-confirm.is-loading .nv-download-confirm__loading {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    .nv-download-confirm.is-success {
      min-width: 290px;
      min-height: 74px;
      border-radius: 18px;
      color: var(--nv-black);
      box-shadow: 0 18px 46px rgba(0,0,0,.44), 0 0 0 1px rgba(250,227,133,.28);
    }

    .nv-download-confirm.is-success::before { height: 100%; }
    .nv-download-confirm.is-success .nv-download-confirm__idle,
    .nv-download-confirm.is-success .nv-download-confirm__loading { opacity: 0; transform: translateY(-18px) scale(.96); }
    .nv-download-confirm.is-success .nv-download-confirm__success { opacity: 1; transform: translateY(0) scale(1); }

    @keyframes nv-loading-fill {
      from { height: 28%; }
      to { height: 58%; }
    }

    @media (prefers-reduced-motion: reduce) {
      .nv-download-confirm,
      .nv-download-confirm::before,
      .nv-download-confirm__idle,
      .nv-download-confirm__loading,
      .nv-download-confirm__success {
        transition-duration: 0ms;
        animation: none;
      }
    }

    @media (max-width: 720px) {
      body { padding: 24px 16px; }
      .cta-preview {
        width: 100%;
        flex-direction: column;
        align-items: stretch;
      }
      .nv-download-confirm {
        width: 100%;
        min-width: 0;
      }
      .nv-download-confirm.is-loading,
      .nv-download-confirm.is-success {
        min-width: 0;
      }
    }
  </style>
</head>
<body>
  <main class="cta-preview" aria-label="Nurovelle CTA Button Preview">
    <button class="nv-download-confirm" type="button" data-target="analyse.html">
      <span class="nv-download-confirm__idle">Kostenlose KI-Potenzialanalyse anfordern</span>
      <span class="nv-download-confirm__loading">Analyse wird angefragt</span>
      <span class="nv-download-confirm__success">Danke – Anfrage erhalten</span>
    </button>

    <button class="nv-download-confirm" type="button" data-target="#kontakt">
      <span class="nv-download-confirm__idle">Kostenloses Erstgespräch vereinbaren</span>
      <span class="nv-download-confirm__loading">Gespräch wird angefragt</span>
      <span class="nv-download-confirm__success">Danke – Anfrage erhalten</span>
    </button>

    <button class="nv-download-confirm" type="button" data-target="#downloads">
      <span class="nv-download-confirm__idle">Praxisleitfaden herunterladen</span>
      <span class="nv-download-confirm__loading">Download wird vorbereitet</span>
      <span class="nv-download-confirm__success">Danke – Download startet</span>
    </button>
  </main>

  <script>
    document.querySelectorAll('.nv-download-confirm').forEach((button) => {
      button.addEventListener('click', () => {
        if (button.classList.contains('is-loading')) return;

        button.classList.remove('is-success');
        button.classList.add('is-loading');

        window.setTimeout(() => {
          button.classList.remove('is-loading');
          button.classList.add('is-success');
        }, 900);
      });
    });
  </script>
</body>
</html>

```


### 99.x – Hero-Orb Original SCSS

Ursprüngliche Zusatzdatei: `nurovelle-hero-orb-original.scss`  
Status: in Projektfiles übernommen / Original- oder Arbeitsreferenz

```scss
// ORIGINALVORGABE HERO-ORB AUS CHAT
// Status: Original sichern, nicht als Nurovelle-Adaption verändern.
// Einsatz: Hero hinter den Cube.
// Hinweis: SCSS, nicht direktes Browser-CSS.

// best in chrome
$total: 300; // total particles
$orb-size: 100px;
$particle-size: 2px;
$time: 14s; 
$base-hue: 0; // change for diff colors (180 is nice)

html, body {
  height: 100%;
}

body {
  background: black;
  overflow: hidden; // no scrollbars.. 
}

.wrap {
  position: relative;
  top: 50%;
  left: 50%;
  width: 0; 
  height: 0; 
  transform-style: preserve-3d;
  perspective: 1000px;
  animation: rotate $time infinite linear; // rotate orb
}

@keyframes rotate {
  100% {
    transform: rotateY(360deg) rotateX(360deg);
  }
}

.c {
  position: absolute;
  width: $particle-size;
  height: $particle-size;
  border-radius: 50%;
  opacity: 0; 
}

@for $i from 1 through $total {
  $z: (random(360) * 1deg); // random angle to rotateZ
  $y: (random(360) * 1deg); // random to rotateX
  $hue: ((40/$total * $i) + $base-hue); // set hue
  
  .c:nth-child(#{$i}){ // grab the nth particle
    animation: orbit#{$i} $time infinite;
    animation-delay: ($i * .01s); 
    background-color: hsla($hue, 100%, 50%, 1);
  }

  @keyframes orbit#{$i}{ 
    20% {
      opacity: 1; // fade in
    }
    30% {
      transform: rotateZ(-$z) rotateY($y) translateX($orb-size) rotateZ($z); // form orb
    }
    80% {
      transform: rotateZ(-$z) rotateY($y) translateX($orb-size) rotateZ($z); // hold orb state 30-80
      opacity: 1; // hold opacity 20-80
    }
    100% {
       transform: rotateZ(-$z) rotateY($y) translateX( ($orb-size * 3) ) rotateZ($z); // translateX * 3
    }
  }
}

```


### 99.x – Hero-Orb Original HAML

Ursprüngliche Zusatzdatei: `nurovelle-hero-orb-original.haml`  
Status: in Projektfiles übernommen / Original- oder Arbeitsreferenz

```haml
%div.wrap
  -300.times do
    %div.c

```


### 99.x – Divider Originalreferenz C – Diagonal Box / SkewY + Clip-Path

Ursprüngliche Zusatzdatei: `nurovelle-divider-diagonal-original-reference.txt`  
Status: in Projektfiles übernommen / Original- oder Arbeitsreferenz

```text

  --width: min(100vw, 42rem);
  --full-width: 100vw;
  
  
  --angle: -11deg;
  /* Make sure we always have the absolute value */
  /* negative values don't work with CSS tan() */
  --abs-angle: max(var(--angle), var(--angle) * -1);
  --tan-alpha: tan(var(--abs-angle));
  --skew-padding: calc(var(--width) * var(--tan-alpha) / 2);
  --clip-padding: calc(var(--full-width) * var(--tan-alpha) / 2);
}

.diagonal-box {
  position: relative;
  padding: var(--skew-padding) 0;
  margin-top: -1px;
  
  &:before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    transform: skewy(var(--angle));
    transform-origin: 50% 0;
    outline: 1px solid transparent;
    backface-visibility: hidden;
  }
}

.bg-one:before {
  background-image: linear-gradient(45deg, #654ea3, #eaafc8);
}

.bg-two:before {
  background-image: linear-gradient(-135deg, #ff0084, #33001b);
}

.bg-three:before {
  background-image: linear-gradient(-135deg, #007, #003);
}

.content {
  max-width: var(--width);
  margin: 0 auto;
  padding: 1.5em;
  position: relative;
  
  /* -----------
  enable the border to see, that the content
  perfectly fits into the section withou
  bleeding into the adjecting areas:
  ------------ */
  // border: 2px dashed #fff8;
}

/* --------------------
Clip Path Update
-------------------- */

.clip-path {
  position: relative;
  margin-top: calc( ( var(--clip-padding) * -1 ) - 2px );
  background-image: 
    linear-gradient(rgba(0,0,0,0.05) 50%, 0, transparent 100%), 
    linear-gradient(-135deg, #0cc, #066);
  background-size: .5em .5em, 100% 100%;
  padding: calc( ( var(--clip-padding) * 2 ) - ( var(--clip-padding) - var(--skew-padding) ) ) 0 4em;
  clip-path: polygon(
    0% calc(var(--clip-padding) * 2), 
    100% 0%, 
    100% 100%, 
    0% 100% );
  -webkit-clip-path: polygon(
    0% calc(var(--clip-padding) * 2), 
    100% 0%, 
    100% 100%, 
    0% 100% );
}

/* --------------------
Presentational Styles 
-------------------- */

*, *:before, *:after {
  box-sizing: border-box; 
}

html {
  font-size: 100%;
  transition: font-size 0.2s linear;
  
  @media (min-width: 70em) {
    font-size: 125%;
  }
}

body {
  background: #003;
  padding-top: 8em;
  color: #fff;
  font-family: 'Raleway', sans-serif;
}

h1 {
  text-align: center;
  margin:0 auto 1em;
  padding: 0 1em;
  line-height: 1.2;
  transform: skewY(var(--angle));
  font-size: 3em;
  text-transform: uppercase;
  font-weight: 900;
}

h2 {
  font-size: 2.5em;
  margin: 0 0 0.5em;
  font-weight: 900;
}

.intro {
  font-size: 1.25em;
  transform: skewY(var(--angle));
  margin: 0em auto 0em;
  text-align: center;
  background: #fff;
  color: #003;
  font-weight: 900;
  padding: 0.5em;
  text-transform: uppercase;
  
  a {
    background-image: linear-gradient(transparent 90%, 0, #003 100%);
    background-image: none;
    border-bottom: 4px solid;
    transition: none;
    
    &:hover {
      border-color: #a06;
      opacity: 1;
    }
  }
}

p {
  font-size: 1.25em;
  margin: 0;
  line-height: 1.5;
  
  & + &,
  svg + & {
    margin-top: 1em;
  }
  
  code {
    background: #0033;
    padding: 0.125em 0.375em;
    border-radius: 0.125em;
    
    @media (min-width: 35em) {
      white-space: nowrap;
    }
  }
  
  a {
    color: inherit;
    text-decoration: none;
    background-image: linear-gradient(transparent 90%, 0, #fffa 100%);
    padding: 0.125em 0;
    //display: inline-block;
    transition: opacity 0.3s ease-out;
    
    &:hover {
      text-decoration: none;
      opacity: 0.8;
    }
  }
}

.columns {
  display: flex;
  margin: 2em -1em;
}

.figure {
  display: block;
  width: 100%;
  margin: 0 1em;
  
  svg {
    display: block;
    width: 100%;
  }
  
  .object {
    transform-origin: 140px 140px;    
    &--rotate {
      animation: rotate 3s ease-in-out alternate infinite;
    }
    
    &--skew {
      animation: skew 3s ease-in-out alternate infinite;
    }
    
    &--skew-pause {
      animation: skew-pause 6s ease-in-out infinite;
    }
    &--skew-pause-alt {
      animation: skew-pause-alt 6s ease-in-out infinite;
    }
  }
  
  figcaption {
    margin-top: 0.5em;
    line-height: 1.5;
    font-weight: 700;
    opacity: 0.9;
  }
}

@keyframes rotate {
  0% {transform: rotate(0deg);}
  50% {transform: rotate(-11deg);}
  100% {transform: rotate(-11deg) scaleX(1.2);}
}

@keyframes skew {
  to {transform: skewY(-11deg);}
}

@keyframes skew-pause {
  0%, 70%, 100% {transform: skewY(0deg);}
  20%, 50% {transform: skewY(-11deg);}
}

@keyframes skew-pause-alt {
  0%, 40%, 100% {transform: skewY(0deg);}
  20%, 30% {transform: skewY(-11deg);}
}

.formula {
  font-family: monospace;
  font-size: 1.5em;
  display: block;
  margin: 1em auto;
  text-align: center;
  
  @media (min-width: 26em) {
    font-size: 2em;
  }
}

.boxes {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 3%;
  margin: 2em 0;
  
  .reversed & {
    direction: rtl;
  }
  
  --translation: 0;
  
  .box {
    width: 100%;
    height: 0;
    padding-bottom: 100%;
    border: 1px solid #fff;
    background: #fff3;
    transform: translateY( var(--translation) );
    animation: translate 3s ease-in-out infinite;
    
    &:nth-child(1) { --translation: calc(var(--skew-padding) * 1.5)}
    &:nth-child(2) { --translation: calc(var(--skew-padding) * 1)}
    &:nth-child(3) { --translation: calc(var(--skew-padding) * 0.5)}
    &:nth-child(4) { --translation: calc(var(--skew-padding) * 0)}    
  }
}

@keyframes translate {
  0%, 20%, 100% { transform: translateY(0); }
  50%, 70% { transform: translateY(var(--translation)); }
}


/* ---------------------------------
   Interactive Controls
--------------------------------- */

.controls {
  background: #FFF3;
  z-index: 5;
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 0 0 0.5em 0.5em;
  max-width: 90%;
  
  &__headline {
    color: #fff;
    margin: 0.75em 1.125em 0.625em;
    font-size: 1em;
    text-align: center;
    font-weight: 400;
  }
}

.angle-control {
  padding: 0.75em 0.625em 0.625em;
  margin: 0 0.5em;
  font-size: 1em;
  border-top: 1px solid #fff3;
  display: flex;
  
  > * {
    vertical-align: middle;
    margin: 0 0.5em;
  }
  span {
    display: inline-block;
    min-width: 6ch;    
  }
  
  input {
    width: 8em;
    flex-shrink: 1;
  }
}

.result {
  text-align: right;
}

[hidden] {
  display: none;
}

<div class="controls">
  <h2 class="controls__headline">
    Playground:
  </h2>
  <div class="angle-control">
    <input type="range" id="angle-control" min="-60" max="60" step="1" value="-11">
    <span id="angle-result" class="result">-11 deg</span>
  </div>
</div>
<div class="diagonal-box">
  <div class="content">
    <h1>Tips for Pure CSS Diagonal Layouts<br>
Updated Version 2023</h1>
    <p class="intro">
      Below you will find a few tips for creating diagonal layouts. If this is all too fast for you, check out this <a href="https://9elements.com/blog/pure-css-diagonal-layouts/" target="_blank">step-by-step tutorial</a>.    
    </p>
  </div>
</div>
<div class="diagonal-box bg-one">
  <div class="content">
    <h2>1. Skew to the rescue.</h2>
    <p>
      When you <a href="#">rotate</a> a 100%-width box, you get some ugly corners and need to
      make the whole box wider than 100%. The problem here is that you maybe
      don't know the height of the element, and then you also don't know how
      much wider than 100% it has to be.
    </p>
    <p>
      So instead of <code>transform: rotate(-11deg)</code> use
      <code>transform: skewY(-11deg)</code> and the transformed section stays
      within it's horizontal boundaries.
    </p>
    <div class="columns">
      <figure class="figure">
        <svg viewBox="0 0 280 280">
          <rect
            fill="none"
            x="1"
            y="1"
            width="278"
            height="278"
            stroke="#FFF"
            stroke-width="2"
          />
          <rect
            class="object object--rotate"
            width="270"
            height="130"
            x="5"
            y="75"
            fill="#FFF"
            opacity="0.4"
          />
        </svg>
        <figcaption>transform: rotate(-11deg);</figcaption>
      </figure>

      <figure class="figure">
        <svg viewBox="0 0 280 280">
          <rect
            fill="none"
            x="1"
            y="1"
            width="278"
            height="278"
            stroke="#FFF"
            stroke-width="2"
          />
          <rect
            class="object object--skew"
            width="270"
            height="130"
            x="5"
            y="75"
            fill="#FFF"
            opacity="0.4"
          />
        </svg>
        <figcaption>transform: skew(-11deg);</figcaption>
      </figure>
    </div>
  </div>
</div>

<div class="diagonal-box bg-two">
  <div class="content">
    <h2>2. Use a pseudo-element.</h2>
    <p>
      If you want diagonal sections, but still write horizontally, you need to
      re-transform the content inside the section. What you can do instead is
      insert a <code>:before</code> pseudo-element, position it
      <code>absolute</code> and then transform this element instead of the
      section itself.
    </p>
    <div class="columns">
      <figure class="figure">
        <svg viewBox="0 0 280 280">
          <rect
            fill="none"
            x="1"
            y="1"
            width="278"
            height="278"
            stroke="#FFF"
            stroke-width="2"
          />
          <rect
            class="object object--skew-pause"
            width="270"
            height="130"
            x="5"
            y="75"
            fill="#FFF"
            opacity="0.4"
          />
          <rect
            class="object object--skew-pause-alt"
            width="220"
            height="80"
            x="30"
            y="100"
            fill="#FFF"
            opacity="0.4"
          />
        </svg>
        <figcaption>
          The content needs to be re-transformed, when you transform the whole
          section.
        </figcaption>
      </figure>

      <figure class="figure">
        <svg viewBox="0 0 280 280">
          <rect
            fill="none"
            x="1"
            y="1"
            width="278"
            height="278"
            stroke="#FFF"
            stroke-width="2"
          />
          <rect
            class="object object--skew-pause"
            width="270"
            height="130"
            x="5"
            y="75"
            fill="#FFF"
            opacity="0.4"
          />
          <rect
            class="object"
            width="220"
            height="80"
            x="30"
            y="100"
            fill="#FFF"
            opacity="0.4"
          />
        </svg>
        <figcaption>
          Content is not affected when transforming a pseudo-element in the
          background.
        </figcaption>
      </figure>
    </div>
  </div>
</div>

<div class="diagonal-box bg-three">
  <div class="content">
    <h2>3. Find the right padding.</h2>
    <p>
      Because of the transformation, some elements <em>bleed</em> into the previous and the next element. To find a safe area where you can place content, you need to add some padding. The amount of padding can be calculated with this formula:<br>
      <span class="formula">x = tan(&alpha;) * a / 2</span>
    </p>
    <svg viewBox="0 0 560 305">
      <g fill="none" fill-rule="evenodd">
        <rect
          width="558"
          height="198"
          x="1"
          y="53"
          stroke="#FFF"
          stroke-width="2"
        />
        <polygon
          fill="#FFF"
          points="6 106.52 554 0 554 198 6 304.52"
          opacity=".3"
        />
        <line
          x1="554.5"
          x2="554.5"
          y2="51"
          stroke="#FFF"
          stroke-dasharray="2 2"
          stroke-width="2"
        />
        <line
          x1="6.5"
          x2="6.5"
          y1="53"
          y2="104"
          stroke="#FFF"
          stroke-dasharray="2 2"
          stroke-width="2"
        />
        <path
          fill="#FFF"
          fill-rule="nonzero"
          d="M325.1 33.3c1.3 0 2-1.7 2-3.7h-.3c-.2 1.5-.5 2-.9 2-.7 0-1.5-2.3-1.7-3.5l2.8-6.8h-2.5l-1.2 3.5c-.5-1.8-1.7-3.8-4-3.8-3.2 0-5.1 2.9-5.1 6.2 0 3.5 2 6 4.9 6 2 0 3-1.2 4-2.8.3 1.7 1 2.9 2 2.9zm-5.8-.8c-2.3 0-2.8-4.7-2.8-6.6 0-3 1.4-4.1 2.7-4.1 1.9 0 2.6 3.9 2.8 5.8-.2 1.4-1 5-2.7 5z"
        />
        <text fill="#FFF" font-family="Raleway" font-size="26">
          <tspan x="273" y="153">a</tspan>
        </text>
        <text fill="#FFF" font-family="Raleway" font-size="26">
          <tspan x="17.1" y="88">x</tspan>
        </text>
        <text fill="#FFF" font-family="Raleway" font-size="26">
          <tspan x="530.1" y="35">x</tspan>
        </text>
        <line
          x1="6"
          x2="554"
          y1="165"
          y2="165"
          stroke="#FFF"
          stroke-dasharray="2 2"
          stroke-width="2"
        />
        <path
          stroke="#FFF"
          stroke-dasharray="1 1"
          d="M346 53c0-4.1-.4-8.1-1-12"
        />
      </g>
    </svg>
    <p>In 2020, when this article was originally published, calculating the tangent of an angle in CSS required some complex workarounds or the use of JavaScript. However, with the latest updates in CSS, we can now use the <strong>tan()</strong> function to calculate the tangent of an angle directly in our stylesheets.</p>
  </div>
</div>

<div class="diagonal-box bg-one">
  <div class="content">
    <h2>4. Use CSS-Variables to store the padding-value.</h2>
    <p>You can use CSS Custom Properties to store the calculated value for the needed padding and reuse it. For example you can translate elements so that they are in line with the diagonal background-line.</p>
    <p><code>transform: translateY(var(--skew-padding))</code></p>
    <div class="boxes">
      <div class="box"></div>
      <div class="box"></div>
      <div class="box"></div>
      <div class="box"></div>
    </div>
  </div>
</div>

<div class="diagonal-box bg-two">
  <div class="content">
    <h2>And that's it</h2>
    <p>
      If this all went too fast for you, you find a more <a href="https://9elements.com/blog/pure-css-diagonal-layouts/" target="_blank">detailed article here</a>. And for all further questions, you can find me on <a href="https://twitter.com/supremebeing09" target="_blank">Twitter</a>.
      Thanks for reading. 
    </p>
  </div>
</div>
<div class="clip-path">
  <div class="content">
    <h2>Update 28. Feb. 2020:<br>Combine with Clip-Path</h2>
    <p>Quite a few people mentioned to me that you could also do this by using clip-path. So I added this section here, where there is no skew-transform, but parts of the section are hidden with clip-path.</p>
    <p>This technique works fine as well, only the calculation of the padding is a little harder, as you need both the width of the container and the width of the viewport.</p>
    <p>The significant advantage, though: you can place background-images to the section without them being transformed.</p>
  </div>
</div>
```


### 99.x – Divider Originalreferenz A – SVG-Schräg-Divider

Ursprüngliche Zusatzdatei: `nurovelle-divider-svg-original-reference.txt`  
Status: in Projektfiles übernommen / Original- oder Arbeitsreferenz

```text
body {
  overflow-x: hidden;
}

.section-one {
  background-color: #5FC18B;
  position: relative;
  padding: 200px 0 350px;
  .section-one__title {
    color: #fff;
    font-size: 35px;
    margin-bottom: 30px;
    text-align: center;
  }
  .section-one__descr {
    color: #fff;
    font-size: 16px;
    line-height: 1.5;
    max-width: 300px;
    margin: 0 auto;
    text-align: center;
  }
}

.section-two {
  background-color: #44a36f;
  padding: 100px 0 200px;
  position: relative;
  z-index: 10;
  .section-two__title {
    color: #fff;
    font-size: 35px;
    margin-bottom: 30px;
    text-align: center;
  }
  .section-two__descr {
    color: #fff;
    font-size: 16px;
    line-height: 1.5;
    max-width: 300px;
    margin: 0 auto;
    text-align: center;
  }
}

/* -------------------------------------------------------------------------
   begin Separator
 * ------------------------------------------------------------------------- */
.separator {
  bottom: -4px;
  left: 0;
  overflow: hidden;
  position: absolute;

  width: 100%;
}
/* -------------------------------------------------------------------------
   end Separator
 * ------------------------------------------------------------------------- */

/* begin Media Max-Width 767
============================================================================ */

@media screen and (max-width: 767px) {
  .section-one {
    padding: 130px 0 190px;
  }
  .separator {
    bottom: -110px;
    .separator__svg {
      left: -20%;
      position: relative;
      transform: rotate(15deg);
      width: 140%;
    }
  }
}

/* end Media Max-Width 767
============================================================================ */

<div class="section-one">
  <h2 class="section-one__title">Awesome Section - 1</h2>
  <p class="section-one__descr">Not far stuff she think the jokes. Going as by do known noise he wrote round leave. Warmly put branch people narrow see. Winding its waiting yet parlors married own feeling. Marry fruit do spite jokes an times. Whether at it unknown warrant herself
    winding if. Him same none name sake had post love. An busy feel form hand am up help. Parties it brother amongst an fortune of. Twenty behind wicket why age now itself ten.</p>
  <!-- begin Separator -->
  <div class="separator">
    <svg class="separator__svg" width="100%" height="400" viewBox="0 0 100 100" preserveAspectRatio="none" fill="#44A36F" version="1.1" xmlns="http://www.w3.org/2000/svg">
       <path d="M 100 100 V 10 L 0 100"/>
       <path d="M 30 73 L 100 18 V 10 Z" fill="#308355" stroke-width="0"/>
      </svg>
  </div>
  <!-- end Separator -->
</div>
<div class="section-two">
  <h2 class="section-two__title">Awesome Section - 2</h2>
  <p class="section-two__descr">From they fine john he give of rich he. They age and draw mrs like. Improving end distrusts may instantly was household applauded incommode. Why kept very ever home mrs. Considered sympathize ten uncommonly occasional assistance sufficient not. Letter
    of on become he tended active enable to. Vicinity relation sensible sociable surprise screened no up as.</p>
</div>

```


### 99.x – Divider Originalreferenz B – Pure-CSS-Angled-Sections

Ursprüngliche Zusatzdatei: `nurovelle-divider-pure-css-angled-original-reference.scss`  
Status: in Projektfiles übernommen / Original- oder Arbeitsreferenz

```scss
﻿@use 'sass:math';

// set an angled section value
$angle: 5deg;

// have guardails in place for angle value
$angle: math.max(0deg, math.min($angle, 15deg));
// compute vertical spacing needed for this angle
$space: 100vw*math.tan($angle);
// length of angled edge for this angle
$hypot: 100vw/math.cos($angle);

$base: .5rem; // base spacing
$size: 2*$base; // footer background size

/* register variables so they have fallback values 
 * for no CSS trigonometric functions support
 * (as of Feb 2023, Chromium supports @property, 
 * but only supports CSS trigonometric functions 
 * starting with version 111 and behind a flag) */
@property --angle {
	syntax: '<angle>';
	initial-value: #{$angle};
	inherits: true
}

@property --space {
	syntax: '<length-percentage>';
	initial-value: #{$space};
	inherits: true
}

@property --hypot {
	syntax: '<length-percentage>';
	initial-value: #{$hypot};
	inherits: true
}

* { margin: 0 } /* silly little reset */

/* basic layout */
html, body, section, footer { display: grid }
/* guardrails */
html { overflow-x: hidden; }

body {
	overflow: hidden; /* cut off bottom footer margin */
	/* responsive, but within limits font */
	font: clamp(.75em, 3.25vw, 1.5em)/ 1.25 ubuntu, 
		trebuchet ms, verdana, arial, sans-serif;
	/* avoid weird dark spacing between sectins glitch */
	filter: drop-shadow(0 1px 1px #dedede)
}

header, section, footer {
	/* negative vertical spacing needed for overlap */
	margin: calc(-.5*var(--space)) 0;
	/* spacing allowed by angled verion vertically, 
	 * base spacing laterally */
	padding: calc(var(--space)) #{$base};
}

header, footer { /* page ends base styles */
	background: #121212;
	color: #ededed
}

header {
	/* se it doesn't stick to left */
	padding-left: 5vw;
	/* graphing paper */
	background-image: 
		conic-gradient(from 90deg at 1px 1px, 
				transparent 25%, 
				hsla(0, 0%, 100%, .1) 0%);
	background-size: $base $base
}

section, footer {
	grid-gap: 2*$base; /* space between paragraphs */
	/* put each item on their grid in its cell middle
	 * along both axes */
	place-items: center
}

/* for reference: 
 * DRY switching for numeric values
 * https://css-tricks.com/dry-switching-with-css-variables-the-difference-of-one-declaration/ 
 * DRY switching for keyword values 
 * https://css-tricks.com/dry-state-switching-with-css-variables-fallbacks-and-invalid-values/ */
section {
	--_p: var(--p, 0); /* parity flag dfault value */
	--not-p: calc(1 - var(--_p)); /* complementary */
	--sgn-p: calc(2*var(--_p) - 1); /* parity sign */
	/* to attach absolutely positioned pseudo */
	position: relative;
	/* tiny adjustment to bottom padding */
	padding-bottom: calc(var(--space) + #{$base});
	/* give each a pastel gradient */
	background: 
		linear-gradient(to bottom right, var(--sl));
	/* angled clip */
	clip-path: 
		polygon(calc(var(--not-p)*100%) 0, 
			calc(var(--_p)*100%) var(--space), 
			calc(var(--_p)*100%) calc(100% - var(--space)), 
			calc(var(--not-p)*100%) 100%);
	
	/* change parity flag value from default 0 
	 * to 1 on even items */
	&:nth-of-type(2n) { --p: 1 }
	
	&::after { /* creates to section shadow */
		position: absolute; /* take out of flow */
		/* middle of vertical spacing from top */
		top: calc(.5*var(--space));
		/* from half the parent minus half of itself */
		left: calc(50% - .5*var(--hypot));
		/* its width is that of the angled edge */
		width: var(--hypot);
		height: 2*$base; /* small height */
		/* rotate one way or another depending on parity */
		transform: rotate(calc(var(--sgn-p)*var(--angle)));
		background: /* visual "shadow" */
			radial-gradient(farthest-side at 50% 0, 
					hsla(0, 0%, 0%, .375), 
					hsla(0, 0%, 0%, .125), 
					transparent) 50% 0/ 115% 100%;
		/* thought it makes it look better
		 * not that important, could be ditched */
		mix-blend-mode: multiply;
		content: '' /* so pseudo shows up */
	}
}

h2 {
	/* avoid padding adding to width */
	box-sizing: border-box;
	margin: 
		/* move up to attach to top of angled section */
		calc(-1*var(--space)) 
		/* if even, go outside section on the right
		 * by its own width minus parent's width */
		calc(var(--_p)*(100% - var(--hypot)))
		/* compensate for negative top margin, so  
		 * elements after it don't move up too */
		var(--space)
		/* if odd, go outside section on the left
		 * by its own width minus parent's width */
		calc(var(--not-p)*(100% - var(--hypot)));
	/* its width is that of an angled section */
	width: var(--hypot);
	/* limit text line length via padding lateral */
	padding: $base calc(.5*(var(--hypot) - 18em));
	/* rotate around top right/ left depending on parity */
	transform-origin: calc(var(--not-p)*100%) 0;
	/* rotate one way or another depending on parity */
	transform: rotate(calc(var(--sgn-p)*var(--angle)));
	/* align right or default left depending on parity */
	text-align: var(--p, right);
	/* for better contrast with background
	 * not that important, could be ditched */
	text-shadow: 1px 1px #fff
}

/* limit paragraph width */
p { max-width: 39em }

/* for reference: feature support info boxes
 * https://codepen.io/thebabydino/full/qBKvjKM */
.box {
	/* initial value for passing support test flag */
	--pass: 0;
	--not-pass: calc(1 - var(--pass)); /* complementary */
	/* avoid padding & border adding to width */
	box-sizing: border-box;
	border: solid 1px 
		/* border-color depends on passing support test */
		hsl(
			calc(359 - var(--pass)*261), 
			calc(47% - var(--pass)*15%), 
			calc(51% - var(--pass)*6%));
	border-left-width: 5px; /* thicker left border */
	padding: $base;
	/* box palette depends on passing support test */
	background: hsla(0, 0%, calc(var(--pass)*100%), .57);
	color: hsl(0, 0%, calc(var(--not-pass)*100%));
	
	/* change flag on passed support test box */
	&[data-view='pass'] { --pass: 1 }
}

/* before testing, hasn't passed support test, 
 * default to fail */
[data-view='fail'] { display: block }
[data-view='pass'] { display: none }

/* code boxes text */
code, kbd, style { font: 1.125em ubuntu mono, consolas, monaco, monospace }

code, kbd {
	/* since we're adding a background, prevent text 
	 * from sticking to edges of this background */
	padding: 1px 3px;
	background: hsla(0, 0%, 100%, .25)
}

style, a {
	--hl: 0; /* highlight state flag, initial value */
	/* shrink width to content for style, 
	 * avoid messing up pseudo edge attachment for links */
	display: inline-block;
	/* to attach absolutely positioned pseudo */
	position: relative;
	
	/* ditch ugly focus outline */
	&:focus { outline: none }
	/* switch highlight flag to 1 */
	&:focus, &:hover { --hl: 1 }
	
	&::before {
		position: absolute; /* take out of flow */
		content: '' /* so that pseudo shows up */
	}
}

style { /* interactive code box */
	margin-top: $base; /* a bit of spacing around */
	/* create spacing around to be fille by 
	 * pseudo-created background */
	border: solid $base transparent;
	/* box glow in a highlight state (hover, focus) */
	box-shadow: 
		2px 2px 5px hsla(0, 0%, 7%, calc(var(--hl)*.65));
	color: #dedede; /* fallback text color */
	/* some stupid syntax highlighting
	 * remove it by removing / at end of this line */
	background: 
		linear-gradient(-90deg, white 1ch, transparent 0), 
		linear-gradient(90deg, #ffe53b 4.5ch, 
				#dedede 0 6.5ch, #f58ad9 0 21ch, 
				#dedede 0 22ch, #3bffa3 0);
	-webkit-background-clip: text;
	color: transparent;/**/
	/* text glow in a highlight state (hover, focus) */
	text-shadow: 
		0 0 calc(var(--hl)*5px) hsla(0, 0%, 100%, .65);
	transition: .3s ease-out; /* smooth state change */
	transition-property: box-shadow, text-shadow;
	
	&::before {
		z-index: -1; /* place under parent */
		/* fill border space around parent */
		inset: -1*$base;
		background: #121212; /* dark contrasting background */
	}
}

footer {
	/* avoid stop list & full gradient repetition */
	--sl: calc(100% - 1px), transparent;
	--g0: 
		radial-gradient(circle 2px, 
				hsl(0, 0%, 3%) var(--sl));
	--g1: 
		radial-gradient(circle 2px 
				at calc(50% + 1px) calc(50% + 1px), 
				hsl(0, 0%, 17%) var(--sl));
	/* "holes" background made up of multiple gradients */
	background-image: 
		var(--g0), var(--g0), var(--g1), var(--g1);
	background-position: 0 0, $base $base;
	background-size: $size $size;
	font-size: Max(.625rem, .75em); /* limit font size */
	text-align: center /* middle-align text */
}

/* for reference: link XOR effect explained
 * https://css-tricks.com/taming-blend-modes-difference-and-exclusion/#aa-now-lets-turn-to-the-what-of-blend-modes */
a {
	z-index: 1;
	/* since we're adding a background, prevent text 
	 * from sticking to edges of this background */
	padding: 0 2px;
	color: #fc8621;
	text-decoration: none; /* ditch underline */
	isolation: isolate;
	
	&::before {
		/* for reference: inset
		 * https://twitter.com/anatudor/status/1478412237295566850 */
		inset: 0; /* cover parent's padding area */
		transform-origin: 0 100%; /* relative to bottom */
		/* cover parent of just tiny strip at bottom 
		 * depending on whether in highlight state or not */
		transform: 
			scaley(calc(var(--hl) + .1*(1 - var(--hl))));
		/* same background as parent color */
		background: currentcolor;
		mix-blend-mode: difference; /* XOR effect */
		/* smooth grow from underline to parent cover */
		transition: transform .3s ease-out
	}
}

[data-ico] { /* if followed by emoji icon */
	margin-right: 1.5em; /* pretty much icon size */
	
	&::after {
		position: absolute; /* take out of flow */
		/* its left edge is 2px to the right of right edge */
		left: calc(100% + 2px);
		content: attr(data-ico) /* so it shows up */
	}
}

@supports (z-index: tan(0deg)) { /* if trig in CSS is supported */
	body {
		/* make angle & all values depending on it actually dynamic, 
		 * not just "glorified constants" */
		--angle: clamp(0deg, var(--custom-angle), var(--limit, 15deg));
		--space: calc(100vw*tan(var(--angle)));
		--hypot: calc(100vw/cos(var(--angle)))
	}
	
	[data-feat='trig'] {
		/* CSS trig support info boxes display toggle */
		&[data-view='fail'] { display: none }
		&[data-view='pass'] { display: block }
	}
}

/* this is a funny one, not supported everywhere */
@supports (rotate: atan2(1vh, 1vw)) {
	/* make angle limit actually dynamic depending on 
	 * viewport aspect ratio if supported */
	body { --limit: calc(.25*atan2(1vh, 1vw)) }
}






```


### 99.x – CTA-Button Originalreferenzen

Ursprüngliche Zusatzdatei: `nurovelle-button-original-references.md`  
Status: in Projektfiles übernommen / Original- oder Arbeitsreferenz

```markdown
# Nurovelle Button Original References

Status: Originalreferenzen aus Nutzervorgabe 2026-07-07  
Einordnung: Referenzcode, nicht Produktionscode.  
Regel: Es wird nur die Logik übernommen. Demo-Texte, React-Struktur, styled-components-Pflicht und Demo-Farben werden nicht übernommen. Die Gold-Farblogik wird separat als Farbbasis verwendet.

---

## 1. Arrow-Reveal / Circle-Fill Button – Originalreferenz

Quelle: vom Nutzer gelieferter React/styled-components Code.  
Übernehmbar: Pfeil rechts raus, Pfeil links rein, Textverschiebung, Kreis expandiert zur Buttonfläche, Active-Scale.  
Nicht übernehmen: `greenyellow`, Demo-Text `Modern Button`, React-/styled-components-Pflicht.

```jsx
<button className="animated-button">
  <svg viewBox="0 0 24 24" className="arr-2" xmlns="http://www.w3.org/2000/svg">
    <path d="M16.1716 10.9999L10.8076 5.63589L12.2218 4.22168L20 11.9999L12.2218 19.778L10.8076 18.3638L16.1716 12.9999H4V10.9999H16.1716Z" />
  </svg>
  <span className="text">Modern Button</span>
  <span className="circle" />
  <svg viewBox="0 0 24 24" className="arr-1" xmlns="http://www.w3.org/2000/svg">
    <path d="M16.1716 10.9999L10.8076 5.63589L12.2218 4.22168L20 11.9999L12.2218 19.778L10.8076 18.3638L16.1716 12.9999H4V10.9999H16.1716Z" />
  </svg>
</button>
```

```css
.animated-button {
  position: relative;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 16px 36px;
  border: 4px solid;
  border-color: transparent;
  font-size: 16px;
  background-color: inherit;
  border-radius: 100px;
  font-weight: 600;
  color: greenyellow;
  box-shadow: 0 0 0 2px greenyellow;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button svg {
  position: absolute;
  width: 24px;
  fill: greenyellow;
  z-index: 9;
  transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button .arr-1 { right: 16px; }
.animated-button .arr-2 { left: -25%; }

.animated-button .circle {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 20px;
  height: 20px;
  background-color: greenyellow;
  border-radius: 50%;
  opacity: 0;
  transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button .text {
  position: relative;
  z-index: 1;
  transform: translateX(-12px);
  transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button:hover {
  box-shadow: 0 0 0 12px transparent;
  color: #212121;
  border-radius: 12px;
}

.animated-button:hover .arr-1 { right: -25%; }
.animated-button:hover .arr-2 { left: 16px; }
.animated-button:hover .text { transform: translateX(12px); }
.animated-button:hover svg { fill: #212121; }
.animated-button:active {
  scale: 0.95;
  box-shadow: 0 0 0 4px greenyellow;
}
.animated-button:hover .circle {
  width: 220px;
  height: 220px;
  opacity: 1;
}
```

---

## 2. Press-Button / haptische Absenkung – Originalreferenz

Quelle: vom Nutzer gelieferter React/styled-components Code.  
Übernehmbar: echte Buttonstruktur mit Top-, Bottom- und Base-Ebene; Topfläche senkt sich bei Active; Unterteil verändert Radius/Polsterung.  
Nicht übernehmen: Demo-Türkis/Grün, Demo-Text `Button`, React-/styled-components-Pflicht.

```jsx
<button type="button" className="button">
  <div className="button-top">Button</div>
  <div className="button-bottom" />
  <div className="button-base" />
</button>
```

```css
.button {
  -webkit-appearance: none;
  appearance: none;
  position: relative;
  border-width: 0;
  padding: 0 8px 12px;
  min-width: 10em;
  box-sizing: border-box;
  background: transparent;
  font: inherit;
  cursor: pointer;
}

.button-top {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 0;
  padding: 8px 16px;
  transform: translateY(0);
  text-align: center;
  color: #fff;
  text-shadow: 0 -1px rgba(0, 0, 0, .25);
  transition-property: transform;
  transition-duration: .2s;
  -webkit-user-select: none;
  user-select: none;
}

.button:active .button-top { transform: translateY(6px); }

.button-top::after {
  content: '';
  position: absolute;
  z-index: -1;
  border-radius: 4px;
  width: 100%;
  height: 100%;
  box-sizing: content-box;
  background-image: radial-gradient(#3dcd9e, #369d8d);
  text-align: center;
  color: #fff;
  box-shadow: inset 0 0 0px 1px rgba(255, 255, 255, .2), 0 1px 2px 1px rgba(255, 255, 255, .2);
  transition-property: border-radius, padding, width, transform;
  transition-duration: .2s;
}

.button:active .button-top::after {
  border-radius: 6px;
  padding: 0 2px;
}

.button-bottom {
  position: absolute;
  z-index: -1;
  bottom: 4px;
  left: 4px;
  border-radius: 8px / 16px 16px 8px 8px;
  padding-top: 6px;
  width: calc(100% - 8px);
  height: calc(100% - 10px);
  box-sizing: content-box;
  background-color: #38a19d;
  background-image: radial-gradient(4px 8px at 4px calc(100% - 8px), rgba(255, 255, 255, .25), transparent), radial-gradient(4px 8px at calc(100% - 4px) calc(100% - 8px), rgba(255, 255, 255, .25), transparent), radial-gradient(16px at -4px 0, white, transparent), radial-gradient(16px at calc(100% + 4px) 0, white, transparent);
  box-shadow: 0px 2px 3px 0px rgba(0, 0, 0, 0.5), inset 0 -1px 3px 3px rgba(0, 0, 0, .4);
  transition-property: border-radius, padding-top;
  transition-duration: .2s;
}

.button:active .button-bottom {
  border-radius: 10px 10px 8px 8px / 8px;
  padding-top: 0;
}

.button-base {
  position: absolute;
  z-index: -2;
  top: 4px;
  left: 0;
  border-radius: 12px;
  width: 100%;
  height: calc(100% - 4px);
  background-color: rgba(0, 0, 0, .15);
  box-shadow: 0 1px 1px 0 black, inset 0 2px 2px rgba(0, 0, 0, .25);
}
```

---

## 3. Golden-Button-Farblogik – Originalreferenz

Quelle: vom Nutzer gelieferter Goldbutton-Code.  
Übernehmbar: Gold-Gradient, Border, Innenkanten, Textfarbe, Shadow-Logik, Hover-Aufweitung von `background-size`.  
Nicht übernehmen: Demo-Text `Golden Button`, `role="button"` auf echtem `<button>`, Casino-/Spielautomatwirkung.

```css
:root {
  --cta-gold-dark: #a54e07;
  --cta-gold-mid: #b47e11;
  --cta-gold-light: #fef1a2;
  --cta-gold-core: #bc881b;
  --cta-gold-border: #a55d07;
  --cta-gold-inner-dark: #8b4208;
  --cta-gold-inner-mid: #b17d10;
  --cta-gold-highlight: #fae385;
  --cta-gold-text-dark: rgb(120, 50, 5);
  --cta-gold-gradient: linear-gradient(160deg, #a54e07, #b47e11, #fef1a2, #bc881b, #a54e07);
}
```

```css
.golden-button {
  touch-action: manipulation;
  display: inline-block;
  outline: none;
  font-family: inherit;
  font-size: 1em;
  box-sizing: border-box;
  border: none;
  border-radius: 0.3em;
  height: 2.75em;
  line-height: 2.5em;
  text-transform: uppercase;
  padding: 0 1em;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(110, 80, 20, 0.4), inset 0 -2px 5px 1px rgba(139, 66, 8, 1), inset 0 -1px 1px 3px rgba(250, 227, 133, 1);
  background-image: linear-gradient(160deg, #a54e07, #b47e11, #fef1a2, #bc881b, #a54e07);
  border: 1px solid #a55d07;
  color: rgb(120, 50, 5);
  text-shadow: 0 2px 2px rgba(250, 227, 133, 1);
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  background-size: 100% 100%;
  background-position: center;
}

.golden-button:focus,
.golden-button:hover {
  background-size: 150% 150%;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23), inset 0 -2px 5px 1px #b17d10, inset 0 -1px 1px 3px rgba(250, 227, 133, 1);
  border: 1px solid rgba(165, 93, 7, 0.6);
  color: rgba(120, 50, 5, 0.8);
}

.golden-button:active {
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(110, 80, 20, 0.4), inset 0 -2px 5px 1px #b17d10, inset 0 -1px 1px 3px rgba(250, 227, 133, 1);
}
```

```


### 99.x – Section-/Board-CodePen-Referenz

Ursprüngliche Zusatzdatei: `nurovelle-section-board-codepen-reference.md`  
Status: in Projektfiles übernommen / Original- oder Arbeitsreferenz

```markdown
# Nurovelle Section-/Board-CodePen-Referenz

Status: externe Referenz / Prüfoption, nicht finale Umsetzung.  
Quelle: https://codepen.io/josephrexme/pen/oNNpZYJ  
Abruf: 2026-07-07

Einordnung:
- Option für eine Section-/Board-Komponente.
- Keine Produktionsfreigabe.
- Keine 1:1-Übernahme.
- Externe Demo-Inhalte, Namen, Avatare, Farben, Finanz-/Wallet-Kontext und Demo-Icons werden nicht übernommen.
- Semantik und Accessibility müssen korrigiert werden; in der Referenz kommt `arial-label` vor, korrekt ist `aria-label`.

Übernehmbar nach Prüfung:
- Board-/Panel-Struktur
- seitliche Icon-Navigation
- aktiver Zustand über Attribut/Klasse
- Panel-/Dashboard-Anmutung als technische Prüfvariante
- Hover-/Focus-Zustände

Nicht übernehmen:
- Demo-Farben
- Demo-Texte
- Demo-Logo
- externe Bild-URLs
- Finanz-/Wallet-Inhalte
- fehlerhafte ARIA-Schreibweise

```


### Korrektur 2026-07-10 – Divider-A-Doppelprüfung

Für die aktuelle Live-Prüfung ist die Divider-Abfolge testweise. Variante A muss zweimal direkt nacheinander über aufeinanderfolgende Section-Übergänge dargestellt werden, damit ihre Wirkung im wiederholten Einsatz beurteilt werden kann. Erst nach Sichtprüfung wird festgelegt, welcher Divider tatsächlich verwendet wird.

Testabfolge:

1. Hero → Section 2: Divider A
2. Section 2 → Section 3: Divider A erneut
3. Section 3 → Section 4: Divider B normal
4. Section 4 → Section 5: Divider B reverse
5. Section 5 → Section 6: Divider C
