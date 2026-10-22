from copy import deepcopy
import re

from bs4 import BeautifulSoup, Comment
from ki_agenten import complete_form


SECTION_IDS = ("hero", "was-ist-das", "warum", "leistungen", "einsatzbereiche", "nutzen", "analyse-formular", "faq")


def copy_contents(target, source):
    target.clear()
    for child in source.contents:
        target.append(deepcopy(child))


def replace_children(target, children):
    target.clear()
    for child in children:
        target.append(deepcopy(child))


def heading(section, source):
    copy_contents(section.select_one("h2"), source.select_one("h2"))
    copy_contents(section.select_one("p.sub"), source.select_one("p.sub"))


def render_main(reference, data, assets):
    document = BeautifulSoup(str(reference.main), "html.parser")
    main = document.main
    source = BeautifulSoup("".join(item["html"] for item in data["sections"]), "html.parser")
    roles = {}
    for item in data["sections"]:
        roles.setdefault(item["role"], []).append(BeautifulSoup(item["html"], "html.parser").section)
    for comment in main.find_all(string=lambda value: isinstance(value, Comment)):
        comment.extract()

    hero = main.select_one("#hero")
    original_hero = roles["hero"][0]
    copy_contents(hero.select_one(".kicker"), original_hero.select_one(".kicker"))
    title = original_hero.h1.get_text(strip=True)
    if " ".join(assets["title_lines"]) != title:
        raise ValueError(f"Titelzeilen veraendern den Text: {data['source']}")
    hero.h1.clear()
    for index, line in enumerate(assets["title_lines"]):
        if index:
            hero.h1.append(" ")
        span = document.new_tag("span", attrs={"class": "hero-title-line"})
        span.string = line
        hero.h1.append(span)
    for selector in ("p.sub", "p.lead"):
        copy_contents(hero.select_one(selector), original_hero.select_one(selector))
    replace_children(hero.select_one(".actions"), original_hero.select(".actions > a"))
    hero_image = hero.select_one(".visual-card--hero img")
    hero_image["src"] = "assets/detail_pages_grafics/" + assets["hero"]
    hero_image["alt"] = ""
    hero_image["fetchpriority"] = "high"

    definition = main.select_one("#was-ist-das")
    panels = roles["definition"][0].select("article.panel")
    copy_contents(definition.select_one(".definition-intro h2"), panels[0].h2)
    paragraphs = panels[0].find_all("p", recursive=False)
    sentences = re.split(r"(?<=\.)\s+", paragraphs[0].get_text(" ", strip=True), maxsplit=1)
    if len(sentences) != 2:
        raise ValueError(f"Definitionszuordnung benoetigt zwei Saetze: {data['source']}")
    definition.select_one(".definition-intro .sub").string = sentences[0]
    target_panels = definition.select(".analysis-intro-cards > article")
    for paragraph in target_panels[0].select("p"):
        paragraph.decompose()
    paragraph = document.new_tag("p")
    paragraph.string = sentences[1]
    target_panels[0].append(paragraph)
    for paragraph in paragraphs[1:]:
        target_panels[0].append(deepcopy(paragraph))
    copy_contents(target_panels[1].h3, panels[1].h2)
    for paragraph in target_panels[1].select("p"):
        paragraph.decompose()
    for paragraph in panels[1].find_all("p", recursive=False):
        target_panels[1].append(deepcopy(paragraph))
    replace_children(definition.select_one(".actions"), original_hero.select(".actions > a"))
    for element in definition.select(".actions [id]"):
        del element["id"]

    problem = main.select_one("#warum")
    original_problem = roles["ausgangslage"][0]
    heading(problem, original_problem)
    target_list = problem.select_one(".label-list")
    if original_problem.select_one(".label-list"):
        replace_children(target_list, original_problem.select(".label-list > li"))
    else:
        target_list.clear()
        for item in original_problem.select(".card-bullets > li"):
            bullet = document.new_tag("li")
            label = document.new_tag("strong")
            copy_contents(label, item)
            bullet.append(label)
            target_list.append(bullet)
    problem.select_one(".section-photo img")["src"] = "assets/Fotos/" + assets["photos"][0]
    problem.select_one(".section-photo img")["alt"] = ""

    services = main.select_one("#leistungen")
    heading(services, source.select_one("#leistungsumfang"))
    modules = source.select("#module .num-list > li")
    if not modules:
        raise ValueError(f"Module fehlen: {data['source']}")
    prototype = deepcopy(services.select_one(".num-list > li"))
    target_list = services.select_one(".num-list")
    target_list.clear()
    for module in modules:
        item = deepcopy(prototype)
        image = deepcopy(module.select_one("img"))
        image["class"] = ["module-icon"]
        for attribute in ("width", "height"):
            image.attrs.pop(attribute, None)
        item.select_one(".module-icon").replace_with(image)
        copy_contents(item.b, module.b)
        copy_contents(item.select_one("li > span:not(.module-icon-frame)"), module.select_one("div > span"))
        target_list.append(item)

    application = main.select_one("#einsatzbereiche")
    original_application = source.select_one("#moeglich")
    heading(application, original_application)
    replace_children(application.select_one(".pair-grid"), original_application.select(".pair-grid > .pair"))
    after_text = original_application.select_one("p.text")
    if after_text is None:
        application.select_one(".text--after").decompose()
    else:
        copy_contents(application.select_one(".text--after"), after_text)

    benefits = main.select_one("#nutzen")
    original_benefits = roles["nutzen"][0]
    heading(benefits, original_benefits)
    replace_children(benefits.select_one(".label-list"), original_benefits.select(".label-list > li"))
    benefits.select_one(".section-photo img")["src"] = "assets/Fotos/" + assets["photos"][1]
    benefits.select_one(".section-photo img")["alt"] = ""

    replace_children(main.select_one("#faq .faq-grid"), roles["faq"][0].select(".faq-grid > details"))
    for item in roles.get("extras", []):
        main.select_one("#analyse-formular").insert_before(deepcopy(item))
        main.select_one("#analyse-formular").insert_before(deepcopy(reference.select_one(".section-divider")))
    if source.select_one("#nv-seo-inline"):
        widget_section = source.select_one("#nv-seo-inline").find_parent("section")
        main.select_one("#analyse-formular").insert_before(deepcopy(widget_section))

    destinations = {
        "hero": "hero", "definition": "was-ist-das", "ausgangslage": "warum",
        "leistungen": "leistungen", "anwendung": "einsatzbereiche",
        "nutzen": "nutzen", "conversion": "analyse-formular", "faq": "faq",
    }
    for role, identifier in destinations.items():
        main.select_one("#" + identifier)["data-section-role"] = role
    for item in data["sections"]:
        section = BeautifulSoup(item["html"], "html.parser").section
        destination = main.select_one("#" + destinations.get(item["role"], "analyse-formular") + " .section-inner")
        for element in [section, *section.select("[id]")]:
            identifier = element.get("id")
            if identifier and main.find(id=identifier) is None:
                destination.insert(0, document.new_tag("span", attrs={"id": identifier, "aria-hidden": "true"}))
    if data["source"] == "detail_ki-agenten.html":
        complete_form(document)
    return main.decode_contents()


def reference_scripts(reference):
    return "\n".join(str(script) for script in reference.select("script") if script.string and (
        "const NUROVELLE_API_BASE" in script.string or 'getContext("webgl"' in script.string
    ))
