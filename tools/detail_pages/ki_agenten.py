import re


LAYOUT = {
    ":root": {
        "--content-max": "1000px",
        "--t-sektionstitel": "clamp(28px, 3.7vw, 52px)",
        "--t-kartentitel": "var(--t-sektionstitel)",
        "--t-kicker-sektion": "var(--t-subtitle)",
        "--t-subtitle": "16px",
        "--t-bulletlabel": "15px",
        "--t-bildunterschrift": "15px",
        "--t-fliesstext": "14px",
        "--detail-section-space": "48px",
        "--analysis-sub-body-gap": "28px",
    },
    ".detail-hero .sub": {"font-size": "16px", "margin-bottom": "24px"},
    ".detail-hero .actions": {"margin-top": "28px", "--t-cta": "12.8px"},
    ".section": {
        "scroll-margin-top": "var(--header-height)",
        "container-type": "inline-size",
        "--detail-photo-base": "calc((min(1000px, 100cqw) - 40px) / 2)",
        "--detail-photo-width": "calc(var(--detail-photo-base) * .8)",
        "--detail-hero-width": "calc((min(1000px, 100cqw) - 32px) * .52)",
        "--detail-hero-image-width": "80%",
        "--detail-content-width": "960px",
    },
    ".section-inner": {"margin-left": "max(0px, calc((100cqw - var(--content-max)) / 4))", "margin-right": "auto"},
    "#hero h1": {"width": "max-content", "max-width": "min(var(--content-max), 100cqw)", "position": "relative", "z-index": "3"},
    "#hero .hero-title-line": {"display": "inline", "white-space": "nowrap"},
    "#hero .visual-card--hero img": {
        "width": "var(--detail-hero-image-width)", "max-width": "100%", "max-height": "none", "left": "auto", "transform": "none",
    },
    "#hero .visual-card--hero::before": {"inset": "0"},
    ".definition-intro": {"margin-bottom": "32px"},
    ".analysis-intro-cards": {
        "gap": "24px",
        "grid-template-columns": "repeat(auto-fit, minmax(min(100%, calc((var(--detail-content-width) - 24px) / 2)), 1fr))",
    },
    ".section-photo": {"justify-self": "center"},
    ".analysis-intro-cards .panel": {"min-width": "0", "overflow-wrap": "anywhere"},
    "#was-ist-das .actions": {"margin-top": "32px", "--t-cta": "12.8px"},
    ".analysis-layout": {
        "grid-template-columns": "minmax(0, .85fr) minmax(0, 1.15fr)",
        "gap": "36px", "margin-top": "32px",
    },
    ".form-grid": {"grid-template-columns": "repeat(auto-fit, minmax(min(100%, 180px), 1fr))"},
    "#leistungen .num-list": {"row-gap": "28px", "column-gap": "36px"},
    ".label-list--single": {"margin-top": "0"},
    ".label-list li": {"color": "var(--nv-gold-highlight)", "margin-bottom": "18px"},
    ".num-list li": {"color": "var(--nv-gold-highlight)", "padding-left": "60px"},
}


NARROW_CONTENT = {
    "width": "var(--detail-content-width)",
    "max-width": "96%",
    "margin-left": "calc((100% - min(var(--detail-content-width), 96%)) / 2 + max(0px, calc((100cqw - var(--content-max)) / 4)))",
    "margin-right": "auto",
}
BODY_SELECTORS = {
    ".analysis-intro-cards", "#leistungen .num-list",
    "#einsatzbereiche > .section-inner > .panel", "#analyse-formular .analysis-layout",
}


def compact_styles(styles):
    styles = styles.replace("\\n", "\n")
    found = set()

    def update_rule(match):
        selector, declarations = match.groups()
        key = re.sub(r"/\*.*?\*/", "", selector, flags=re.S).strip()
        key = re.sub(r"\s+", " ", key)
        changes = dict(LAYOUT.get(key, {}))
        if key in LAYOUT:
            found.add(key)
        if key == ".section" and "18px" in declarations:
            changes["--detail-photo-base"] = "min(1000px, 100cqw)"
        if {part.strip() for part in key.split(",")} == BODY_SELECTORS or key in ("#leistungen .num-list", ".faq-grid", "#was-ist-das .actions"):
            changes.update(NARROW_CONTENT)
        if key in (".detail-hero", "#hero .detail-hero") and declarations.count("minmax") > 1:
            changes.update({"grid-template-columns": "minmax(0, 1fr) var(--detail-hero-width)", "gap": "64px", "--detail-hero-image-width": "100%"})
        if key == "#hero .detail-hero" and "grid-template-columns:1fr" in declarations:
            changes["--detail-hero-image-width"] = "80%"
        if key in (".media-split", "#warum .media-split") and "minmax" in declarations:
            changes.update(NARROW_CONTENT)
            changes.update({
                "grid-template-columns": "var(--detail-photo-width) minmax(0, 1fr)", "gap": "40px",
            })
        if key in (".media-split--visual-left", "#nutzen .media-split--visual-left") and "minmax" in declarations:
            changes.update({
                "grid-template-columns": "var(--detail-photo-width) minmax(0, 1fr)", "gap": "40px",
            })
        if key in ("#warum .section-photo", "#nutzen .section-photo") or key.replace(" ", "") == "#warum.section-photo,#nutzen.section-photo":
            changes.update({"width": "var(--detail-photo-width)", "max-width": "100%"})
        if key == ".analysis-layout" and "minmax(0,1fr); gap: 32px" in declarations:
            changes["grid-template-columns"] = "minmax(0, 1fr)"
        for property_name, value in changes.items():
            pattern = rf"(?<![\w-]){re.escape(property_name)}\s*:\s*([^;}}]+)"
            if re.search(pattern, declarations):
                declarations = re.sub(pattern, lambda current: property_name + ":" + value + (
                    "!important" if "!important" in current.group(1) else ""
                ), declarations)
            else:
                declarations = declarations.rstrip() + f";{property_name}:{value};\n"
        return selector + "{" + declarations + "}"

    result = re.sub(r"([^{}]+)\{([^{}]*)\}", update_rule, styles)
    if set(LAYOUT) != found:
        raise ValueError(f"KI-Layoutreferenz fehlt: {set(LAYOUT) - found}")
    return result


def position_section_headings(document):
    for identifier in ("warum", "nutzen"):
        split = document.select_one(f"#{identifier} .media-split")
        copy = split.select_one(".media-copy")
        for element in list(copy.find_all(recursive=False)):
            if element.name == "h2" or "kicker" in element.get("class", []) or "sub" in element.get("class", []):
                split.insert_before(element.extract())
        if identifier == "warum":
            split["class"] = ["media-split", "media-split--visual-left"]
            split.insert(0, split.select_one(".section-photo").extract())


def complete_form(document):
    form = document.select_one("#nurovelle-analysis-form")
    for control in form.select("input[placeholder], textarea[placeholder], select"):
        control["aria-label"] = control.get("placeholder") or control.option.get_text(strip=True)
    button = document.new_tag("button", attrs={
        "class": "hero-cta", "type": "submit", "id": "nurovelle-analysis-submit",
    })
    surface = document.new_tag("span", attrs={"class": "golden-button"})
    label = document.new_tag("span", attrs={"class": "golden-text"})
    label.string = form.h3.get_text(strip=True)
    surface.append(label)
    button.append(surface)
    form.select_one(".form-grid").append(button)
