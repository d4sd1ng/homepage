#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

HTML_START = "<!-- NUROVELLE SECTION 5 START -->"
HTML_END = "<!-- NUROVELLE SECTION 5 END -->"
CSS_START = "/* NUROVELLE SECTION 5 START */"
CSS_END = "/* NUROVELLE SECTION 5 END */"
JS_START = "/* NUROVELLE SECTION 5 JS START */"
JS_END = "/* NUROVELLE SECTION 5 JS END */"

CSS_BLOCK = r"""
/* NUROVELLE SECTION 5 START */
.nvp5-analysis {
  position: relative;
  overflow: hidden;
  padding: 42px var(--side);
  background:
    radial-gradient(circle at 50% 52%, #112A2052 0%, #0A191326 34%, #00000000 70%),
    #000000;
}

.nvp5-analysis::before {
  content: "";
  position: absolute;
  inset: 0 0 auto;
  height: 1px;
  background: linear-gradient(
    90deg,
    #00000000 0%,
    #F0A05A5C 4%,
    #F0A05AB8 12%,
    #F0A05AB8 88%,
    #F0A05A5C 96%,
    #00000000 100%
  );
}

.nvp5-analysis__inner {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 1280px;
  margin: 0 auto 0 0;
}

.nvp5-analysis__head {
  max-width: 760px;
  margin: 0 auto 26px;
  text-align: center;
}

.nvp5-analysis__kicker {
  margin: 0 0 var(--section-kicker-gap);
  color: #E8B048;
  font-family: "Anca Coder", monospace;
  font-size: 10.5px;
  line-height: 1.4;
  letter-spacing: 1.8px;
  text-transform: uppercase;
}

.nvp5-analysis__title {
  margin: 0 0 var(--section-title-gap);
  color: #F5F1E8;
  font-family: "Bebas Neue", sans-serif;
  font-size: clamp(24px, 2.1vw, 36px);
  font-weight: 400;
  line-height: 1.04;
  letter-spacing: 0.035em;
  text-transform: uppercase;
}

.nvp5-analysis__intro {
  margin: 0 auto;
  max-width: 680px;
  color: #FFFFFFC7;
  font-family: "Anca Coder", monospace;
  font-size: 12px;
  line-height: 1.48;
}

.nvp5-analysis__diagram {
  position: relative;
  width: min(100%, 1120px);
  min-height: 600px;
  margin: 0 auto;
}

.nvp5-analysis__puzzle {
  position: absolute;
  left: 50%;
  top: 50%;
  width: min(42vw, 470px);
  min-width: 360px;
  transform: translate(-50%, -50%);
  overflow: visible;
}

.nvp5-analysis__part {
  opacity: 0;
  transform-box: fill-box;
  transform-origin: center;
}

.nvp5-analysis__part--1 {
  fill: #112A20;
  stroke: #2E8B67;
}

.nvp5-analysis__part--2 {
  fill: #252B2C;
  stroke: #D4AF37;
}

.nvp5-analysis__part--3 {
  fill: #163A35;
  stroke: #2E8B67;
}

.nvp5-analysis__part--4 {
  fill: #15191A;
  stroke: #D4AF37;
}

.nvp5-analysis__part {
  stroke-width: 2;
  vector-effect: non-scaling-stroke;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__part--1 {
  animation: nvp5-puzzle-reveal 420ms ease forwards;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__part--2 {
  animation: nvp5-puzzle-reveal 420ms ease 180ms forwards;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__part--3 {
  animation: nvp5-puzzle-reveal 420ms ease 360ms forwards;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__part--4 {
  animation: nvp5-puzzle-reveal 420ms ease 540ms forwards;
}

@keyframes nvp5-puzzle-reveal {
  from {
    opacity: 0;
    transform: scale(0.97);
  }

  to {
    opacity: 1;
    transform: scale(1);
  }
}

.nvp5-analysis__icon {
  position: absolute;
  z-index: 3;
  display: grid;
  place-items: center;
  width: 92px;
  aspect-ratio: 1;
  border: 2px solid #D4AF37;
  border-radius: 50%;
  background: #080B09;
  box-shadow:
    0 0 0 8px #112A20,
    0 12px 28px #00000080;
  opacity: 0;
  transform: scale(0.92);
}

.nvp5-analysis__icon svg {
  width: 48px;
  height: 48px;
  fill: none;
  stroke: #F7EF8A;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.nvp5-analysis__icon--1 {
  left: calc(50% - 300px);
  top: 88px;
}

.nvp5-analysis__icon--2 {
  right: calc(50% - 300px);
  top: 88px;
}

.nvp5-analysis__icon--3 {
  left: calc(50% - 300px);
  bottom: 88px;
}

.nvp5-analysis__icon--4 {
  right: calc(50% - 300px);
  bottom: 88px;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__icon--1 {
  animation: nvp5-icon-reveal 320ms ease 260ms forwards;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__icon--2 {
  animation: nvp5-icon-reveal 320ms ease 440ms forwards;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__icon--3 {
  animation: nvp5-icon-reveal 320ms ease 620ms forwards;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__icon--4 {
  animation: nvp5-icon-reveal 320ms ease 800ms forwards;
}

@keyframes nvp5-icon-reveal {
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.nvp5-analysis__gold-button {
  position: absolute;
  z-index: 2;
  width: 270px;
  min-height: 56px;
  border: 1px solid #D4AF37;
  border-radius: 999px;
  background: linear-gradient(
    135deg,
    #F9F295 0%,
    #E0AA3E 38%,
    #FAF398 68%,
    #B88A44 100%
  );
  box-shadow:
    0 0 18px #D4AF372E,
    0 12px 26px #0000005C;
  opacity: 0;
  transform: translateY(16px);
}

.nvp5-analysis__gold-button--1 {
  left: 0;
  top: 116px;
}

.nvp5-analysis__gold-button--2 {
  right: 0;
  top: 116px;
}

.nvp5-analysis__gold-button--3 {
  left: 0;
  bottom: 116px;
}

.nvp5-analysis__gold-button--4 {
  right: 0;
  bottom: 116px;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__gold-button--1 {
  animation: nvp5-button-reveal 340ms ease 320ms forwards;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__gold-button--2 {
  animation: nvp5-button-reveal 340ms ease 500ms forwards;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__gold-button--3 {
  animation: nvp5-button-reveal 340ms ease 680ms forwards;
}

.nvp5-analysis__diagram.is-visible .nvp5-analysis__gold-button--4 {
  animation: nvp5-button-reveal 340ms ease 860ms forwards;
}

@keyframes nvp5-button-reveal {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.nvp5-analysis__cta-row {
  display: flex;
  justify-content: center;
  margin-top: 8px;
}

.nvp5-analysis__cta {
  display: inline-flex;
  min-height: 44px;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 0 22px;
  border: 1px solid #D89828;
  border-radius: 4px;
  color: #050505;
  background: linear-gradient(
    180deg,
    #FFD7A3 0%,
    #F0A05A 24%,
    #D89828 60%,
    #7A3518 100%
  );
  font-family: "Bebas Neue", sans-serif;
  font-size: 16px;
  line-height: 1;
  letter-spacing: 0.045em;
  text-decoration: none;
  text-transform: uppercase;
  transition: transform 180ms ease, filter 180ms ease;
}

.nvp5-analysis__cta::after {
  content: "→";
  margin-left: 8px;
  font-size: 15px;
  line-height: 1;
}

.nvp5-analysis__cta:hover,
.nvp5-analysis__cta:focus-visible {
  filter: brightness(1.06);
  transform: translateY(-2px);
}

.nvp5-analysis__cta:focus-visible {
  outline: 2px solid #F7EF8A;
  outline-offset: 4px;
}

@media (max-width: 1099px) {
  .nvp5-analysis__diagram {
    min-height: 540px;
  }

  .nvp5-analysis__puzzle {
    width: 420px;
    min-width: 0;
  }

  .nvp5-analysis__icon--1,
  .nvp5-analysis__icon--3 {
    left: calc(50% - 265px);
  }

  .nvp5-analysis__icon--2,
  .nvp5-analysis__icon--4 {
    right: calc(50% - 265px);
  }

  .nvp5-analysis__gold-button {
    width: 220px;
  }
}

@media (max-width: 899px) {
  .nvp5-analysis__diagram {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px 18px;
    min-height: 0;
    padding-top: 390px;
  }

  .nvp5-analysis__puzzle {
    top: 180px;
    width: 340px;
  }

  .nvp5-analysis__icon {
    width: 76px;
    position: relative;
    inset: auto;
    justify-self: center;
  }

  .nvp5-analysis__gold-button {
    position: relative;
    inset: auto;
    width: 100%;
    min-height: 50px;
  }

  .nvp5-analysis__icon--1,
  .nvp5-analysis__icon--2,
  .nvp5-analysis__icon--3,
  .nvp5-analysis__icon--4 {
    grid-row: auto;
  }

  .nvp5-analysis__icon--1 {
    grid-column: 1;
  }

  .nvp5-analysis__gold-button--1 {
    grid-column: 1;
  }

  .nvp5-analysis__icon--2 {
    grid-column: 2;
    grid-row: 1;
  }

  .nvp5-analysis__gold-button--2 {
    grid-column: 2;
  }

  .nvp5-analysis__icon--3 {
    grid-column: 1;
  }

  .nvp5-analysis__gold-button--3 {
    grid-column: 1;
  }

  .nvp5-analysis__icon--4 {
    grid-column: 2;
  }

  .nvp5-analysis__gold-button--4 {
    grid-column: 2;
  }
}

@media (max-width: 639px) {
  .nvp5-analysis {
    padding-left: var(--side);
    padding-right: var(--side);
  }

  .nvp5-analysis__diagram {
    grid-template-columns: 1fr;
    gap: 18px;
    padding-top: 330px;
  }

  .nvp5-analysis__puzzle {
    top: 150px;
    width: 290px;
  }

  .nvp5-analysis__icon,
  .nvp5-analysis__gold-button {
    grid-column: 1;
  }

  .nvp5-analysis__cta {
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nvp5-analysis__part,
  .nvp5-analysis__icon,
  .nvp5-analysis__gold-button {
    opacity: 1;
    transform: none;
    animation: none;
  }

  .nvp5-analysis__cta {
    transition: none;
  }
}
/* NUROVELLE SECTION 5 END */
"""

HTML_BLOCK = r"""
<!-- NUROVELLE SECTION 5 START -->
<section class="nvp5-analysis" id="potenzialanalyse" aria-labelledby="nvp5-analysis-title">
  <div class="nvp5-analysis__inner">
    <header class="nvp5-analysis__head">
      <p class="nvp5-analysis__kicker">Potenziale erkennen</p>
      <h2 class="nvp5-analysis__title" id="nvp5-analysis-title">Kostenlose KI-Potenzialanalyse</h2>
      <p class="nvp5-analysis__intro">Finden Sie heraus, wo KI in Ihrem Unternehmen sinnvoll ansetzen kann.</p>
    </header>

    <div class="nvp5-analysis__diagram" data-nvp5-analysis-diagram>
      <svg class="nvp5-analysis__puzzle" viewBox="0 0 400 400" role="img" aria-label="Vierteiliger Puzzle-Kreis für die KI-Potenzialanalyse">
        <path class="nvp5-analysis__part nvp5-analysis__part--1"
          d="M200 20 A180 180 0 0 0 20 200 H92
             C92 180 108 164 128 164
             C148 164 164 180 164 200
             H200 V128
             C220 128 236 112 236 92
             C236 72 220 56 200 56 Z"/>
        <path class="nvp5-analysis__part nvp5-analysis__part--2"
          d="M200 20 A180 180 0 0 1 380 200 H308
             C308 180 292 164 272 164
             C252 164 236 180 236 200
             H200 V128
             C220 128 236 112 236 92
             C236 72 220 56 200 56 Z"/>
        <path class="nvp5-analysis__part nvp5-analysis__part--3"
          d="M20 200 A180 180 0 0 0 200 380 V308
             C180 308 164 292 164 272
             C164 252 180 236 200 236
             V200 H128
             C128 180 112 164 92 164
             C72 164 56 180 56 200 Z"/>
        <path class="nvp5-analysis__part nvp5-analysis__part--4"
          d="M380 200 A180 180 0 0 1 200 380 V308
             C220 308 236 292 236 272
             C236 252 220 236 200 236
             V200 H272
             C272 220 288 236 308 236
             C328 236 344 220 344 200 Z"/>
      </svg>

      <span class="nvp5-analysis__gold-button nvp5-analysis__gold-button--1" aria-hidden="true"></span>
      <span class="nvp5-analysis__gold-button nvp5-analysis__gold-button--2" aria-hidden="true"></span>
      <span class="nvp5-analysis__gold-button nvp5-analysis__gold-button--3" aria-hidden="true"></span>
      <span class="nvp5-analysis__gold-button nvp5-analysis__gold-button--4" aria-hidden="true"></span>

      <span class="nvp5-analysis__icon nvp5-analysis__icon--1" role="img" aria-label="Abläufe analysieren">
        <svg viewBox="0 0 48 48" aria-hidden="true">
          <circle cx="10" cy="12" r="4"></circle>
          <circle cx="38" cy="12" r="4"></circle>
          <circle cx="24" cy="36" r="4"></circle>
          <path d="M14 12h20M12 16l9 16M36 16l-9 16"></path>
        </svg>
      </span>

      <span class="nvp5-analysis__icon nvp5-analysis__icon--2" role="img" aria-label="Datenlage prüfen">
        <svg viewBox="0 0 48 48" aria-hidden="true">
          <ellipse cx="21" cy="10" rx="12" ry="5"></ellipse>
          <path d="M9 10v16c0 3 5 5 12 5c2 0 4 0 6-1"></path>
          <path d="M33 10v10"></path>
          <path d="M9 18c0 3 5 5 12 5c5 0 9-1 12-3"></path>
          <circle cx="34" cy="32" r="7"></circle>
          <path d="M39 37l5 5"></path>
        </svg>
      </span>

      <span class="nvp5-analysis__icon nvp5-analysis__icon--3" role="img" aria-label="Potenziale priorisieren">
        <svg viewBox="0 0 48 48" aria-hidden="true">
          <circle cx="22" cy="26" r="15"></circle>
          <circle cx="22" cy="26" r="9"></circle>
          <circle cx="22" cy="26" r="3"></circle>
          <path d="M26 22l14-14M33 8h7v7"></path>
        </svg>
      </span>

      <span class="nvp5-analysis__icon nvp5-analysis__icon--4" role="img" aria-label="Nächsten Schritt definieren">
        <svg viewBox="0 0 48 48" aria-hidden="true">
          <circle cx="9" cy="36" r="3"></circle>
          <circle cx="23" cy="25" r="3"></circle>
          <circle cx="37" cy="14" r="3"></circle>
          <path d="M12 34l8-7M26 23l8-7M37 11V5M37 5l6 4"></path>
        </svg>
      </span>
    </div>

    <div class="nvp5-analysis__cta-row">
      <a class="nvp5-analysis__cta" href="analyse.html">Kostenlose KI-Potenzialanalyse anfordern</a>
    </div>
  </div>
</section>
<!-- NUROVELLE SECTION 5 END -->
"""

JS_BLOCK = r"""
/* NUROVELLE SECTION 5 JS START */
(() => {
  const diagram = document.querySelector("[data-nvp5-analysis-diagram]");
  if (!diagram) return;

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (reducedMotion || !("IntersectionObserver" in window)) {
    diagram.classList.add("is-visible");
    return;
  }

  const observer = new IntersectionObserver(
    (entries, currentObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        currentObserver.unobserve(entry.target);
      });
    },
    { threshold: 0.25 }
  );

  observer.observe(diagram);
})();
/* NUROVELLE SECTION 5 JS END */
"""

def remove_block(text: str, start: str, end: str) -> str:
    while start in text:
        start_at = text.index(start)
        end_at = text.find(end, start_at)
        if end_at == -1:
            raise RuntimeError(f"Endmarker fehlt: {end}")
        text = text[:start_at] + text[end_at + len(end):]
    return text

def find_section_end(text: str, section_id: str) -> int:
    opening = re.search(
        rf'<section\b(?=[^>]*\bid\s*=\s*["\']{re.escape(section_id)}["\'])[^>]*>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if not opening:
        raise RuntimeError(f'Section mit id="{section_id}" nicht gefunden.')

    token_pattern = re.compile(r'</?section\b[^>]*>', re.IGNORECASE | re.DOTALL)
    depth = 0

    for token_match in token_pattern.finditer(text, opening.start()):
        token = token_match.group(0)
        if token.lower().startswith("</section"):
            depth -= 1
            if depth == 0:
                return token_match.end()
        else:
            depth += 1

    raise RuntimeError(f'Abschluss von Section mit id="{section_id}" nicht gefunden.')

def patch(index_path: Path) -> Path:
    if not index_path.is_file():
        raise FileNotFoundError(f"index.html nicht gefunden: {index_path}")

    text = index_path.read_text(encoding="utf-8")
    text = remove_block(text, HTML_START, HTML_END)
    text = remove_block(text, CSS_START, CSS_END)
    text = remove_block(text, JS_START, JS_END)

    foreign_section = re.search(
        r'<section\b(?=[^>]*\bid\s*=\s*["\']potenzialanalyse["\'])[^>]*>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if foreign_section:
        raise RuntimeError(
            'Eine fremde Section mit id="potenzialanalyse" existiert bereits. '
            "Das Skript überschreibt sie nicht."
        )

    style_close = text.lower().find("</style>")
    body_close = text.lower().rfind("</body>")

    if style_close == -1:
        raise RuntimeError("Kein </style>-Tag gefunden.")
    if body_close == -1:
        raise RuntimeError("Kein </body>-Tag gefunden.")

    text = text[:style_close] + CSS_BLOCK + "\n" + text[style_close:]

    insert_at = find_section_end(text, "projektidee")
    text = text[:insert_at] + "\n" + HTML_BLOCK + text[insert_at:]

    body_close = text.lower().rfind("</body>")
    text = text[:body_close] + "<script>\n" + JS_BLOCK + "\n</script>\n" + text[body_close:]

    backup = index_path.with_suffix(index_path.suffix + ".bak-sektion5")
    if not backup.exists():
        shutil.copy2(index_path, backup)

    index_path.write_text(text, encoding="utf-8")
    return backup

def main() -> int:
    project_root = Path("/media/d4sd1ng/AI-Data/Projects/homepage_repo/homepage")

    parser = argparse.ArgumentParser(
        description="Fügt Sektion 5 direkt nach #projektidee in index.html ein."
    )
    parser.add_argument(
        "--index",
        default=str(project_root / "index.html"),
        help="Pfad zur index.html",
    )
    args = parser.parse_args()

    try:
        index_path = Path(args.index).resolve()
        backup = patch(index_path)
    except Exception as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 1

    print(f"FERTIG: {index_path}")
    print(f"BACKUP: {backup}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
