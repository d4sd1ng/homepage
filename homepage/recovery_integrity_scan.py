#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

CSS_START = "/* SECTION 4 PATCH START */"
CSS_END = "/* SECTION 4 PATCH END */"
HTML_START = "<!-- SECTION 4 PATCH START -->"
HTML_END = "<!-- SECTION 4 PATCH END -->"
JS_START = "/* SECTION 4 JS PATCH START */"
JS_END = "/* SECTION 4 JS PATCH END */"

CSS_BLOCK = r"""
/* SECTION 4 PATCH START */
#projektidee {
  position: relative;
  overflow: hidden;
  padding: 42px var(--side);
  background:
    radial-gradient(circle at 78% 48%, rgba(17,42,32,.42), transparent 48%),
    #000;
}

#projektidee::before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(240,160,90,.36) 4%,
    rgba(240,160,90,.72) 12%,
    rgba(240,160,90,.72) 88%,
    rgba(240,160,90,.36) 96%,
    transparent 100%
  );
  opacity: .75;
}

.project-idea-layout {
  display: grid;
  grid-template-columns: minmax(0,.86fr) minmax(420px,1.14fr);
  gap: clamp(34px,5vw,72px);
  align-items: center;
}

.project-idea-copy {
  position: relative;
  z-index: 3;
  max-width: 620px;
}

.project-idea-copy .section-text {
  max-width: 620px;
}

.project-idea-copy .section-text p {
  margin: 0;
}

.project-idea-copy .section-text p + p {
  margin-top: 14px;
}

.project-idea-copy .btn {
  margin-top: 24px;
}

.project-idea-visual {
  position: relative;
  min-height: clamp(430px,42vw,590px);
  isolation: isolate;
}

.project-idea-photo {
  position: absolute;
  margin: 0;
  overflow: hidden;
  border-radius: 12px;
  background: #010403;
  opacity: 0;
  transform: translateY(72px);
  will-change: opacity, transform;
}

.project-idea-photo img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.project-idea-photo--back {
  z-index: 1;
  left: 0;
  bottom: 3%;
  width: 76%;
  aspect-ratio: 3 / 2;
  border: 1px solid rgba(240,160,90,.26);
  box-shadow: 0 18px 42px rgba(0,0,0,.42);
}

.project-idea-photo--front {
  z-index: 2;
  top: 2%;
  right: 0;
  width: 72%;
  aspect-ratio: 3 / 2;
  border: 1px solid rgba(240,160,90,.72);
  box-shadow:
    0 22px 50px rgba(0,0,0,.50),
    0 0 20px rgba(240,160,90,.16);
}

.project-idea-visual.is-visible .project-idea-photo--back {
  animation: projectIdeaRise .76s cubic-bezier(.22,1,.36,1) forwards;
}

.project-idea-visual.is-visible .project-idea-photo--front {
  animation: projectIdeaRise .76s cubic-bezier(.22,1,.36,1) .26s forwards;
}

@keyframes projectIdeaRise {
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
  .project-idea-layout {
    grid-template-columns: 1fr;
  }

  .project-idea-visual {
    min-height: clamp(370px,95vw,520px);
  }
}

@media (max-width: 639px) {
  #projektidee {
    padding-left: var(--side);
    padding-right: var(--side);
  }

  .project-idea-copy .btn {
    width: 100%;
  }

  .project-idea-visual {
    min-height: clamp(310px,105vw,430px);
  }

  .project-idea-photo--back {
    width: 82%;
  }

  .project-idea-photo--front {
    width: 80%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .project-idea-photo {
    opacity: 1;
    transform: none;
    animation: none !important;
  }
}
/* SECTION 4 PATCH END */
"""

HTML_TEMPLATE = r"""
<!-- SECTION 4 PATCH START -->
<section class="section bg" id="projektidee" aria-labelledby="projektidee-title">
  <div class="section-inner project-idea-layout">
    <div class="project-idea-copy">
      <div class="kicker">Von der Idee zum Projekt</div>

      <h2 class="section-title" id="projektidee-title">
        Sie haben bereits eine <span class="gold">konkrete KI-Idee?</span>
      </h2>

      <div class="section-text">
        <p>Wenn Sie bereits wissen, welcher Prozess verbessert, welche Datenquelle nutzbar gemacht oder welche interne Aufgabe unterstützt werden soll, ist der nächste Schritt keine allgemeine Orientierung.</p>

        <p>Nurovelle prüft mit Ihnen, ob die Idee technisch realistisch ist, welche Systeme, Daten oder Schnittstellen benötigt werden und welcher Umsetzungsweg sinnvoll ist.</p>

        <p>So wird aus einer ersten Idee ein konkreter Projektansatz für KI-Agenten, Automatisierung, Datenverarbeitung oder individuelle Software.</p>
      </div>

      <a class="btn btn-primary" href="analyse.html">Projektidee prüfen lassen</a>
    </div>

    <div class="project-idea-visual" data-project-idea-visual>
      <figure class="project-idea-photo project-idea-photo--back">
        <img src="{photo16}" alt="" loading="lazy" decoding="async">
      </figure>

      <figure class="project-idea-photo project-idea-photo--front">
        <img src="{photo9}" alt="Beratung zu einer konkreten KI-Projektidee" loading="lazy" decoding="async">
      </figure>
    </div>
  </div>
</section>
<!-- SECTION 4 PATCH END -->
"""

JS_BLOCK = r"""
/* SECTION 4 JS PATCH START */
(() => {
  const visual = document.querySelector("[data-project-idea-visual]");
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
/* SECTION 4 JS PATCH END */
"""

def strip_block(text: str, start: str, end: str) -> str:
    while start in text:
        start_pos = text.index(start)
        end_pos = text.find(end, start_pos)
        if end_pos == -1:
            raise RuntimeError(f"Startmarker gefunden, Endmarker fehlt: {start}")
        end_pos += len(end)
        text = text[:start_pos] + text[end_pos:]
    return text

def rel_asset(index_path: Path, asset_arg: str) -> str:
    asset = Path(asset_arg)
    if not asset.is_absolute():
        asset = (index_path.parent / asset).resolve()

    if not asset.exists():
        raise FileNotFoundError(f"Bild nicht gefunden: {asset}")

    try:
        return asset.relative_to(index_path.parent.resolve()).as_posix()
    except ValueError:
        raise ValueError(
            f"Bild liegt außerhalb des Projektordners: {asset}\n"
            "Lege das Bild innerhalb des Repositorys ab und übergib den relativen Pfad."
        )

def patch(index_path: Path, photo9_arg: str, photo16_arg: str) -> Path:
    if not index_path.exists():
        raise FileNotFoundError(f"index.html nicht gefunden: {index_path}")

    photo9 = rel_asset(index_path, photo9_arg)
    photo16 = rel_asset(index_path, photo16_arg)

    original = index_path.read_text(encoding="utf-8")
    text = original

    text = strip_block(text, CSS_START, CSS_END)
    text = strip_block(text, HTML_START, HTML_END)
    text = strip_block(text, JS_START, JS_END)

    if "</style>" not in text:
        raise RuntimeError("Kein </style>-Tag gefunden.")
    if "</body>" not in text:
        raise RuntimeError("Kein </body>-Tag gefunden.")

    services_marker = '<section class="section bg" id="leistungen">'
    if services_marker not in text:
        raise RuntimeError(
            'Einfügepunkt nicht gefunden: <section class="section bg" id="leistungen">'
        )

    html_block = HTML_TEMPLATE.format(photo9=photo9, photo16=photo16)

    text = text.replace("</style>", CSS_BLOCK + "\n</style>", 1)
    text = text.replace(services_marker, html_block + "\n" + services_marker, 1)
    text = text.replace("</body>", "<script>\n" + JS_BLOCK + "\n</script>\n</body>", 1)

    backup = index_path.with_suffix(index_path.suffix + ".bak-sektion4")
    if not backup.exists():
        shutil.copy2(index_path, backup)

    index_path.write_text(text, encoding="utf-8")
    return backup

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Patcht Sektion 4 direkt in die vorhandene index.html."
    )
    parser.add_argument("--index", default="index.html", help="Pfad zur index.html")
    parser.add_argument("--photo9", required=True, help="Relativer Repository-Pfad zu Foto 9")
    parser.add_argument("--photo16", required=True, help="Relativer Repository-Pfad zu Foto 16")
    args = parser.parse_args()

    try:
        index_path = Path(args.index).resolve()
        backup = patch(index_path, args.photo9, args.photo16)
    except Exception as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 1

    print(f"FERTIG: {index_path}")
    print(f"BACKUP: {backup}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
