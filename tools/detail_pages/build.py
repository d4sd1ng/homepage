import argparse
from collections import Counter
import hashlib
import html
import json
import re
from pathlib import Path
from string import Template

from bs4 import BeautifulSoup, Comment

from reference import reference_scripts, render_main
from ki_agenten import compact_styles


ROOT = Path(__file__).resolve().parents[2]
HOME = ROOT / "homepage"
CONFIG = Path(__file__).resolve().parent
CONTENT = CONFIG / "content"
PROTECTED = [HOME / name for name in (
    "analyse.html", "index.html", "shared-header-footer.css", "nurovelle-tokens.css"
)]
ROLES = ("hero", "definition", "ausgangslage", "leistungen", "anwendung", "nutzen", "extras", "conversion", "faq")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def preview_path(filename):
    return HOME / ("preview-" + filename)


def attributes(tag):
    result = []
    for name, value in tag.attrs.items():
        if isinstance(value, list):
            value = " ".join(value)
        result.append(f'{name}="{html.escape(str(value), quote=True)}"')
    return " ".join(result)


def text_inventory(markup):
    soup = BeautifulSoup(markup, "html.parser")
    return Counter(
        text.strip() for text in soup.strings
        if text.strip() and not isinstance(text, Comment)
        and text.parent.name not in ("style", "script")
    )


def section_role(section, index):
    identifier = section.get("id", "")
    if index == 0:
        return "hero"
    if index == 1 and not identifier:
        return "definition"
    if identifier == "was-ist-das":
        return "definition"
    if identifier in ("ausgangslage", "warum", "engpaesse"):
        return "ausgangslage"
    if identifier in ("leistungsumfang", "leistungen", "module", "loesungsansatz"):
        return "leistungen"
    if identifier in ("anwendung", "moeglich", "moeglichkeiten", "einsatzbereiche", "bereiche", "prompts", "projektablauf"):
        return "anwendung"
    if identifier.startswith("gruppe-") or section.select_one("#nv-seo-inline"):
        return "anwendung"
    if identifier == "nutzen":
        return "nutzen"
    if identifier in ("kontakt", "analyse-formular"):
        return "conversion"
    if identifier == "faq":
        return "faq"
    if identifier in ("preis", "datenschutz"):
        return "extras"
    raise ValueError(f"Nicht zugeordnete Sektion: {identifier!r}")


def extract_page(filename):
    source = HOME / filename
    soup = BeautifulSoup(source.read_text(), "html.parser")
    main = soup.find("main")
    if main is None:
        raise ValueError(f"main fehlt: {filename}")
    before = []
    after = []
    reached_main = False
    for child in soup.body.children:
        if child is main:
            reached_main = True
            continue
        if getattr(child, "name", None) == "script":
            continue
        (after if reached_main else before).append(str(child))
    head = []
    for child in soup.head.children:
        if getattr(child, "name", None) in ("style", "script"):
            continue
        if getattr(child, "name", None) == "link" and "stylesheet" in child.get("rel", []):
            continue
        head.append(str(child))
    sections = []
    for index, section in enumerate(main.find_all("section", recursive=False)):
        sections.append({"role": section_role(section, index), "html": str(section)})
    if text_inventory(str(main)) != text_inventory("".join(section["html"] for section in sections)):
        raise ValueError(f"Inhalte ausserhalb der Sektionen: {filename}")
    return {
        "source": filename,
        "source_sha256": digest(source),
        "html_attributes": attributes(soup.html),
        "body_attributes": attributes(soup.body),
        "main_attributes": attributes(main),
        "head": "".join(head),
        "before_main": "".join(before),
        "after_main": "".join(after),
        "scripts": "\n".join(str(script) for script in soup.find_all("script")),
        "sections": sections,
    }


def build_page(data, assets):
    source = HOME / data["source"]
    if digest(source) != data["source_sha256"]:
        raise ValueError(f"Original seit Extraktion geaendert: {data['source']}")
    files = [assets["hero"], *assets["photos"]]
    if any(filename is None for filename in files):
        raise ValueError(f"Bildzuordnung offen: {data['source']}")
    for path in [HOME / "assets/detail_pages_grafics" / assets["hero"], *[
        HOME / "assets/Fotos" / filename for filename in assets["photos"]
    ]]:
        if not path.is_file():
            raise ValueError(f"Asset fehlt: {path.relative_to(ROOT)}")
    reference = BeautifulSoup((HOME / "analyse.html").read_text(), "html.parser")
    sections = render_main(reference, data, assets)
    styles = "\n".join(str(style) for style in reference.select("head > style"))
    styles = styles.replace(
        "@media(max-width:1100px){\n  #hero .hero-title-line",
        "@media(max-width:900px){\n  #hero .hero-title-line",
    )
    if data["source"] == "detail_ki-agenten.html":
        styles = compact_styles(styles)
    extension_styles = ""
    if data["source"] == "detail_seo.html":
        original = BeautifulSoup(source.read_text(), "html.parser")
        extension_styles = "<style>" + "\n".join(re.findall(r"\.nv-seo-inline[^{}]*\{[^{}]*\}", original.style.string)) + "</style>"
    return Template((CONFIG / "template.html").read_text()).substitute(
        **{name: data[name] for name in (
            "html_attributes", "body_attributes", "main_attributes", "head",
            "after_main",
        )}, sections=sections, reference_styles=styles, extension_styles=extension_styles,
        before_main=str(reference.header),
        scripts=data["scripts"] + "\n" + reference_scripts(reference),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--extract", action="store_true")
    parser.add_argument("--pages", nargs="+")
    arguments = parser.parse_args()
    manifest = json.loads((CONFIG / "pages.json").read_text())
    pages = arguments.pages or ["detail_ki-agenten.html"]
    if any(name not in manifest["pages"] for name in pages):
        parser.error("Nur ausdruecklich aufgefuehrte Detailseiten sind erlaubt")
    protected = {str(path): digest(path) for path in PROTECTED}
    CONTENT.mkdir(exist_ok=True)
    for filename in pages:
        content_path = CONTENT / (Path(filename).stem + ".json")
        if arguments.extract:
            if content_path.exists():
                raise ValueError(f"Seitendaten existieren bereits: {content_path.name}")
            data = extract_page(filename)
            content_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        else:
            data = json.loads(content_path.read_text())
        rendered = build_page(data, manifest["pages"][filename])
        destination = preview_path(filename)
        destination.write_text(rendered)
        print(f"Vorschau erzeugt: {destination.relative_to(ROOT)}")
    if protected != {str(path): digest(path) for path in PROTECTED}:
        raise ValueError("Geschuetzte Dateien wurden veraendert")


if __name__ == "__main__":
    main()
