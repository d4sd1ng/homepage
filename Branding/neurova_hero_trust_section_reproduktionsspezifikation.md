# Neurova Homepage – Hero + Trust Section Reproduktionsspezifikation

Stand: final festgelegt
Ziel: Diese Sektion muss später 1:1 reproduzierbar sein.

---

## 1. Grundregel

Die Trust Section ist keine neue, eigenständige Sektion.
Sie ist die direkte Erweiterung der Hero Section.

Nicht erlaubt:
- keine fremden Boxen
- keine billigen Icons
- keine weißen oder hellen Container
- keine neue Designrichtung
- keine sichtbare starke Section-Trennung
- keine grünen Buttons
- keine generischen Karten
- keine Standard-Trust-Badges

Erlaubt:
- gleiche dunkle Hintergrundwelt wie Hero
- gleiche goldene Linien und Akzente
- gleiche Circuit-/Tech-Atmosphäre
- gleiche Typografie
- gleiche horizontale Struktur
- dezente goldene Trennlinien
- Tech-Stats statt Cards
- keine großen Symbol-Illustrationen

---

## 2. Hero Section – finaler Zustand

### Layout

- Full-width Desktop Hero
- Header oben
- Hero Content links
- 3D-Tech-Cube rechts
- dunkler Background mit Smoke und Circuit-Strukturen
- Gold/Weiß-Kontrast
- CTA-Bereich links unter Text

### Header

Links:
- Neurova Logo
- Claim: Building Intelligent Systems

Navigation:
- HOME
- LEISTUNGEN
- SAAS-PRODUKTE
- LÖSUNGEN
- ÜBER MICH
- BLOG
- KONTAKT

Rechts:
- Button: KOSTENLOSE ANALYSE
- Button gold oder gold umrandet
- kleines Kalender-Icon ist erlaubt, aber hochwertig und reduziert

### Hero Text

Obere Hauptzeile:
KI-AUTOMATISIERUNG

Zweite Hauptzeile:
FÜR UNTERNEHMEN

Subheadline:
KÜNSTLICHE INTELLIGENZ. ECHTE ERGEBNISSE.

Fließtext:
Ich entwickle KI-Agenten, smarte Prozesse und maßgeschneiderte Automatisierungslösungen für Ihr Unternehmen.

CTA 1:
KOSTENLOSE POTENZIAL ANALYSE BUCHEN

CTA 2:
UNSERE KI LÖSUNGEN ENTDECKEN

---

## 3. Trust Section – final festgelegt

### Position

Direkt unter der Hero Section.
Sie muss wie eine Hero-Bottom-Bar wirken.
Nicht wie eine neue Content-Sektion.

### Aufbau

Die Trust Section besteht aus zwei horizontalen Bereichen:

Links:
- Headline
- kurzer Vertrauens-/Story-Text

Rechts:
- 4 horizontale Tech-Stats
- getrennt durch feine goldene Vertikallinien
- keine großen Icons
- keine Card-Boxen
- keine Emoji-Icons

### Headline

35+ JAHRE CODE. EINE MISSION: FUNKTIONIERENDE KI-SYSTEME.

### Text

Meine Reise begann mit BASIC auf dem Commodore 64. Heute entwickle ich autonome KI-Agenten, Automatisierungssysteme und datengetriebene Prozesse für Unternehmen. Der Fokus blieb dabei immer gleich: robuste Technik statt kurzfristiger Hype.

### Tech-Stats

Stat 1:
35+
JAHRE
PROGRAMMIERERFAHRUNG

Stat 2:
KI-AGENTEN
& AUTOMATISIERUNG

Stat 3:
MESSBARE
PROZESSOPTIMIERUNG

Stat 4:
PERSÖNLICHE
BETREUUNG

---

## 4. Visuelle Regeln für die Trust Section

### Hintergrund

- gleicher dunkler Hintergrund wie Hero
- Schwarz bis sehr dunkles Blau/Anthrazit
- dezente Circuit-Linien im Hintergrund
- goldene Glow-Punkte nur sehr sparsam
- keine neue Textur
- keine weiße Fläche

### Trennung zur Hero

- eine dünne goldene horizontale Linie zwischen Hero und Trust-Bar
- keine große Lücke
- keine helle Section-Kante

### Trust-Bar Layout

Desktop:
- Höhe ca. 230–280 px
- links ca. 42 % Breite
- rechts ca. 58 % Breite
- Innenabstand links/rechts wie Hero
- vertikale Ausrichtung mittig

Links:
- Headline oben
- Text darunter
- Textbreite begrenzt

Rechts:
- 4 gleich breite Stat-Spalten
- feine goldene vertikale Trenner
- keine runden Icons
- keine Illustrationen
- optional: kleine technische Linienpunkte auf der unteren Achse

### Typografie

Titel / große Hero-Schrift:
- Bebas Neue

Überschriften / Tech-Headlines:
- Anca Coder
- Fallback: monospace / Courier New

Fließtexte:
- Raleway

### Farben

Background:
- #030404
- #05070B
- #0A1018

Gold:
- #D9A12F
- #F0B739
- #C8871A

Weiß:
- #F5F5F2

Muted Text:
- #B9B6AE
- #A7A39A

Linien:
- rgba(217,161,47,0.55)
- rgba(255,255,255,0.08)

---

## 5. Was ausdrücklich nicht wieder passieren darf

- keine Roboter-Icons
- keine Chart-Icons
- keine Personen-Icons
- keine Code-Klammer-Icons als große Symbole
- keine billigen Line-Icons
- keine Kartenoptik für die Trust-Werte
- keine neue Section mit eigenem Hintergrund
- keine farbigen Fremdakzente
- keine grünen Akzente
- keine Standard-SaaS-Trust-Badges
- keine generische Bootstrap-Optik

---

## 6. Reproduktionsprompt für Bildgenerierung / Design-Tool

Erstelle nur die Trust-Erweiterung unter der bestehenden Hero Section. Die Hero selbst bleibt unverändert. Die Trust Section muss wie eine direkte Hero-Bottom-Bar wirken: gleicher dunkler High-Tech-Hintergrund, goldene Circuit-Linien, keine neue Section-Optik, keine Cards, keine billigen Icons. Links steht die Headline „35+ JAHRE CODE. EINE MISSION: FUNKTIONIERENDE KI-SYSTEME.“ in gold/weiß mit Anca-Coder/Bebas-Neue-Anmutung. Darunter der Text: „Meine Reise begann mit BASIC auf dem Commodore 64. Heute entwickle ich autonome KI-Agenten, Automatisierungssysteme und datengetriebene Prozesse für Unternehmen. Der Fokus blieb dabei immer gleich: robuste Technik statt kurzfristiger Hype.“ Rechts vier horizontale Tech-Stats ohne Icons, getrennt durch feine goldene vertikale Linien: „35+ JAHRE PROGRAMMIERERFAHRUNG“, „KI-AGENTEN & AUTOMATISIERUNG“, „MESSBARE PROZESSOPTIMIERUNG“, „PERSÖNLICHE BETREUUNG“. Keine Roboter-Icons, keine Chart-Icons, keine Personen-Icons, keine Card-Container. Dunkel, hochwertig, technisch, goldene Akzente, exakt passend zur bestehenden Neurova Hero.

---

## 7. HTML/CSS-Implementationshinweis

Die Trust Section sollte im Code nicht als klassische Card-Sektion aufgebaut werden, sondern als `<section class="hero-trustbar">` direkt nach der Hero.

Empfohlene Struktur:

```html
<section class="hero-trustbar">
  <div class="trust-copy">
    <h2>35+ JAHRE CODE. EINE MISSION: FUNKTIONIERENDE KI-SYSTEME.</h2>
    <p>Meine Reise begann ...</p>
  </div>
  <div class="trust-stats">
    <div class="trust-stat"><strong>35+ JAHRE</strong><span>PROGRAMMIERERFAHRUNG</span></div>
    <div class="trust-stat"><strong>KI-AGENTEN</strong><span>& AUTOMATISIERUNG</span></div>
    <div class="trust-stat"><strong>MESSBARE</strong><span>PROZESSOPTIMIERUNG</span></div>
    <div class="trust-stat"><strong>PERSÖNLICHE</strong><span>BETREUUNG</span></div>
  </div>
</section>
```

Wichtig:
- `.hero-trustbar` nutzt den Hero-Hintergrund weiter.
- `.trust-stat` bekommt keine Card-Optik.
- Trenner über `border-left` oder `::before`.
- Goldene Bottom-Line möglich.
- Keine Icons.
