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

DEST = {
 "index.html": ("RISCRIVI", "fatta — nuova home rivolta alla direzione"),
 "azienda.html": ("RISCRIVI", "portare nel menu; aggiungere persone, numeri e casi"),
 "contatti.html": ("FONDI", "in una sola pagina Contatti"),
 "indicazioni.html": ("FONDI", "in una sola pagina Contatti"),
 "modulo.html": ("FONDI", "in una sola pagina Contatti, con form proprio"),
 "lavoraconnoi.html": ("RISCRIVI", "posizioni aperte + form proprio"),
 "gestionalix.html": ("FONDI", "in Soluzioni > Sistema gestionale ERP"),
 "gestionali.html": ("FONDI", "in Soluzioni > Sistema gestionale ERP"),
 "prodottinew.html": ("ARCHIVIA", "sostituita dal menu Soluzioni; 301"),
 "verticali.html": ("RISCRIVI", "verticali per settore, con casi reali"),
 "mago.html": ("FONDI", "in Mago4"),
 "mago4.html": ("RISCRIVI", "da fonte Zucchetti ufficiale"),
 "magoweb.html": ("RISCRIVI", "da fonte Zucchetti"),
 "magocloud.html": ("RISCRIVI", "da fonte Zucchetti"),
 "magoamministrativa.html": ("RISCRIVI", "area amministrazione, da fonte Zucchetti"),
 "magovenditeacquisti.html": ("RISCRIVI", "area vendite e acquisti, da fonte Zucchetti"),
 "magomagazzino.html": ("RISCRIVI", "area magazzino, da fonte Zucchetti"),
 "magoproduzione.html": ("RISCRIVI", "area produzione, da fonte Zucchetti"),
 "ahi.html": ("RISCRIVI", "da fonte Zucchetti ufficiale"),
 "ahiamministrazione.html": ("RISCRIVI", "da fonte Zucchetti"),
 "ahivendite.html": ("RISCRIVI", "da fonte Zucchetti"),
 "ahigestione.html": ("RISCRIVI", "da fonte Zucchetti"),
 "ahilogistica.html": ("RISCRIVI", "da fonte Zucchetti"),
 "infinity.html": ("RISCRIVI", "Infinity oggi, non 4.2 — da fonte Zucchetti"),
 "crm.html": ("RISCRIVI", "buona base testuale, tono da rifare"),
 "dms.html": ("RISCRIVI", "da fonte Zucchetti"),
 "hr.html": ("RISCRIVI", "oggi senza testo: da fonte Zucchetti HR Infinity"),
 "portal.html": ("RISCRIVI", "da fonte Zucchetti"),
 "infobusiness.html": ("RISCRIVI", "da fonte Zucchetti"),
 "bussinessapps.html": ("RISCRIVI", "oggi senza testo; correggere anche l'URL"),
 "cloudapp.html": ("FONDI", "in Business Apps"),
 "fepasos.html": ("RISCRIVI", "fatturazione e conservazione, da fonte Zucchetti"),
 "presenzeweb.html": ("FONDI", "in Persone e presenze, con testo vero"),
 "smplice.html": ("FONDI", "in Persone e presenze"),
 "ztravel.html": ("FONDI", "in Persone e presenze"),
 "itek4.html": ("RISCRIVI", "soluzione nostra: problema prima del prodotto"),
 "operames.html": ("FONDI", "in Fabbrica connessa"),
 "easytime.html": ("RISCRIVI", "soluzione nostra: ottima base, tono da rifare"),
 "easyind40.html": ("RISCRIVI", "collegare a Finanza agevolata 5.0"),
 "wapp.html": ("RISCRIVI", "soluzione nostra"),
 "mobileticketnew.html": ("FONDI", "in Assistenza e ticketing con ITEK4"),
 "rfid.html": ("FONDI", "in Logistica di magazzino"),
 "sistemi.html": ("RISCRIVI", "togliere il gergo, tenere il ragionamento consulenziale"),
 "tecnologia.html": ("FONDI", "in Continuità e sicurezza"),
 "ruckus.html": ("FONDI", "in Continuità e sicurezza"),
 "newsnew.html": ("MANTIENI", "da riattivare: ferma al 2018"),
 "news.html": ("ARCHIVIA", "doppione storico; 301 su News"),
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
L.append("Colonna **Destino** secondo il riposizionamento definito in `STRATEGIA.md`: "
         "`MANTIENI` · `RISCRIVI` · `FONDI` (confluisce in un'altra pagina, con 301) · `ARCHIVIA` (resta online con 301).\n")
for c in order:
    if c not in by: continue
    L.append(f"\n## {c}\n")
    L.append("| Pagina | Titolo | Parole | Contenuto | Destino |")
    L.append("|---|---|---:|---|---|")
    for p, note in sorted(by[c], key=lambda x: -x[0]["words"]):
        d = DEST.get(p["file"], ("", ""))
        L.append(f"| `{p['file']}` | {p['title'] or '—'} | {p['words']} | {note} | **{d[0]}** {d[1]} |")
open("/home/user/DoveW/INVENTARIO.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L[:12]))
