# CSS Value Matrix (Single Source)

Status: 2026-07-31

## Global Tokens (only here)

File: homepage/index.html
Block: :root

- Typography and shared section values:
  - --nv-section-kicker-size
  - --nv-section-title-size
  - --nv-section-body-size
  - --nv-section-body-line
  - --nv-kicker-color-hero
  - --nv-kicker-color-section
  - --nv-kicker-line-height-hero
  - --nv-kicker-line-height-section
  - --nv-kicker-letter-spacing

- Global rhythm values:
  - --nv-kicker-title-gap
  - --nv-title-text-gap
  - --nv-section-text-content-gap
  - --nv-section-divider-before-gap
  - --nv-section-divider-after-gap

- Shared structural values:
  - --nv-section-inner-max
  - --nv-section-head-max
  - --nv-section-intro-max
  - --nv-footer-inner-max
  - --nv-section-title-gradient
  - --nv-gold-divider-strong

- Shared spacing values:
  - --nv-space-xxs
  - --nv-space-xs
  - --nv-space-sm
  - --nv-space-md
  - --nv-space-lg
  - --nv-space-xl
  - --nv-space-2xl
  - --nv-radius-sm
  - --nv-radius-md

## Global Section Rhythm (only here)

File: homepage/index.html

- Section alternation (black/emerald)
- Section separators (::before line)
- Global section top/bottom padding by rhythm variables
- Global tablet/mobile rhythm variable overrides

## Section-Internal Styles

### Section 7 (service cards)

File: homepage/components/nurovelle-service-cards.css

- Card grid geometry, card dimensions, offsets, hover behavior
- Section-specific media/card internals

### Downloads / Resources / Form / FAQ

File: homepage/components/nurovelle-resources-contact-faq.css

- Download library/form/faq internal layout and component geometry
- Section-specific internals for cards/controls

### Process / Why / Footer internals

File: homepage/components/nurovelle-section-rhythm.css

- Process steps internal geometry and module placement
- Why points internal layout
- Footer internal grid and typography behavior

## Rule

1. Visible text content changes only in homepage/index.html markup.
2. Reused global values change only in homepage/index.html :root.
3. Component files keep only section-internal geometry/behavior.
4. No duplicated global literal values across component files when a global token exists.

## Typo-Rollen (2026-07-31)

File: homepage/index.html
Block: :root

Je Rolle ein Tokenpaar. Nur hier ändern, nie in den Komponentenregeln.

```
--t-sektionstitel: clamp(48px, 7.5vw, 100px);  --w-sektionstitel: 800;
--t-hero-kennzahl: 42px;                        --w-hero-kennzahl: 750;
--t-kartentitel: 36px;                          --w-kartentitel: 750;
--t-kennzahl: 26px;                             --w-kennzahl: 650;
--t-subtitle: 24px;                             --w-subtitle: 600;
--t-zwischentitel: 24px;                        --w-zwischentitel: 600;
--t-bulletlabel: 22px;                          --w-bulletlabel: 550;
--t-fliesstext: 20px;                           --w-fliesstext: 400;
--t-kartenbullet: 20px;                         --w-kartenbullet: 500;
--t-feldlabel: 20px;                            --w-feldlabel: 500;
--t-wert: 20px;                                 --w-wert: 500;
--t-formularfeld: 20px;                         --w-formularfeld: 400;
--t-kicker-sektion: 16px;                       --w-kicker-sektion: 600;
--t-bildunterschrift: 16px;                     --w-bildunterschrift: 500;
--t-cta: 16px;                                  --w-cta: 600;
--t-hero-statlabel: 16px;                       --w-hero-statlabel: 400;
--t-kicker-karte: 15px;                         --w-kicker-karte: 600;
```

## Flächen und Rahmen (2026-07-31)

```
Sektion dunkel        #050505
Sektion grün          #010603
Karte auf dunkel      #17251d
Karte auf grün        #1a1a1a
Element auf Karte     #17251d
Rahmenverlauf         var(--gold-3)
```

## Skalierung (2026-07-31)

`body { zoom: 0.8 }` — jeder Wert hier ist CSS-Pixel, gerendert wird das 0.8-fache.

- sichtbarer Zielwert ÷ 0.8 = einzutragender Wert
- Viewporthöhe: `calc(125vh - var(--header-height))`
- Hairline: 1.25px CSS = 1 Bildschirmpixel
- `.nv-s7__cards` hat zusätzlich `zoom: 0.75`, dort also Faktor 0.6
