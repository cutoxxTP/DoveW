# -*- coding: utf-8 -*-
"""Portali/e-commerce, hub gestionali ERP e pagine confluite (con canonical verso la nuova)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tpl_pagina import pagina
OUT = "/home/user/DoveW/sito"

portal = """
<h2>Il sito che parla con il gestionale</h2>
<p>Infinity Portal &egrave; il software della suite Infinity con cui si realizzano e si gestiscono
<b>portali aziendali, siti internet, extranet, intranet e siti di commercio elettronico B2B e B2C</b>,
integrati con il sistema informativo dell'azienda.</p>
<p>La differenza rispetto a un sito costruito a parte sta tutta in quell'ultima parola: gli ordini
inseriti online <b>entrano automaticamente nel gestionale</b> e si gestiscono l&igrave;, senza che
qualcuno li ricopi.</p>

<h2>Che cosa comprende</h2>
<div class="tpGrid">
  <div><h4>CMS</h4><p>Strumento per creare portali web e gestire e pubblicare i contenuti
    senza dipendere da un fornitore per ogni modifica.</p></div>
  <div><h4>Aree pubbliche e riservate</h4><p>Portale informativo multiaziendale con accesso
    profilato: ogni utente vede quello che gli compete.</p></div>
  <div><h4>Commercio elettronico</h4><p>Moduli B2B e B2C per rendere disponibile online
    l'offerta commerciale.</p></div>
  <div><h4>Mobile</h4><p>Accesso e navigazione rapidi anche da smartphone e tablet, dove ormai
    arriva la maggior parte delle visite.</p></div>
  <div><h4>Integrazione</h4><p>Si collega al gestionale in uso: gli ordini online entrano
    e si gestiscono nel software che gi&agrave; usate.</p></div>
  <div><h4>Cloud</h4><p>Disponibile come soluzione cloud, con la flessibilit&agrave; di gestione
    che ne consegue.</p></div>
</div>

<h2>Che cosa aggiungiamo noi</h2>
<p>Il software &egrave; di Zucchetti; il progetto &egrave; nostro. Un portale B2B funziona se listini,
sconti e disponibilit&agrave; che mostra sono quelli veri: &egrave; la parte di integrazione con il
gestionale, ed &egrave; quella di cui rispondiamo. Siamo <b>Top Partner ERP Zucchetti</b>.</p>
"""

hub = """
<h2>Cinque strade, e non sono intercambiabili</h2>
<p>&laquo;Ci serve un gestionale nuovo&raquo; &egrave; una frase che pu&ograve; voler dire cinque cose
diverse. La scelta dipende da quante persone lo useranno, da quante sedi avete, da quanto conta
lavorare da fuori, da quanto &egrave; articolata la produzione e da quanto siete disposti a gestire
in casa.</p>

<div class="tpGrid">
  <div><h4>Mago4</h4>
    <p>Il gestionale per le PMI commerciali, industriali e di servizi. Oltre 50 moduli,
      installato sui vostri sistemi, personalizzabile in profondit&agrave;.</p>
    <a href="mago4.html">Scheda Mago4 &rarr;</a></div>
  <div><h4>MagoWeb</h4>
    <p>Lo stesso mondo, ma dentro un browser: nessuna installazione sui computer,
      accesso da rete locale o da internet.</p>
    <a href="magoweb.html">Scheda MagoWeb &rarr;</a></div>
  <div><h4>MagoCloud</h4>
    <p>Interamente in cloud, senza server da comprare e mantenere. Quattro edizioni
      per crescere senza cambiare sistema.</p>
    <a href="magocloud.html">Scheda MagoCloud &rarr;</a></div>
  <div><h4>Ad Hoc Infinity</h4>
    <p>L'ERP web per le aziende strutturate: oltre 60 moduli e controllo di gestione
      con analisi di scenario.</p>
    <a href="ahi.html">Scheda Ad Hoc Infinity &rarr;</a></div>
  <div><h4>Infinity Zucchetti</h4>
    <p>La piattaforma che tiene insieme ERP, CRM, documentale, analisi e portali
      nello stesso ambiente web.</p>
    <a href="infinity.html">Scheda Infinity &rarr;</a></div>
</div>

<h2>Come si decide</h2>
<p>Non con un confronto di funzionalit&agrave;: quelle, su questo livello di prodotti, ci sono quasi
tutte ovunque. Si decide guardando i vostri processi &mdash; dove nascono i dati, chi li inserisce,
dove si fermano &mdash; e la vostra situazione tecnica: che cosa avete gi&agrave;, che cosa &egrave; da
sostituire, che cosa conviene tenere.</p>
<p>&Egrave; il lavoro che facciamo prima del preventivo, ed &egrave; la ragione per cui a volte
la risposta &egrave; &laquo;il gestionale che avete va bene, il problema &egrave; un altro&raquo;.</p>

<h2>Che cosa aggiungiamo noi</h2>
<p>Siamo <b>Top Partner ERP Zucchetti</b> e <b>Mago Platinum Partner</b>: il livello pi&ugrave; alto
della rete. Analisi, configurazione, personalizzazioni, formazione e assistenza restano in capo a noi,
con un referente che conosce la vostra azienda. E quando serve, ci mettiamo anche il software
che abbiamo scritto noi: <a href="fabbrica50.html">EasyTime ed EasyInd</a> per la fabbrica.</p>
"""

def confluita(slug, titolo_pagina, h1, testo, dove, etichetta, desc):
    body = """
<h2>%s</h2>
<p>%s</p>
<p style="margin-top:22px"><a class="btn" href="%s" style="display:inline-block;background:#000080;
  color:#fff;text-decoration:none;font-weight:bold;padding:11px 20px;border-radius:5px">Vai a %s</a></p>
""" % (h1, testo, dove, etichetta)
    return dict(slug=slug, title=titolo_pagina, desc=desc,
        crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; %s' % etichetta,
        kick="Pagina spostata", h1=h1,
        lead="Questo contenuto &egrave; stato riunito in una pagina sola, pi&ugrave; completa e aggiornata.",
        body=body, ctah="Preferite parlarne direttamente?",
        ctap="Un contatto diretto risolve in dieci minuti quello che una pagina spiega in dieci paragrafi.",
        fonte='Pagina mantenuta attiva per non perdere i collegamenti esistenti. Il contenuto aggiornato &egrave; su <a href="%s">%s</a>.' % (dove, etichetta))

PAGES = [
 dict(slug="portal.html",
  title="Infinity Portal: portali aziendali ed e-commerce Zucchetti | Technology Partners Italia",
  desc="Infinity Portal: portali aziendali, intranet, extranet ed e-commerce B2B e B2C integrati con il gestionale. CMS, aree riservate profilate, ordini online che entrano direttamente nel sistema.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; Portali ed e-commerce',
  kick="Portali ed e-commerce &middot; Zucchetti",
  h1="Infinity Portal: l'ordine online entra dritto nel gestionale",
  lead="Portali aziendali, intranet, extranet e siti di commercio elettronico B2B e B2C, integrati con il sistema informativo invece di vivere accanto ad esso.",
  body=portal, ctah="Avete gi&agrave; un e-commerce che non parla con il gestionale?",
  ctap="&Egrave; la situazione pi&ugrave; comune, e la pi&ugrave; costosa: ogni ordine viene ricopiato a mano. Vale la pena misurare quanto tempo se ne va.",
  fonte='Contenuti riscritti sulla pagina ufficiale Zucchetti dedicata a Infinity Portal '
        '(<a href="https://www.zucchetti.it/it/cms/soluzioni/marketing-e-vendite/portali-e-commerce/infinity-portal/ecommerce-portali-descrizione.html" rel="nofollow">zucchetti.it</a>). '
        'Ultima verifica: agosto 2026.'),
 dict(slug="gestionalix.html",
  title="Quale gestionale ERP scegliere: Mago4, MagoWeb, MagoCloud, Ad Hoc Infinity | Technology Partners Italia",
  desc="Le cinque soluzioni gestionali Zucchetti a confronto: Mago4, MagoWeb, MagoCloud, Ad Hoc Infinity e la piattaforma Infinity. Come si sceglie, e perché non si decide da un elenco di funzionalità.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; Sistema gestionale ERP',
  kick="Sistema gestionale ERP", h1="Quale gestionale, e soprattutto perch&eacute;",
  lead="Mago4, MagoWeb, MagoCloud, Ad Hoc Infinity, Infinity: cinque soluzioni Zucchetti che servono esigenze diverse. Qui trovate le differenze che contano davvero nella scelta.",
  body=hub, ctah="Partiamo da dove siete oggi",
  ctap="Che gestionale usate, che cosa fate fuori dal gestionale e dove si ferma l'informazione. Con queste tre risposte la scelta diventa quasi ovvia.",
  fonte='Le schede collegate riportano contenuti riscritti sulle pagine ufficiali Zucchetti, con data di verifica indicata su ciascuna.'),
 confluita("mago.html","Mago: il gestionale Zucchetti | Technology Partners Italia",
   "Le pagine su Mago sono ora una sola",
   "Le informazioni su Mago sono state riunite nella scheda di Mago4, aggiornata sulle fonti ufficiali Zucchetti, "
   "con le quattro aree funzionali e le versioni web e cloud collegate.",
   "mago4.html","Mago4","Le informazioni su Mago sono state riunite nella scheda Mago4, aggiornata sulle fonti ufficiali Zucchetti."),
 confluita("gestionali.html","Software gestionali | Technology Partners Italia",
   "Questa pagina &egrave; confluita nel confronto tra i gestionali",
   "Il contenuto sui software gestionali &egrave; ora nella pagina che mette a confronto le cinque soluzioni Zucchetti "
   "e spiega come si sceglie tra di loro.",
   "gestionalix.html","Sistema gestionale ERP","Il contenuto è confluito nella pagina di confronto tra i gestionali ERP Zucchetti."),
 confluita("presenzeweb.html","PresenzeWeb: rilevazione presenze | Technology Partners Italia",
   "La rilevazione presenze &egrave; ora nella pagina Persone e presenze",
   "Presenze, assenze, straordinari, piano ferie e app per i dipendenti sono descritti nella pagina dedicata "
   "alla gestione del personale con HR Infinity.",
   "hr.html","Persone e presenze","Presenze, assenze e piano ferie sono ora descritti nella pagina dedicata a HR Infinity."),
 confluita("smplice.html","Rilevazione presenze semplice | Technology Partners Italia",
   "La rilevazione presenze &egrave; ora nella pagina Persone e presenze",
   "Le soluzioni per la rilevazione delle presenze, dalla pi&ugrave; semplice alla suite completa, sono descritte "
   "nella pagina dedicata alla gestione del personale.",
   "hr.html","Persone e presenze","Le soluzioni per la rilevazione presenze sono ora descritte nella pagina dedicata a HR Infinity."),
 confluita("bussinessapps.html","Business Apps Infinity | Technology Partners Italia",
   "Le Business Apps fanno parte della piattaforma Infinity",
   "Le applicazioni di business Zucchetti vivono dentro la piattaforma Infinity, insieme a ERP, CRM, documentale, "
   "analisi e portali. La descrizione aggiornata &egrave; nella scheda della piattaforma.",
   "infinity.html","Infinity Zucchetti","Le Business Apps sono descritte nella scheda della piattaforma Infinity Zucchetti."),
 confluita("cloudapp.html","Cloud Apps Infinity | Technology Partners Italia",
   "Le applicazioni cloud fanno parte della piattaforma Infinity",
   "Le applicazioni disponibili in cloud sono parte della suite Infinity, accessibile via browser senza installazioni. "
   "La descrizione aggiornata &egrave; nella scheda della piattaforma.",
   "infinity.html","Infinity Zucchetti","Le applicazioni cloud sono descritte nella scheda della piattaforma Infinity Zucchetti."),
]

for p in PAGES:
    open(os.path.join(OUT, p["slug"]), "w", encoding="utf-8").write(pagina(**p))
    print(p["slug"], "ok")
