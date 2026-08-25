import os, re, json, io, base64
from PIL import Image
SITE="/home/user/DoveW/sito"
PAGES=[("index","Home"),("ai","AI nativa"),("esg","ESG"),("fabbrica50","Fabbrica 5.0"),
 ("gestionalix","Quale ERP"),("mago4","Mago4"),("magoamministrativa","Mago4 · Amministrazione"),
 ("magovenditeacquisti","Mago4 · Vendite"),("magomagazzino","Mago4 · Magazzino"),
 ("magoproduzione","Mago4 · Produzione"),("magoweb","MagoWeb"),("magocloud","MagoCloud"),
 ("ahi","Ad Hoc Infinity"),("ahiamministrazione","AHI · Amministrazione"),("ahivendite","AHI · Vendite"),
 ("ahilogistica","AHI · Logistica"),("ahigestione","AHI · Controllo"),("infinity","Infinity"),
 ("crm","CRM"),("dms","Documentale"),("hr","Persone e presenze"),("ztravel","ZTravel"),
 ("fepasos","Fatturazione elettronica"),("infobusiness","InfoBusiness"),("portal","Portali e e-commerce"),
 ("mago","Mago (confluita)")]

# --- immagini citate da queste pagine e dai loro CSS ---
def refs(text):
    return set(re.findall(r'(?:rc_images|wsp_images)/[A-Za-z0-9._%()-]+', text))
need=set()
for slug,_ in PAGES:
    h=open(os.path.join(SITE,slug+".html"),encoding="utf-8",errors="replace").read()
    need|=refs(h)
    for m in re.findall(r'href="([^"]+\.css)[^"]*"', h):
        p=os.path.join(SITE,m.split("?")[0])
        if os.path.exists(p): need|=refs(open(p,encoding="utf-8",errors="replace").read())
for js in ("rc_images/wsp_menu.js","rc_images/wsp_slideshow.js","rc_images/wsp_gallery.js"):
    need.discard(js)

IMG={}
tot=0
for rel in sorted(need):
    p=os.path.join(SITE,rel)
    if not os.path.exists(p): continue
    ext=os.path.splitext(p)[1].lower()
    if ext in (".ico",".js",".css",".pdf",".mp4"): continue
    try:
        im=Image.open(p); im.load()
    except Exception: continue
    if im.mode=="P": im=im.convert("RGBA")
    if im.mode=="LA": im=im.convert("RGBA")
    if im.width>1100:
        r=1100/im.width; im=im.resize((1100,max(1,int(im.height*r))), Image.LANCZOS)
    buf=io.BytesIO(); im.save(buf,"WEBP",quality=62,method=5); b=buf.getvalue(); tot+=len(b)
    IMG[rel]="data:image/webp;base64,"+base64.b64encode(b).decode()
print(f"{len(IMG)} immagini, {tot/1048576:.2f} MB")

RUNTIME = r"""
<script>
(function(){
  var M=(window.parent&&window.parent.__IMG)||{};
  function d(u){ if(!u||u.indexOf('data:')===0) return null;
    var m=/((?:rc_images|wsp_images)\/[^"')?#]+)/.exec(u); return (m&&M[m[1]])?M[m[1]]:null; }
  function img(e){ var s=e.getAttribute('data-src')||e.getAttribute('src'); var x=d(s);
    if(x&&e.getAttribute('src')!==x) e.setAttribute('src',x); }
  function sheets(){ var ss=document.styleSheets;
    for(var i=0;i<ss.length;i++){ var r; try{r=ss[i].cssRules}catch(e){continue} if(!r)continue;
      for(var j=0;j<r.length;j++){ var st=r[j].style; if(!st)continue;
        var x=d(st.backgroundImage); if(x) st.backgroundImage='url("'+x+'")'; } } }
  function sweep(){ var a=document.getElementsByTagName('img');
    for(var i=0;i<a.length;i++) img(a[i]);
    var b=document.querySelectorAll('[style*="rc_images"],[style*="wsp_images"]');
    for(var k=0;k<b.length;k++){ var x=d(b[k].style.backgroundImage); if(x) b[k].style.backgroundImage='url("'+x+'")'; } }
  sweep(); sheets();
  new MutationObserver(sweep).observe(document.documentElement,{childList:true,subtree:true,attributes:true,attributeFilter:['src','style']});
  var t=0,iv=setInterval(function(){sweep(); if(++t>20) clearInterval(iv);},400);
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href]'); if(!a) return;
    var h=a.getAttribute('href')||'';
    if(/^javascript:/i.test(h)||h.charAt(0)==='#'||/^(mailto|tel):/i.test(h)) return;
    e.preventDefault();
    parent.postMessage({go:h.replace(/^.*\//,'').replace(/\.html?$/i,'')},'*');
  },true);
})();
</script>"""

BOX=('<div style="border:2px dashed #9aa6b5;background:#eef1f5;color:#41505f;'
     'font:bold 13px/1.5 Arial,sans-serif;padding:20px;margin:10px auto;max-width:620px;'
     'text-align:center">{}</div>')

pages={}
for slug,_ in PAGES:
    h=open(os.path.join(SITE,slug+".html"),encoding="utf-8",errors="replace").read()
    def css(m):
        p=os.path.join(SITE,m.group(1).split("?")[0])
        return "<style>\n"+open(p,encoding="utf-8",errors="replace").read()+"\n</style>" if os.path.exists(p) else ""
    h=re.sub(r'<link[^>]+rel="stylesheet"[^>]*href="([^"]+)"[^>]*>', css, h)
    def js(m):
        src=m.group(1); p=os.path.join(SITE,src.split("?")[0])
        return "<script>\n"+open(p,encoding="utf-8",errors="replace").read()+"\n</script>" if src.startswith("rc_images/") and os.path.exists(p) else ""
    h=re.sub(r'<script[^>]*src="([^"]+)"[^>]*>\s*</script>', js, h)
    h=re.sub(r'<script>(?:(?!</script>).)*?gtag\((?:(?!</script>).)*?</script>','',h,flags=re.S)
    h=re.sub(r'<link[^>]+rel="(?:shortcut )?icon"[^>]*>','',h,flags=re.I)
    h=re.sub(r'(<img\b[^>]*?)\bsrc="((?:rc_images|wsp_images)/[^"]+)"',
             lambda m:m.group(1)+'data-src="'+m.group(2)+'" src=""', h)
    h=re.sub(r'<iframe\b[^>]*>(?:\s*</iframe>)?', BOX.format('Contenuto esterno &mdash; non caricabile in anteprima'), h, flags=re.I)
    h=h.replace("</body>", RUNTIME+"</body>")
    pages[slug]=h

SHELL=open("/home/user/DoveW/strumenti/shell_prev.html",encoding="utf-8").read()
out=(SHELL.replace("__PAGES__", json.dumps(pages, ensure_ascii=True).replace("</","<\\/"))
          .replace("__IMGS__", json.dumps(IMG, ensure_ascii=True).replace("</","<\\/"))
          .replace("__TABS__", json.dumps([[s,l] for s,l in PAGES], ensure_ascii=True)))
p="/home/user/DoveW/anteprima/nuovo-sito.html"
open(p,"w",encoding="utf-8").write(out)
print(p, round(os.path.getsize(p)/1048576,2),"MB")
