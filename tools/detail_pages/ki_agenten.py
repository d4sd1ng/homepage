import re


LAYOUT = {
    ":root": {
        "--content-max": "1000px",
        "--t-sektionstitel": "clamp(28px, 3.7vw, 52px)",
        "--t-kartentitel": "clamp(26px, 2.1vw, 34px)",
        "--t-subtitle": "16px",
        "--t-bulletlabel": "15px",
        "--t-bildunterschrift": "15px",
        "--t-fliesstext": "14px",
        "--detail-section-space": "48px",
        "--analysis-sub-body-gap": "28px",
    },
    ".detail-hero .sub": {"font-size": "16px", "margin-bottom": "24px"},
    ".detail-hero .actions": {"margin-top": "28px"},
    ".section": {"scroll-margin-top": "var(--header-height)"},
    "#hero h1": {"width": "max-content", "position": "relative", "z-index": "3"},
    "#hero .hero-title-line": {"white-space": "nowrap"},
    "#hero .visual-card--hero img": {
        "width": "100%", "max-width": "100%", "max-height": "none", "left": "auto", "transform": "none",
    },
    "#hero .visual-card--hero::before": {"inset": "0"},
    ".definition-intro": {"margin-bottom": "32px"},
    ".analysis-intro-cards": {"gap": "24px"},
    "#was-ist-das .actions": {"margin-top": "32px"},
    ".analysis-layout": {
        "grid-template-columns": "minmax(0, .85fr) minmax(0, 1.15fr)",
        "gap": "36px", "margin-top": "32px",
    },
    ".form-grid": {"grid-template-columns": "repeat(auto-fit, minmax(min(100%, 220px), 1fr))"},
    "#leistungen .num-list": {"row-gap": "28px", "column-gap": "36px"},
    ".label-list--single": {"margin-top": "28px"},
    ".label-list li": {"color": "var(--nv-gold-highlight)", "margin-bottom": "18px"},
    ".num-list li": {"color": "var(--nv-gold-highlight)", "padding-left": "60px"},
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
        if key in (".detail-hero", "#hero .detail-hero") and declarations.count("minmax") > 1:
            changes.update({"grid-template-columns": "minmax(0, .7fr) minmax(0, 1.3fr)", "gap": "32px"})
        if key in (".media-split", "#warum .media-split") and "minmax" in declarations:
            changes.update({"grid-template-columns": "minmax(0, 1fr) minmax(0, 1fr)", "gap": "40px"})
        if key in (".media-split--visual-left", "#nutzen .media-split--visual-left") and "minmax" in declarations:
            changes.update({"grid-template-columns": "minmax(0, 1fr) minmax(0, 1fr)", "gap": "40px"})
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
