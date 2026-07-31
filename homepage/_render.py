from playwright.sync_api import sync_playwright
url = "file:///G:/Projects/homepage_repo/homepage/index.html"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 3840, "height": 1900}, device_scale_factor=1)
    pg.goto(url, wait_until="networkidle"); pg.wait_for_timeout(900)
    top = pg.eval_on_selector(".nv-about","el=>Math.round(el.getBoundingClientRect().top+window.scrollY)")
    pg.evaluate(f"window.scrollTo(0,{top}-84)"); pg.wait_for_timeout(400)
    pg.screenshot(path=r"G:\Projects\homepage_repo\homepage\_s2.png")
    b.close()
print("OK")
