import os, re, json, base64
SITE="/home/user/DoveW/sito"
PAGES=[("index","Home"),("ai","AI nativa"),("esg","Sostenibilità ESG"),("finanza-agevolata","Finanza agevolata")]

def datauri(path):
    ext=os.path.splitext(path)[1].lower()
    mime={"png":"image/png","jpg":"image/jpeg","jpeg":"image/jpeg","webp":"image/webp"}[ext[1:]]
    return "data:%s;base64,%s"%(mime, base64.b64encode(open(path,"rb").read()).decode())

IMG={f:datauri(os.path.join(SITE,"img",f)) for f in sorted(os.listdir(os.path.join(SITE,"img")))}
css=open(os.path.join(SITE,"assets","style.css"),encoding="utf-8").read()
css=re.sub(r'url\("\.\./img/([^"]+)"\)', lambda m:'url("%s")'%IMG[m.group(1)], css)

pages={}
for slug,_ in PAGES:
    h=open(os.path.join(SITE,slug+".html"),encoding="utf-8").read()
    h=h.replace('<link rel="stylesheet" href="assets/style.css">', "<style>\n"+css+"\n</style>")
    h=re.sub(r'src="img/([^"]+)"', lambda m:'src="%s"'%IMG[m.group(1)], h)
    h=re.sub(r'<link rel="icon"[^>]*>', '', h)
    # i link fra le pagine passano al guscio dell'anteprima
    h=h.replace("</body>", """
<script>
document.addEventListener('click', function(e){
  var a=e.target.closest && e.target.closest('a[href]'); if(!a) return;
  var h=a.getAttribute('href')||'';
  if(h.charAt(0)==='#'||/^(mailto|tel):/i.test(h)) return;
  e.preventDefault();
  var slug=h.replace(/^.*\\//,'').replace(/\\.html?$/i,'').replace(/#.*$/,'');
  parent.postMessage({go:slug, raw:h}, '*');
}, true);
</script>
</body>""")
    pages[slug]=h

SHELL="""<title>Nuovo tp-italia.com</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&family=IBM+Plex+Mono:wght@400&family=Source+Sans+3:wght@400;600&display=swap">
<style>
:root{--ground:#eef1f6;--chrome:#fff;--ink:#131a25;--muted:#5d6b7c;--line:#dbe2ec;
  --accent:#1d3f77;--accent-soft:#e5ecf8;--focus:#2f6fd0}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#0d1218;--chrome:#151c25;--ink:#e3eaf3;--muted:#8f9dae;--line:#232d3a;
  --accent:#84aae6;--accent-soft:#1b2534;--focus:#6ea3ea}}
:root[data-theme="dark"]{--ground:#0d1218;--chrome:#151c25;--ink:#e3eaf3;--muted:#8f9dae;
  --line:#232d3a;--accent:#84aae6;--accent-soft:#1b2534;--focus:#6ea3ea}
*{box-sizing:border-box}
body{margin:0;height:100dvh;display:flex;flex-direction:column;background:var(--ground);color:var(--ink);
  font-family:"Source Sans 3",system-ui,sans-serif;overflow:hidden}
header{display:flex;align-items:center;gap:14px;padding:9px 14px;background:var(--chrome);
  border-bottom:1px solid var(--line);flex-wrap:wrap}
.name{display:flex;flex-direction:column;line-height:1.2;margin-right:auto}
.name b{font-family:Archivo,sans-serif;font-size:14px}
.name span{font:400 11px/1.3 "IBM Plex Mono",monospace;color:var(--muted)}
.tabs{display:flex;gap:4px;flex-wrap:wrap}
button{font:600 13px/1 "Source Sans 3",sans-serif;color:var(--ink);background:none;
  border:1px solid var(--line);border-radius:7px;padding:8px 12px;cursor:pointer}
button:hover{border-color:var(--accent);color:var(--accent)}
button[aria-pressed="true"]{background:var(--accent-soft);border-color:var(--accent);color:var(--accent)}
button:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
.seg{display:flex}
.seg button{border-radius:0;margin-left:-1px}
.seg button:first-child{border-radius:7px 0 0 7px;margin-left:0}
.seg button:last-child{border-radius:0 7px 7px 0}
.frame{flex:1;overflow:auto;display:flex;justify-content:center;background:var(--ground)}
iframe{border:0;width:100%;height:100%;background:#fff}
iframe.mob{width:390px;max-width:100%;box-shadow:0 0 0 1px var(--line)}
.toast{position:fixed;left:50%;transform:translateX(-50%);bottom:18px;background:var(--ink);
  color:var(--ground);padding:9px 15px;border-radius:8px;font-size:12.5px;opacity:0;
  pointer-events:none;transition:opacity .18s;max-width:80vw;text-align:center}
.toast.on{opacity:.96}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
<header>
  <div class="name"><b>Nuovo tp-italia.com</b><span>bozza &middot; 4 pagine su 47</span></div>
  <div class="tabs" id="tabs"></div>
  <div class="seg">
    <button id="bD" aria-pressed="true">Desktop</button>
    <button id="bM" aria-pressed="false">Mobile</button>
  </div>
</header>
<div class="frame"><iframe id="fr" title="Anteprima del nuovo sito"></iframe></div>
<div class="toast" id="toast"></div>
<script type="application/json" id="d">__DATA__</script>
<script>
var P=JSON.parse(document.getElementById('d').textContent);
var LAB=__LABELS__;
var fr=document.getElementById('fr'), tabs=document.getElementById('tabs'), toast=document.getElementById('toast');
LAB.forEach(function(x){
  var b=document.createElement('button'); b.textContent=x[1]; b.dataset.slug=x[0];
  b.onclick=function(){go(x[0]);}; tabs.appendChild(b);
});
function go(slug){
  if(!P[slug]){say('Questa pagina non fa parte della bozza: '+slug+'.html \\u2014 nel sito vero resta quella attuale.');return;}
  fr.srcdoc=P[slug];
  [].forEach.call(tabs.children,function(b){b.setAttribute('aria-pressed', b.dataset.slug===slug?'true':'false');});
}
function say(t){toast.textContent=t;toast.classList.add('on');clearTimeout(say._t);
  say._t=setTimeout(function(){toast.classList.remove('on');},3200);}
addEventListener('message',function(e){ if(e.data && e.data.go) go(e.data.go); });
var bD=document.getElementById('bD'), bM=document.getElementById('bM');
bD.onclick=function(){fr.classList.remove('mob');bD.setAttribute('aria-pressed','true');bM.setAttribute('aria-pressed','false');};
bM.onclick=function(){fr.classList.add('mob');bM.setAttribute('aria-pressed','true');bD.setAttribute('aria-pressed','false');};
go('index');
</script>
"""
out=(SHELL.replace("__DATA__", json.dumps(pages, ensure_ascii=True).replace("</","<\\/"))
          .replace("__LABELS__", json.dumps([[s,l] for s,l in PAGES], ensure_ascii=True)))
p="/home/user/DoveW/anteprima/nuovo-sito.html"
open(p,"w",encoding="utf-8").write(out)
print(p, round(os.path.getsize(p)/1048576,2),"MB")
