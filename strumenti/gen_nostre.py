# -*- coding: utf-8 -*-
"""Le soluzioni di Technology Partners Italia: EasyTime, EasyInd, W.App, iTek4,
Mobile Ticket, identificazione automatica, Opera MES."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tpl_pagina import pagina
OUT = "/home/user/DoveW/sito"

FN = ('Funzionalit&agrave; descritte a partire dalla documentazione delle soluzioni installate presso i nostri '
      'clienti. Le configurazioni variano da impianto a impianto: quelle applicabili al vostro le vediamo insieme.')

# ---------------------------------------------------------------- EASYTIME
easytime = """
<h2>Il problema: i tempi veri li sa solo il reparto</h2>
<p>In produzione i tempi si sanno. Il problema &egrave; che restano in reparto: su un foglio, in testa a
chi sta alla macchina, in un cartellino compilato a fine turno. Quando arrivano in ufficio &mdash; se
arrivano &mdash; sono stime, non misure. E su quelle stime si fanno preventivi, si calcolano costi e
si promettono consegne.</p>
<p><b>EasyTime</b> &egrave; la soluzione MES estesa che abbiamo sviluppato per chiudere quel buco:
coordina le operazioni e raccoglie i tempi <b>in tempo reale</b>, direttamente dai reparti e dalle
macchine interconnesse.</p>

<h2>Come lo vede chi ci lavora</h2>
<p>L'interfaccia &egrave; <b>touch</b>, con pulsanti grandi e colorati, pochi dati da digitare e
percorsi guidati: iniziare un'attivit&agrave;, sospenderla, chiuderla. Il tempo tra una dichiarazione e
l'altra viene calcolato dal sistema, quindi i consuntivi sono veri e consultabili subito, non a fine
mese.</p>
<p>All'operatore il sistema dice <b>che cosa produrre, in quale quantit&agrave;, quando e in quale
sequenza</b>. Gli ordini di produzione arrivano dal gestionale con articolo, lotto, materiale,
dimensioni e quantit&agrave;, e possono essere riordinati in reparto secondo le valutazioni di chi
conosce le macchine. All'avvio si possono imporre <b>controlli obbligatori</b> in stile lista di
verifica: le cose da guardare prima di dare il via.</p>

<h2>Che cosa vede la direzione</h2>
<div class="tpGrid">
  <div><h4>Avanzamento in tempo reale</h4>
    <p>Quali fasi sono in esecuzione, quali sospese, quali finite, per ogni ordine e per ogni linea.</p></div>
  <div><h4>Cruscotti di back office</h4>
    <p>Performance delle linee, dei centri di lavoro e degli operatori, con stato di avanzamento
      e quantit&agrave; prodotte.</p></div>
  <div><h4>Modulo chart</h4>
    <p>Tempo di lavoro per centro di lavoro e per operatore, tempi di ogni fase divisi per giorno.</p></div>
  <div><h4>Sinottico macchine</h4>
    <p>Le macchine in tempo reale con il lavoro in corso, pi&ugrave; i lavori conclusi con operatore
      e quantit&agrave; dichiarata.</p></div>
</div>

<h2>La pista di controllo, prima che i dati entrino in contabilit&agrave;</h2>
<p>Tutte le rilevazioni finiscono in una pista di controllo dove si possono correggere gli errori
prevedibili &mdash; una timbratura mancata, una quantit&agrave; sbagliata. Solo dopo la conferma di un
addetto una procedura schedulata (con frequenza configurabile) le importa nel gestionale, allineando
consuntivazione degli ordini, scarico della materia prima e avanzamento della produzione.</p>
<div class="tpBox">
  <p><b>Perch&eacute; conta.</b> &Egrave; il passaggio che distingue un sistema di raccolta dati da un
    sistema su cui si pu&ograve; chiudere un costo. I dati sbagliati vengono intercettati prima di
    diventare numeri di bilancio.</p>
</div>
<p style="margin-top:22px"><a href="easyind40.html"><b>EasyInd: la parte che parla con le macchine &rarr;</b></a>
&nbsp;&nbsp;<a href="fabbrica50.html"><b>Interconnessione e incentivi &rarr;</b></a></p>
"""

# ---------------------------------------------------------------- EASYIND
easyind = """
<h2>Il dato che nasce dalla macchina, non dal ricordo</h2>
<p><b>EasyInd</b> &egrave; la soluzione extended MES realizzata da Technology Partners Italia:
distribuisce le informazioni per coordinare il personale di fabbrica e raccoglie i dati in tempo reale
dai reparti e dalle <b>macchine interconnesse</b>, secondo il paradigma Industry 4.0.</p>
<p>Sullo schermo l'operatore ha la lista delle macchine disponibili, il lavoro in corso su ciascuna e
gli eventuali allarmi. Selezionando una macchina vede la lavorazione in corso e quelle in coda.</p>

<h2>Le fasi, dichiarate una per una</h2>
<p>Ogni fase ha un inizio e una fine dichiarati: <b>preparazione, attrezzaggio, lavorazione, operazioni
finali</b>. Di ciascuna restano ordine di produzione, quantit&agrave;, scheda tecnica &mdash; visibile
a tutto schermo &mdash; ed eventuali valori di controllo. Il lavoro si pu&ograve; mettere in pausa in
qualsiasi momento scegliendo la causale, con la possibilit&agrave; di annotare.</p>
<p>A fine lavorazione l'operatore chiude confermando o correggendo il numero di pezzi buoni
<b>recuperato dalla macchina</b>, e dichiara pezzi di seconda scelta e scarti.</p>

<h2>Che cosa si porta dietro</h2>
<div class="tpGrid">
  <div><h4>Informazioni macchina</h4>
    <p>Contatore, part-program, tempo ciclo e tempo di fermo salvati e recuperabili in tempo reale.
      Il software si adatta alle diverse tipologie di macchinario.</p></div>
  <div><h4>Scarti e qualit&agrave;</h4>
    <p>Ogni scarto ha causale e note e decrementa il contatore dei pezzi buoni. Il modulo qualit&agrave;
      aggiunge un livello intermedio: i pezzi in sospeso li verifica un addetto, che decide se
      scartarli o rimetterli in produzione.</p></div>
  <div><h4>Etichette di lotto</h4>
    <p>Stampa da EasyLabel su etichette Zebra del lotto in produzione, con progressivo per
      ogni etichetta.</p></div>
  <div><h4>Schede tecniche</h4>
    <p>L'operatore ha davanti la revisione corretta, senza cercare il raccoglitore.</p></div>
  <div><h4>Controllo per il superutente</h4>
    <p>Lavorazioni in diretta e chiuse con ordine, contatore e data, storico degli allarmi macchina,
      visione degli scarti, gestione degli utenti.</p></div>
  <div><h4>Integrazioni gi&agrave; fatte</h4>
    <p>Gestionale Mago, <b>DMG Mori Messenger</b> e <b>Fanuc</b>. Applicazione web responsive,
      utilizzabile su piattaforme diverse.</p></div>
</div>
<div class="tpBox">
  <p><b>E gli incentivi.</b> Interconnessione al gestionale, tracciabilit&agrave; del lotto e dati di
    produzione conservati sono anche i requisiti tecnici su cui si gioca l'accesso alle misure
    agevolative. <a href="fabbrica50.html">Come funziona &rarr;</a></p>
</div>
"""

# ---------------------------------------------------------------- W.APP
wapp = """
<h2>Un magazzino che risponde alle tre domande</h2>
<p>Che cosa c'&egrave;, dov'&egrave;, quanto vale. <b>W.App</b> &egrave; la nostra soluzione WMS
(Warehouse Management System): gestisce merce in entrata e in uscita, ubicazioni, movimentazioni
interne, inventari e supporto alla produzione, ed &egrave; <b>nativamente integrata</b> con i terminali
Android e con il gestionale Mago.net/Mago4 &mdash; oltre che integrabile con gli ERP pi&ugrave; diffusi.</p>
<p>Funziona <b>anche senza rete</b>: quando la copertura manca il terminale continua a lavorare e i
dati si allineano al rientro. In un magazzino vero &egrave; una differenza sostanziale.</p>

<h2>I moduli</h2>
<div class="tpGrid">
  <div><h4>Ingresso merci</h4>
    <p>Dal terminale si identifica l'ordine a fornitore o di conto lavoro e si vedono le righe.
      Ogni articolo si conta e si carica da barcode; se manca, si stampa l'etichetta. Alla conferma,
      parziale o totale, il sistema genera la bolla di carico e chiude gli ordini.</p></div>
  <div><h4>Ubicazioni</h4>
    <p>Posizionamento, prelievo, trasferimento e ricerca per ubicazione leggendo il barcode dell'unit&agrave;
      di carico e dell'ubicazione. Il terminale <b>suggerisce dove mettere o dove trovare</b> la merce,
      in base alla topologia del magazzino, alle statistiche dei movimenti o alle preferenze impostate.
      Gestisce limiti di peso e volume e caratteristiche come temperatura o categoria merce.</p></div>
  <div><h4>Uscita merci</h4>
    <p>Preparazione da ordine cliente, lista di prelievo o documento di trasporto, con controllo delle
      quantit&agrave;, suggerimento delle ubicazioni da cui prelevare e <b>missione di prelievo
      ottimizzata</b>. In chiusura genera il documento di trasporto, ed eventualmente la fattura,
      e chiude l'ordine.</p></div>
  <div><h4>Produzione</h4>
    <p>Scarico dei componenti e carico del prodotto finito sugli ordini di produzione aperti, compresi
      gli articoli non a distinta (viti, colla, materiali di consumo). Scarti e avanzi vengono tracciati
      con causale; con il modulo di produzione esterna si controlla anche il conto lavoro.</p></div>
  <div><h4>Inventario</h4>
    <p>Normale o a campione, con o senza ubicazione, alla cieca o con raffronto, con report di confronto
      tra quantit&agrave; contate e quantit&agrave; a gestionale.</p></div>
  <div><h4>Stampanti industriali</h4>
    <p>Modulo dedicato per la stampa di etichette articolo, scatola o pallet nel momento in cui servono.</p></div>
</div>
<p style="margin-top:22px"><a href="rfid.html"><b>Barcode o RFID? &rarr;</b></a></p>
"""

# ---------------------------------------------------------------- ITEK4
itek4 = """
<h2>Per chi noleggia, installa e fa manutenzione</h2>
<p><b>iTek4</b> &egrave; una suite di applicazioni per processi ben precisi: noleggio, manutenzione,
assistenza tecnica. &Egrave; <b>integrata con l'ERP Mago</b> lungo tutta la catena &mdash; dall'offerta
di noleggio o di manutenzione fino alla fatturazione elettronica, alla contabilit&agrave; e alla
finanza &mdash; compresa la contrattualistica attiva e passiva, con fatturazione a canone o a intervento.</p>

<h2>Il tecnico non scrive pi&ugrave; rapportini</h2>
<p>Tutto quello che finiva su un rapportino di carta o su una lista di controllo sta dentro un'app:
il documento esce <b>firmato elettronicamente</b> con firma grafometrica e gli interventi da fatturare
passano direttamente a Mago. All'app il tecnico chiede anche quello che gli serve per lavorare,
a partire dallo <b>storico della macchina</b>.</p>

<h2>Il commerciale vede tutto in tempo reale</h2>
<p>Chi vende accede al planning delle macchine disponibili a noleggio o in conto vendita, inserisce
contratti e offerte, e consulta la situazione del cliente sui dati registrati in Mago: esposizione del
credito, macchine, interventi, contratti, preventivi, appuntamenti e trattative, fatture.</p>
<p>Il cliente, dal canto suo, ha un'<b>area riservata</b> da cui scarica i PDF di interventi, contratti,
fatture e schede macchina, e da cui apre un ticket di richiesta intervento.</p>

<h2>Il noleggio, senza contestazioni</h2>
<p>L'app Android per il noleggio consente di <b>fotografare la macchina in uscita e al rientro</b> con
la lista di controllo: la documentazione resta allegata al contratto di noleggio sull'ERP, e chi riceve
la macchina pu&ograve; confrontarla con le foto di partenza anche a distanza di mesi.</p>
<p>Al rientro si registrano gli addebiti aggiuntivi &mdash; chilometri, carburante, danni, altri
addebiti, anche calcolati automaticamente per differenza tra le letture dei contatori &mdash; e
li si ritrova nel sistema di fatturazione.</p>
<div class="tpBox">
  <p><b>Dove si recupera il margine.</b> Nel noleggio i costi che non vengono fatturati sono quasi
    sempre quelli che nessuno riesce a dimostrare. Una fotografia con data e un contatore letto
    dalla macchina chiudono la discussione prima che cominci.</p>
</div>
<p style="margin-top:22px"><a href="mobileticketnew.html"><b>Mobile Ticket: la gestione dei ticket di assistenza &rarr;</b></a></p>
"""

# ---------------------------------------------------------------- MO.TI.
moti = """
<h2>Governare le chiamate, invece di rincorrerle</h2>
<p><b>Mobile Ticket</b> &egrave; l'applicazione per il ticketing, il post-vendita e l'assistenza al
cliente. &Egrave; <b>web based</b>: la usa il personale interno per la parte organizzativa e
amministrativa, e la usa il personale in trasferta per documentare quello che ha fatto, da notebook,
tablet o smartphone, con un'interfaccia touch semplificata.</p>
<p>Il tecnico accede ai ticket, li prende in carico, li evade ed emette il <b>rapportino di intervento</b>
con foto e parti sostituite o riparate, e lo fa firmare al cliente direttamente sul dispositivo.</p>

<h2>I moduli</h2>
<div class="tpGrid">
  <div><h4>Front office</h4>
    <p>Apertura, assegnazione e chiusura dei ticket segnando ore, articoli sostituiti e foto.
      A fine intervento si fa firmare il report e si genera il PDF con tutti i dati.</p></div>
  <div><h4>Back office</h4>
    <p>Gestione degli aspetti commerciali e amministrativi dei contratti: ogni cliente pu&ograve; avere
      pi&ugrave; commesse o contratti attivi, ciascuno con i suoi accordi (tariffa oraria, spese vive).</p></div>
  <div><h4>Ticket</h4>
    <p>Generati da contratto quadro (per esempio manutenzioni programmate) o su commessa specifica
      &mdash; installazione, riparazione, interventi spot &mdash; e consuntivati sulle attivit&agrave; svolte.</p></div>
  <div><h4>Fatturazione</h4>
    <p>Ore, materiali e chilometri passano al gestionale a ticket chiuso e firmato. Con Mago Service
      si crea la chiamata gi&agrave; compilata da confermare; altrimenti i dati finiscono su una
      fattura da confermare.</p></div>
  <div><h4>Notifiche e-mail</h4>
    <p>A ogni cambio di stato partono le e-mail ai soggetti coinvolti: il tecnico assegnato,
      il suo gruppo di lavoro, il cliente con il rapportino in PDF allegato.</p></div>
  <div><h4>Ruoli</h4>
    <p>Tecnico: prende in carico, chiude, fa firmare. Amministratore: in pi&ugrave; apre, assegna,
      annulla e gestisce contratti, utenti e parametri.</p></div>
  <div><h4>Storico e foto</h4>
    <p>Tutti i ticket restano archiviati e consultabili: &egrave; la storia degli interventi per
      cliente. Foto e documenti raccolti sul campo restano allegati al rapportino.</p></div>
  <div><h4>Registrazione vocale</h4>
    <p>Il tecnico detta i lavori eseguiti invece di scriverli: sul campo &egrave; il modo pi&ugrave;
      rapido per non perdere informazioni.</p></div>
  <div><h4>Sopralluoghi e nuovi clienti</h4>
    <p>Procedura dedicata per raccogliere le informazioni del sopralluogo e formulare il preventivo,
      e maschera rapida per censire un nuovo cliente in pochi secondi.</p></div>
</div>
<p>Gestisce matricole e contratti, ed &egrave; compatibile con <b>Ad Hoc Enterprise, Ad Hoc Revolution,
Ad Hoc Infinity, Mago.net, Mago4 e Passpartout</b>.</p>
"""

# ---------------------------------------------------------------- RFID
rfid = """
<h2>La domanda giusta non &egrave; &laquo;barcode o RFID&raquo;</h2>
<p>&Egrave; &laquo;quante volte al giorno qualcuno deve avere in mano un oggetto per sapere che
esiste&raquo;. Il codice a barre richiede che l'operatore veda l'etichetta, la inquadri e la legga,
uno alla volta. La radiofrequenza legge <b>pi&ugrave; oggetti insieme, senza contatto visivo</b>:
un pallet che passa da un varco, uno scaffale intero, un capo dentro una scatola.</p>
<p>La differenza si paga in etichette e infrastruttura, e si recupera in tempo. Per questo la scelta
non &egrave; ideologica: dipende dai volumi, da come &egrave; fatta la merce e da dove si perdono
davvero le ore.</p>

<h2>Dove l'RFID viene usato</h2>
<ul>
  <li>gestione del magazzino e del punto vendita;</li>
  <li>tracciabilit&agrave; dei prodotti dentro e fuori l'azienda;</li>
  <li>controllo degli accessi di persone e veicoli;</li>
  <li>tutela contro la contraffazione;</li>
  <li>automazione di fasi operative e sicurezza.</li>
</ul>

<h2>Che cosa serve, in pratica</h2>
<p>Un magazzino in radiofrequenza non &egrave; solo un lettore: servono <b>copertura Wi-Fi</b> per
dialogare con il sistema centrale, <b>antenne e reader</b> nei punti di passaggio, <b>stampanti</b>
per i tag e i <b>tag</b> stessi, scelti in base al materiale e all'ambiente. &Egrave; un progetto di
infrastruttura, ed &egrave; anche la ragione per cui va dimensionato prima e non durante.</p>
<div class="tpBox">
  <p><b>Come lo affrontiamo.</b> Prima si misura dove va il tempo oggi &mdash; ricevimento, prelievo,
    inventario &mdash; e su quale operazione la lettura multipla farebbe la differenza. Poi si decide
    la tecnologia. Nella maggior parte dei magazzini la risposta &egrave; mista: barcode dove basta,
    radiofrequenza dove paga.</p>
</div>
<p style="margin-top:22px"><a href="wapp.html"><b>W.App, il nostro WMS &rarr;</b></a></p>
"""

# ---------------------------------------------------------------- OPERA MES
opera = """
<h2>Il MES dell'ecosistema Zucchetti</h2>
<p><b>Opera MES</b> &egrave; la piattaforma Manufacturing Execution System che gestisce, monitora e
ottimizza in tempo reale i processi produttivi. Zucchetti la propone tra le soluzioni che si affiancano
ai gestionali Mago per la fabbrica digitale.</p>

<h2>Che cosa fa</h2>
<div class="tpGrid">
  <div><h4>Monitoraggio in tempo reale</h4>
    <p>Stato della produzione sotto controllo momento per momento, per intervenire sui problemi
      quando si presentano e non a consuntivo.</p></div>
  <div><h4>Ottimizzazione</h4>
    <p>Strumenti di pianificazione e controllo per l'uso delle risorse e il flusso di lavoro.</p></div>
  <div><h4>Qualit&agrave;</h4>
    <p>Controllo qualit&agrave; integrato nelle operazioni: difetti e anomalie emergono durante
      la produzione.</p></div>
  <div><h4>Tracciabilit&agrave;</h4>
    <p>Ogni fase tracciata e documentata, a supporto della conformit&agrave; e dei controlli.</p></div>
  <div><h4>Integrazione</h4>
    <p>Si collega ai sistemi aziendali gi&agrave; in uso, ERP compresi, per una gestione centralizzata
      dei dati.</p></div>
</div>

<h2>Opera MES o EasyTime?</h2>
<p>Dipende da che cosa serve davvero. <b>Opera MES</b> &egrave; una piattaforma di prodotto, ampia e
strutturata. <b>EasyTime</b> ed <b>EasyInd</b> li abbiamo scritti noi: sono pi&ugrave; leggeri, si
adattano ai processi invece di chiedere che i processi si adattino, e li modifichiamo direttamente
quando la vostra fabbrica cambia.</p>
<p>La scelta si fa guardando i vostri reparti, il tipo di macchine e quanto &egrave; standard il ciclo
produttivo. &Egrave; una delle poche decisioni in cui essere partner di entrambe le strade &egrave;
un vantaggio per voi, perch&eacute; non abbiamo un'unica risposta da vendere.</p>
<p style="margin-top:22px"><a href="easytime.html"><b>EasyTime &rarr;</b></a>
&nbsp;&nbsp;<a href="easyind40.html"><b>EasyInd &rarr;</b></a></p>
"""

def P(slug, title, desc, crumb_txt, kick, h1, lead, body, ctah, ctap, fonte=FN, marchio=None):
    return dict(slug=slug, title=title, desc=desc,
        crumb='<a href="index.html">Home</a> &rsaquo; <a href="prodottinew.html">Prodotti</a> &rsaquo; '+crumb_txt,
        kick=kick, h1=h1, lead=lead, body=body, ctah=ctah, ctap=ctap, fonte=fonte, marchio=marchio)

PAGES=[
 P("easytime.html","EasyTime, il MES esteso per i tempi di produzione | Technology Partners Italia",
   "EasyTime: raccolta dei tempi di produzione in tempo reale dai reparti e dalle macchine interconnesse, interfaccia touch per l'operatore, cruscotti e consuntivazione automatica nel gestionale Mago.",
   "EasyTime","Soluzione sviluppata da noi &middot; MES esteso",
   "EasyTime: i tempi di produzione, misurati mentre accadono",
   "La soluzione MES estesa che abbiamo sviluppato per coordinare i reparti e raccogliere tempi, fasi e quantit&agrave; in tempo reale, portandoli nel gestionale senza ricopiature.",
   easytime,"I vostri preventivi si basano su tempi misurati o stimati?",
   "&Egrave; la domanda che apre quasi tutti i progetti di reparto. Se la risposta &egrave; &laquo;stimati&raquo;, il margine reale per commessa oggi non lo conosce nessuno."),
 P("easyind40.html","EasyInd, MES per macchine interconnesse e Industria 4.0 | Technology Partners Italia",
   "EasyInd: extended MES sviluppato da Technology Partners Italia. Fasi dichiarate, dati macchina in tempo reale, scarti e qualità, etichette di lotto EasyLabel su Zebra, integrazioni DMG Mori Messenger e Fanuc.",
   "EasyInd","Soluzione sviluppata da noi &middot; Industry 4.0",
   "EasyInd: la fabbrica che scrive da sola quello che ha fatto",
   "Extended MES realizzato da Technology Partners Italia: coordina il personale di fabbrica e raccoglie i dati direttamente dalle macchine interconnesse.",
   easyind,"Le vostre macchine sono davvero interconnesse?",
   "Molti impianti sono collegati sulla carta ma non producono dati utilizzabili. La verifica &egrave; rapida e dice subito a che punto siete."),
 P("wapp.html","W.App, il WMS per la gestione del magazzino | Technology Partners Italia",
   "W.App: WMS integrato nativamente con Mago4 e con i terminali Android. Ingresso merci, ubicazioni con suggerimento, prelievo ottimizzato, produzione, inventari e stampa etichette. Funziona anche offline.",
   "W.App &mdash; WMS","Soluzione sviluppata da noi &middot; Magazzino",
   "W.App: il magazzino sa dove sta ogni cosa",
   "La nostra soluzione WMS: merce in entrata e in uscita, ubicazioni, movimentazioni interne, inventari e supporto alla produzione. Integrata con Mago4 e con i terminali Android, funziona anche senza copertura di rete.",
   wapp,"Quanto durano oggi i vostri inventari?",
   "Se servono giorni di fermo, il conto &egrave; presto fatto. E l'inventario &egrave; solo la parte visibile: il resto si perde in prelievi sbagliati e ricerche."),
 P("itek4.html","iTek4: noleggio, manutenzione e assistenza integrati con Mago | Technology Partners Italia",
   "iTek4: planning del noleggio, contratti a canone o a intervento, rapportino digitale con firma grafometrica, area riservata al cliente, foto di uscita e rientro macchina, addebiti automatici dai contatori.",
   "iTek4","Suite verticale &middot; Noleggio e assistenza",
   "iTek4: dal contratto di noleggio alla fattura, senza carta in mezzo",
   "Suite di applicazioni per noleggio, manutenzione e assistenza tecnica, integrata con l'ERP Mago dall'offerta fino alla fatturazione elettronica.",
   itek4,"Quanti addebiti non arrivano in fattura?",
   "Carburante, chilometri, danni: nel noleggio &egrave; l&igrave; che si perde margine, e quasi sempre perch&eacute; manca la prova, non la regola."),
 P("mobileticketnew.html","Mobile Ticket: assistenza, ticket e rapportini digitali | Technology Partners Italia",
   "Mobile Ticket: apertura e presa in carico dei ticket, rapportino con foto e firma del cliente sul dispositivo, contratti e matricole, notifiche e-mail, registrazione vocale e passaggio automatico dei dati al gestionale.",
   "Mobile Ticket","Soluzione per l'assistenza &middot; Ticketing",
   "Mobile Ticket: l'intervento si chiude sul posto, firmato",
   "Applicazione web per ticketing, post-vendita e assistenza: il tecnico documenta l'intervento dal dispositivo, il cliente firma, i dati passano al gestionale per la fatturazione.",
   moti,"Quanto tempo passa tra l'intervento e la fattura?",
   "Se sono settimane, il problema non &egrave; l'amministrazione: &egrave; il rapportino di carta che deve tornare in sede."),
 P("rfid.html","Identificazione automatica: barcode o RFID? | Technology Partners Italia",
   "Quando conviene la radiofrequenza e quando basta il codice a barre: usi tipici dell'RFID, infrastruttura necessaria (Wi-Fi, antenne, reader, stampanti, tag) e criteri di scelta per il magazzino.",
   "Identificazione automatica","Tecnologia &middot; Magazzino e tracciabilit&agrave;",
   "Barcode o RFID: si decide sui numeri, non sulla tecnologia",
   "La radiofrequenza legge pi&ugrave; oggetti insieme e senza contatto visivo. Costa di pi&ugrave; in etichette e infrastruttura, e va scelta dove quel tempo risparmiato si paga davvero.",
   rfid,"Dove si perde il tempo nel vostro magazzino?",
   "Ricevimento, prelievo o inventario: la risposta decide la tecnologia, non il contrario."),
 P("operames.html","Opera MES, la piattaforma Zucchetti per la fabbrica | Technology Partners Italia",
   "Opera MES: monitoraggio della produzione in tempo reale, ottimizzazione delle risorse, controllo qualità integrato e tracciabilità completa. Confronto con EasyTime ed EasyInd, sviluppati da Technology Partners Italia.",
   "Opera MES","Fabbrica digitale &middot; Zucchetti",
   "Opera MES: la piattaforma MES dell'ecosistema Zucchetti",
   "Monitoraggio in tempo reale, ottimizzazione delle risorse, qualit&agrave; e tracciabilit&agrave;, con integrazione ai sistemi aziendali gi&agrave; in uso.",
   opera,"Piattaforma di prodotto o soluzione su misura?",
   "&Egrave; la scelta vera dietro un progetto MES. Guardiamo i vostri reparti e vi diciamo quale delle due strade conviene, senza averne una sola da vendere.",
   fonte='Opera MES &egrave; una soluzione dell\'ecosistema Zucchetti, indicata tra le integrazioni dei gestionali Mago sulle pagine ufficiali '
         '(<a href="https://www.zucchetti.it/it/cms/soluzioni/software-gestionali/tecnologia/gestionali-in-cloud/magocloud/software-gestionale-cloud-descrizione.html" rel="nofollow">zucchetti.it</a>). '
         'Ultima verifica: agosto 2026. EasyTime ed EasyInd sono soluzioni sviluppate da Technology Partners Italia S.r.l.'),
]

for p in PAGES:
    open(os.path.join(OUT, p["slug"]), "w", encoding="utf-8").write(pagina(**p))
    print(p["slug"], "ok")
