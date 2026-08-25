import json, os
idx = json.load(open("/home/user/DoveW/archivio/contenuti/_index.json"))
cat = {
 "index.html": ("Home", "Homepage: 4 blocchi soluzioni + Top Partner Zucchetti + news + Infinity"),
 "gestionalix.html": ("Panoramica", "Landing 'Gestionali ERP' (hub verso Mago / Ad Hoc Infinity)"),
 "gestionali.html": ("Panoramica", "Software gestionali — pagina descrittiva"),
 "prodottinew.html": ("Panoramica", "Indice prodotti (solo elenco link, testo quasi assente)"),
 "verticali.html": ("Panoramica", "Prodotti verticali / specifici"),
 "mago.html": ("ERP Mago", "Hub Mago"),
 "mago4.html": ("ERP Mago", "Mago 4"),
 "magoweb.html": ("ERP Mago", "Mago Web"),
 "magocloud.html": ("ERP Mago", "Mago Cloud"),
 "magoamministrativa.html": ("ERP Mago", "Area amministrativa/contabile"),
 "magomagazzino.html": ("ERP Mago", "Area magazzino"),
 "magoproduzione.html": ("ERP Mago", "Area produzione"),
 "magovenditeacquisti.html": ("ERP Mago", "Area vendite e acquisti"),
 "ahi.html": ("ERP Ad Hoc Infinity", "Hub Ad Hoc Infinity"),
 "ahiamministrazione.html": ("ERP Ad Hoc Infinity", "Area amministrazione"),
 "ahigestione.html": ("ERP Ad Hoc Infinity", "Area gestione"),
 "ahilogistica.html": ("ERP Ad Hoc Infinity", "Area logistica"),
 "ahivendite.html": ("ERP Ad Hoc Infinity", "Area vendite"),
 "infinity.html": ("Suite Zucchetti", "Infinity 4.2 — panoramica"),
 "crm.html": ("Suite Zucchetti", "CRM"),
 "dms.html": ("Suite Zucchetti", "Gestione documentale"),
 "hr.html": ("Suite Zucchetti", "Human Resource (pagina con soli PDF, testo assente)"),
 "portal.html": ("Suite Zucchetti", "Portali aziendali / e-commerce"),
 "infobusiness.html": ("Suite Zucchetti", "Business Intelligence"),
 "bussinessapps.html": ("Suite Zucchetti", "Business Apps (testo assente, solo slideshow)"),
 "cloudapp.html": ("Suite Zucchetti", "Cloud Apps"),
 "ztravel.html": ("Suite Zucchetti", "ZTravel note spese (testo assente)"),
 "fepasos.html": ("Suite Zucchetti", "Fatturazione elettronica PA / conservazione sostitutiva"),
 "presenzeweb.html": ("Suite Zucchetti", "PresenzeWeb (testo assente, solo brochure PDF)"),
 "smplice.html": ("Suite Zucchetti", "Rilevazione presenze semplice (testo assente)"),
 "itek4.html": ("Soluzioni TP", "ITEK4 — ticketing/assistenza"),
 "operames.html": ("Soluzioni TP", "OPERA MES"),
 "wapp.html": ("Soluzioni TP", "W.App — WMS magazzino"),
 "easytime.html": ("Soluzioni TP", "EasyTime — rilevazione tempi di produzione"),
 "easyind40.html": ("Soluzioni TP", "EasyInd 4.0 — industria 4.0"),
 "mobileticketnew.html": ("Soluzioni TP", "MO.TI. — mobile ticket assistenza"),
 "rfid.html": ("Soluzioni TP", "Identificazione automatica / RFID"),
 "sistemi.html": ("Sistemistica", "Soluzioni sistemistiche, sicurezza, cloud, vendor"),
 "tecnologia.html": ("Sistemistica", "Innovazione tecnologica"),
 "ruckus.html": ("Sistemistica", "WiFi professionale Ruckus (testo assente)"),
 "news.html": ("News", "News storiche (vecchia versione)"),
 "newsnew.html": ("News", "News aziendali (versione in uso)"),
 "azienda.html": ("Azienda", "Chi siamo: Mission + Company Profile — nata negli anni '80, \"Knowledge Company\""),
 "contatti.html": ("Azienda", "Contatti / Assistenza Pro — quasi solo immagini"),
 "modulo.html": ("Azienda", "Richiedi informazioni — form Google Forms in iframe"),
 "indicazioni.html": ("Azienda", "Sede, mappa, telefono, email"),
 "lavoraconnoi.html": ("Azienda", "Lavora con noi — form Google Forms in iframe"),
}
order = ["Home","Panoramica","ERP Mago","ERP Ad Hoc Infinity","Suite Zucchetti","Soluzioni TP","Sistemistica","News","Azienda"]
by = {}
for p in idx:
    c, note = cat.get(p["file"], ("Altro",""))
    by.setdefault(c, []).append((p, note))

L = []
L.append("# Inventario contenuti — www.tp-italia.com\n")
L.append(f"Archivio catturato il 25/08/2026. **{len(idx)} pagine HTML**, "
         f"{sum(p['words'] for p in idx):,} parole, 540 file totali (~97 MB tra immagini, PDF e 6 video).\n")
L.append("Tutto il materiale originale è in `archivio/sito/` (copia byte per byte del sito online) "
         "e in `archivio/contenuti/` (testo di ogni pagina estratto in Markdown, riutilizzabile).\n")
L.append("La colonna **Destino** va compilata insieme al nuovo intento: `MANTIENI` · `RISCRIVI` · `FONDI` · `ARCHIVIA`.\n")
for c in order:
    if c not in by: continue
    L.append(f"\n## {c}\n")
    L.append("| Pagina | Titolo | Parole | Contenuto | Destino |")
    L.append("|---|---|---:|---|---|")
    for p, note in sorted(by[c], key=lambda x: -x[0]["words"]):
        L.append(f"| `{p['file']}` | {p['title'] or '—'} | {p['words']} | {note} | |")
open("/home/user/DoveW/INVENTARIO.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L[:12]))
