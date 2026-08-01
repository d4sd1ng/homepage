#!/usr/bin/env python3
"""Generate detail pages from homepage/detail_template.html + homepage/detail_content/*.json.

Usage:
  python3 tools/build_detailpages.py            # build all content files
  python3 tools/build_detailpages.py --check    # build and diff against existing output files

Each content JSON chooses its sections: a missing section key removes that
section from the generated page. The Potenzialanalyse form section (and its
API script) is included only when "cta_form" is present; other pages use
"cta_buttons" for a simple closing CTA.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "homepage" / "detail_template.html"
CONTENT_DIR = ROOT / "homepage" / "detail_content"
OUT_DIR = ROOT / "homepage"

# Section start markers (comment line) -> removed up to and including the next </section>
SECTION_MARKERS = {
    "cards": "<!-- ==================== SCHWERPUNKTE / KERNNUTZEN ==================== -->",
    "definition": "<!-- ========================= DEFINITION ========================= -->",
    "warum": "<!-- ========================= WARUM ========================= -->",
    "leistungen": "<!-- ========================= LEISTUNGEN ========================= -->",
    "pairs": "<!-- ============ EINSATZBEREICHE + WAS DAMIT MÖGLICH WIRD ============ -->",
    "nutzen": "<!-- ========================= NUTZEN ========================= -->",
    "cta_form": "<!-- ==================== CTA — POTENZIALANALYSE STARTEN ==================== -->",
    "cta_buttons": "<!-- ==================== CTA — BUTTONS ==================== -->",
}
API_SCRIPT_START = "<script>\nconst NUROVELLE_API_BASE"


def render_label_items(items):
    return "\n".join(f"<li><strong>{i['label']}</strong>{i['text']}</li>" for i in items)


def render_num_items(items):
    return "\n".join(f"<li><b>{i['label']}</b><span>{i['text']}</span></li>" for i in items)


def render_bullets(items):
    return "".join(f"<li>{t}</li>" for t in items)


def render_paragraphs(items):
    return "".join(f"<p>{t}</p>" for t in items)


def render_cols(items):
    return "\n".join(f"<p>{t}</p>" for t in items)


def render_buttons(items):
    return "".join(f'<a class="btn" href="{b["href"]}">{b["label"]}</a>' for b in items)


def render_pairs(items):
    chip = (
        '<span class="pair-chip"><svg class="chip-icon" viewBox="0 0 24 24" '
        'aria-hidden="true"><use href="#i-{icon}"/></svg>{label}</span>'
    )
    arrow = (
        '<span class="pair-arrow"><svg viewBox="0 0 24 24" aria-hidden="true">'
        '<use href="#i-chev"/></svg></span>'
    )
    out = []
    for p in items:
        left = chip.format(icon=p["from_icon"], label=p["from"])
        right = chip.format(icon=p["to_icon"], label=p["to"]).replace(
            'class="pair-chip"', 'class="pair-chip pair-chip--gold"'
        )
        out.append(f'<div class="pair">{left}{arrow}{right}</div>')
    return "\n".join(out)


def drop_block(html, start_marker, end_marker):
    start = html.find(start_marker)
    if start < 0:
        raise SystemExit(f"marker not found: {start_marker!r}")
    end = html.index(end_marker, start) + len(end_marker)
    if html[end : end + 1] == "\n":
        end += 1
    return html[:start] + html[end:]


def placeholder_map(c):
    m = {
        "{{PAGE_TITLE}}": c["page"]["title"],
        "{{PAGE_DESC}}": c["page"]["description"],
        "{{HERO_KICKER}}": c["hero"]["kicker"],
        "{{HERO_TITLE}}": c["hero"]["title"],
        "{{HERO_SUB}}": c["hero"]["sub"],
        "{{HERO_LEAD}}": c["hero"]["lead"],
        "{{HERO_IMAGE}}": c["hero"]["image"],
        "{{HERO_IMAGE_ALT}}": c["hero"]["image_alt"],
        "{{HERO_ACTIONS}}": render_buttons(c["hero"]["actions"]),
    }
    if "cards" in c:
        left, gold = c["cards"]["left"], c["cards"]["gold"]
        m.update({
            "{{CARD_TITLE}}": left["title"],
            "{{CARD_SUB}}": left["sub"],
            "{{CARD_TEXT}}": left["text"],
            "{{CARD_BULLETS}}": render_bullets(left["bullets"]),
            "{{GOLD_TITLE}}": gold["title"],
            "{{GOLD_SUB}}": gold["sub"],
            "{{GOLD_TEXTS}}": render_paragraphs(gold["texts"]),
        })
    if "definition" in c:
        m.update({
            "{{DEF_KICKER}}": c["definition"]["kicker"],
            "{{DEF_TITLE}}": c["definition"]["title"],
            "{{DEF_SUB}}": c["definition"]["sub"],
            "{{DEF_COLS}}": render_cols(c["definition"]["cols"]),
        })
    if "warum" in c:
        m.update({
            "{{WARUM_KICKER}}": c["warum"]["kicker"],
            "{{WARUM_TITLE}}": c["warum"]["title"],
            "{{WARUM_ITEMS}}": render_label_items(c["warum"]["items"]),
        })
    if "leistungen" in c:
        m.update({
            "{{LEIST_KICKER}}": c["leistungen"]["kicker"],
            "{{LEIST_TITLE}}": c["leistungen"]["title"],
            "{{LEIST_ITEMS}}": render_num_items(c["leistungen"]["items"]),
        })
    if "pairs" in c:
        m.update({
            "{{PAIRS_KICKER}}": c["pairs"]["kicker"],
            "{{PAIRS_TITLE}}": c["pairs"]["title"],
            "{{PAIRS_SUB}}": c["pairs"]["sub"],
            "{{PAIRS_ITEMS}}": render_pairs(c["pairs"]["items"]),
            "{{PAIRS_NOTE}}": c["pairs"]["note"],
        })
    if "nutzen" in c:
        m.update({
            "{{NUTZEN_KICKER}}": c["nutzen"]["kicker"],
            "{{NUTZEN_TITLE}}": c["nutzen"]["title"],
            "{{NUTZEN_ITEMS}}": render_label_items(c["nutzen"]["items"]),
        })
    if "cta_buttons" in c:
        m.update({
            "{{CTAB_KICKER}}": c["cta_buttons"]["kicker"],
            "{{CTAB_TITLE}}": c["cta_buttons"]["title"],
            "{{CTAB_SUB}}": c["cta_buttons"]["sub"],
            "{{CTAB_BUTTONS}}": render_buttons(c["cta_buttons"]["buttons"]),
        })
    return m


def build(content):
    html = TEMPLATE.read_text(encoding="utf-8")

    for key, marker in SECTION_MARKERS.items():
        if key not in content and marker in html:
            html = drop_block(html, marker, "</section>")
    if "cta_form" not in content:
        html = drop_block(html, API_SCRIPT_START, "</script>")

    for placeholder, value in placeholder_map(content).items():
        if placeholder not in html:
            raise SystemExit(f"placeholder missing in template: {placeholder}")
        html = html.replace(placeholder, value)

    leftover = [line for line in html.splitlines() if "{{" in line]
    if leftover:
        raise SystemExit(f"unfilled placeholders remain: {leftover[:3]}")
    return html


def main():
    check = "--check" in sys.argv
    failed = False
    for path in sorted(CONTENT_DIR.glob("*.json")):
        content = json.loads(path.read_text(encoding="utf-8"))
        out_path = OUT_DIR / content["page"]["output"]
        html = build(content)
        if check:
            existing = out_path.read_text(encoding="utf-8") if out_path.exists() else ""
            status = "OK" if existing == html else "DIFFERS"
            failed |= status == "DIFFERS"
            print(f"{path.name} -> {out_path.name}: {status}")
        else:
            out_path.write_text(html, encoding="utf-8")
            print(f"{path.name} -> {out_path.name}: written")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
