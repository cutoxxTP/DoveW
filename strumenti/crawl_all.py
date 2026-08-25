import os, glob
for k in ("HTTP_PROXY","HTTPS_PROXY","http_proxy","https_proxy"): os.environ.pop(k, None)
from playwright.sync_api import sync_playwright
SITE="/home/user/DoveW/archivio/sito"
pages=sorted(os.path.basename(f) for f in glob.glob(SITE+"/*.html"))
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CHROME, args=["--no-sandbox","--disable-dev-shm-usage"])
    ctx=b.new_context(viewport={"width":1440,"height":900})
    ctx.route("**/*", lambda r: r.abort() if "127.0.0.1" not in r.request.url else r.continue_())
    pg=ctx.new_page()
    for f in pages:
        try:
            pg.goto(f"http://127.0.0.1:8123/{f}", wait_until="load", timeout=30000)
            pg.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            pg.wait_for_timeout(2500)
        except Exception as e: print("ERR",f,e)
    b.close()
print(f"visitate {len(pages)} pagine")
