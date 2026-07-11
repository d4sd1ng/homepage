#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

HTML_START = "<!-- NUROVELLE SECTION 4 START -->"
HTML_END = "<!-- NUROVELLE SECTION 4 END -->"
CSS_START = "/* NUROVELLE SECTION 4 START */"
CSS_END = "/* NUROVELLE SECTION 4 END */"
JS_START = "/* NUROVELLE SECTION 4 JS START */"
JS_END = "/* NUROVELLE SECTION 4 JS END */"

CSS_BLOCK = r"""
/* NUROVELLE SECTION 4 START */
.nvp4-projectidea {
  position: relative;
  overflow: hidden;
  padding: 42px var(--side);
  background:
    radial-gradient(circle at 78% 48%, #112A206B 0%, #071C142E 34%, #00000000 68%),
    #000000;
}

.nvp4-projectidea::before {
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

.nvp4-projectidea__inner {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: minmax(0, 0.86fr) minmax(420px, 1.14fr);
  gap: clamp(34px, 5vw, 72px);
  align-items: center;
  width: 100%;
  max-width: 1280px;
  margin: 0 auto 0 0;
}

.nvp4-projectidea__copy {
  max-width: 620px;
}

.nvp4-projectidea__kicker {
  margin: 0 0 var(--section-kicker-gap);
  color: #E8B048;
  font-family: "Anca Coder", monospace;
  font-size: 10.5px;
  line-height: 1.4;
  letter-spacing: 1.8px;
  text-transform: uppercase;
}

.nvp4-projectidea__title {
  max-width: 720px;
  margin: 0 0 var(--section-title-gap);
  color: #F5F1E8;
  font-family: "Bebas Neue", sans-serif;
  font-size: clamp(20px, 1.55vw, 31px);
  font-weight: 400;
  line-height: 1.04;
  letter-spacing: 0.035em;
  text-transform: uppercase;
}

.nvp4-projectidea__title-accent {
  color: transparent;
  background: linear-gradient(
    180deg,
    #FFD7A3 0%,
    #F0A05A 24%,
    #D89828 58%,
    #7A3518 100%
  );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nvp4-projectidea__text {
  max-width: 620px;
  color: #FFFFFFC7;
  font-family: "Anca Coder", monospace;
  font-size: 12px;
  font-weight: 400;
  line-height: 1.48;
}

.nvp4-projectidea__text p {
  margin: 0;
}

.nvp4-projectidea__text p + p {
  margin-top: 14px;
}

.nvp4-projectidea__cta {
  display: inline-flex;
  min-height: 36px;
  align-items: center;
  justify-content: center;
  gap: 7px;
  margin-top: 24px;
  padding: 0 16px;
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

.nvp4-projectidea__cta::after {
  content: "→";
  margin-left: 8px;
  font-size: 15px;
  line-height: 1;
}

.nvp4-projectidea__cta:hover,
.nvp4-projectidea__cta:focus-visible {
  filter: brightness(1.06);
  transform: translateY(-2px);
}

.nvp4-projectidea__cta:focus-visible {
  outline: 2px solid #F7EF8A;
  outline-offset: 4px;
}

.nvp4-projectidea__visual {
  position: relative;
  min-height: clamp(430px, 42vw, 590px);
  isolation: isolate;
}

.nvp4-projectidea__photo {
  position: absolute;
  margin: 0;
  overflow: hidden;
  border-radius: 12px;
  background: #010403;
  opacity: 0;
  transform: translateY(72px);
  will-change: opacity, transform;
}

.nvp4-projectidea__photo img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.nvp4-projectidea__photo--back {
  z-index: 1;
  left: 0;
  bottom: 3%;
  width: 76%;
  aspect-ratio: 3 / 2;
  border: 1px solid #F0A05A42;
  box-shadow: 0 18px 42px #0000006B;
}

.nvp4-projectidea__photo--front {
  z-index: 2;
  top: 2%;
  right: 0;
  width: 72%;
  aspect-ratio: 3 / 2;
  border: 1px solid #F0A05AB8;
  box-shadow:
    0 22px 50px #00000080,
    0 0 20px #F0A05A29;
}

.nvp4-projectidea__visual.is-visible .nvp4-projectidea__photo--back {
  animation: nvp4-projectidea-rise 760ms cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

.nvp4-projectidea__visual.is-visible .nvp4-projectidea__photo--front {
  animation: nvp4-projectidea-rise 760ms cubic-bezier(0.22, 1, 0.36, 1) 260ms forwards;
}

@keyframes nvp4-projectidea-rise {
  from {
    opacity: 0;
    transform: translateY(72px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 899px) {
  .nvp4-projectidea__inner {
    grid-template-columns: 1fr;
  }

  .nvp4-projectidea__visual {
    min-height: clamp(370px, 95vw, 520px);
  }
}

@media (max-width: 639px) {
  .nvp4-projectidea__cta {
    width: 100%;
    min-height: 44px;
  }

  .nvp4-projectidea__visual {
    min-height: clamp(310px, 105vw, 430px);
  }

  .nvp4-projectidea__photo--back {
    width: 82%;
  }

  .nvp4-projectidea__photo--front {
    width: 80%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nvp4-projectidea__photo {
    opacity: 1;
    transform: none;
    animation: none;
  }

  .nvp4-projectidea__cta {
    transition: none;
  }
}
/* NUROVELLE SECTION 4 END */
"""

HTML_TEMPLATE = r"""
<!-- NUROVELLE SECTION 4 START -->
<section class="nvp4-projectidea" id="projektidee" aria-labelledby="nvp4-projectidea-title">
  <div class="nvp4-projectidea__inner">
    <div class="nvp4-projectidea__copy">
      <p class="nvp4-projectidea__kicker">Von der Idee zum Projekt</p>

      <h2 class="nvp4-projectidea__title" id="nvp4-projectidea-title">
        Sie haben bereits eine
        <span class="nvp4-projectidea__title-accent">konkrete KI-Idee?</span>
      </h2>

      <div class="nvp4-projectidea__text">
        <p>Wenn Sie bereits wissen, welcher Prozess verbessert, welche Datenquelle nutzbar gemacht oder welche interne Aufgabe unterstützt werden soll, ist der nächste Schritt keine allgemeine Orientierung.</p>

        <p>Nurovelle prüft mit Ihnen, ob die Idee technisch realistisch ist, welche Systeme, Daten oder Schnittstellen benötigt werden und welcher Umsetzungsweg sinnvoll ist.</p>

        <p>So wird aus einer ersten Idee ein konkreter Projektansatz für KI-Agenten, Automatisierung, Datenverarbeitung oder individuelle Software.</p>
      </div>

      <a class="nvp4-projectidea__cta" href="analyse.html">Projektidee prüfen lassen</a>
    </div>

    <div class="nvp4-projectidea__visual" data-nvp4-projectidea-visual>
      <figure class="nvp4-projectidea__photo nvp4-projectidea__photo--back">
        <img src="{photo16}" alt="" loading="lazy" decoding="async">
      </figure>

      <figure class="nvp4-projectidea__photo nvp4-projectidea__photo--front">
        <img src="{photo9}" alt="Beratung zu einer konkreten KI-Projektidee" loading="lazy" decoding="async">
      </figure>
    </div>
  </div>
</section>
<!-- NUROVELLE SECTION 4 END -->
"""

JS_BLOCK = r"""
/* NUROVELLE SECTION 4 JS START */
(() => {
  const visual = document.querySelector("[data-nvp4-projectidea-visual]");
  if (!visual) return;

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (reducedMotion || !("IntersectionObserver" in window)) {
    visual.classList.add("is-visible");
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

  observer.observe(visual);
})();
/* NUROVELLE SECTION 4 JS END */
"""

def remove_marked_block(text: str, start: str, end: str) -> str:
    while start in text:
        start_at = text.index(start)
        end_at = text.find(end, start_at)

        if end_at == -1:
            raise RuntimeError(f"Endmarker fehlt: {end}")

        end_at += len(end)
        text = text[:start_at] + text[end_at:]

    return text

def relative_asset(index_path: Path, asset_path: Path) -> str:
    resolved_asset = asset_path.resolve()

    if not resolved_asset.is_file():
        raise FileNotFoundError(f"Asset nicht gefunden: {resolved_asset}")

    try:
        return resolved_asset.relative_to(index_path.parent.resolve()).as_posix()
    except ValueError as exc:
        raise RuntimeError(
            f"Asset liegt außerhalb des Homepage-Projektordners: {resolved_asset}"
        ) from exc


def find_matching_section_end(text: str, opening_start: int) -> int:
    token_pattern = re.compile(r"</?section\b[^>]*>", re.IGNORECASE | re.DOTALL)
    depth = 0

    for token_match in token_pattern.finditer(text, opening_start):
        token = token_match.group(0)

        if token.lower().startswith("</section"):
            depth -= 1
            if depth == 0:
                return token_match.end()
        else:
            depth += 1

    raise RuntimeError("Schließendes </section> nicht gefunden.")


def find_section_containing_text(text: str, needle: str) -> int | None:
    needle_pos = text.casefold().find(needle.casefold())
    if needle_pos == -1:
        return None

    openings = list(
        re.finditer(r"<section\b[^>]*>", text[:needle_pos], re.IGNORECASE | re.DOTALL)
    )

    for opening in reversed(openings):
        try:
            section_end = find_matching_section_end(text, opening.start())
        except RuntimeError:
            continue

        if opening.start() <= needle_pos < section_end:
            return section_end

    return None


def find_third_top_level_section_end(text: str) -> int:
    main_open = re.search(r"<main\b[^>]*>", text, re.IGNORECASE | re.DOTALL)
    main_close = re.search(r"</main\s*>", text, re.IGNORECASE)

    search_start = main_open.end() if main_open else 0
    search_end = main_close.start() if main_close else len(text)

    token_pattern = re.compile(r"</?section\b[^>]*>", re.IGNORECASE | re.DOTALL)
    depth = 0
    top_level_sections: list[tuple[int, int]] = []
    current_start: int | None = None

    for token_match in token_pattern.finditer(text, search_start, search_end):
        token = token_match.group(0)

        if token.lower().startswith("</section"):
            depth -= 1
            if depth == 0 and current_start is not None:
                top_level_sections.append((current_start, token_match.end()))
                current_start = None
        else:
            if depth == 0:
                current_start = token_match.start()
            depth += 1

    if len(top_level_sections) < 3:
        raise RuntimeError(
            "Abschnitt 3 konnte strukturell nicht ermittelt werden: "
            "Im <main>-Bereich wurden weniger als drei Haupt-Sections gefunden."
        )

    return top_level_sections[2][1]


def find_section_3_end(text: str) -> int:
    marker = "<!-- NUROVELLE SECTION 3 END -->"
    marker_pos = text.find(marker)
    if marker_pos != -1:
        return marker_pos + len(marker)

    for section_id in ("section-3", "sektion-3"):
        match = re.search(
            rf'<section\b(?=[^>]*\bid\s*=\s*["\']{re.escape(section_id)}["\'])[^>]*>',
            text,
            re.IGNORECASE | re.DOTALL,
        )
        if match:
            return find_matching_section_end(text, match.start())

    for heading in (
        "Der erste Schritt zu Ihrem KI-Projekt",
        "Der erste Schritt zu Ihrem KI Projekt",
    ):
        section_end = find_section_containing_text(text, heading)
        if section_end is not None:
            return section_end

    return find_third_top_level_section_end(text)

def patch(index_path: Path, photo9_path: Path, photo16_path: Path) -> Path:
    if not index_path.is_file():
        raise FileNotFoundError(f"index.html nicht gefunden: {index_path}")

    original = index_path.read_text(encoding="utf-8")
    text = original

    text = remove_marked_block(text, HTML_START, HTML_END)
    text = remove_marked_block(text, CSS_START, CSS_END)
    text = remove_marked_block(text, JS_START, JS_END)

    existing_projectidea = re.search(
        r'<section\b(?=[^>]*\bid\s*=\s*["\']projektidee["\'])[^>]*>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if existing_projectidea:
        raise RuntimeError(
            'Eine fremde Section mit id="projektidee" existiert bereits. '
            "Das Skript überschreibt sie nicht."
        )

    style_close = text.lower().find("</style>")
    body_close = text.lower().rfind("</body>")

    if style_close == -1:
        raise RuntimeError("Kein </style>-Tag gefunden.")

    if body_close == -1:
        raise RuntimeError("Kein </body>-Tag gefunden.")

    photo9 = relative_asset(index_path, photo9_path)
    photo16 = relative_asset(index_path, photo16_path)
    html_block = HTML_TEMPLATE.format(photo9=photo9, photo16=photo16)

    text = text[:style_close] + CSS_BLOCK + "\n" + text[style_close:]

    insert_at = find_section_3_end(text)
    text = text[:insert_at] + "\n" + html_block + text[insert_at:]

    body_close = text.lower().rfind("</body>")
    text = text[:body_close] + "<script>\n" + JS_BLOCK + "\n</script>\n" + text[body_close:]

    backup_path = index_path.with_suffix(index_path.suffix + ".bak-sektion4")
    if not backup_path.exists():
        shutil.copy2(index_path, backup_path)

    index_path.write_text(text, encoding="utf-8")
    return backup_path

def main() -> int:
    project_root = Path("/media/d4sd1ng/AI-Data/Projects/homepage_repo/homepage")

    parser = argparse.ArgumentParser(
        description="Fügt Abschnitt 4 direkt nach der dritten Haupt-Section ein."
    )
    parser.add_argument(
        "--index",
        default=str(project_root / "index.html"),
        help="Pfad zur index.html",
    )
    parser.add_argument(
        "--photo9",
        default=str(project_root / "assets/Fotos/9.png"),
        help="Pfad zu Foto 9",
    )
    parser.add_argument(
        "--photo16",
        default=str(project_root / "assets/Fotos/16.png"),
        help="Pfad zu Foto 16",
    )
    args = parser.parse_args()

    try:
        index_path = Path(args.index).resolve()
        backup_path = patch(
            index_path=index_path,
            photo9_path=Path(args.photo9),
            photo16_path=Path(args.photo16),
        )
    except Exception as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 1

    print(f"FERTIG: {index_path}")
    print(f"BACKUP: {backup_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
