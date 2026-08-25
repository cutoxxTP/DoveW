# -*- coding: utf-8 -*-
"""Mette il menu unico e la mappa del piede anche sulle pagine originali del sito
(quelle generate da RocketCake), togliendo il menu costruito in JavaScript."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tpl_menu import menu_html, mappa_html, MENU_CSS, BURGER_JS

SITE = "/home/user/DoveW/sito"
PAGINE = ["index","azienda","contatti","indicazioni","lavoraconnoi","modulo","news","newsnew",
          "prodottinew","sistemi","tecnologia","ruckus","verticali"]

BASE_CSS = """
<style>
/* barra di navigazione e mappa del piede — aggiunte 2026, indipendenti dagli stili della pagina */
.tpw{max-width:1120px;margin:0 auto;padding:0 20px;text-align:left;
  font-family:Arial,Helvetica,sans-serif;box-sizing:border-box}
.tpTop *,.tpMappa *{box-sizing:border-box}
.tpTop{font-family:Arial,Helvetica,sans-serif}
/* i contenuti originali sono flottanti: senza questo il piede risalirebbe sopra la pagina */
body > div:not(.tpTop):not(.tpMappa)::after{content:"";display:table;clear:both}

%s
</style>
""" % MENU_CSS

def togli_menu_js(html):
    """Rimuove il contenitore del menu RocketCake, script inclusi, mantenendo i div bilanciati."""
    m = re.search(r'<div id="menu_[0-9a-f]+"[^>]*>', html)
    if not m: return html, False
    i = m.start(); pos = m.end(); depth = 1
    tag = re.compile(r'<div\b[^>]*>|</div>', re.I)
    while depth > 0:
        t = tag.search(html, pos)
        if not t: return html, False
        depth += 1 if t.group(0).lower().startswith("<div") else -1
        pos = t.end()
    return html[:i] + "<!-- menu JavaScript sostituito dal menu in HTML in cima alla pagina -->" + html[pos:], True

def applica(slug):
    p = os.path.join(SITE, slug + ".html")
    h = open(p, encoding="utf-8", errors="replace").read()
    if "tpDrop" in h:
        return slug, "già fatto"
    h, tolto = togli_menu_js(h)
    # eventuale inclusione residua di wsp_menu.js
    h = re.sub(r'<script[^>]*src="rc_images/wsp_menu\.js"[^>]*>\s*</script>', '', h)
    # stili nel <head>
    if "</head>" in h:
        h = h.replace("</head>", BASE_CSS + "</head>", 1)
    else:
        h = BASE_CSS + h
    # barra subito dopo <body>
    mb = re.search(r'<body[^>]*>', h, re.I)
    menu = menu_html(slug + ".html")
    h = h[:mb.end()] + "\n" + menu + "\n" + h[mb.end():] if mb else menu + h
    # mappa e script prima di </body>
    coda = "\n" + mappa_html() + BURGER_JS + "\n"
    h = h.replace("</body>", coda + "</body>", 1) if "</body>" in h else h + coda
    open(p, "w", encoding="utf-8").write(h)
    return slug, ("menu JS rimosso" if tolto else "nessun menu JS trovato")

if __name__ == "__main__":
    for s in PAGINE:
        print("%-16s %s" % applica(s))
