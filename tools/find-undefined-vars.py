#!/usr/bin/env python3
"""Static hygiene checks for a CSS/HTML file (incl. single-file inline <style>).

Checks:
  1. CSS custom properties used via var() but never defined  -> HARD FAIL
  2. Classes used in HTML but with no matching CSS rule       -> warning
  3. Classes defined in CSS but never used in HTML            -> warning

Class checks are heuristic: classes toggled by JS (is-*, has-*, querySelector,
classList.add) legitimately appear on only one side. Such names are reported
but never cause a non-zero exit. Only undefined var()s fail the run.

Usage:
  python3 tools/find-undefined-vars.py [--vars-only|--classes-only] [file ...]
Default file: homepage/index.html
"""
import re
import sys

VAR = r"--[a-z0-9-]+"  # narrow to r"--nv-[a-z0-9-]+" for tokens only
# class names commonly added/removed by JS -> don't warn about these
JS_STATE = re.compile(r"^(is-|has-|js-|active$|open$|show$|hidden$)")


def split_style_html(doc):
    """Return (concatenated <style> contents, the rest of the document)."""
    styles = re.findall(r"<style[^>]*>(.*?)</style>", doc, re.S | re.I)
    html = re.sub(r"<style[^>]*>.*?</style>", "", doc, flags=re.S | re.I)
    return "\n".join(styles), html


def strip_css_noise(css):
    """Drop comments, url(...) and quoted strings so a '.foo' inside a
    data-URI or content:"" is not mistaken for a class selector."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"url\([^)]*\)", "", css, flags=re.S)
    css = re.sub(r'"[^"]*"|\'[^\']*\'', "", css)
    return css


def check_vars(doc):
    used = set(re.findall(r"var\(\s*(" + VAR + r")\s*[,)]", doc))
    defined = set(re.findall(r"^\s*(" + VAR + r")\s*:", doc, re.M))
    broken = sorted(
        m for m in used - defined
        if re.search(r"var\(\s*" + re.escape(m) + r"\s*\)", doc)
    )
    print(f"  vars: used={len(used)} defined={len(defined)}")
    print(f"  UNDEFINED var() (no fallback -> BROKEN): {broken or 'none'}")
    return not broken


def check_classes(doc):
    css, html = split_style_html(doc)

    defined = set(re.findall(r"\.([A-Za-z_][\w-]*)", strip_css_noise(css)))

    used = set()
    for attr in re.findall(r'class\s*=\s*"([^"]*)"', html):
        used.update(attr.split())
    for attr in re.findall(r"class\s*=\s*'([^']*)'", html):
        used.update(attr.split())

    in_html_not_css = sorted(c for c in used - defined if not JS_STATE.search(c))
    in_css_not_html = sorted(c for c in defined - used if not JS_STATE.search(c))

    print(f"  classes: used-in-html={len(used)} defined-in-css={len(defined)}")
    print(f"  used in HTML but NO css rule ({len(in_html_not_css)}):")
    print("    " + (", ".join(in_html_not_css) or "none"))
    print(f"  defined in CSS but UNUSED in html ({len(in_css_not_html)}):")
    print("    " + (", ".join(in_css_not_html) or "none"))
    print("  (heuristic: JS-toggled/queried classes may show on one side)")


def main(argv):
    mode, files = "all", []
    for a in argv:
        if a == "--vars-only":
            mode = "vars"
        elif a == "--classes-only":
            mode = "classes"
        else:
            files.append(a)
    files = files or ["homepage/index.html"]

    ok = True
    for path in files:
        doc = open(path, encoding="utf-8").read()
        print(f"\n{path}")
        if mode in ("all", "vars"):
            ok = check_vars(doc) and ok
        if mode in ("all", "classes"):
            check_classes(doc)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
