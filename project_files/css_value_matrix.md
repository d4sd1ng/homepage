# CSS Value Matrix (Single Source)

Status: 2026-07-15

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
