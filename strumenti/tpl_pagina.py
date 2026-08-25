# Modello comune delle pagine nuove di tp-italia.com (grafica del sito: Arial, blu #000080)
from tpl_menu import menu_html, mappa_html, MENU_CSS, BURGER_JS
STYLE = """<style>
body{margin:0;background:#fff;color:#333;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.6}
a{color:#0000A0}
.tpw{max-width:1120px;margin:0 auto;padding:0 20px}
/* ---- barra di navigazione unica del sito ---- */
.tpTop{border-bottom:1px solid #D6D5D7;background:#fff;position:relative;z-index:60}
.tpTop .tpw{display:flex;align-items:center;gap:22px;padding-top:10px;padding-bottom:10px}
.tpTop .tpLogo img{height:52px;width:auto;display:block}
.tpNav{margin-left:auto;display:flex;align-items:center;gap:4px}
.tpNav>a,.tpDrop>span{display:block;color:#000080;text-decoration:none;font-weight:bold;
  font-size:14.5px;padding:9px 10px;border-radius:4px;cursor:pointer;white-space:nowrap}
.tpNav>a:hover,.tpDrop:hover>span{background:#F0F3F9;color:#0000A0}
.tpNav>a.on,.tpDrop.on>span{box-shadow:inset 0 -2px 0 #000080}
.tpDrop{position:relative}
.tpDrop>span::after{content:" \25be";font-size:10px;color:#7a86a8}
.tpMenu{display:none;position:absolute;top:100%;left:0;min-width:262px;background:#fff;
  border:1px solid #D6D5D7;border-top:3px solid #000080;border-radius:0 0 6px 6px;
  box-shadow:0 14px 30px -12px rgba(0,0,40,.35);padding:8px 0}
.tpDrop:hover .tpMenu,.tpDrop:focus-within .tpMenu{display:block}
.tpDrop:last-of-type .tpMenu{left:auto;right:0}
.tpMenu a{display:block;padding:7px 18px;color:#233;text-decoration:none;font-size:14px;font-weight:normal}
.tpMenu a:hover{background:#F0F3F9;color:#000080}
.tpMenu a.on{color:#000080;font-weight:bold}
.tpMenu hr{border:0;border-top:1px solid #E6E9F0;margin:7px 14px}
.tpNav .tpCta{background:#000080;color:#fff;margin-left:8px}
.tpNav .tpCta:hover{background:#0000A0;color:#fff}
.tpBurger{display:none;margin-left:auto;background:#fff;border:1px solid #000080;color:#000080;
  font-weight:bold;font-size:14px;border-radius:5px;padding:9px 14px;cursor:pointer}
.tpTop a:focus-visible,.tpTop button:focus-visible,.tpDrop>span:focus-visible{outline:2px solid #0000A0;outline-offset:2px}
@media (max-width:1080px){
  .tpNav{display:none;position:absolute;top:100%;left:0;right:0;background:#fff;flex-direction:column;
    align-items:stretch;gap:0;padding:6px 16px 16px;border-bottom:1px solid #D6D5D7;
    box-shadow:0 18px 30px -18px rgba(0,0,40,.5);max-height:76vh;overflow:auto}
  .tpNav.open{display:flex}
  .tpBurger{display:block}
  .tpDrop>span{padding:11px 4px}
  .tpMenu{display:block;position:static;border:0;box-shadow:none;padding:0 0 8px 14px;min-width:0;border-top:0}
  .tpMenu a{padding:7px 4px}
  .tpNav .tpCta{margin:10px 0 0;text-align:center}
}
/* ---- mappa nel piede ---- */
.tpMappa{background:#0a1a52;color:#c9d8ef;padding:30px 0 6px;font-size:13.5px}
.tpMappa .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:24px}
.tpMappa h4{color:#fff;font-size:12px;letter-spacing:.12em;text-transform:uppercase;margin:0 0 10px}
.tpMappa a{color:#c9d8ef;text-decoration:none;display:block;padding:3px 0;line-height:1.4}
.tpMappa a:hover{color:#fff;text-decoration:underline}
.tpHero{background:#000080;color:#fff;padding:34px 0 30px}
.tpHero .tpw{display:flex;gap:30px;align-items:center;flex-wrap:wrap}
.tpHero .txt{flex:1 1 460px}
.tpHero .marchio{flex:0 0 auto;background:#fff;border-radius:6px;padding:14px 18px}
.tpHero .marchio img{max-height:64px;width:auto;display:block}
.tpHero .kick{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:#9fc0ea;margin:0 0 8px}
.tpHero h1{margin:0;font-size:31px;line-height:1.18;font-weight:bold;max-width:22ch}
.tpHero p{margin:14px 0 0;font-size:16.5px;line-height:1.55;color:#dfe8f6;max-width:74ch}
.tpHero .crumb{font-size:13px;color:#9fc0ea;margin:0 0 14px}
.tpHero .crumb a{color:#9fc0ea}
main{padding:38px 0 10px}
main h2{color:#000080;font-size:23px;margin:34px 0 12px;line-height:1.25}
main h2:first-child{margin-top:0}
main h3{color:#000080;font-size:17px;margin:22px 0 8px}
main p{margin:0 0 14px;max-width:82ch}
main ul{margin:0 0 16px;padding-left:22px;max-width:82ch}
main li{margin-bottom:8px}
.tpBox{background:#F4F6FA;border-left:4px solid #000080;padding:16px 20px;margin:22px 0;max-width:82ch}
.tpBox b{color:#000080}
.tpGrid{display:flex;gap:16px;flex-wrap:wrap;margin:18px 0 8px}
.tpGrid div{flex:1 1 228px;background:#fff;border:1px solid #D6D5D7;border-top:3px solid #000080;
  border-radius:5px;padding:16px 18px}
.tpGrid h4{margin:0 0 7px;color:#000080;font-size:15.5px}
.tpGrid p{margin:0;font-size:14px;line-height:1.5;color:#444}
.tpGrid a{font-size:13.5px;font-weight:bold;display:inline-block;margin-top:9px}
.faq{border-top:1px solid #D6D5D7;max-width:82ch}
.faq details{border-bottom:1px solid #D6D5D7;padding:16px 0}
.faq summary{font-weight:bold;font-size:16px;color:#000080;cursor:pointer;list-style:none;
  display:flex;justify-content:space-between;gap:16px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";color:#0000A0;font-size:20px;line-height:1}
.faq details[open] summary::after{content:"\2013"}
.faq p{margin-top:10px}
.tpFonte{font-size:13px;color:#777;margin:26px 0 0;max-width:82ch}
.tpCta{background:#F4F6FA;border-top:1px solid #D6D5D7;margin-top:34px;padding:28px 0}
.tpCta h2{margin:0 0 8px;color:#000080;font-size:21px}
.tpCta p{margin:0 0 14px;max-width:70ch}
.tpCta a.btn{display:inline-block;background:#000080;color:#fff;text-decoration:none;font-weight:bold;
  padding:11px 20px;border-radius:5px;font-size:14.5px}
.tpCta a.btn:hover{background:#0000A0}
.tpCta .rec{margin-left:16px;font-size:14.5px;color:#000080;font-weight:bold;text-decoration:none}
.tpFoot{background:#000080;color:#c9d8ef;padding:26px 0 22px;font-size:13.5px}
.tpFoot .loghi{display:flex;flex-wrap:wrap;align-items:center;gap:26px;margin-bottom:20px}
.tpFoot .loghi img{height:34px;width:auto}
.tpFoot .righe{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;
  border-top:1px solid rgba(255,255,255,.2);padding-top:16px}
.tpFoot a{color:#c9d8ef}
@media (max-width:760px){.tpHero h1{font-size:24px}.tpNav{gap:14px}.tpTop .tpw{gap:14px}}
</style>"""

NAV = [("ai.html","AI nativa"),("esg.html","Sostenibilit&agrave; ESG"),("fabbrica50.html","Fabbrica 5.0"),
       ("index.html","Home"),("prodottinew.html","Prodotti"),("azienda.html","Azienda"),("modulo.html","Contatti")]

LOGHI = ["topartner_erp_bn.png","m4platinumpabn.png","silver_cloud_micorsoft_1.png","vmw__1.png",
         "hpbusiness.png","ruckus_bn.png","trendmicro_bn.png","zebra_bn.png","honeywell.png",
         "fortinet_logo_bn2.png","azurebn.png"]

def pagina(slug, title, desc, crumb, kick, h1, lead, body, ctah, ctap, fonte, on="", marchio=None):
    menu = menu_html(on or slug)
    marchio_html = ('<div class="marchio"><img src="rc_images/%s" alt=""></div>' % marchio) if marchio else ''
    loghi_html = ''.join('<img src="rc_images/%s" alt="">' % g for g in LOGHI)
    return """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="https://www.tp-italia.com/%(slug)s">
<link rel="icon" href="rc_images/custom.ico">
%(style)s
</head>
<body>

%(menu)s

<div class="tpHero"><div class="tpw">
  <div class="txt">
    <p class="crumb">%(crumb)s</p>
    <p class="kick">%(kick)s</p>
    <h1>%(h1)s</h1>
    <p>%(lead)s</p>
  </div>
  %(marchio)s
</div></div>

<main><div class="tpw">
%(body)s
<p class="tpFonte">%(fonte)s</p>
</div></main>

<div class="tpCta"><div class="tpw">
  <h2>%(ctah)s</h2>
  <p>%(ctap)s</p>
  <a class="btn" href="modulo.html">Richiedi informazioni</a>
  <a class="rec" href="tel:+390362163629">+39 0362 1636293</a>
  <a class="rec" href="mailto:commerciale@tp-italia.com">commerciale@tp-italia.com</a>
</div></div>

%(mappa)s

<div class="tpFoot"><div class="tpw">
  <div class="loghi">%(loghi)s</div>
  <div class="righe">
    <span>Technology Partners Italia S.r.l. &middot; Via Vincenzo Monti, 74 &middot; 20832 Desio (MB)
      &middot; Tel +39 0362 1636293 &middot; <a href="mailto:commerciale@tp-italia.com">commerciale@tp-italia.com</a></span>
    <span>P.IVA e C.F. 05660080960 &middot;
      <a href="https://www.privacylab.it/informativa.php?13064379882">Informativa privacy</a></span>
  </div>
</div></div>

%(burger)s
</body>
</html>
""" % dict(title=title, desc=desc, slug=slug, style=STYLE, menu=menu, mappa=mappa_html(),
           burger=BURGER_JS, crumb=crumb, kick=kick,
           h1=h1, lead=lead, marchio=marchio_html, body=body, fonte=fonte, ctah=ctah, ctap=ctap, loghi=loghi_html)
