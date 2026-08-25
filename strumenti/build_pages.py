import os, re, json, glob
SITE="/home/user/DoveW/archivio/sito"
SP="/tmp/claude-0/-home-user-DoveW/421a1c9a-0586-599a-9164-946f1d5f712f/scratchpad"

RUNTIME = r"""
<script>
(function(){
  var M = (window.parent && window.parent.__IMG) || {};
  function dataFor(u){
    if(!u || u.indexOf('data:')===0) return null;
    var m = /((?:rc_images|wsp_images)\/[^"')?#]+)/.exec(u);
    return (m && M[m[1]]) ? M[m[1]] : null;
  }
  function doImg(el){
    var s = el.getAttribute('data-src') || el.getAttribute('src');
    var d = dataFor(s);
    if(d && el.getAttribute('src') !== d) el.setAttribute('src', d);
  }
  function doBg(el){
    var b = el.style && el.style.backgroundImage;
    if(!b) return;
    var d = dataFor(b);
    if(d) el.style.backgroundImage = 'url("'+d+'")';
  }
  function sheets(){
    var ss = document.styleSheets;
    for(var i=0;i<ss.length;i++){
      var rules; try{ rules = ss[i].cssRules; }catch(e){ continue; }
      if(!rules) continue;
      for(var j=0;j<rules.length;j++){
        var st = rules[j].style; if(!st) continue;
        var d = dataFor(st.backgroundImage);
        if(d) st.backgroundImage = 'url("'+d+'")';
      }
    }
  }
  function sweep(){
    var im = document.getElementsByTagName('img');
    for(var i=0;i<im.length;i++) doImg(im[i]);
    var all = document.querySelectorAll('[style*="rc_images"],[style*="wsp_images"]');
    for(var k=0;k<all.length;k++) doBg(all[k]);
  }
  sweep(); sheets();
  new MutationObserver(sweep).observe(document.documentElement,
    {childList:true, subtree:true, attributes:true, attributeFilter:['src','style']});
  var t=0, iv=setInterval(function(){ sweep(); if(++t>24) clearInterval(iv); }, 400);

  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href]');
    if(!a) return;
    var h = a.getAttribute('href')||'';
    if(/^javascript:/i.test(h)) return;
    if(/\.html?$/i.test(h)){
      e.preventDefault();
      parent.postMessage({tpNav: h.replace(/^.*\//,'').replace(/\.html?$/i,'')}, '*');
    } else if(/^https?:/i.test(h)){
      e.preventDefault();
      parent.postMessage({tpExt: h}, '*');
    }
  }, true);
})();
</script>
"""

BOX = ('<div style="border:2px dashed #9aa6b5;background:#eef1f5;color:#41505f;'
       'font:600 13px/1.5 system-ui,sans-serif;padding:22px;margin:10px auto;max-width:640px;'
       'text-align:center;border-radius:8px">{}</div>')

def inline_css(html):
    def rep(m):
        href = m.group(1).split('?')[0]
        p = os.path.join(SITE, href)
        if os.path.exists(p):
            return "<style>\n" + open(p, encoding="utf-8", errors="replace").read() + "\n</style>"
        return ""
    return re.sub(r'<link[^>]+rel="stylesheet"[^>]*href="([^"]+)"[^>]*>', rep, html)

def inline_js(html):
    def rep(m):
        src = m.group(1)
        p = os.path.join(SITE, src.split('?')[0])
        if src.startswith(('rc_images/', 'wsp_images/')) and os.path.exists(p):
            return "<script>\n" + open(p, encoding="utf-8", errors="replace").read() + "\n</script>"
        return ""   # scripts esterni: bloccati dalla CSP, li togliamo
    return re.sub(r'<script[^>]*src="([^"]+)"[^>]*>\s*</script>', rep, html)

def strip_analytics(html):
    return re.sub(r'<script>(?:(?!</script>).)*?(?:gtag\(|GoogleAnalyticsObject)(?:(?!</script>).)*?</script>',
                  '', html, flags=re.S)

def defer_images(html):
    return re.sub(r'(<img\b[^>]*?)\bsrc="((?:rc_images|wsp_images)/[^"]+)"',
                  lambda m: m.group(1) + 'data-src="' + m.group(2) + '" src=""', html)

def replace_video(html):
    return re.sub(r'<video\b.*?</video>',
                  BOX.format('Video — escluso da questa anteprima per non superare il limite di peso.'
                             '<br>Il file originale è nell\'archivio su GitHub.'),
                  html, flags=re.S|re.I)

def replace_iframe(html):
    def rep(m):
        src = m.group(0)
        if 'google.com/maps' in src: label = 'Mappa Google — non caricabile in anteprima'
        elif 'docs.google.com/forms' in src: label = 'Modulo Google Forms — non caricabile in anteprima'
        elif 'youtube' in src: label = 'Video YouTube — non caricabile in anteprima'
        else: label = 'Contenuto esterno — non caricabile in anteprima'
        return BOX.format(label)
    return re.sub(r'<iframe\b[^>]*>(?:\s*</iframe>)?', rep, html, flags=re.I)

def strip_icons(html):
    return re.sub(r'<link[^>]+rel="(?:shortcut )?icon"[^>]*>', '', html, flags=re.I)

pages = {}
for f in sorted(glob.glob(SITE + "/*.html")):
    slug = os.path.basename(f)[:-5]
    h = open(f, encoding="utf-8", errors="replace").read()
    for fn in (strip_analytics, strip_icons, inline_css, inline_js,
               defer_images, replace_video, replace_iframe):
        h = fn(h)
    h = h.replace("</body>", RUNTIME + "</body>") if "</body>" in h else h + RUNTIME
    pages[slug] = h

json.dump(pages, open(SP + "/pages.json", "w"))
print(len(pages), "pagine,", round(os.path.getsize(SP + "/pages.json") / 1048576, 2), "MB")
