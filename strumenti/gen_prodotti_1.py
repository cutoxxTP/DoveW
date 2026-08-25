# -*- coding: utf-8 -*-
"""Schede prodotto Zucchetti — lotto 1: Mago4, MagoWeb, MagoCloud, Ad Hoc Infinity, Infinity, CRM.
Contenuti riscritti sulle pagine ufficiali zucchetti.it (verifica: agosto 2026)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tpl_pagina import pagina
OUT = "/home/user/DoveW/sito"

def F(url, cosa):
    return ('Contenuti riscritti sulla pagina ufficiale Zucchetti dedicata a %s '
            '(<a href="%s" rel="nofollow">zucchetti.it</a>). Ultima verifica: agosto 2026. '
            'Le funzionalit&agrave; effettivamente disponibili dipendono dai moduli e dalla versione '
            'in licenza: le verifichiamo insieme sulla vostra configurazione.') % (cosa, url)

RUOLO = """
<h2>Che cosa aggiungiamo noi</h2>
<p>Il software &egrave; di Zucchetti; il progetto &egrave; nostro. Siamo <b>Top Partner ERP Zucchetti</b> e
<b>Mago Platinum Partner</b>: significa che l'analisi, la configurazione, le personalizzazioni,
la formazione e l'assistenza restano in capo a noi, con un referente che conosce la vostra azienda.
%s</p>
"""

# ------------------------------------------------------------------ MAGO4
mago4 = """
<h2>Per chi &egrave; pensato</h2>
<p>Mago4 &egrave; il gestionale Zucchetti per le <b>piccole e medie imprese</b> commerciali, industriali e
di servizi: copre il ciclo completo, dall'offerta al cliente fino alla pianificazione della produzione
e alla logistica di magazzino.</p>
<p>La logica &egrave; modulare: si parte da quello che serve oggi e si aggiungono i pezzi quando servono.
Zucchetti mette a disposizione <b>oltre 50 moduli</b>, e il profilo si costruisce sulla realt&agrave;
di ciascuna azienda invece di adattare l'azienda al programma.</p>

<h2>Le quattro aree</h2>
<div class="tpGrid">
  <div><h4>Amministrazione e finanza</h4>
    <p>Contabilit&agrave; generale, analitica e previsionale, adempimenti fiscali, gestione banche
      e tesoreria.</p>
    <a href="magoamministrativa.html">Vai all'area &rarr;</a></div>
  <div><h4>Vendite e acquisti</h4>
    <p>Offerte, ordini, listini e sconti, documenti di trasporto, fatturazione attiva e passiva.</p>
    <a href="magovenditeacquisti.html">Vai all'area &rarr;</a></div>
  <div><h4>Magazzino e logistica</h4>
    <p>Giacenze, movimentazioni, ubicazioni, lotti e matricole, inventari.</p>
    <a href="magomagazzino.html">Vai all'area &rarr;</a></div>
  <div><h4>Produzione</h4>
    <p>Distinta base, cicli di lavorazione, avanzamento e pianificazione MRP.</p>
    <a href="magoproduzione.html">Vai all'area &rarr;</a></div>
</div>

<h2>Le anagrafiche, che &egrave; dove si vede la differenza</h2>
<p>Un gestionale si giudica anche da quanto sa essere preciso sulle informazioni di base. In Mago4 le
anagrafiche di clienti e fornitori <b>pilotano il comportamento del programma</b> sulla base delle
necessit&agrave; del singolo interlocutore:</p>
<ul>
  <li>collegamenti tra anagrafiche e selezione di un cliente di fatturazione diverso dal destinatario;</li>
  <li>note automatiche che compaiono dove servono, senza doversele ricordare;</li>
  <li>censimento e gestione di <b>sedi alternative</b>, anche con coordinate geografiche;</li>
  <li>invio dei documenti via e-mail e gestione dell'informativa privacy;</li>
  <li>controllo del credito e dei limiti di importo.</li>
</ul>

<h2>Come &egrave; fatto</h2>
<ul>
  <li><b>Multiaziendale senza limiti di numero</b>, con profilazione degli utenti sulle singole aziende.</li>
  <li><b>Multilingua, multivaluta e multinormativa</b>, con localizzazione su pi&ugrave; normative fiscali:
    utile a chi ha sedi o societ&agrave; all'estero.</li>
  <li><b>Console di amministrazione centralizzata</b> per la gestione del sistema.</li>
  <li><b>Tracciabilit&agrave;</b>: resta registrato chi ha modificato che cosa e quando.</li>
  <li><b>Accesso remoto e WebService</b>, per lavorare fuori sede e per integrare altri sistemi.</li>
  <li><b>Profili di accesso differenziati</b> per utente e per ruolo.</li>
</ul>
""" + RUOLO % ("Su Mago lavoriamo da anni e abbiamo sviluppato verticalizzazioni nostre "
               "che si innestano nel gestionale: rilevazione dei tempi di produzione, magazzino, assistenza in mobilit&agrave;.")

# ------------------------------------------------------------------ MAGOWEB
magoweb = """
<h2>Il gestionale che si apre con un browser</h2>
<p>MagoWeb &egrave; la versione web del gestionale Zucchetti per le PMI: <b>accessibile via browser</b>,
in rete locale o via internet, senza installazioni sui singoli computer. Si lavora dall'ufficio,
da casa o dal cliente con lo stesso sistema e gli stessi dati.</p>
<p>&Egrave; costruito sulla stessa impostazione di MagoCloud e pensato per aziende che vogliono un sistema
<b>leggero e scalabile</b>, senza rinunciare alla profondit&agrave; di un ERP.</p>

<h2>Le aree disponibili</h2>
<div class="tpGrid">
  <div><h4>Amministrativa</h4>
    <p>Contabilit&agrave; generale, contabilit&agrave; previsionale e contabilit&agrave; analitica.</p></div>
  <div><h4>Vendite e acquisti</h4>
    <p>Preventivi, ordini, bolle e fatturazione, con il flusso documentale collegato.</p></div>
  <div><h4>Produzione</h4>
    <p>Distinta base, cicli produttivi, gestione delle varianti e configuratore commerciale.</p></div>
</div>

<h2>Che cosa ci si collega</h2>
<p>MagoWeb non nasce isolato: si integra con le altre soluzioni Zucchetti &mdash; <b>Digital Hub</b> per
i flussi documentali, <b>Anticipay</b>, <b>Opera MES</b> per la fabbrica, <b>CyberPlan</b> per la
pianificazione &mdash; e mette a disposizione strumenti per estenderlo: il framework
<b>TaskBuilder</b>, le <b>API REST</b> e i moduli aperti <b>OpenPOS</b>, <b>OpenECommerce</b> e
<b>OpenMES</b>.</p>
<div class="tpBox">
  <p><b>Quando conviene rispetto a Mago4.</b> Quando contano l'accesso da fuori sede, la riduzione
    delle installazioni da mantenere e la possibilit&agrave; di far lavorare pi&ugrave; sedi sullo stesso
    sistema. La scelta tra le due versioni si fa guardando i vostri processi, non le brochure:
    &egrave; il primo tema di cui parliamo.</p>
</div>
""" + RUOLO % ""

# ------------------------------------------------------------------ MAGOCLOUD
magocloud = """
<h2>Cloud vero, non un server in affitto</h2>
<p>MagoCloud &egrave; la versione interamente cloud del gestionale Zucchetti: nessuna installazione locale,
nessun hardware da comprare e mantenere, accesso da qualunque postazione con una connessione internet.
Zucchetti lo presenta come &laquo;il software gestionale veramente cloud&raquo;, con
<b>sicurezza a pi&ugrave; livelli</b> e backup garantito.</p>
<p>La differenza pratica per un'impresa &egrave; sui costi che spariscono: licenza, manutenzione e
gestione della sicurezza non sono pi&ugrave; voci a carico vostro.</p>

<h2>Quattro edizioni, si cresce senza cambiare sistema</h2>
<p>MagoCloud &egrave; disponibile in edizioni <b>Standard, Premium, Professional ed Enterprise</b>:
si parte dalla configurazione adeguata all'azienda di oggi e si sale di edizione quando serve,
senza interruzioni e senza migrazioni.</p>

<h2>Che cosa gli si affianca</h2>
<div class="tpGrid">
  <div><h4>Punto vendita</h4><p>POS Zucchetti per il ciclo di vendita retail e <b>InStore App</b>.</p></div>
  <div><h4>Magazzino in mobilit&agrave;</h4><p><b>WMS Mobile</b> per le operazioni di magazzino
    direttamente dal terminale.</p></div>
  <div><h4>Indicatori</h4><p><b>KPI Dashboard</b> per tenere sotto controllo l'andamento senza estrazioni manuali.</p></div>
  <div><h4>Commercio elettronico</h4><p><b>Mago E-Commerce</b> per B2C e B2B, collegato al gestionale.</p></div>
  <div><h4>Conservazione</h4><p><b>SOS Connector</b> per la conservazione digitale a norma.</p></div>
  <div><h4>Fabbrica e pianificazione</h4><p><b>Opera MES</b> per la fabbrica digitale e <b>CyberPlan</b>
    per la pianificazione della produzione.</p></div>
</div>
<p>Zucchetti mette inoltre a disposizione configurazioni specifiche per settore &mdash; moda, servizi,
alimentare, manifattura, retail &mdash; che riducono il lavoro di adattamento iniziale.</p>
""" + RUOLO % ""

# ------------------------------------------------------------------ AD HOC INFINITY
ahi = """
<h2>L'ERP web per le aziende strutturate</h2>
<p>Ad Hoc Infinity &egrave; il gestionale web di Zucchetti per le imprese di dimensioni maggiori:
<b>oltre 60 moduli personalizzabili</b> e un'impostazione che va oltre il gestionale tradizionale,
basata sulla condivisione delle informazioni tra le funzioni aziendali.</p>

<h2>Le aree coperte</h2>
<div class="tpGrid">
  <div><h4>Amministrazione e finanza</h4>
    <p>Gestione economica e finanziaria in regime ordinario o semplificato, multivaluta, fatturazione
      elettronica automatizzata, adempimenti (730, Unico, IVA, Intrastat) e monitoraggio finanziario
      in tempo reale.</p>
    <a href="ahiamministrazione.html">Vai all'area &rarr;</a></div>
  <div><h4>Vendite e acquisti</h4>
    <p>Documenti di acquisto e vendita collegati con travaso automatico dei dati, listini e sconti,
      confronto dei preventivi fornitori, pianificazione degli approvvigionamenti per fabbisogni.</p>
    <a href="ahivendite.html">Vai all'area &rarr;</a></div>
  <div><h4>Magazzino e logistica</h4>
    <p>Ciclo attivo e passivo di magazzino con gestione per ubicazioni e articoli a varianti,
      Logistica Avanzata dall'evasione ordini alla spedizione (DDT e fatturazione),
      Distinta Base per la movimentazione automatica.</p>
    <a href="ahilogistica.html">Vai all'area &rarr;</a></div>
  <div><h4>Controllo di gestione</h4>
    <p>Cruscotti e report configurabili sugli indicatori, budget, analisi degli scostamenti e della
      redditivit&agrave;, con impiego di intelligenza artificiale e machine learning per le analisi
      di scenario.</p>
    <a href="ahigestione.html">Vai all'area &rarr;</a></div>
</div>

<h2>Un pezzo di una piattaforma pi&ugrave; ampia</h2>
<p>Ad Hoc Infinity dialoga con le altre soluzioni Zucchetti: contabilit&agrave;, area commerciale,
logistica, produzione e gestione del personale lavorano sugli stessi dati, senza le riconciliazioni
manuali che nascono quando i sistemi sono separati.</p>
""" + RUOLO % ""

# ------------------------------------------------------------------ INFINITY
infinity = """
<h2>Che cos'&egrave;</h2>
<p>Infinity Zucchetti &egrave; la piattaforma che tiene insieme le applicazioni gestionali dell'azienda.
Non &egrave; un singolo programma: &egrave; un ambiente <b>totalmente web-nativo</b>, sviluppato con un
linguaggio comune, in cui le diverse applicazioni si presentano e si usano allo stesso modo.</p>
<p>Il vantaggio dichiarato da Zucchetti &egrave; di sostanza per chi gestisce un budget:
<b>minori costi di acquisto, di manutenzione e di infrastruttura</b>, perch&eacute; gli strumenti
trasversali &mdash; analisi, gestione dei flussi di lavoro, collaborazione &mdash; sono gi&agrave;
dentro la piattaforma e non vanno comprati e integrati uno per uno.</p>

<h2>Le applicazioni della suite</h2>
<div class="tpGrid">
  <div><h4>ERP</h4><p>Il governo dei processi centrali dell'azienda.</p></div>
  <div><h4>CRM</h4><p>Gestione della relazione con il cliente, prima e dopo la vendita.</p>
    <a href="crm.html">Scheda CRM &rarr;</a></div>
  <div><h4>Fatturazione elettronica</h4><p>Emissione e ricezione conformi alla normativa.</p>
    <a href="fepasos.html">Scheda &rarr;</a></div>
  <div><h4>Gestione documentale</h4><p>Archiviazione e processi approvativi al posto della carta.</p>
    <a href="dms.html">Scheda DMS &rarr;</a></div>
  <div><h4>Business Intelligence e Analytics</h4><p>Analisi e controllo di gestione sui dati aziendali.</p>
    <a href="infobusiness.html">Scheda &rarr;</a></div>
  <div><h4>Asset Management</h4><p>Gestione dei beni aziendali, comprese le sfide energetiche
    e organizzative.</p></div>
  <div><h4>E-commerce e portali</h4><p>Vendita online e portali aziendali collegati al gestionale.</p>
    <a href="portal.html">Scheda &rarr;</a></div>
  <div><h4>Collaboration</h4><p>Strumenti di lavoro condiviso integrati nelle altre applicazioni.</p></div>
</div>
""" + RUOLO % ""

# ------------------------------------------------------------------ CRM
crm = """
<h2>Prima della vendita</h2>
<p>Infinity CRM governa le informazioni sui contatti e sulle opportunit&agrave; commerciali che coinvolgono
marketing e vendite. Un contatto si gestisce in modo completo: lo si classifica con le informazioni
che contano davvero per voi &mdash; profilo, attivit&agrave;, settore, informazioni finanziarie &mdash; e in
qualsiasi momento se ne ha lo <b>storico</b>: azioni eseguite, opportunit&agrave; generate, esiti.</p>
<ul>
  <li><b>Ogni fase della trattativa monitorata</b>, con stime e previsioni di vendita.</li>
  <li><b>Ritorno delle campagne di marketing</b> analizzato, non stimato a memoria.</li>
  <li><b>Concorrenza e mercato</b>: le informazioni raccolte restano nel sistema, non nella testa
    del commerciale.</li>
  <li><b>Offerte create automaticamente</b> e collegate alla parte contabile: meno tempo perso
    e meno errori di trascrizione.</li>
</ul>

<h2>Dopo la vendita</h2>
<p>La parte post-vendita registra e assegna tutto quello che succede dopo la consegna, e d&agrave; all'area
commerciale e all'assistenza una visibilit&agrave; completa: assistenza tecnica, manutenzioni, contratti
di garanzia, assistenza commerciale e amministrativa.</p>
<p>Le richieste del cliente diventano <b>ticket</b> che si pianificano, si consuntivano e si analizzano,
con regole automatiche per lo smistamento. &Egrave; il punto in cui un'azienda smette di rincorrere le
segnalazioni e comincia a governarle.</p>

<h2>Dove vive</h2>
<p>Infinity CRM &egrave; nativamente integrato con il client di posta e con la <b>Collaboration</b> di
Infinity Zucchetti: le comunicazioni con il cliente restano attaccate alla sua scheda, non sparse
nelle caselle dei singoli.</p>
""" + RUOLO % ("Un CRM non fallisce per il software: fallisce quando nessuno lo alimenta. "
               "Per questo la parte su cui insistiamo &egrave; l'innesto nei processi di vendita che avete gi&agrave;.")

PAGES = [
 dict(slug="mago4.html", on="", marchio="mago4.png",
  title="Mago4, il gestionale ERP Zucchetti per le PMI | Technology Partners Italia",
  desc="Mago4: oltre 50 moduli per amministrazione, vendite, acquisti, magazzino e produzione. Multiaziendale, multilingua e multinormativa. Installato e assistito da Technology Partners Italia, Mago Platinum Partner.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; Mago4',
  kick="Gestionale ERP &middot; Zucchetti", h1="Mago4: l'ERP che si costruisce sulla vostra azienda",
  lead="Il gestionale Zucchetti per le PMI commerciali, industriali e di servizi: dall'offerta al cliente fino alla pianificazione della produzione, con oltre 50 moduli da attivare solo quando servono.",
  body=mago4, ctah="Da dove conviene partire",
  ctap="Se avete gi&agrave; un gestionale, il tema non &egrave; sostituirlo: &egrave; capire quali processi oggi vi costano tempo. Da l&igrave; si vede che cosa serve davvero attivare.",
  fonte=F("https://www.zucchetti.it/it/cms/soluzioni/software-gestionali/tecnologia/gestionali-client-server/mago4","Mago4")),
 dict(slug="magoweb.html", on="", marchio="logo_magoweb.png",
  title="MagoWeb, il gestionale Zucchetti via browser | Technology Partners Italia",
  desc="MagoWeb: ERP web per PMI accessibile da browser. Area amministrativa, vendite e acquisti, produzione. Integrazioni Digital Hub, Opera MES, CyberPlan, API REST e moduli Open.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; MagoWeb',
  kick="Gestionale ERP web &middot; Zucchetti", h1="MagoWeb: lo stesso gestionale, dentro un browser",
  lead="Nessuna installazione sui computer, accesso in rete locale o via internet. Un ERP leggero e scalabile per le PMI, costruito sull'impostazione di MagoCloud.",
  body=magoweb, ctah="Mago4, MagoWeb o MagoCloud?",
  ctap="Le tre versioni servono esigenze diverse. La scelta dipende da come lavorate, da quante sedi avete e da chi deve accedere da fuori: ne parliamo prima di qualsiasi preventivo.",
  fonte=F("https://www.zucchetti.it/it/cms/soluzioni/software-gestionali/tecnologia/gestionali-in-cloud/magoweb/software-gestionale-cloud-descrizione.html","MagoWeb")),
 dict(slug="magocloud.html", on="", marchio="logomagocloud.png",
  title="MagoCloud, il gestionale Zucchetti in cloud | Technology Partners Italia",
  desc="MagoCloud: gestionale interamente cloud, senza costi di licenza, manutenzione e sicurezza. Quattro edizioni, POS, WMS Mobile, e-commerce, Opera MES e CyberPlan.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; MagoCloud',
  kick="Gestionale ERP in cloud &middot; Zucchetti", h1="MagoCloud: il gestionale senza server da mantenere",
  lead="Nessuna installazione locale, nessun hardware, sicurezza e backup a carico della piattaforma. Quattro edizioni per crescere senza cambiare sistema.",
  body=magocloud, ctah="Quanto costa davvero il vostro server?",
  ctap="Tra licenze, manutenzione, backup e ore di sistemista, il confronto con il cloud si fa sui numeri. Li mettiamo in fila insieme.",
  fonte=F("https://www.zucchetti.it/it/cms/soluzioni/software-gestionali/tecnologia/gestionali-in-cloud/magocloud/software-gestionale-cloud-descrizione.html","MagoCloud")),
 dict(slug="ahi.html", on="", marchio="ahi_logo.png",
  title="Ad Hoc Infinity, l'ERP web Zucchetti per aziende strutturate | Technology Partners Italia",
  desc="Ad Hoc Infinity: oltre 60 moduli per amministrazione e finanza, vendite e acquisti, magazzino e logistica, controllo di gestione con analisi di scenario in machine learning.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; Ad Hoc Infinity',
  kick="Gestionale ERP web &middot; Zucchetti", h1="Ad Hoc Infinity: l'ERP web per le aziende strutturate",
  lead="Oltre 60 moduli personalizzabili e un'impostazione basata sulla condivisione delle informazioni tra le funzioni aziendali, non sulla somma di programmi separati.",
  body=ahi, ctah="Vale la pena vederlo sui vostri processi",
  ctap="Un ERP di questa portata si valuta sul caso concreto: i vostri flussi, i vostri documenti, i vostri numeri. &Egrave; il modo in cui organizziamo la presentazione.",
  fonte=F("https://www.zucchetti.it/it/cms/soluzioni/software-gestionali/dimensione-azienda/grandi-aziende/ad-hoc-infinity/programma-gestionale-web-funzionalita.html","Ad Hoc Infinity")),
 dict(slug="infinity.html", on="", marchio="infinity_crm_a.jpg",
  title="Infinity Zucchetti, la piattaforma integrata d'impresa | Technology Partners Italia",
  desc="Infinity Zucchetti: piattaforma web-nativa che tiene insieme ERP, CRM, fatturazione elettronica, documentale, business intelligence, asset management, e-commerce e collaboration.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; Infinity Zucchetti',
  kick="Piattaforma &middot; Zucchetti", h1="Infinity: le applicazioni aziendali che parlano la stessa lingua",
  lead="Una piattaforma web-nativa in cui ERP, CRM, documentale, analisi e portali si presentano e si usano allo stesso modo. Meno costi di integrazione, meno strumenti da comprare a parte.",
  body=infinity, ctah="Da quale applicazione conviene cominciare",
  ctap="Non si adotta una piattaforma tutta insieme. Si parte dal processo che oggi costa di pi&ugrave;, e il resto si aggiunge quando serve.",
  fonte=F("https://www.zucchetti.it/website/cms/infinity-zucchetti/1059-infinity-zucchetti.html","Infinity Zucchetti")),
 dict(slug="crm.html", on="", marchio="infinity_crm_a.jpg",
  title="Infinity CRM: prevendita, vendita e assistenza | Technology Partners Italia",
  desc="Infinity CRM Zucchetti: storico completo del contatto, monitoraggio della trattativa, previsioni di vendita, offerte collegate alla contabilità, ticket di assistenza e regole automatiche.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; CRM',
  kick="Relazione con il cliente &middot; Zucchetti", h1="Infinity CRM: quello che il cliente ha fatto, in un posto solo",
  lead="Prevendita, vendita e post-vendita nello stesso flusso: storico dei contatti, previsioni, offerte collegate alla contabilità e ticket di assistenza governati da regole.",
  body=crm, ctah="Il vostro storico clienti dov'&egrave; oggi?",
  ctap="Nella maggior parte delle aziende &egrave; diviso tra caselle di posta, fogli di calcolo e memoria delle persone. Il primo passo &egrave; guardare dove sono davvero le informazioni.",
  fonte=F("https://www.zucchetti.it/it/cms/soluzioni/marketing-e-vendite/crm/infinity-crm/software-crm-funzionalita.html","Infinity CRM")),
]

for p in PAGES:
    html = pagina(**p)
    open(os.path.join(OUT, p["slug"]), "w", encoding="utf-8").write(html)
    print(p["slug"], len(html), "byte")
