# -*- coding: utf-8 -*-
"""Menu unico del sito e mappa nel piede. Un solo posto da cambiare quando nasce una pagina."""

# (etichetta, file, indentata?)
MENU = [
 ("Home", "index.html", []),
 ("Aree d'impatto", None, [
    ("AI nativa", "ai.html"),
    ("Sostenibilit&agrave; ESG", "esg.html"),
    ("Fabbrica 5.0 e finanza agevolata", "fabbrica50.html"),
 ]),
 ("Gestionali ERP", None, [
    ("Quale gestionale scegliere", "gestionalix.html"),
    ("&mdash;", None),
    ("Mago4", "mago4.html"),
    ("&nbsp;&nbsp;Amministrazione e finanza", "magoamministrativa.html"),
    ("&nbsp;&nbsp;Vendite e acquisti", "magovenditeacquisti.html"),
    ("&nbsp;&nbsp;Magazzino e logistica", "magomagazzino.html"),
    ("&nbsp;&nbsp;Produzione", "magoproduzione.html"),
    ("MagoWeb", "magoweb.html"),
    ("MagoCloud", "magocloud.html"),
    ("&mdash;", None),
    ("Ad Hoc Infinity", "ahi.html"),
    ("&nbsp;&nbsp;Amministrazione", "ahiamministrazione.html"),
    ("&nbsp;&nbsp;Vendite e acquisti", "ahivendite.html"),
    ("&nbsp;&nbsp;Magazzino e logistica", "ahilogistica.html"),
    ("&nbsp;&nbsp;Controllo di gestione", "ahigestione.html"),
    ("&mdash;", None),
    ("Infinity Zucchetti", "infinity.html"),
 ]),
 ("Applicazioni", None, [
    ("CRM", "crm.html"),
    ("Gestione documentale", "dms.html"),
    ("Portali ed e-commerce", "portal.html"),
    ("Business Intelligence", "infobusiness.html"),
    ("Fatturazione elettronica", "fepasos.html"),
    ("Persone e presenze", "hr.html"),
    ("Trasferte e note spese", "ztravel.html"),
    ("&mdash;", None),
    ("Tutti i prodotti", "prodottinew.html"),
    ("Prodotti verticali", "verticali.html"),
 ]),
 ("Fabbrica e magazzino", None, [
    ("EasyTime &mdash; tempi di produzione", "easytime.html"),
    ("EasyInd &mdash; macchine interconnesse", "easyind40.html"),
    ("Opera MES", "operames.html"),
    ("&mdash;", None),
    ("W.App &mdash; WMS magazzino", "wapp.html"),
    ("Barcode o RFID", "rfid.html"),
 ]),
 ("Assistenza", None, [
    ("iTek4 &mdash; noleggio e manutenzione", "itek4.html"),
    ("Mobile Ticket &mdash; ticketing", "mobileticketnew.html"),
    ("&mdash;", None),
    ("Assistenza Pro", "contatti.html"),
 ]),
 ("Sistemi", None, [
    ("Sistemistica e sicurezza", "sistemi.html"),
    ("Innovazione tecnologica", "tecnologia.html"),
    ("WiFi professionale Ruckus", "ruckus.html"),
 ]),
 ("Azienda", None, [
    ("Chi siamo", "azienda.html"),
    ("News", "newsnew.html"),
    ("Lavora con noi", "lavoraconnoi.html"),
    ("Dove siamo", "indicazioni.html"),
 ]),
]

CTA = ("Contatti", "modulo.html")

MENU_CSS = """
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
.tpDrop>span::after{content:" \\25be";font-size:10px;color:#7a86a8}
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
"""

def menu_html(active=""):
    out=['<div class="tpTop"><div class="tpw">',
         '<a class="tpLogo" href="index.html" aria-label="Technology Partners Italia, home">'
         '<img src="rc_images/newlogoquadro300x300.png" alt="Technology Partners Italia"></a>',
         '<button class="tpBurger" id="tpBurger" aria-expanded="false" aria-controls="tpNav">Menu</button>',
         '<nav class="tpNav" id="tpNav" aria-label="Navigazione principale">']
    for label, href, figli in MENU:
        if not figli:
            cls=' class="on"' if href==active else ''
            out.append('<a href="%s"%s>%s</a>' % (href, cls, label))
            continue
        attivo = any(f[1]==active for f in figli)
        out.append('<div class="tpDrop%s">' % (" on" if attivo else ""))
        out.append('<span tabindex="0" role="button">%s</span>' % label)
        out.append('<div class="tpMenu">')
        for t,h in figli:
            if h is None: out.append("<hr>")
            else:
                cls=' class="on"' if h==active else ''
                out.append('<a href="%s"%s>%s</a>' % (h, cls, t))
        out.append('</div></div>')
    out.append('<a class="tpCta" href="%s">%s</a>' % (CTA[1], CTA[0]))
    out.append('</nav></div></div>')
    return "\n".join(out)

def mappa_html():
    cols=[]
    for label, href, figli in MENU:
        if not figli:
            continue
        voci=''.join('<a href="%s">%s</a>' % (h, t.replace("&nbsp;&nbsp;","")) for t,h in figli if h)
        cols.append('<div><h4>%s</h4>%s</div>' % (label, voci))
    cols.append('<div><h4>Contatti</h4>'
                '<a href="modulo.html">Richiedi informazioni</a>'
                '<a href="indicazioni.html">Dove siamo</a>'
                '<a href="contatti.html">Assistenza</a>'
                '<a href="tel:+390362163629">+39 0362 1636293</a>'
                '<a href="mailto:commerciale@tp-italia.com">commerciale@tp-italia.com</a></div>')
    return ('<div class="tpMappa"><div class="tpw"><div class="cols">%s</div></div></div>' % "".join(cols))

BURGER_JS = """
<script>
(function(){
  var b=document.getElementById('tpBurger'), n=document.getElementById('tpNav');
  if(!b||!n) return;
  b.addEventListener('click', function(){
    var open=n.classList.toggle('open');
    b.setAttribute('aria-expanded', open?'true':'false');
  });
})();
</script>"""
