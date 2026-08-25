import os, re, json, html
from bs4 import BeautifulSoup

SRC = "/home/user/DoveW/archivio/sito"
OUT = "/home/user/DoveW/archivio/contenuti"
os.makedirs(OUT, exist_ok=True)

index = []
for fn in sorted(os.listdir(SRC)):
    if not fn.endswith(".html"): continue
    raw = open(os.path.join(SRC, fn), encoding="utf-8", errors="replace").read()
    soup = BeautifulSoup(raw, "lxml")
    for t in soup(["script", "style"]): t.decompose()
    title = (soup.title.string or "").strip() if soup.title else ""
    kw = soup.find("meta", attrs={"name": "keywords"})
    desc = soup.find("meta", attrs={"name": "description"})
    text = soup.get_text("\n")
    lines = [re.sub(r"\s+", " ", l).strip() for l in text.split("\n")]
    lines = [l for l in lines if l and l not in ("\xa0",)]
    # dedup consecutive
    clean = []
    for l in lines:
        if not clean or clean[-1] != l: clean.append(l)
    imgs = [i.get("src", "") for i in soup.find_all("img")]
    links = []
    for a in soup.find_all("a", href=True):
        txt = re.sub(r"\s+", " ", a.get_text(" ")).strip()
        links.append((a["href"], txt))
    words = sum(len(l.split()) for l in clean)
    index.append({"file": fn, "title": title,
                  "keywords": kw.get("content","") if kw else "",
                  "description": desc.get("content","") if desc else "",
                  "words": words, "images": len(imgs), "links": len(links)})
    with open(os.path.join(OUT, fn.replace(".html", ".md")), "w", encoding="utf-8") as f:
        f.write(f"# {fn}\n\n**Title:** {title}\n")
        f.write(f"**Keywords:** {kw.get('content','') if kw else '—'}\n")
        f.write(f"**Description:** {desc.get('content','') if desc else '—'}\n\n## Testo\n\n")
        f.write("\n".join(clean))
        f.write("\n\n## Immagini\n\n" + "\n".join(f"- {i}" for i in imgs))
        f.write("\n\n## Link\n\n" + "\n".join(f"- [{t}]({h})" for h, t in links) + "\n")

json.dump(index, open(os.path.join(OUT, "_index.json"), "w"), indent=1, ensure_ascii=False)
print(f"{len(index)} pagine estratte, {sum(p['words'] for p in index)} parole totali")
for p in index:
    print(f"{p['file']:<32} {p['words']:>5}w {p['images']:>3}img  {p['title'][:40]}")
