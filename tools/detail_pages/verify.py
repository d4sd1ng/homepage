import argparse
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
import html5lib

from build import CONFIG, CONTENT, HOME, ROOT, build_page, preview_path
from reference import SECTION_IDS, reference_scripts


def require(condition, message):
    if not condition:
        raise ValueError(message)


def texts(document, selector):
    return [element.get_text(" ", strip=True) for element in document.select(selector)]


def verify_structure(preview, original, reference, assets):
    require([element["id"] for element in preview.select("[data-section-role]")] == list(SECTION_IDS), "Acht Referenzsektionen fehlen")
    identifiers = Counter(element["id"] for element in preview.select("[id]"))
    require(all(count == 1 for count in identifiers.values()), "Doppelte IDs")
    require(set(element["id"] for element in original.select("main [id]")) <= set(identifiers), "Original-Sprungziele fehlen")
    require(texts(preview, "#hero .hero-title-line") == assets["title_lines"], "Titelzeilen veraendert")
    for selector in (".kicker", ".sub", ".lead", ".actions a"):
        require(texts(preview, "#hero " + selector) == texts(original.main.section, selector), "Hero-Text veraendert: " + selector)
    require(str(preview.header) == str(reference.header), "Referenzheader veraendert")
    require(str(preview.footer) == str(original.footer), "Originalfooter veraendert")
    for destination, source in (("#warum", "#ausgangslage"), ("#leistungen", "#leistungsumfang"), ("#einsatzbereiche", "#moeglich"), ("#nutzen", "#nutzen")):
        for selector in ("h2", "p.sub"):
            require(texts(preview, destination + " " + selector) == texts(original, source + " " + selector)[:1], "Sektionsinhalt veraendert: " + destination)
    require(len(preview.select("#was-ist-das .analysis-intro-cards > article")) == 2, "Definitionskomponente falsch")
    definition = original.main.find_all("section", recursive=False)[1]
    panels = definition.select("article.panel")
    require(texts(preview, ".definition-intro h2") == texts(panels[0], "h2"), "Definitionstitel veraendert")
    first_paragraphs = texts(preview, ".definition-intro .sub, #was-ist-das .analysis-intro-cards > article:first-child p")
    require(" ".join(first_paragraphs) == " ".join(texts(panels[0], "p")), "Definitionstext veraendert")
    require(texts(preview, "#was-ist-das .summary h3") == texts(panels[1], "h2"), "Goldkartentitel veraendert")
    require(texts(preview, "#was-ist-das .summary p") == texts(panels[1], "p"), "Goldkartentext veraendert")
    require(len(preview.select("#leistungen .num-list > li")) == 8, "Nicht genau acht Module")
    require(not preview.select("#leistungen .panel, #leistungen .card-bullets"), "Doppelte Leistungskarten")
    for destination, source in (("#leistungen .num-list li > b", "#module .num-list li b"), ("#leistungen .num-list li > span:not(.module-icon-frame)", "#module .num-list li div > span"), ("#warum .label-list li", "#ausgangslage .card-bullets li"), ("#nutzen .label-list li", "#nutzen .label-list li")):
        require(texts(preview, destination) == texts(original, source), "Listeninhalt veraendert: " + destination)
    require([str(element) for element in preview.select(".pair-grid > .pair")] == [str(element) for element in original.select("#moeglich .pair-grid > .pair")], "Anwendungsbeispiele veraendert")
    require([str(element) for element in preview.select("#faq details")] == [str(element) for element in original.select("#faq details")], "FAQ-Inhalte oder Komponente veraendert")
    require(len(preview.select("#faq details")) == 8, "Nicht genau acht FAQ")
    require(preview.select_one("#hero img")["src"] == "assets/detail_pages_grafics/" + assets["hero"], "Hero falsch")
    require([element["src"] for element in preview.select(".section-photo img")] == ["assets/Fotos/" + name for name in assets["photos"]], "Fotos falsch")


def verify_form(preview, reference):
    form = deepcopy(preview.select_one("#nurovelle-analysis-form"))
    submit = form.select_one("button#nurovelle-analysis-submit[type=submit]")
    require(submit is not None and submit.select_one(".golden-button > .golden-text") is not None, "Absende-CTA fehlt")
    require(submit.get_text(strip=True) == form.h3.get_text(strip=True), "Absende-Text nicht aus Referenz")
    submit.decompose()
    for control in form.select("input[placeholder], textarea[placeholder], select"):
        require(control.get("aria-label") == (control.get("placeholder") or control.option.get_text(strip=True)), "Feldbeschriftung fehlt")
        del control["aria-label"]
    require(str(form) == str(reference.select_one("#nurovelle-analysis-form")), "Formularlogik, Consents oder Honeypot veraendert")


def verify_code(preview, original, reference):
    scripts = [str(script) for script in original.select("script")]
    scripts += [str(script) for script in BeautifulSoup(reference_scripts(reference), "html.parser").select("script")]
    require([str(script) for script in preview.select("script")] == scripts, "JavaScript veraendert")
    for index, script in enumerate(preview.select("script")):
        if script.get("type") == "application/ld+json":
            json.loads(script.string)
        elif not script.get("src"):
            result = subprocess.run(["node", "--check"], input=script.get_text(), text=True, capture_output=True)
            require(result.returncode == 0, f"JavaScript-Syntaxfehler {index}: {result.stderr}")
    css = "\n".join(style.get_text() for style in preview.select("head > style"))
    require("\\n" not in css, "Defekte CSS-Zeilenumbrueche")
    result = subprocess.run(["node", "-e", "require('postcss').parse(require('fs').readFileSync(0,'utf8'))"], input=css, text=True, capture_output=True, cwd=ROOT)
    require(result.returncode == 0, "CSS-Syntaxfehler: " + result.stderr)
    reference_css = reference.style.get_text()
    for selector in (".btn", ".faq-item summary > span", ".faq-item summary:hover > span", ".faq-item summary > span::after", ".faq-item[open] summary > span::after"):
        pattern = re.escape(selector) + r"\s*\{([^{}]*)\}"
        require(re.findall(pattern, css) == re.findall(pattern, reference_css), "FAQ-/CTA-Material veraendert: " + selector)
    require(css.count("!important") == reference_css.count("!important"), "Neue important-Regel")
    require("@media (prefers-reduced-motion: reduce)" in css and ".result-strip h3, .form-panel h3 { animation: none; }" in css, "Reduced Motion fehlt")


def verify_page(filename, assets):
    data = json.loads((CONTENT / (Path(filename).stem + ".json")).read_text())
    original = BeautifulSoup((HOME / filename).read_text(), "html.parser")
    reference = BeautifulSoup((HOME / "analyse.html").read_text(), "html.parser")
    markup = preview_path(filename).read_text()
    preview = BeautifulSoup(markup, "html.parser")
    require(markup == build_page(data, assets), "Vorschau weicht vom Generator ab")
    parser = html5lib.HTMLParser()
    parser.parse(markup)
    require(not parser.errors, f"HTML5-Fehler: {parser.errors}")
    require(preview.find("base") is None, "base wuerde lokale Sprunglinks umleiten")
    require(preview.select_one('meta[name="robots"][content="noindex,nofollow"]') is not None, "noindex fehlt")
    verify_structure(preview, original, reference, assets)
    verify_form(preview, reference)
    verify_code(preview, original, reference)
    missing = []
    for element in preview.select("[src], link[rel=stylesheet], a[href]"):
        address = element.get("src", element.get("href", ""))
        parsed = urlsplit(address)
        if parsed.scheme or parsed.netloc:
            continue
        path = HOME / unquote(parsed.path.lstrip("/")) if parsed.path else preview_path(filename)
        if not path.is_file():
            missing.append(address)
        elif parsed.fragment and path.suffix == ".html":
            target = preview if not parsed.path else BeautifulSoup(path.read_text(), "html.parser")
            if target.find(id=unquote(parsed.fragment)) is None:
                missing.append(address)
    require(not missing, f"Lokale Assets oder Sprungziele fehlen: {missing}")
    print(f"geprueft: {filename} - HTML5, CSS, JS-Syntax, Inhalte, IDs, Links, Header/Footer, Formular, Bilder, acht Sektionen")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pages", nargs="+", choices=["detail_ki-agenten.html"], default=["detail_ki-agenten.html"])
    arguments = parser.parse_args()
    manifest = json.loads((CONFIG / "pages.json").read_text())
    for filename in arguments.pages:
        verify_page(filename, manifest["pages"][filename])


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as error:
        print(f"Pruefung fehlgeschlagen: {error}", file=sys.stderr)
        sys.exit(1)
