# -*- coding: utf-8 -*-
"""Schede prodotto Zucchetti — lotto 2: DMS, HR e presenze, Digital Hub, InfoBusiness, ZTravel."""
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
<p>Il software &egrave; di Zucchetti; il progetto &egrave; nostro. Siamo <b>Top Partner ERP Zucchetti</b>:
analisi, configurazione, collegamento con il gestionale che gi&agrave; usate, formazione e assistenza
restano in capo a noi, con un referente che conosce la vostra azienda.%s</p>
"""

# ------------------------------------------------------------------ DMS
dms = """
<h2>Il problema non &egrave; archiviare: &egrave; ritrovare</h2>
<p>Ogni azienda archivia. Poche riescono a ritrovare in trenta secondi il contratto firmato tre anni fa,
la bolla che il cliente contesta, la revisione del disegno che era in produzione a marzo. Il costo non
si vede in bilancio, ma si paga tutti i giorni in ore di ricerca e in decisioni prese senza il documento
davanti.</p>
<p>Infinity DMS &egrave; il sistema documentale di Zucchetti: digitalizza, archivia, condivide e
soprattutto <b>fa ritrovare</b> i documenti di qualsiasi natura.</p>

<h2>Che cosa fa</h2>
<div class="tpGrid">
  <div><h4>Acquisizione e classificazione</h4>
    <p>Importazione, protocollazione e classificazione di documenti di qualsiasi formato, cartacei o
      gi&agrave; digitali.</p></div>
  <div><h4>Ricerca avanzata</h4>
    <p>Motore di ricerca su titolo, data, tipo, <b>contenuto</b>, parole chiave, etichette e altri
      criteri: si cerca per quello che il documento dice, non per dove &egrave; stato messo.</p></div>
  <div><h4>Distribuzione</h4>
    <p>I documenti si assegnano a utenti o gruppi e arrivano sulla loro scrivania virtuale,
      con notifiche via e-mail o SMS e liste di distribuzione automatiche.</p></div>
  <div><h4>Flussi di lavoro</h4>
    <p>Percorsi di approvazione automatizzati: chi deve vedere che cosa, in che ordine,
      con quale scadenza.</p></div>
  <div><h4>Archiviazione sicura</h4>
    <p>I documenti cartacei diventano file digitali conservati in modo ordinato, in cloud o
      sui vostri sistemi.</p></div>
  <div><h4>Integrazione</h4>
    <p>Si collega ai gestionali Zucchetti e anche a software di terze parti, comunicando
      direttamente con il sistema che genera i documenti amministrativi.</p></div>
</div>
""" + RUOLO % (" Il valore di un documentale si misura sul primo mese di uso reale: "
               "per questo la classificazione la disegniamo sui vostri documenti, non su un modello standard.")

# ------------------------------------------------------------------ HR / PRESENZE
hr = """
<h2>Le presenze, senza software da installare nelle filiali</h2>
<p>Il software presenze di Zucchetti gestisce presenze e assenze <b>via web</b>, in autonomia,
senza dover installare nulla nelle singole sedi. Il sistema calcola automaticamente ore teoriche,
ore lavorate, ordinario, <b>straordinari</b>, maggiorazioni e indennit&agrave; di turno: quello che
oggi in molte aziende viene ricontato a mano ogni mese.</p>

<h2>L'app che toglie lavoro all'ufficio del personale</h2>
<p>Con l'app HR Infinity il dipendente ha accesso ai propri documenti 24 ore su 24 &mdash;
cedolino, cartellino, CU &mdash; legge le comunicazioni aziendali, verifica le anomalie del proprio
cartellino, inserisce i giustificativi di assenza, consulta il piano ferie e chiede le ferie.</p>
<p>Il modulo <b>Workflow HR</b> chiude il cerchio: permessi, malattie, cartellini e richieste di ferie
partono dall'app del dipendente e arrivano al responsabile, che li vede in tempo reale e approva o
respinge. Nessun modulo cartaceo, nessuna e-mail da rincorrere, e una traccia di chi ha approvato
che cosa.</p>

<h2>Le aree della suite HR</h2>
<div class="tpGrid">
  <div><h4>HCM</h4><p>Gestione del percorso della persona in azienda.</p></div>
  <div><h4>Time &amp; Payroll</h4><p>Presenze e paghe.</p></div>
  <div><h4>Welfare</h4><p>Benefit e servizi al dipendente.</p></div>
  <div><h4>HR Mobility</h4><p>Trasferte e note spese.<a href="ztravel.html">Scheda ZTravel &rarr;</a></p></div>
  <div><h4>HR Cost &amp; Planning</h4><p>Organizzazione delle squadre e dei turni.</p></div>
  <div><h4>Safety &amp; Security</h4><p>Sicurezza delle persone e degli ambienti.</p></div>
  <div><h4>Workspace</h4><p>Gestione degli spazi e delle postazioni.</p></div>
</div>
<p>Sotto c'&egrave; una base tecnica che conta pi&ugrave; di quanto sembri: <b>database unico</b>,
strumenti di analisi, sistema di workflow e gestione della relazione con il dipendente. &Egrave; ci&ograve;
che permette di non reinserire gli stessi dati in tre posti diversi.</p>
""" + RUOLO % (" La rilevazione presenze tocca terminali, badge, orari e contratti: "
               "la parte hardware e la configurazione degli orari sono la met&agrave; del lavoro, e le facciamo noi.")

# ------------------------------------------------------------------ DIGITAL HUB
fepasos = """
<h2>Un solo passaggio per fattura, firma e conservazione</h2>
<p>Digital Hub &egrave; il servizio online di Zucchetti che tiene insieme l'intero processo della
fatturazione elettronica: <b>emissione e ricezione</b> delle fatture, <b>trasmissione allo SdI</b>,
<b>firma elettronica</b> e <b>conservazione digitale a norma</b>. Non tre fornitori e tre passaggi
manuali: un unico flusso.</p>

<h2>La conservazione, che &egrave; la parte che si dimentica</h2>
<p>Tutti i documenti che passano da Digital Hub vengono conservati digitalmente per <b>dieci anni</b>,
secondo la normativa vigente. Conservare a norma non significa fare una copia: significa mantenere
nel tempo <b>immodificabilit&agrave;, autenticit&agrave;, reperibilit&agrave;, valore legale, sicurezza,
leggibilit&agrave; e integrit&agrave;</b> del documento. &Egrave; la differenza tra avere un file e avere
una prova.</p>
<div class="tpBox">
  <p><b>Perch&eacute; conta per la direzione.</b> Una verifica fiscale o una contestazione arrivano anni
    dopo, quando il gestionale &egrave; cambiato e chi seguiva la pratica magari non c'&egrave; pi&ugrave;.
    In quel momento vale solo quello che si riesce a esibire.</p>
</div>

<h2>Non solo fatture</h2>
<p>Digital Hub &egrave; integrato nativamente con i gestionali per aziende, professionisti, associazioni
di categoria e con le altre applicazioni del gruppo Zucchetti che emettono fatture. Gestisce anche
altri documenti elettronici, tra cui gli <b>ordini NSO</b> e i documenti che viaggiano sulla
<b>rete PEPPOL</b>.</p>
""" + RUOLO % ""

# ------------------------------------------------------------------ INFOBUSINESS
ib = """
<h2>Analisi fatte da chi le deve usare</h2>
<p>Il limite di quasi tutti i progetti di reportistica &egrave; che ogni domanda nuova richiede qualcuno
che scriva una query. InfoBusiness nasce per togliere quel passaggio: si analizzano le informazioni e
si costruiscono estrazioni <b>senza codice e senza conoscere la struttura dei dati</b>.</p>
<p>&Egrave; uno strumento pensato per chi guida l'azienda, non per l'ufficio informatico:
Zucchetti lo propone da vent'anni a imprenditori e responsabili di funzione.</p>

<h2>Come si lavora</h2>
<ul>
  <li><b>Cruscotti dinamici</b> costruiti in modo rapido, con visualizzazioni da condividere con
    il proprio gruppo di lavoro.</li>
  <li><b>Parametri, filtri e drill-down</b> applicabili direttamente su grafici e tabelle:
    si parte dal totale e si scende fino al documento che lo genera.</li>
  <li><b>Dati da qualsiasi fonte strutturata</b>: gestionale, CRM, HR, applicazioni su database
    e file Excel.</li>
  <li><b>Versione web</b>, per avere le analisi aggiornate ovunque ci si trovi.</li>
</ul>

<h2>Modelli di analisi gi&agrave; pronti</h2>
<p>Non si parte dal foglio bianco: sono disponibili modelli su ciclo attivo e passivo,
contabilit&agrave;, magazzino, rate e scadenze, punti vendita, opportunit&agrave; commerciali,
ticket di assistenza e progetti. Si attivano e si adattano, invece di costruirli da zero.</p>
""" + RUOLO % (" La business intelligence non fallisce sui grafici: fallisce quando i dati di partenza "
               "non sono affidabili. La prima cosa che guardiamo &egrave; quella.")

# ------------------------------------------------------------------ ZTRAVEL
ztravel = """
<h2>La nota spese &egrave; un processo, non un foglio</h2>
<p>Tra chi autorizza la trasferta, chi prenota, chi conserva gli scontrini, chi controlla e chi
contabilizza, una singola trasferta attraversa quattro o cinque persone. ZTravel governa l'intero
percorso: <b>autorizzazione, organizzazione del viaggio, servizi al trasfertista, gestione
amministrativa delle spese e analisi dei costi</b>.</p>

<h2>Le funzioni che tolgono davvero lavoro</h2>
<div class="tpGrid">
  <div><h4>Foto invece di scontrini</h4>
    <p>La spesa si registra allegando la fotografia del giustificativo scattata con il telefono.</p></div>
  <div><h4>Riconoscimento automatico</h4>
    <p>Con l'OCR basta fotografare lo scontrino: importo, data, valuta e partita IVA vengono
      riconosciuti e compilati in automatico.</p></div>
  <div><h4>Prenotazione nelle regole</h4>
    <p>Integrazione con self-booking tool per acquistare i titoli di viaggio nel rispetto della
      travel policy aziendale.</p></div>
  <div><h4>Anticipi</h4>
    <p>Richiesta e gestione degli anticipi per cassa, bonifico o ricarica di carte prepagate.</p></div>
  <div><h4>Flussi di pagamento</h4>
    <p>Registrazione e gestione automatica dei movimenti da carta di credito, Telepass, fuel card,
      agenzie e fornitori.</p></div>
  <div><h4>Fatture riconciliate</h4>
    <p>Riconciliazione automatica dei flussi di fatturazione elettronica delle spese di trasferta,
      con associazione della fattura al dipendente giusto.</p></div>
</div>
<p>I giustificativi cartacei vengono <b>conservati digitalmente</b>: il processo diventa
completamente senza carta, comprese le verifiche successive.</p>

<h2>Per le PMI: ZTravel Smart</h2>
<p>Per chi vuole passare al digitale senza un progetto lungo, Zucchetti propone <b>ZTravel Smart</b>:
soluzione cloud per la nota spese, operativa subito, senza implementazioni complesse.</p>
""" + RUOLO % ""

PAGES = [
 dict(slug="dms.html",
  title="Infinity DMS, la gestione documentale Zucchetti | Technology Partners Italia",
  desc="Infinity DMS: digitalizzazione, protocollazione e classificazione dei documenti, ricerca sul contenuto, distribuzione con notifiche e flussi approvativi. Integrato con i gestionali Zucchetti e di terze parti.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; Gestione documentale',
  kick="Gestione documentale &middot; Zucchetti",
  h1="Infinity DMS: ritrovare un documento in trenta secondi",
  lead="Digitalizzazione, classificazione, ricerca sul contenuto e flussi di approvazione. Il sistema documentale Zucchetti, collegato al gestionale che gi&agrave; usate.",
  body=dms, ctah="Quante ore al mese cercate documenti?",
  ctap="&Egrave; la domanda da cui partiamo: di solito la risposta sorprende, e rende il conto economico dell'intervento molto semplice.",
  fonte=F("https://www.zucchetti.it/it/cms/soluzioni/gestione-documentale/gestione-e-archiviazione-infinity-dms/gestione-archiviazione-documentale-funzionalita.html","Infinity DMS")),
 dict(slug="hr.html",
  title="Presenze e gestione del personale con HR Infinity | Technology Partners Italia",
  desc="HR Infinity Zucchetti: presenze e assenze via web, calcolo automatico di straordinari e maggiorazioni, app per cedolino, cartellino e ferie, Workflow HR per le approvazioni.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; Persone e presenze',
  kick="Gestione del personale &middot; Zucchetti",
  h1="Presenze, ferie e cedolini senza carta che gira",
  lead="Presenze e assenze via web, straordinari e maggiorazioni calcolati dal sistema, richieste che partono dall'app del dipendente e arrivano al responsabile.",
  body=hr, ctah="Quanto tempo costa oggi la chiusura del mese?",
  ctap="Se l'ufficio del personale passa giorni a rincorrere cartellini e giustificativi, il recupero &egrave; immediato e misurabile.",
  fonte=F("https://www.zucchetti.it/it/cms/soluzioni/software-hr-zucchetti/software-gestione-presenze","HR Infinity e alla gestione presenze")),
 dict(slug="fepasos.html",
  title="Fatturazione elettronica e conservazione a norma con Digital Hub | Technology Partners Italia",
  desc="Digital Hub Zucchetti: emissione e ricezione fatture elettroniche, trasmissione allo SdI, firma elettronica e conservazione digitale a norma per dieci anni. Ordini NSO e rete PEPPOL.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; Fatturazione elettronica',
  kick="Obblighi normativi &middot; Zucchetti",
  h1="Fattura, firma e conservazione in un flusso solo",
  lead="Digital Hub gestisce emissione, ricezione, trasmissione allo SdI, firma e conservazione a norma. Dieci anni di conservazione per tutto ci&ograve; che passa dal servizio.",
  body=fepasos, ctah="La vostra conservazione regge una verifica?",
  ctap="&Egrave; una domanda che conviene farsi prima del controllo, non durante. La verifica &egrave; breve e dice subito se ci sono buchi.",
  fonte=F("https://www.zucchetti.it/it/cms/soluzioni/obblighi-normativi/fatturazione-elettronica/digital-hub/fatturazione-elettronica-aziende-descrizione.html","Digital Hub")),
 dict(slug="infobusiness.html",
  title="InfoBusiness, la business intelligence Zucchetti | Technology Partners Italia",
  desc="InfoBusiness: cruscotti dinamici senza codice, drill-down su grafici e tabelle, dati da ERP, CRM, HR, database ed Excel, modelli di analisi già pronti su ciclo attivo, magazzino, scadenze e ticket.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; Business Intelligence',
  kick="Analisi e controllo &middot; Zucchetti",
  h1="InfoBusiness: le domande le fa chi deve decidere",
  lead="Cruscotti e analisi costruiti senza scrivere codice e senza conoscere la struttura dei dati, con drill-down fino al singolo documento.",
  body=ib, ctah="Quali tre numeri vi servono ogni luned&igrave;?",
  ctap="Si parte da quelli. Se oggi arrivano tardi o non arrivano affatto, l'analisi ha gi&agrave; un motivo concreto per esistere.",
  fonte=F("https://www.zucchetti.it/it/cms/soluzioni/business-intelligence-analytics/software/infobusiness/software-business-intelligence-funzionalita.html","InfoBusiness")),
 dict(slug="ztravel.html",
  title="ZTravel, trasferte e note spese Zucchetti | Technology Partners Italia",
  desc="ZTravel: autorizzazione trasferte, self-booking nella travel policy, anticipi, foto dei giustificativi con riconoscimento OCR, riconciliazione delle fatture elettroniche e conservazione digitale.",
  crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; Trasferte e note spese',
  kick="Trasferte e note spese &middot; Zucchetti",
  h1="ZTravel: la nota spese si chiude con una fotografia",
  lead="Autorizzazione, prenotazione nel rispetto della travel policy, giustificativi fotografati e letti in automatico, fatture riconciliate e conservazione digitale.",
  body=ztravel, ctah="Quante note spese passano dalle vostre mani ogni mese?",
  ctap="Il ritorno qui si calcola con una moltiplicazione semplice: numero di note spese per i minuti che ciascuna costa oggi, tra chi la compila e chi la controlla.",
  fonte=F("https://www.zucchetti.it/it/cms/soluzioni/software-hr-zucchetti/hr-mobility/trasferte-note-spese/ztravel/software-trasferte-note-spese-funzionalita.html","ZTravel")),
]

for p in PAGES:
    html = pagina(**p)
    open(os.path.join(OUT, p["slug"]), "w", encoding="utf-8").write(html)
    print(p["slug"], len(html), "byte")
