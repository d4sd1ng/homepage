#!/usr/bin/env python3
"""Generate detail pages from homepage/detail_template.html + homepage/detail_content/*.json.

DESIGN RULE (fixed): every detail page mirrors the Potenzialanalyse page
(analyse.html) exactly — same sections, same order, same forms:
  1 Hero | 2 black+gold cards | 3 two-column text | 4 gold-label list
  | 5 numbered tiles | 6 emerald base card (chips/pairs) | 7 gold-label list
  | 8 CTA (form only on analyse, buttons elsewhere) | 9 FAQ (always last).
Layout hints inside delivered copy (e.g. "Holo-Card", "best_card_single")
are IGNORED — content is distributed into the fixed slots above.

Usage:
  python3 tools/build_detailpages.py            # build all content files
  python3 tools/build_detailpages.py --check    # build and diff against existing output files

The template holds the page skeleton (head, CSS, header, hero, footer,
scripts) with a {{SECTIONS}} slot, plus a fragment library at the end of the
file between <!--FRAGMENTS--> markers (stripped from output). Each content
JSON provides "sections": an ordered list of section objects; the same type
may repeat. The Potenzialanalyse form section ("cta_form") brings the API
script with it; pages without it get the script removed.

Section types and fields (optional fields may be omitted):
  cards      left{title,sub,text,bullets[]}, gold{title,sub,texts[]}
  textcols   kicker,title,sub,cols[]
  labellist  kicker,title,[sub],[text],items[{label,text}]
  numlist    kicker,title,[sub],[text],items[{label,text}]
  autocards  kicker,title,[sub],[text],items[{icon,label,text}]  (3-col card grid)
  bullets    kicker,title,[sub],[text],[group],items[]   (gold-dot list)
  chips      kicker,title,[sub],[text],[group],items[]   (gold-framed chip grid;
             items may be {icon,label}; "base": true wraps the grid in a panel card)
  split      kicker,title,[sub],[text],[group],[style:"dots"|"chips"],items[]
             (text column left, list column right)
  groups     kicker,title,[sub],[text],groups[{title,items[]}]
  pairs      kicker,title,sub,items[{from_icon,from,to_icon,to}],[note]
  panel_cta  title,sub,text,buttons[{label,href}]
  faq        kicker,title,[sub],[text],items[{q,a}]
  cta_form   kicker,title,sub
  cta_buttons kicker,title,sub,[text],buttons[{label,href}]
Every section may set "id" (anchor); defaults to its type name.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "homepage" / "detail_template.html"
CONTENT_DIR = ROOT / "homepage" / "detail_content"
OUT_DIR = ROOT / "homepage"

API_SCRIPT_START = "<script>\nconst NUROVELLE_API_BASE"
FRAG_REGION = re.compile(r"\n<!--FRAGMENTS-->\n(.*)<!--/FRAGMENTS-->\n?", re.S)
FRAG_ITEM = re.compile(r"<!--F:(\w+)-->\n(.*?)<!--/F-->\n", re.S)


def load_template():
    tpl = TEMPLATE.read_text(encoding="utf-8")
    m = FRAG_REGION.search(tpl)
    if not m:
        raise SystemExit("fragment region missing in template")
    fragments = dict(FRAG_ITEM.findall(m.group(1)))
    skeleton = tpl[: m.start()] + tpl[m.end():]
    return skeleton, fragments


def sub_text_extra(s):
    out = ""
    if s.get("sub"):
        out += f'\n<p class="sub">{s["sub"]}</p>'
    if s.get("text"):
        out += f'\n<p class="text">{s["text"]}</p>'
    return out


def render_chip_items(items):
    out = []
    for i in items:
        if isinstance(i, dict):
            inner = (f'<svg class="chip-icon" viewBox="0 0 24 24" aria-hidden="true">'
                     f'<use href="#i-{i["icon"]}"/></svg>{i["label"]}')
            if i.get("href"):
                inner = f'<a href="{i["href"]}">{inner}</a>'
            out.append(f"<li>{inner}</li>")
        else:
            out.append(f"<li>{i}</li>")
    return "\n".join(out)


def render_buttons(items):
    return "".join(f'<a class="btn" href="{b["href"]}">{b["label"]}</a>' for b in items)


def render_pair_items(items):
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


def render_section(s, fragments):
    t = s["type"]
    frag = fragments.get(t)
    if frag is None:
        raise SystemExit(f"unknown section type: {t}")
    r = frag.replace("{{SID}}", s.get("id", t))
    for key in ("kicker", "title", "sub", "text", "note"):
        r = r.replace("{{" + key.upper() + "}}", s.get(key, ""))

    if t == "cards":
        left, gold = s["left"], s["gold"]
        r = (r.replace("{{LEFT_TITLE}}", left["title"])
             .replace("{{LEFT_SUB}}", left["sub"])
             .replace("{{LEFT_TEXT}}", left["text"])
             .replace("{{LEFT_BULLETS}}", "".join(f"<li>{b}</li>" for b in left["bullets"]))
             .replace("{{GOLD_TITLE}}", gold["title"])
             .replace("{{GOLD_SUB}}", gold["sub"])
             .replace("{{GOLD_TEXTS}}", "".join(f"<p>{p}</p>" for p in gold["texts"])))
    elif t == "textcols":
        if s.get("single") or len(s["cols"]) == 1:
            r = r.replace('class="text-cols"', 'class="text-cols text-cols--1"')
        r = r.replace("{{COLS}}", "\n".join(f"<p>{c}</p>" for c in s["cols"]))
    elif t == "labellist":
        r = r.replace("{{EXTRA}}", sub_text_extra(s))
        r = r.replace("{{ITEMS}}", "\n".join(
            f"<li><strong>{i['label']}</strong>{i['text']}</li>" for i in s["items"]))
    elif t == "numlist":
        r = r.replace("{{EXTRA}}", sub_text_extra(s))
        r = r.replace("{{ITEMS}}", "\n".join(
            f"<li><b>{i['label']}</b><span>{i['text']}</span></li>" for i in s["items"]))
    elif t == "autocards":
        r = r.replace("{{EXTRA}}", sub_text_extra(s))
        r = r.replace("{{ITEMS}}", "\n".join(
            '<article class="panel auto-card"><h3><svg class="chip-icon" viewBox="0 0 24 24" '
            'aria-hidden="true"><use href="#i-{icon}"/></svg>{label}</h3><p>{text}</p></article>'.format(**i)
            for i in s["items"]))
    elif t == "bullets":
        r = r.replace("{{EXTRA}}", sub_text_extra(s))
        r = r.replace("{{GROUP_HEAD}}", f'\n<h3>{s["group"]}</h3>' if s.get("group") else "")
        r = r.replace("{{ITEMS}}", "\n".join(f"<li>{i}</li>" for i in s["items"]))
    elif t == "groups":
        r = r.replace("{{EXTRA}}", sub_text_extra(s))
        r = r.replace("{{GROUPS}}", "\n".join(
            '<article class="{cls}">{head}<ul class="dot-list">{items}</ul></article>'.format(
                cls="panel summary" if g.get("gold") else "panel",
                head=f'<h3>{g["title"]}</h3>' if g.get("title") else "",
                items="".join(f"<li>{i}</li>" for i in g["items"]))
            for g in s["groups"]))
    elif t == "chips":
        r = r.replace("{{EXTRA}}", sub_text_extra(s))
        r = r.replace("{{GROUP_HEAD}}", f'\n<h3>{s["group"]}</h3>' if s.get("group") else "")
        grid = f'<ul class="chip-list">\n{render_chip_items(s["items"])}\n</ul>'
        if s.get("base"):
            grid = f'<article class="panel chips-panel">\n{grid}\n</article>'
        r = r.replace('<ul class="chip-list">\n{{ITEMS}}\n</ul>', grid)
    elif t == "split":
        r = r.replace("{{EXTRA}}", sub_text_extra(s))
        head = f'<h3>{s["group"]}</h3>\n' if s.get("group") else ""
        n = len(s["items"])
        if s.get("style") == "chips":
            side = f'<ul class="chip-list chip-list--2">\n{render_chip_items(s["items"])}\n</ul>'
        else:
            cls = "dot-list dot-list--1" if n <= 6 else "dot-list"
            side = f'<ul class="{cls}">\n' + "\n".join(f"<li>{i}</li>" for i in s["items"]) + "\n</ul>"
        r = r.replace("{{SIDE}}", head + side)
    elif t == "pairs":
        r = r.replace("{{CHIPS_ROW}}",
                      f'<ul class="chip-list pair-chips-row">\n{render_chip_items(s["chips"])}\n</ul>\n'
                      if s.get("chips") else "")
        r = r.replace("{{ITEMS}}", render_pair_items(s["items"]))
        r = r.replace("{{NOTE_BLOCK}}",
                      f'\n<p class="text text--after">{s["note"]}</p>' if s.get("note") else "")
    elif t in ("panel_cta", "cta_buttons"):
        r = r.replace("{{EXTRA}}", sub_text_extra({"text": s.get("text")}))
        r = r.replace("{{BUTTONS}}", render_buttons(s["buttons"]))
    elif t == "faq":
        r = r.replace("{{EXTRA}}", sub_text_extra(s))
        r = r.replace("{{ITEMS}}", "\n".join(
            f'<details class="faq-item"><summary><span>{i["q"]}</span></summary>'
            f'<p>{i["a"]}</p></details>' for i in s["items"]))
    elif t == "cta_form":
        pass  # kicker/title/sub already substituted above
    return f"<!-- ===== {t} ===== -->\n{r}"


def build(content, skeleton, fragments):
    html = skeleton
    h = content["hero"]
    subs = {
        "{{PAGE_TITLE}}": content["page"]["title"],
        "{{PAGE_DESC}}": content["page"]["description"],
        "{{HERO_KICKER}}": h["kicker"],
        "{{HERO_TITLE}}": h["title"],
        "{{HERO_SUB}}": h["sub"],
        "{{HERO_LEAD}}": h["lead"],
        "{{HERO_IMAGE}}": h["image"],
        "{{HERO_IMAGE_ALT}}": h["image_alt"],
        "{{HERO_ACTIONS}}": render_buttons(h["actions"]),
    }
    for ph, value in subs.items():
        if ph not in html:
            raise SystemExit(f"placeholder missing in template: {ph}")
        html = html.replace(ph, value)

    ordered = sorted(content["sections"], key=lambda s: s["type"] == "faq")
    sections = "".join(render_section(s, fragments) for s in ordered)
    html = html.replace("{{SECTIONS}}\n", sections)

    if not any(s["type"] == "cta_form" for s in content["sections"]):
        start = html.find(API_SCRIPT_START)
        if start >= 0:
            end = html.index("</script>", start) + len("</script>")
            if html[end : end + 1] == "\n":
                end += 1
            html = html[:start] + html[end:]

    leftover = [line for line in html.splitlines() if "{{" in line]
    if leftover:
        raise SystemExit(f"unfilled placeholders remain: {leftover[:3]}")
    return html


def main():
    check = "--check" in sys.argv
    skeleton, fragments = load_template()
    failed = False
    for path in sorted(CONTENT_DIR.glob("*.json")):
        content = json.loads(path.read_text(encoding="utf-8"))
        out_path = OUT_DIR / content["page"]["output"]
        html = build(content, skeleton, fragments)
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
