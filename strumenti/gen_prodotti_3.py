# -*- coding: utf-8 -*-
"""Aree funzionali: Mago4 (4 pagine) e Ad Hoc Infinity (4 pagine)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tpl_pagina import pagina
OUT = "/home/user/DoveW/sito"

FM = ('Descrizioni dei moduli tratte dalla documentazione ufficiale Zucchetti su Mago4 '
      '(<a href="https://www.zucchetti.it/it/cms/soluzioni/software-gestionali/tecnologia/gestionali-client-server/mago4" rel="nofollow">zucchetti.it</a>). '
      'Ultima verifica: agosto 2026. I moduli attivabili dipendono dalla licenza: li verifichiamo insieme sulla vostra configurazione.')
FA = ('Contenuti riscritti sulla pagina ufficiale Zucchetti dedicata ad Ad Hoc Infinity '
      '(<a href="https://www.zucchetti.it/it/cms/soluzioni/software-gestionali/dimensione-azienda/grandi-aziende/ad-hoc-infinity/programma-gestionale-web-funzionalita.html" rel="nofollow">zucchetti.it</a>). '
      'Ultima verifica: agosto 2026. I moduli attivabili dipendono dalla licenza: li verifichiamo insieme sulla vostra configurazione.')

def grid(items):
    out=['<div class="tpGrid">']
    for t,d in items:
        out.append('<div><h4>%s</h4><p>%s</p></div>' % (t,d))
    out.append('</div>')
    return "\n".join(out)

TORNA = '<p style="margin-top:26px"><a href="%s"><b>&larr; Torna alla scheda %s</b></a></p>'

# ---------------------------------------------------------------- MAGO AMMINISTRAZIONE
amm = """
<h2>Dalla registrazione al bilancio, senza doppi passaggi</h2>
<p>L'area amministrativa di Mago4 copre gli obblighi della contabilit&agrave; ordinaria e, nello stesso
impianto, gli strumenti che servono alla direzione per capire come sta andando l'azienda prima
della chiusura d'esercizio.</p>
""" + grid([
 ("Contabilit&agrave; Generale","Scritture in partita doppia, libri e registri fiscali, bilanci e riclassificazioni libere dei saldi. Gli archivi collegati &mdash; saldi, partite, dati IVA &mdash; si aggiornano in tempo reale, con quadratura costante tra saldi e scadenzari."),
 ("Contabilit&agrave; Previsionale","Movimenti paralleli per fatti non ancora registrabili, come le quote mensili degli accantonamenti: si ottiene un bilancio di periodo pi&ugrave; vicino alla realt&agrave;, senza aspettare fine anno."),
 ("Contabilit&agrave; Analitica","Centri di costo e commesse pluriennali sullo stesso piano dei conti della generale. I movimenti analitici nascono dai documenti di vendita e acquisto, dal magazzino e dagli ammortamenti."),
 ("Ammortamenti","Anagrafica cespiti dettagliata, calcolo nei vari regimi, prima nota generata in automatico, registro dei beni ammortizzabili. Con la contabilit&agrave; analitica le quote si ripartiscono su centri di costo e commesse."),
 ("Bilancio Consolidato","Per chi controlla altre societ&agrave;: raccolta ed elaborazione dei bilanci del gruppo, conversione dei saldi in divisa estera, esclusione delle operazioni intercompany tramite modelli di consolidamento."),
 ("XBRL Bilancio","Trasformazione del bilancio nel formato standard XBRL per il deposito al Registro delle Imprese, sfruttando la riclassificazione UE gi&agrave; presente in contabilit&agrave; generale."),
 ("Analisi Bilancio Basilea 2","Foglio Excel collegato dinamicamente al database aziendale per l'autovalutazione secondo i principi di Basilea 2: utile a preparare la presentazione dell'azienda agli istituti di credito."),
 ("Gestione Banche Avanzato","File SEPA XML per bonifici (SCT) e addebiti diretti (SDD CORE/B2B), stampa dei mandati da far sottoscrivere, anagrafiche bancarie aggiornate via web-service."),
 ("Gestione Cassa","Entrate, uscite, incassi e pagamenti su una sessione dedicata che si consolida in prima nota. Ogni operazione ha il suo pulsante: non servono conoscenze contabili per usarlo."),
 ("Intrastat, Spesometro e adempimenti","Elenchi riepilogativi e comunicazioni periodiche prodotti dai dati gi&agrave; presenti in contabilit&agrave;."),
 ("Libro Inventari e Allegati","Stampa dei libri obbligatori con gli allegati previsti."),
 ("Importazione Paghe","Acquisizione delle scritture provenienti dal software paghe, senza reinserimenti manuali."),
]) + TORNA % ("mago4.html","Mago4")

# ---------------------------------------------------------------- MAGO VENDITE ACQUISTI
va = """
<h2>Il ciclo commerciale, dall'offerta all'incasso</h2>
<p>&Egrave; l'area in cui un gestionale si fa sentire tutti i giorni: quanto tempo serve per fare
un'offerta, quanto per sapere se un cliente pu&ograve; ancora comprare a credito, quanto per capire
se un fornitore ha rispettato le condizioni.</p>
""" + grid([
 ("Ordini da Clienti","Offerte anche in divisa diversa da quella aziendale, ordini inseriti o travasati dall'offerta. All'inserimento Mago4 impegna le quantit&agrave;, controlla la disponibilit&agrave; e propone la data di prevista consegna."),
 ("Listini e politiche di prezzo","Pi&ugrave; listini di vendita e scalette personalizzate di proposizione di prezzi e sconti: le condizioni commerciali smettono di essere una trattativa a memoria."),
 ("Gestione Fidi","Quattro criteri di controllo del fido applicati lungo il flusso di vendita, con azione configurabile per ciascuno e un indicatore a semaforo sull'esposizione complessiva del cliente."),
 ("Sales Force Management","Anagrafica agenti e politiche provvigionali, pi&ugrave; metodi di calcolo, gestione delle provvigioni anche in caso di insoluto, due agenti o agente e capoarea sullo stesso documento."),
 ("Ordini a Fornitori","Offerte fornitore trasformate in ordini, generazione automatica degli ordini per garantire le consegne ai clienti, riordino da impegnato e sottoscorta, analisi dell'andamento futuro delle scorte."),
 ("Acquisti","Bolle di carico, fatture e note di credito, controllo di conformit&agrave; della merce ricevuta, oneri accessori ripartiti sulla merce. Integrato con ordini a fornitore, magazzino e contabilit&agrave;."),
 ("Controllo Qualit&agrave;","Ordine di collaudo generato in automatico dalla bolla di carico per gli articoli soggetti a verifica; l'esito genera il carico nel deposito appropriato o il reso al fornitore."),
 ("CONAI e RAEE","Calcolo automatico dei contributi ambientali, esenzioni per i clienti che ne hanno diritto, liste e dati per le dichiarazioni periodiche."),
]) + TORNA % ("mago4.html","Mago4")

# ---------------------------------------------------------------- MAGO MAGAZZINO
mag = """
<h2>Sapere che cosa c'&egrave;, dov'&egrave; e quanto vale</h2>
<p>Le tre domande a cui un magazzino deve saper rispondere in qualsiasi momento. Quando la risposta
richiede un giro fisico tra gli scaffali, il costo si scarica su consegne, inventari e capitale
immobilizzato.</p>
""" + grid([
 ("Magazzino","Anagrafica articoli con codice a barre e codice parlante, unit&agrave; di misura multiple, kit assortiti, movimenti fiscali e fisici, pi&ugrave; depositi con valore e disponibilit&agrave; sempre noti, rettifiche inventariali."),
 ("Lotti e Matricole","Tracciabilit&agrave; dell'articolo per tutta la sua vita in azienda: numerazione dei lotti del fornitore o autonumerazione, prelievo per lotto o per data di scadenza, matricole interne ed esterne sul ciclo attivo e passivo."),
 ("WMS","Ricevimento, stoccaggio e movimentazione con mappatura configurabile del magazzino, missioni di magazzino, strategie e priorit&agrave; di stoccaggio per l'ubicazione ottimale, picking e packing fino al DDT, inventari periodici e continui."),
 ("WMS Mobile","Le stesse operazioni dal terminale: carico e scarico, trasferimenti, packing e inventario con la lettura del barcode. Funziona anche senza copertura Wi-Fi, salvando i dati sul terminale e allineandoli al rientro."),
 ("Barcode Manager","Lettori in emulazione tastiera per identificare i codici a barre su qualsiasi documento &mdash; ordini, acquisti, vendite, documenti WMS &mdash; riducendo la digitazione e gli errori che ne derivano."),
]) + TORNA % ("mago4.html","Mago4")

# ---------------------------------------------------------------- MAGO PRODUZIONE
prod = """
<h2>Dalla distinta base alla pianificazione della capacit&agrave;</h2>
<p>L'area produzione di Mago4 cresce con l'azienda: si parte dalla distinta base e dalla produzione
base, si arriva alla pianificazione dei fabbisogni e della capacit&agrave; produttiva quando i volumi
e le commesse lo richiedono.</p>
""" + grid([
 ("Distinta Base","Componenti e operazioni del prodotto, collegate a risorse e cicli di lavorazione. Navigazione grafica, esplosione e implosione, archivio dei disegni di progettazione, costificazione per materiali, lavorazioni e costi accessori."),
 ("Varianti","Articoli simili gestiti su una sola distinta che raggruppa le parti comuni: si specifica che cosa aggiungere, togliere o modificare rispetto al prototipo, con costificazione e vendita in variante."),
 ("Configuratore","Alternative di composizione del prodotto fattibili dal punto di vista produttivo e convenienti da quello economico. Lavora anche dai documenti di vendita, con varianti ai listini e generazione dei prezzi."),
 ("Produzione Base","Per la piccola e media impresa manifatturiera o chimica: piano di produzione, ordine di produzione, gestione scorte, avanzamento e costificazione preventiva e consuntiva."),
 ("Produzione Avanzata","Per le imprese di media dimensione, con funzionalit&agrave; pi&ugrave; estese sulla gestione degli ordini e dei cicli."),
 ("Ordini Aperti","Gestione delle forniture ricorrenti concordate a monte e rilasciate nel tempo."),
 ("Manufacturing Mobile","Le dichiarazioni di reparto raccolte direttamente sul dispositivo, senza passaggi su carta."),
 ("MRP &mdash; Material Requirements Planning","Pianificazione dei fabbisogni a partire da produzione in corso, situazione di magazzino, ordini cliente e fornitore e politiche di gestione degli articoli."),
 ("CRP &mdash; Capacity Requirements Planning","Verifica della capacit&agrave; produttiva disponibile rispetto al piano: dove si formano i colli di bottiglia prima che si formino davvero."),
]) + """
<div class="tpBox">
  <p><b>Il pezzo che aggiungiamo noi.</b> La pianificazione vale quanto valgono i dati di consuntivo.
    <b>EasyTime</b> ed <b>EasyInd</b>, sviluppati da Technology Partners Italia, raccolgono tempi,
    fermi e scarti direttamente dalle macchine e dai reparti, e li riportano nel gestionale.
    <a href="fabbrica50.html">Come funzionano &rarr;</a></p>
</div>
""" + TORNA % ("mago4.html","Mago4")

# ---------------------------------------------------------------- AHI
ahi_amm = """
<h2>Amministrazione e finanza</h2>
<p>Ad Hoc Infinity gestisce l'area economica e finanziaria in regime ordinario o semplificato,
con supporto multivaluta per chi lavora con l'estero.</p>
<ul>
  <li><b>Fatturazione elettronica automatizzata</b>, senza passaggi manuali tra gestionale e servizio di invio.</li>
  <li><b>Adempimenti fiscali</b>: modelli 730, Unico, IVA e Intrastat prodotti dai dati gi&agrave; in contabilit&agrave;.</li>
  <li><b>Monitoraggio finanziario in tempo reale</b> attraverso gli strumenti di reporting della piattaforma:
    la situazione di cassa non &egrave; una fotografia di fine mese.</li>
</ul>
""" + TORNA % ("ahi.html","Ad Hoc Infinity")

ahi_ven = """
<h2>Vendite e acquisti</h2>
<p>I documenti del ciclo attivo e di quello passivo sono collegati fra loro, con <b>travaso automatico
dei dati</b> da un documento all'altro: l'offerta diventa ordine, l'ordine diventa consegna e fattura
senza reinserimenti.</p>
<ul>
  <li><b>Listini e sconti commerciali</b> gestiti per cliente, articolo e condizione.</li>
  <li><b>Confronto dei preventivi fornitori</b>, per scegliere sui numeri e non sull'abitudine.</li>
  <li><b>Pianificazione degli approvvigionamenti</b> a partire dall'analisi dei fabbisogni.</li>
</ul>
""" + TORNA % ("ahi.html","Ad Hoc Infinity")

ahi_log = """
<h2>Magazzino e logistica</h2>
<ul>
  <li><b>Magazzino Ciclo Attivo e Passivo</b>: gestione delle giacenze con ubicazioni e articoli a varianti.</li>
  <li><b>Logistica Avanzata</b>: dall'evasione dell'ordine alla spedizione, con documento di trasporto e fatturazione.</li>
  <li><b>Distinta Base</b>: movimentazione automatica dei materiali collegata alla struttura del prodotto.</li>
</ul>
<p>&Egrave; l'area in cui si vedono per prime le inefficienze: errori di prelievo, inventari che non
tornano, spedizioni incomplete. Ed &egrave; anche quella dove il ritorno di un intervento si misura
pi&ugrave; facilmente.</p>
""" + TORNA % ("ahi.html","Ad Hoc Infinity")

ahi_ges = """
<h2>Controllo di gestione</h2>
<p>La parte che interessa direttamente la direzione: <b>cruscotti e report configurabili</b> sugli
indicatori di performance, costruiti sui dati che le altre aree producono ogni giorno.</p>
<ul>
  <li><b>Budget</b> e confronto con il consuntivo.</li>
  <li><b>Analisi degli scostamenti</b>: non solo quanto si &egrave; discostato, ma dove.</li>
  <li><b>Analisi di redditivit&agrave;</b> per prodotto, cliente, commessa.</li>
  <li><b>Analisi di scenario</b> con impiego di intelligenza artificiale e machine learning.</li>
</ul>
<p>Il valore sta nell'integrazione: i dati arrivano da contabilit&agrave;, vendite, magazzino e produzione
senza estrazioni manuali, quindi il cruscotto &egrave; aggiornato quando serve guardarlo.</p>
""" + TORNA % ("ahi.html","Ad Hoc Infinity")

def P(slug, title, desc, crumb_txt, kick, h1, lead, body, ctah, ctap, fonte, marchio=None):
    return dict(slug=slug, title=title, desc=desc,
        crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; '+crumb_txt,
        kick=kick, h1=h1, lead=lead, body=body, ctah=ctah, ctap=ctap, fonte=fonte, marchio=marchio)

PAGES = [
 P("magoamministrativa.html","Mago4 area amministrativa: contabilità, bilanci, cespiti | Technology Partners Italia",
   "I moduli amministrativi di Mago4: contabilità generale, previsionale e analitica, ammortamenti, bilancio consolidato, XBRL, Basilea 2, gestione banche SEPA e adempimenti.",
   '<a href="mago4.html">Mago4</a> &rsaquo; Area amministrativa',"Mago4 &middot; Area amministrativa",
   "Mago4: l'area amministrativa, modulo per modulo",
   "Contabilit&agrave; generale, previsionale e analitica, cespiti, bilanci e adempimenti: gli strumenti che tengono in ordine i conti e quelli che dicono alla direzione come sta andando.",
   amm,"Quali moduli vi servono davvero?",
   "L'area amministrativa si attiva a pezzi. Guardiamo insieme che cosa oggi fate fuori dal gestionale: di solito &egrave; l&igrave; che si nasconde il tempo perso.", FM, "mago4.png"),
 P("magovenditeacquisti.html","Mago4 vendite e acquisti: ordini, listini, fidi, provvigioni | Technology Partners Italia",
   "I moduli commerciali di Mago4: ordini da clienti e a fornitori, listini e sconti, gestione fidi con controllo dell'esposizione, provvigioni agenti, acquisti, controllo qualità, CONAI e RAEE.",
   '<a href="mago4.html">Mago4</a> &rsaquo; Vendite e acquisti',"Mago4 &middot; Vendite e acquisti",
   "Mago4: il ciclo commerciale, modulo per modulo",
   "Offerte e ordini con disponibilit&agrave; e data di consegna calcolate, fido sotto controllo, provvigioni gestite, acquisti verificati alla ricezione.",
   va,"Quanto tempo passa tra la richiesta e l'offerta?",
   "&Egrave; l'indicatore che pi&ugrave; spesso si muove per primo. Se oggi servono giorni, il margine di miglioramento &egrave; immediato.", FM, "mago4.png"),
 P("magomagazzino.html","Mago4 magazzino e logistica: WMS, lotti, barcode | Technology Partners Italia",
   "I moduli di magazzino di Mago4: gestione articoli e depositi, lotti e matricole, WMS con ubicazioni e missioni, WMS Mobile da terminale, Barcode Manager.",
   '<a href="mago4.html">Mago4</a> &rsaquo; Magazzino e logistica',"Mago4 &middot; Magazzino e logistica",
   "Mago4: il magazzino, modulo per modulo",
   "Articoli, depositi, lotti e matricole, gestione per ubicazioni, picking e packing fino al documento di trasporto, e le stesse operazioni dal terminale in corsia.",
   mag,"Il vostro inventario torna?",
   "Se la risposta richiede una settimana di conteggi, il problema non &egrave; il magazzino: &egrave; come vengono registrati i movimenti.", FM, "mago4.png"),
 P("magoproduzione.html","Mago4 produzione: distinta base, MRP, CRP, configuratore | Technology Partners Italia",
   "I moduli di produzione di Mago4: distinta base e varianti, configuratore, produzione base e avanzata, ordini aperti, Manufacturing Mobile, pianificazione MRP e CRP.",
   '<a href="mago4.html">Mago4</a> &rsaquo; Produzione',"Mago4 &middot; Produzione",
   "Mago4: la produzione, modulo per modulo",
   "Dalla distinta base alla pianificazione dei fabbisogni e della capacit&agrave;, con i dati di reparto che tornano nel gestionale invece di restare sui fogli di produzione.",
   prod,"La pianificazione regge il confronto con il consuntivo?",
   "Se i tempi reali non rientrano nel sistema, il piano resta una previsione senza verifica. &Egrave; il punto da cui partiamo di solito.", FM, "mago4.png"),
 P("ahiamministrazione.html","Ad Hoc Infinity: amministrazione e finanza | Technology Partners Italia",
   "Ad Hoc Infinity area amministrativa: gestione economica e finanziaria in regime ordinario o semplificato, multivaluta, fatturazione elettronica automatizzata, adempimenti e monitoraggio finanziario in tempo reale.",
   '<a href="ahi.html">Ad Hoc Infinity</a> &rsaquo; Amministrazione',"Ad Hoc Infinity &middot; Amministrazione",
   "Ad Hoc Infinity: amministrazione e finanza",
   "Regime ordinario o semplificato, multivaluta, fatturazione elettronica automatizzata e situazione finanziaria aggiornata in tempo reale.",
   ahi_amm,"Vediamolo sui vostri numeri",
   "Un'area amministrativa si valuta sui vostri adempimenti e sulle vostre scadenze, non su una demo standard.", FA, "ahi_logo.png"),
 P("ahivendite.html","Ad Hoc Infinity: vendite e acquisti | Technology Partners Italia",
   "Ad Hoc Infinity ciclo commerciale: documenti collegati con travaso automatico dei dati, listini e sconti, confronto preventivi fornitori, pianificazione degli approvvigionamenti.",
   '<a href="ahi.html">Ad Hoc Infinity</a> &rsaquo; Vendite e acquisti',"Ad Hoc Infinity &middot; Vendite e acquisti",
   "Ad Hoc Infinity: vendite e acquisti",
   "Documenti collegati fra loro con travaso automatico dei dati, listini e sconti, preventivi fornitori messi a confronto, approvvigionamenti pianificati sui fabbisogni.",
   ahi_ven,"Quante volte lo stesso dato viene riscritto?",
   "Ogni reinserimento &egrave; tempo e un'occasione di errore. Contarli &egrave; il modo pi&ugrave; rapido per capire quanto vale l'integrazione.", FA, "ahi_logo.png"),
 P("ahilogistica.html","Ad Hoc Infinity: magazzino e logistica | Technology Partners Italia",
   "Ad Hoc Infinity logistica: magazzino ciclo attivo e passivo con ubicazioni e articoli a varianti, Logistica Avanzata dall'evasione ordini alla spedizione, distinta base per la movimentazione automatica.",
   '<a href="ahi.html">Ad Hoc Infinity</a> &rsaquo; Magazzino e logistica',"Ad Hoc Infinity &middot; Magazzino e logistica",
   "Ad Hoc Infinity: magazzino e logistica",
   "Giacenze per ubicazione, articoli a varianti, evasione ordini fino a documento di trasporto e fattura, movimentazione automatica collegata alla distinta base.",
   ahi_log,"Dove si perdono i vostri ordini?",
   "Tra il magazzino e la spedizione ci sono i passaggi in cui si generano la maggior parte dei reclami. Guardiamo quelli per primi.", FA, "ahi_logo.png"),
 P("ahigestione.html","Ad Hoc Infinity: controllo di gestione | Technology Partners Italia",
   "Ad Hoc Infinity controllo di gestione: cruscotti e report configurabili, budget, analisi degli scostamenti e della redditività, analisi di scenario con intelligenza artificiale e machine learning.",
   '<a href="ahi.html">Ad Hoc Infinity</a> &rsaquo; Controllo di gestione',"Ad Hoc Infinity &middot; Controllo di gestione",
   "Ad Hoc Infinity: controllo di gestione",
   "Cruscotti sugli indicatori, budget e scostamenti, redditivit&agrave; per prodotto e cliente, analisi di scenario con intelligenza artificiale e machine learning.",
   ahi_ges,"Quali indicatori guardate ogni mese?",
   "Se per averli serve una settimana di estrazioni, arrivano quando le decisioni sono gi&agrave; state prese.", FA, "ahi_logo.png"),
]

for p in PAGES:
    open(os.path.join(OUT, p["slug"]), "w", encoding="utf-8").write(pagina(**p))
    print(p["slug"], "ok")
