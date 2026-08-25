import os
OUT="/home/user/DoveW/sito"

HEAD = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://www.tp-italia.com/{slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://www.tp-italia.com/{slug}">
<meta property="og:locale" content="it_IT">
<link rel="icon" href="img/marchio-tp.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&family=Source+Sans+3:wght@400;600&display=swap">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>

<header class="top">
  <div class="wrap">
    <a class="brandlock" href="index.html" aria-label="Technology Partners Italia, home"><img src="img/marchio-tp.png" alt=""><span><b>Technology Partners</b><i>Italia</i></span></a>
    <button class="burger" id="burger" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Principale">
      <a href="ai.html"{a1}>AI nativa</a>
      <a href="esg.html"{a2}>ESG</a>
      <a href="finanza-agevolata.html"{a3}>Finanza agevolata</a>
      <a href="index.html#soluzioni">Soluzioni</a>
      <a href="azienda.html">Azienda</a>
      <a href="modulo.html" class="btn btn-primary">Parliamone</a>
    </nav>
  </div>
</header>

<div class="phead">
  <div class="wrap">
    <p class="crumb"><a href="index.html">Home</a> &rsaquo; Aree d'impatto &rsaquo; {crumb}</p>
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</div>
"""

FOOT = """
<div class="cta">
  <div class="wrap">
    <h2>{ctah}</h2>
    <p>{ctap}</p>
    <div class="row">
      <a href="modulo.html" class="btn btn-primary">Richiedi il confronto</a>
      <a class="tel" href="tel:+390362163629">+39 0362 1636293</a>
      <a class="tel" href="mailto:commerciale@tp-italia.com">commerciale@tp-italia.com</a>
    </div>
  </div>
</div>

<footer>
  <div class="wrap">
    <div class="cols">
      <div>
        <h4>Technology Partners Italia</h4>
        <p>Via Vincenzo Monti, 74<br>20832 Desio (MB)<br>Tel +39 0362 1636293<br>
          <a href="mailto:commerciale@tp-italia.com">commerciale@tp-italia.com</a></p>
      </div>
      <div>
        <h4>Aree d'impatto</h4>
        <a href="ai.html">AI nativa</a>
        <a href="esg.html">Sostenibilit&agrave; ESG</a>
        <a href="finanza-agevolata.html">Finanza agevolata 5.0</a>
      </div>
      <div>
        <h4>Soluzioni</h4>
        <a href="gestionalix.html">Sistema gestionale ERP</a>
        <a href="crm.html">CRM e portali</a>
        <a href="easytime.html">Fabbrica connessa</a>
        <a href="wapp.html">Logistica di magazzino</a>
        <a href="sistemi.html">Continuit&agrave; e sicurezza</a>
      </div>
      <div>
        <h4>Azienda</h4>
        <a href="azienda.html">Chi siamo</a>
        <a href="newsnew.html">News</a>
        <a href="lavoraconnoi.html">Lavora con noi</a>
        <a href="indicazioni.html">Dove siamo</a>
        <a href="modulo.html">Contatti</a>
      </div>
    </div>
    <div class="legal">
      <span>Technology Partners Italia S.r.l. &middot; P.IVA e C.F. 05660080960</span>
      <span><a href="https://www.privacylab.it/informativa.php?13064379882" style="display:inline">Informativa privacy</a></span>
    </div>
  </div>
</footer>

<script>
document.getElementById('burger').addEventListener('click', function(){{
  var n = document.getElementById('nav');
  var open = n.classList.toggle('open');
  this.setAttribute('aria-expanded', open ? 'true' : 'false');
}});
</script>
</body>
</html>
"""

def faq(items):
    out=['<section class="alt"><div class="wrap"><div class="sec-head"><p class="eyebrow">Domande ricorrenti</p>'
         '<h2>Quello che ci chiedono prima di iniziare</h2></div><div class="faq">']
    for q,a in items:
        out.append(f"<details><summary>{q}</summary><p>{a}</p></details>")
    out.append("</div></div></section>")
    return "\n".join(out)

# ---------------------------------------------------------------- AI
ai_body = """
<section>
  <div class="wrap two">
    <div class="prose">
      <p class="lead">Quasi tutte le aziende hanno gi&agrave; i dati che servirebbero per prevedere.
        Sono negli ordini, nei consumi delle macchine, nello storico degli incassi, nei ticket di assistenza.
        Il problema non &egrave; raccoglierli: &egrave; che nessuno li guarda in tempo per decidere diversamente.</p>
      <p>L'automazione predittiva serve a questo e a nient'altro: portare un'informazione sul tavolo
        quando la decisione &egrave; ancora possibile. Un fornitore che sta scivolando sui tempi va saputo
        prima che fermi la linea. Un cliente che riduce la frequenza d'ordine va saputo prima che smetta.
        Una macchina che sta degradando va saputa prima del guasto, non dopo.</p>
      <h2>&laquo;Nativa&raquo; significa dentro i processi che gi&agrave; usate</h2>
      <p>La differenza rispetto a un progetto di intelligenza artificiale tradizionale &egrave; tutta qui.
        Non si costruisce un data lake, non si assume un data scientist, non si aspettano diciotto mesi:
        le funzioni predittive vivono dentro il gestionale, il MES e il CRM che governano gi&agrave;
        l'operativit&agrave;, e producono un avviso dove la persona sta gi&agrave; lavorando.</p>
      <p>&Egrave; anche la ragione per cui funziona: un modello che gira su dati sporchi o parziali
        produce previsioni che nessuno crede. Prima si sistema il flusso informativo, poi si predice.
        Il primo pezzo di lavoro &egrave; quasi sempre il pi&ugrave; noioso, ed &egrave; quello che decide il risultato.</p>
    </div>
    <div>
      <div class="note">
        <p><b>Il criterio che usiamo.</b> Una funzione predittiva entra in progetto solo se
          risponde a tre domande: quale decisione cambia, chi la prende, con quanto anticipo.
          Se una delle tre resta senza risposta, non la mettiamo in campo &mdash; per quanto sia
          tecnicamente affascinante.</p>
      </div>
      <div class="facts" style="margin-top:26px">
        <div class="fact"><b>Domanda</b><span>previsione di vendita e riordino: meno rotture di stock,
          meno capitale immobilizzato a magazzino</span></div>
        <div class="fact"><b>Fabbrica</b><span>degrado macchina e colli di bottiglia riconosciuti
          dai dati raccolti in reparto</span></div>
        <div class="fact"><b>Credito</b><span>scoring dei comportamenti di pagamento: si interviene
          sull'insoluto prima che diventi tale</span></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Dove interviene per prima</p>
      <h2>Quattro punti in cui l'anticipo si trasforma subito in margine</h2>
    </div>
    <div class="cards">
      <article class="card">
        <h3>Pianificazione della domanda</h3>
        <p>Lo storico degli ordini, la stagionalit&agrave; e il portafoglio aperto producono una previsione
          per articolo. Serve a decidere che cosa riordinare e in che quantit&agrave;: meno mancanti sui
          codici che vendono, meno giacenza morta su quelli che non vendono.</p>
      </article>
      <article class="card">
        <h3>Manutenzione predittiva</h3>
        <p>Contatori, tempi ciclo e allarmi raccolti dalle macchine interconnesse mostrano il degrado
          prima del fermo. La manutenzione si programma in finestra utile invece di subirla nel
          momento peggiore.</p>
      </article>
      <article class="card">
        <h3>Qualit&agrave; e scarti</h3>
        <p>Gli scarti dichiarati in reparto, incrociati con lotto, macchina e operatore, fanno emergere
          la combinazione che li genera. &Egrave; il tipo di correlazione che a occhio non si vede
          e che a fine anno pesa in bilancio.</p>
      </article>
      <article class="card">
        <h3>Documenti e anomalie</h3>
        <p>Fatture passive, ordini e bolle letti automaticamente: il sistema segnala ci&ograve; che non torna
          &mdash; prezzo diverso dal contratto, quantit&agrave; non corrispondente, doppio pagamento &mdash;
          invece di farlo scoprire alla chiusura.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Come si verifica</p>
      <h2>Indicatori che concordiamo prima di partire</h2>
      <p class="lead">Sono quelli che finiscono nel business case e che rivediamo insieme a sei e
        dodici mesi. Se non si muovono, il progetto ha un problema e va affrontato.</p>
    </div>
    <ul class="check" style="max-width:74ch">
      <li><b>Giorni di anticipo</b> con cui un problema viene riconosciuto rispetto a oggi.</li>
      <li><b>Rotture di stock</b> sui codici a maggior rotazione, e capitale immobilizzato a magazzino.</li>
      <li><b>Ore di fermo non pianificato</b> e loro incidenza sulla capacit&agrave; produttiva.</li>
      <li><b>Giorni medi di incasso</b> e quota di credito scaduto.</li>
      <li><b>Ore/persona</b> sottratte al controllo manuale dei documenti.</li>
    </ul>
  </div>
</section>
"""

ai_faq = faq([
 ("Serve avere gi&agrave; un gestionale evoluto?",
  "Serve avere dati affidabili, che &egrave; una cosa diversa. L'assessment iniziale verifica proprio questo: "
  "se i dati che gi&agrave; producete sono sufficienti, se vanno prima ripuliti o se manca la rilevazione alla fonte. "
  "In diversi casi il primo intervento utile non &egrave; l'intelligenza artificiale, ma chiudere il buco informativo che la rende impossibile."),
 ("Quanto dura un primo progetto?",
  "Un ambito alla volta, con un rilascio in produzione entro poche settimane. Preferiamo un risultato verificabile su un "
  "processo solo piuttosto che un programma annuale che nessuno riesce a giudicare finch&eacute; non &egrave; finito."),
 ("I nostri dati restano nostri?",
  "S&igrave;. Definiamo in contratto dove risiedono i dati, chi vi accede e per quale finalit&agrave;. "
  "&Egrave; il primo punto che mettiamo per iscritto, prima ancora dell'architettura tecnica."),
 ("Che cosa succede se la previsione sbaglia?",
  "Ogni previsione arriva con il proprio margine d'errore, ed &egrave; questo che la rende utilizzabile: "
  "chi decide sa quanto fidarsi. Un modello che non dichiara la propria incertezza non &egrave; uno strumento di direzione."),
])

# ---------------------------------------------------------------- ESG
esg_body = """
<section>
  <div class="wrap two">
    <div class="prose">
      <p class="lead">La sostenibilit&agrave; ha smesso di essere un capitolo della comunicazione ed &egrave;
        diventata un requisito contrattuale. Le banche la pesano nel rating, i clienti industriali la
        chiedono ai fornitori come condizione di fornitura, le gare la mettono tra i criteri di
        aggiudicazione.</p>
      <p>Il che sposta il problema: non serve un documento ben scritto, serve un dato che regga
        una verifica. E un dato regge una verifica solo se si pu&ograve; risalire a dove &egrave; nato,
        chi l'ha prodotto e con quale misura.</p>
      <h2>La domanda scende lungo la filiera</h2>
      <p>Le imprese soggette a rendicontazione di sostenibilit&agrave; devono dichiarare anche gli impatti
        della propria catena di fornitura. Non potendoli inventare, li chiedono ai fornitori.
        Per una PMI manifatturiera questo significa ricevere questionari sempre pi&ugrave; puntuali &mdash;
        consumi per unit&agrave; prodotta, origine dei materiali, infortuni, formazione &mdash; con tempi di
        risposta stretti.</p>
      <p>Chi risponde con un foglio di calcolo compilato a mano ci mette settimane e resta esposto:
        i numeri non sono ricostruibili. Chi li estrae dai sistemi risponde in giornata e pu&ograve;
        dimostrarli.</p>
      <h2>I dati ESG esistono gi&agrave;, sparsi</h2>
      <p>L'energia &egrave; nei contatori e nei dati macchina raccolti dal MES. I trasporti sono nei documenti
        di consegna. Gli acquisti e la provenienza dei materiali sono nel gestionale. Infortuni, formazione
        e turni sono nella gestione del personale. Il lavoro non &egrave; inventare una nuova raccolta:
        &egrave; collegare quelle che gi&agrave; ci sono e dar loro un'unit&agrave; di misura comune.</p>
    </div>
    <div>
      <div class="note">
        <p><b>Il punto di partenza pratico.</b> Prima si guarda il questionario che il vostro cliente
          pi&ugrave; esigente vi ha gi&agrave; mandato, o il set di indicatori richiesto dalla vostra banca.
          Da l&igrave; si torna indietro fino al sistema che pu&ograve; produrre ogni numero. &Egrave; molto pi&ugrave;
          rapido che partire da un modello teorico di rendicontazione.</p>
      </div>
      <div class="facts" style="margin-top:26px">
        <div class="fact"><b>Ambientale</b><span>energia per unit&agrave; prodotta, rifiuti e scarti,
          consumi di reparto, logistica</span></div>
        <div class="fact"><b>Sociale</b><span>sicurezza sul lavoro, formazione erogata,
          composizione e continuit&agrave; dell'organico</span></div>
        <div class="fact"><b>Governance</b><span>tracciabilit&agrave; delle approvazioni, gestione dei
          fornitori, conservazione a norma dei documenti</span></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Che cosa facciamo</p>
      <h2>Dalla richiesta del cliente al dato che la soddisfa</h2>
    </div>
    <div class="steps">
      <div class="step">
        <b>Fase 01</b><h3>Mappa degli indicatori</h3>
        <p>Quali numeri vi vengono effettivamente chiesti, da chi e con quale frequenza. Nessun
          indicatore entra se nessuno lo domanda.</p>
      </div>
      <div class="step">
        <b>Fase 02</b><h3>Origine del dato</h3>
        <p>Per ciascun indicatore: da quale sistema nasce, chi lo inserisce, dove si perde.
          Qui emergono i buchi da chiudere.</p>
      </div>
      <div class="step">
        <b>Fase 03</b><h3>Raccolta automatica</h3>
        <p>Contatori, macchine, documenti e gestione del personale collegati, cos&igrave; che il dato
          si aggiorni da solo e non dipenda da chi si ricorda di compilarlo.</p>
      </div>
      <div class="step">
        <b>Fase 04</b><h3>Cruscotto e risposta</h3>
        <p>Un pannello per la direzione e l'esportazione nei formati richiesti da clienti,
          banche e stazioni appaltanti.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Il ritorno</p>
      <h2>Perch&eacute; conviene prima ancora dell'obbligo</h2>
    </div>
    <ul class="check" style="max-width:74ch">
      <li><b>Fornitura difesa</b> &mdash; restare nell'albo fornitori di chi sta gi&agrave; chiedendo dati ESG.</li>
      <li><b>Accesso al credito</b> &mdash; un rating di sostenibilit&agrave; documentato incide sulle condizioni.</li>
      <li><b>Consumi che calano</b> &mdash; misurare l'energia per reparto e per lotto fa emergere sprechi
        che nessuno aveva quantificato.</li>
      <li><b>Tempo liberato</b> &mdash; i questionari si compilano in ore invece che in settimane.</li>
      <li><b>Gare</b> &mdash; criteri ambientali soddisfatti con evidenze, non con dichiarazioni.</li>
    </ul>
  </div>
</section>
"""

esg_faq = faq([
 ("Siamo una PMI: la rendicontazione non riguarda le grandi imprese?",
  "L'obbligo diretto s&igrave;, ma l'effetto arriva comunque per via contrattuale. Sono i vostri clienti "
  "soggetti all'obbligo a chiedervi i dati, perch&eacute; devono dichiarare anche gli impatti della filiera. "
  "In pratica il requisito vi raggiunge come richiesta commerciale, spesso prima che come norma."),
 ("Serve un software specifico per l'ESG?",
  "Non &egrave; il primo pezzo. La maggior parte del valore sta nel collegare i sistemi che avete gi&agrave; "
  "e nel dare un'unit&agrave; di misura comune ai dati. Uno strumento dedicato ha senso dopo, quando la raccolta "
  "&egrave; automatica e il volume di richieste lo giustifica."),
 ("Quanto tempo per essere in grado di rispondere a un questionario?",
  "Dipende da quanti indicatori sono gi&agrave; coperti dai sistemi in uso. La mappa iniziale lo dice con "
  "precisione in poche settimane, e di solito il primo blocco di indicatori &mdash; energia e acquisti &mdash; "
  "si automatizza prima degli altri."),
 ("Chi certifica i numeri?",
  "Noi rendiamo il dato tracciabile e ricostruibile: da dove nasce, chi l'ha prodotto, con quale misura. "
  "L'eventuale asseverazione o certificazione resta in capo all'ente o al professionista che la rilascia, "
  "e lavora molto meglio su dati che hanno una fonte verificabile."),
])

# ---------------------------------------------------------------- FINANZA
fin_body = """
<section>
  <div class="wrap two">
    <div class="prose">
      <p class="lead">Le misure che sostengono la digitalizzazione e l'efficienza produttiva hanno
        un tratto in comune: non premiano l'acquisto, premiano il risultato dimostrato.
        Interconnessione, tracciabilit&agrave;, risparmio energetico misurato. Cose che si dimostrano
        con dati prodotti dai sistemi &mdash; o non si dimostrano affatto.</p>
      <p>&Egrave; il motivo per cui una pratica agevolativa si vince o si perde molto prima della domanda:
        si decide quando si sceglie come impostare il progetto, quali dati far produrre agli impianti
        e come conservarli. Un progetto disegnato senza pensarci arriva alla scadenza con le fatture
        in ordine e le evidenze tecniche mancanti.</p>
      <h2>Il nostro ruolo &egrave; tecnico, non burocratico</h2>
      <p>Non ci sostituiamo al vostro commercialista n&eacute; al professionista che firma le perizie:
        lavoriamo accanto a loro. Noi rispondiamo della parte che nessuno dei due pu&ograve; coprire &mdash;
        far s&igrave; che macchine, gestionale e sistema di fabbrica producano davvero, e conservino,
        le evidenze che la misura richiede.</p>
      <p>In concreto: interconnessione reale al sistema gestionale, tracciamento dell'ordine di produzione,
        registrazione dei consumi prima e dopo l'intervento, archiviazione a norma di ci&ograve; che dovr&agrave;
        essere esibito in caso di controllo, anche a distanza di anni.</p>
    </div>
    <div>
      <div class="note">
        <p><b>Una precisazione doverosa.</b> Le misure agevolative cambiano: aliquote, finestre temporali
          e requisiti vengono aggiornati di anno in anno e alcune si esauriscono con le risorse stanziate.
          Per questo non troverete percentuali su questa pagina: verifichiamo caso per caso quali misure
          sono aperte al momento in cui il vostro progetto parte, e su quelle costruiamo il piano.</p>
      </div>
      <div class="facts" style="margin-top:26px">
        <div class="fact"><b>Prima</b><span>verifica di ammissibilit&agrave; e stima della copertura,
          prima di firmare qualsiasi ordine</span></div>
        <div class="fact"><b>Durante</b><span>i sistemi configurati per generare le evidenze
          richieste, non adattati dopo</span></div>
        <div class="fact"><b>Dopo</b><span>conservazione delle prove per l'intero periodo
          in cui possono essere richieste</span></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Come procediamo</p>
      <h2>Dalla verifica al credito riconosciuto</h2>
    </div>
    <div class="cards">
      <article class="card">
        <h3>Verifica di ammissibilit&agrave;</h3>
        <p>Che cosa avete in programma di fare, quali misure lo intercettano, quali requisiti tecnici
          comporta ciascuna. Il risultato &egrave; un s&igrave; o un no motivato, non una promessa.</p>
      </article>
      <article class="card">
        <h3>Progetto che regge i requisiti</h3>
        <p>L'impianto tecnico viene disegnato perch&eacute; i requisiti siano soddisfatti per costruzione:
          interconnessione, tracciabilit&agrave; e misure energetiche nascono dal progetto, non da una
          rincorsa finale.</p>
      </article>
      <article class="card">
        <h3>Evidenze e fascicolo</h3>
        <p>Raccogliamo e ordiniamo la documentazione tecnica che la pratica richiede, nella forma
          in cui va presentata, e la mettiamo a disposizione di chi firma perizie e dichiarazioni.</p>
      </article>
      <article class="card">
        <h3>Tenuta nel tempo</h3>
        <p>Le verifiche possono arrivare anni dopo. Le prove restano conservate a norma e recuperabili,
          insieme allo storico dei dati che le sostengono.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">Su che cosa si applica</p>
      <h2>Gli interventi che pi&ugrave; spesso rientrano</h2>
      <p class="lead">Sono anche quelli su cui lavoriamo tutti i giorni: &egrave; la sovrapposizione
        che rende sensato occuparcene noi.</p>
    </div>
    <ul class="check" style="max-width:74ch">
      <li><b>Interconnessione di macchine e impianti</b> al sistema gestionale, con raccolta dei dati
        di produzione in tempo reale.</li>
      <li><b>Sistemi di fabbrica</b> per tempi, fermi, scarti e qualit&agrave;, e loro integrazione con
        la pianificazione.</li>
      <li><b>Logistica di magazzino</b> con identificazione automatica e tracciabilit&agrave; dei lotti.</li>
      <li><b>Misura dei consumi energetici</b> per reparto, macchina o lotto, con confronto prima/dopo.</li>
      <li><b>Formazione del personale</b> sulle nuove competenze digitali, quando la misura la prevede.</li>
    </ul>
  </div>
</section>
"""

fin_faq = faq([
 ("Vi occupate voi della pratica?",
  "Ci occupiamo della parte tecnica: ammissibilit&agrave;, progettazione dei requisiti, evidenze e documentazione "
  "tecnica. La presentazione e gli adempimenti fiscali restano al vostro commercialista o al consulente "
  "specializzato, con cui lavoriamo in modo coordinato. Se non ne avete uno, vi indichiamo con chi abbiamo gi&agrave; collaborato."),
 ("E se l'agevolazione non viene riconosciuta?",
  "Per questo la verifica di ammissibilit&agrave; viene prima di tutto il resto e ha come esito possibile un no. "
  "Un progetto che regge in s&eacute; deve restare conveniente anche senza incentivo: l'agevolazione migliora il ritorno, "
  "non deve essere ci&ograve; che lo giustifica."),
 ("Possiamo partire adesso o conviene aspettare la prossima misura?",
  "Dipende dalle finestre aperte e dalle risorse ancora disponibili, che verifichiamo al momento. "
  "Aspettare ha un costo: i mesi di inefficienza che continuate a pagare mentre attendete. "
  "Nel confronto iniziale mettiamo a confronto le due ipotesi con i numeri."),
 ("Quali dati dovremo conservare, e per quanto?",
  "Dipende dalla misura, ma il principio &egrave; costante: deve essere possibile ricostruire a distanza di anni "
  "che cosa &egrave; stato installato, come era interconnesso e quali risultati ha prodotto. "
  "Configuriamo la conservazione perch&eacute; questo sia possibile senza dipendere dalla memoria delle persone."),
])

PAGES = [
 dict(slug="ai.html", a1=' aria-current="page"', a2="", a3="",
   title="AI nativa per l'impresa — automazione predittiva dentro i processi | Technology Partners Italia",
   desc="Previsione della domanda, manutenzione predittiva, controllo qualità e anomalie sui documenti: "
        "intelligenza artificiale dentro il gestionale e il MES che già usate, con indicatori di ritorno concordati.",
   crumb="AI nativa", eyebrow="Area d'impatto 01",
   h1="L'automazione predittiva vale solo se cambia una decisione",
   lead="Anticipare un problema di qualche settimana vale pi&ugrave; di qualsiasi cruscotto. "
        "Portiamo le funzioni predittive dentro i sistemi che governano gi&agrave; la vostra operativit&agrave;, "
        "con un indicatore di ritorno concordato prima di partire.",
   body=ai_body, faqs=ai_faq,
   ctah="Quanto anticipo vi manca oggi?",
   ctap="Un'ora con la direzione basta per capire dove l'informazione arriva troppo tardi e quanto costa. "
        "Da l&igrave; si vede subito se l'automazione predittiva ha senso per voi, o se prima va sistemato altro."),
 dict(slug="esg.html", a1="", a2=' aria-current="page"', a3="",
   title="Dati ESG che reggono una verifica — sostenibilità misurata dai sistemi | Technology Partners Italia",
   desc="Energia, filiera, sicurezza e governance: indicatori ESG estratti dai sistemi che già governano "
        "l'operatività, tracciabili e pronti per banche, clienti industriali e gare.",
   crumb="Sostenibilit&agrave; ESG", eyebrow="Area d'impatto 02",
   h1="I dati ESG o nascono dai sistemi, o non reggono una verifica",
   lead="Banche, clienti industriali e stazioni appaltanti hanno smesso di accontentarsi delle dichiarazioni. "
        "Colleghiamo le fonti che gi&agrave; avete &mdash; macchine, gestionale, personale &mdash; per produrre "
        "indicatori ricostruibili, in giornata.",
   body=esg_body, faqs=esg_faq,
   ctah="Quali dati vi stanno gi&agrave; chiedendo?",
   ctap="Portate l'ultimo questionario ricevuto da un cliente o dalla banca. In un incontro vi diciamo "
        "quali indicatori i vostri sistemi possono gi&agrave; produrre e quali no."),
 dict(slug="finanza-agevolata.html", a1="", a2="", a3=' aria-current="page"',
   title="Finanza agevolata e Fabbrica 5.0 — la parte tecnica che decide la pratica | Technology Partners Italia",
   desc="Interconnessione, tracciabilità e misura dei consumi: progettiamo i sistemi perché producano le "
        "evidenze richieste dalle misure agevolative, e le conserviamo per i controlli successivi.",
   crumb="Finanza agevolata &middot; Fabbrica 5.0", eyebrow="Area d'impatto 03",
   h1="Se il progetto &egrave; impostato bene, una parte la finanzia l'incentivo",
   lead="Le misure non premiano l'acquisto: premiano il risultato dimostrato. Impostiamo il progetto "
        "perch&eacute; le evidenze tecniche esistano fin dall'inizio, e restino disponibili quando arriva il controllo.",
   body=fin_body, faqs=fin_faq,
   ctah="Vale la pena verificare prima di firmare.",
   ctap="Se avete un investimento in programma, la verifica di ammissibilit&agrave; si fa adesso: "
        "cambia il modo in cui il progetto va disegnato, e a volte cambia anche la sua convenienza."),
]

for p in PAGES:
    html = HEAD.format(**p) + p["body"] + p["faqs"] + FOOT.format(ctah=p["ctah"], ctap=p["ctap"])
    open(os.path.join(OUT, p["slug"]), "w", encoding="utf-8").write(html)
    print(p["slug"], len(html), "byte")
