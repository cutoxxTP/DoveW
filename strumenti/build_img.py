import os, glob, base64, json, io
from PIL import Image
SITE="/home/user/DoveW/archivio/sito"
OUT="/tmp/claude-0/-home-user-DoveW/421a1c9a-0586-599a-9164-946f1d5f712f/scratchpad/imgmap.json"
m={}; tot=0
for f in sorted(glob.glob(SITE+"/rc_images/*")+glob.glob(SITE+"/wsp_images/*")):
    ext=os.path.splitext(f)[1].lower()
    rel=os.path.relpath(f,SITE)
    if ext==".ico": continue
    if ext not in (".png",".jpg",".jpeg",".webp",".gif"): continue
    try:
        im=Image.open(f); im.load()
    except Exception: continue
    if im.mode=="P": im=im.convert("RGBA")
    if im.mode=="LA": im=im.convert("RGBA")
    if im.width>900:
        r=900/im.width; im=im.resize((900,max(1,int(im.height*r))), Image.LANCZOS)
    buf=io.BytesIO(); im.save(buf,"WEBP",quality=50,method=5)
    b=buf.getvalue(); tot+=len(b)
    m[rel]="data:image/webp;base64,"+base64.b64encode(b).decode()
json.dump(m, open(OUT,"w"))
print(f"{len(m)} immagini, webp {tot/1048576:.1f}MB, json {os.path.getsize(OUT)/1048576:.1f}MB")
