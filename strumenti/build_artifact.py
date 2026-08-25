import json, os
SP="/tmp/claude-0/-home-user-DoveW/421a1c9a-0586-599a-9164-946f1d5f712f/scratchpad"
pages=json.load(open(SP+"/pages.json"))
imgs=json.load(open(SP+"/imgmap.json"))
meta={p["file"][:-5]:p for p in json.load(open("/home/user/DoveW/archivio/contenuti/_index.json"))}

GROUPS=[
 ("Home", ["index"]),
 ("Panoramiche", ["gestionalix","gestionali","prodottinew","verticali"]),
 ("ERP Mago", ["mago","mago4","magoweb","magocloud","magoamministrativa","magovenditeacquisti","magomagazzino","magoproduzione"]),
 ("Ad Hoc Infinity", ["ahi","ahiamministrazione","ahivendite","ahigestione","ahilogistica"]),
 ("Suite Zucchetti", ["infinity","crm","dms","hr","portal","infobusiness","bussinessapps","cloudapp","fepasos","presenzeweb","smplice","ztravel"]),
 ("Soluzioni TP", ["itek4","operames","wapp","easytime","easyind40","mobileticketnew","rfid"]),
 ("Sistemistica", ["sistemi","tecnologia","ruckus"]),
 ("News", ["newsnew","news"]),
 ("Azienda", ["azienda","contatti","indicazioni","modulo","lavoraconnoi"]),
]
LABEL={"index":"Home","gestionalix":"Gestionali ERP","gestionali":"Software gestionali","prodottinew":"Indice prodotti",
"verticali":"Prodotti verticali","mago":"Mago — hub","mago4":"Mago 4","magoweb":"Mago Web","magocloud":"Mago Cloud",
"magoamministrativa":"Mago · Amministrazione","magovenditeacquisti":"Mago · Vendite e acquisti","magomagazzino":"Mago · Magazzino",
"magoproduzione":"Mago · Produzione","ahi":"Ad Hoc Infinity — hub","ahiamministrazione":"AHI · Amministrazione",
"ahivendite":"AHI · Vendite","ahigestione":"AHI · Gestione","ahilogistica":"AHI · Logistica","infinity":"Infinity 4.2",
"crm":"CRM","dms":"Gestione documentale","hr":"Human Resource","portal":"Portali e e-commerce","infobusiness":"Business Intelligence",
"bussinessapps":"Business Apps","cloudapp":"Cloud Apps","fepasos":"Fatturazione elettronica","presenzeweb":"PresenzeWeb",
"smplice":"Presenze Semplice","ztravel":"ZTravel note spese","itek4":"ITEK4","operames":"Opera MES","wapp":"W.App — WMS",
"easytime":"EasyTime","easyind40":"EasyInd 4.0","mobileticketnew":"MO.TI.","rfid":"RFID e identificazione",
"sistemi":"Sistemistica","tecnologia":"Innovazione tecnologica","ruckus":"WiFi Ruckus","newsnew":"News","news":"News (vecchia)",
"azienda":"Chi siamo","contatti":"Contatti / Assistenza","modulo":"Richiedi informazioni","indicazioni":"Dove siamo","lavoraconnoi":"Lavora con noi"}

nav=[]
for title, slugs in GROUPS:
    items=[]
    for s in slugs:
        if s not in pages: continue
        w=meta.get(s,{}).get("words",0)
        items.append({"slug":s,"label":LABEL.get(s,s),"words":w})
    nav.append({"group":title,"items":items})

def js_json(o):
    return json.dumps(o, ensure_ascii=True).replace("</","<\\/")

HTML = """<title>Archivio tp-italia.com</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
:root{
  --ground:#eef1f6; --surface:#ffffff; --rail:#f7f9fc; --ink:#131a25; --muted:#5d6b7c;
  --line:#dbe2ec; --accent:#1d3f77; --accent-soft:#e5ecf8; --focus:#2f6fd0; --chrome:#ffffff;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#0d1218; --surface:#151c25; --rail:#111821; --ink:#e3eaf3; --muted:#8f9dae;
    --line:#232d3a; --accent:#84aae6; --accent-soft:#1b2534; --focus:#6ea3ea; --chrome:#151c25;
  }
}
:root[data-theme="dark"]{
  --ground:#0d1218; --surface:#151c25; --rail:#111821; --ink:#e3eaf3; --muted:#8f9dae;
  --line:#232d3a; --accent:#84aae6; --accent-soft:#1b2534; --focus:#6ea3ea; --chrome:#151c25;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font-family:"IBM Plex Sans",system-ui,-apple-system,Segoe UI,sans-serif;
  height:100dvh;display:flex;flex-direction:column;overflow:hidden}
header{display:flex;align-items:center;gap:12px;padding:10px 14px;background:var(--chrome);
  border-bottom:1px solid var(--line);flex:0 0 auto;flex-wrap:wrap}
.brand{display:flex;flex-direction:column;line-height:1.2;margin-right:auto;min-width:0}
.brand b{font-weight:600;font-size:14px;letter-spacing:.01em}
.brand span{font:400 11px/1.3 "IBM Plex Mono",ui-monospace,monospace;color:var(--muted)}
button{font:inherit;color:inherit;background:none;border:1px solid var(--line);
  border-radius:7px;padding:6px 11px;cursor:pointer;font-size:13px}
button:hover{border-color:var(--accent);color:var(--accent)}
button[aria-pressed="true"]{background:var(--accent-soft);border-color:var(--accent);color:var(--accent);font-weight:600}
button:focus-visible,a:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
.seg{display:flex;gap:0}
.seg button{border-radius:0;margin-left:-1px}
.seg button:first-child{border-radius:7px 0 0 7px;margin-left:0}
.seg button:last-child{border-radius:0 7px 7px 0}
main{flex:1 1 auto;display:flex;min-height:0}
nav{width:246px;flex:0 0 auto;background:var(--rail);border-right:1px solid var(--line);
  overflow-y:auto;padding:10px 0 24px}
nav h2{font:600 10px/1 "IBM Plex Mono",monospace;letter-spacing:.11em;text-transform:uppercase;
  color:var(--muted);margin:16px 14px 7px}
nav h2:first-child{margin-top:6px}
nav a{display:flex;align-items:baseline;gap:8px;padding:6px 14px;text-decoration:none;color:var(--ink);font-size:13.5px}
nav a:hover{background:var(--accent-soft)}
nav a[aria-current="page"]{background:var(--accent-soft);color:var(--accent);font-weight:600;
  box-shadow:inset 3px 0 0 var(--accent)}
nav a i{margin-left:auto;font:400 10.5px/1 "IBM Plex Mono",monospace;color:var(--muted);font-style:normal}
nav a.thin i{color:#c2410c}
:root[data-theme="dark"] nav a.thin i{color:#fb923c}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) nav a.thin i{color:#fb923c}}
.stage{flex:1 1 auto;display:flex;flex-direction:column;min-width:0;background:var(--ground)}
.bar{display:flex;align-items:center;gap:10px;padding:7px 12px;border-bottom:1px solid var(--line);
  background:var(--surface);font-size:12.5px;color:var(--muted);flex-wrap:wrap}
.bar code{font:400 12px/1 "IBM Plex Mono",monospace;color:var(--ink)}
.frame{flex:1 1 auto;overflow:auto;display:flex;justify-content:center;padding:0}
iframe{border:0;width:100%;height:100%;background:#fff;display:block}
iframe.mob{width:390px;max-width:100%;box-shadow:0 0 0 1px var(--line)}
.toast{position:fixed;left:50%;transform:translateX(-50%);bottom:18px;background:var(--ink);
  color:var(--ground);padding:9px 15px;border-radius:8px;font-size:12.5px;max-width:82vw;
  opacity:0;pointer-events:none;transition:opacity .18s}
.toast.on{opacity:.96}
.menu-btn{display:none}
@media (max-width:760px){
  nav{position:absolute;z-index:5;top:0;bottom:0;left:0;transform:translateX(-100%);
    transition:transform .2s;box-shadow:0 0 30px rgba(0,0,0,.22)}
  nav.open{transform:none}
  main{position:relative}
  .menu-btn{display:inline-block}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>

<header>
  <div class="brand"><b>Archivio tp-italia.com</b><span id="stamp">catturato il 25/08/2026 &middot; 47 pagine</span></div>
  <button class="menu-btn" id="menu" aria-label="Elenco pagine">Pagine</button>
  <div class="seg" role="group" aria-label="Larghezza">
    <button id="bDesk" aria-pressed="true">Desktop</button>
    <button id="bMob" aria-pressed="false">Mobile</button>
  </div>
</header>
<main>
  <nav id="nav" aria-label="Pagine del sito"></nav>
  <div class="stage">
    <div class="bar"><code id="fname">index.html</code><span id="pinfo"></span></div>
    <div class="frame"><iframe id="fr" title="Pagina archiviata"></iframe></div>
  </div>
</main>
<div class="toast" id="toast"></div>

<script type="application/json" id="d-nav">__NAV__</script>
<script type="application/json" id="d-pages">__PAGES__</script>
<script type="application/json" id="d-imgs">__IMGS__</script>
<script>
var NAV=JSON.parse(document.getElementById('d-nav').textContent);
var PAGES=JSON.parse(document.getElementById('d-pages').textContent);
window.__IMG=JSON.parse(document.getElementById('d-imgs').textContent);

var nav=document.getElementById('nav'), fr=document.getElementById('fr'),
    fname=document.getElementById('fname'), pinfo=document.getElementById('pinfo'),
    toast=document.getElementById('toast'), cur=null;

NAV.forEach(function(g){
  var h=document.createElement('h2'); h.textContent=g.group; nav.appendChild(h);
  g.items.forEach(function(it){
    var a=document.createElement('a'); a.href='#'+it.slug; a.dataset.slug=it.slug;
    if(it.words<60) a.className='thin';
    a.innerHTML='<span></span><i></i>';
    a.firstChild.textContent=it.label;
    a.lastChild.textContent=it.words+'p';
    a.title=it.words+' parole di testo';
    a.addEventListener('click',function(e){e.preventDefault();show(it.slug);nav.classList.remove('open');});
    nav.appendChild(a);
  });
});

function show(slug){
  if(!PAGES[slug]) return;
  cur=slug;
  fr.srcdoc=PAGES[slug];
  fname.textContent=slug+'.html';
  var it=null;
  NAV.forEach(function(g){g.items.forEach(function(x){if(x.slug===slug) it=x;});});
  pinfo.textContent = it ? '\\u00b7 '+it.label+' \\u00b7 '+it.words+' parole di testo'+(it.words<60?' \\u2014 contenuto solo dentro le immagini':'') : '';
  nav.querySelectorAll('a').forEach(function(a){
    if(a.dataset.slug===slug){a.setAttribute('aria-current','page'); a.scrollIntoView({block:'nearest'});}
    else a.removeAttribute('aria-current');
  });
  history.replaceState(null,'','#'+slug);
}
function say(t){toast.textContent=t;toast.classList.add('on');clearTimeout(say._t);
  say._t=setTimeout(function(){toast.classList.remove('on');},2600);}

addEventListener('message',function(e){
  var d=e.data||{};
  if(d.tpNav){ PAGES[d.tpNav] ? show(d.tpNav) : say('Pagina non presente nell\\'archivio: '+d.tpNav+'.html'); }
  if(d.tpExt){ say('Link esterno: '+d.tpExt); }
});

var bD=document.getElementById('bDesk'), bM=document.getElementById('bMob');
bD.onclick=function(){fr.classList.remove('mob');bD.setAttribute('aria-pressed','true');bM.setAttribute('aria-pressed','false');};
bM.onclick=function(){fr.classList.add('mob');bM.setAttribute('aria-pressed','true');bD.setAttribute('aria-pressed','false');};
document.getElementById('menu').onclick=function(){nav.classList.toggle('open');};

show(location.hash.slice(1) in PAGES ? location.hash.slice(1) : 'index');
</script>
"""

html = (HTML.replace("__NAV__", js_json(nav))
            .replace("__PAGES__", js_json(pages))
            .replace("__IMGS__", js_json(imgs)))
out="/home/user/DoveW/anteprima/archivio-live.html"
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out,"w",encoding="utf-8").write(html)
print(out, round(os.path.getsize(out)/1048576,2), "MB")
