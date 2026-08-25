import os
OUT="/home/user/DoveW/sito"

STYLE = """<style>
body{margin:0;background:#fff;color:#333;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.6}
a{color:#0000A0}
.tpw{max-width:1120px;margin:0 auto;padding:0 20px}
.tpTop{border-bottom:1px solid #D6D5D7;background:#fff}
.tpTop .tpw{display:flex;align-items:center;gap:26px;padding-top:12px;padding-bottom:12px;flex-wrap:wrap}
.tpTop img{height:52px;width:auto}
.tpNav{margin-left:auto;display:flex;gap:20px;flex-wrap:wrap}
.tpNav a{color:#000080;text-decoration:none;font-weight:bold;font-size:14.5px}
.tpNav a:hover{color:#0000A0;text-decoration:underline}
.tpNav a.on{border-bottom:2px solid #000080}
.tpHero{background:#000080;color:#fff;padding:34px 0 30px}
.tpHero .kick{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:#9fc0ea;margin:0 0 8px}
.tpHero h1{margin:0;font-size:31px;line-height:1.18;font-weight:bold;max-width:20ch}
.tpHero p{margin:14px 0 0;font-size:16.5px;line-height:1.55;color:#dfe8f6;max-width:74ch}
.tpHero .crumb{font-size:13px;color:#9fc0ea;margin:0 0 14px}
.tpHero .crumb a{color:#9fc0ea}
main{padding:38px 0 10px}
main h2{color:#000080;font-size:23px;margin:34px 0 12px;line-height:1.25}
main h2:first-child{margin-top:0}
main h3{color:#000080;font-size:17px;margin:22px 0 8px}
main p{margin:0 0 14px;max-width:82ch}
main ul{margin:0 0 16px;padding-left:22px;max-width:82ch}
main li{margin-bottom:8px}
.tpBox{background:#F4F6FA;border-left:4px solid #000080;padding:16px 20px;margin:22px 0;max-width:82ch}
.tpBox b{color:#000080}
.tpGrid{display:flex;gap:16px;flex-wrap:wrap;margin:18px 0 8px}
.tpGrid div{flex:1 1 228px;background:#fff;border:1px solid #D6D5D7;border-top:3px solid #000080;
  border-radius:5px;padding:16px 18px}
.tpGrid h4{margin:0 0 7px;color:#000080;font-size:15.5px}
.tpGrid p{margin:0;font-size:14px;line-height:1.5;color:#444}
.tpFonte{font-size:13px;color:#777;margin:26px 0 0;max-width:82ch}
.tpCta{background:#F4F6FA;border-top:1px solid #D6D5D7;margin-top:34px;padding:28px 0}
.tpCta h2{margin:0 0 8px;color:#000080;font-size:21px}
.tpCta p{margin:0 0 14px;max-width:70ch}
.tpCta a.btn{display:inline-block;background:#000080;color:#fff;text-decoration:none;font-weight:bold;
  padding:11px 20px;border-radius:5px;font-size:14.5px}
.tpCta a.btn:hover{background:#0000A0}
.tpCta .rec{margin-left:16px;font-size:14.5px;color:#000080;font-weight:bold;text-decoration:none}
.tpFoot{background:#000080;color:#c9d8ef;padding:26px 0 22px;margin-top:0;font-size:13.5px}
.tpFoot .loghi{display:flex;flex-wrap:wrap;align-items:center;gap:26px;margin-bottom:20px}
.tpFoot .loghi img{height:34px;width:auto}
.tpFoot .righe{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;
  border-top:1px solid rgba(255,255,255,.2);padding-top:16px}
.tpFoot a{color:#c9d8ef}
@media (max-width:760px){.tpHero h1{font-size:24px}.tpNav{gap:14px}.tpTop .tpw{gap:14px}}
</style>"""

def page(slug, on, title, desc, crumb, kick, h1, lead, body, ctah, ctap, fonte):
    nav = []
    for s2,l in [("ai.html","AI nativa"),("esg.html","Sostenibilit&agrave; ESG"),
                 ("fabbrica50.html","Fabbrica 5.0"),("index.html","Home"),
                 ("prodottinew.html","Prodotti"),("azienda.html","Azienda"),("modulo.html","Contatti")]:
        cls = ' class="on"' if s2 == on else ''
        nav.append('<a href="%s"%s>%s</a>' % (s2, cls, l))
    loghi = ["topartner_erp_bn.png","m4platinumpabn.png","silver_cloud_micorsoft_1.png","vmw__1.png",
             "hpbusiness.png","ruckus_bn.png","trendmicro_bn.png","zebra_bn.png","honeywell.png",
             "fortinet_logo_bn2.png","azurebn.png"]
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://www.tp-italia.com/{slug}">
<link rel="icon" href="rc_images/custom.ico">
{STYLE}
</head>
<body>

<div class="tpTop"><div class="tpw">
  <a href="index.html"><img src="rc_images/newlogoquadro300x300.png" alt="Technology Partners Italia"></a>
  <nav class="tpNav">{''.join(nav)}</nav>
</div></div>

<div class="tpHero"><div class="tpw">
  <p class="crumb"><a href="index.html">Home</a> &rsaquo; Aree d'impatto &rsaquo; {crumb}</p>
  <p class="kick">{kick}</p>
  <h1>{h1}</h1>
  <p>{lead}</p>
</div></div>

<main><div class="tpw">
{body}
<p class="tpFonte">{fonte}</p>
</div></main>

<div class="tpCta"><div class="tpw">
  <h2>{ctah}</h2>
  <p>{ctap}</p>
  <a class="btn" href="modulo.html">Richiedi informazioni</a>
  <a class="rec" href="tel:+390362163629">+39 0362 1636293</a>
  <a class="rec" href="mailto:commerciale@tp-italia.com">commerciale@tp-italia.com</a>
</div></div>

<div class="tpFoot"><div class="tpw">
  <div class="loghi">{''.join(f'<img src="rc_images/{g}" alt="">' for g in loghi)}</div>
  <div class="righe">
    <span>Technology Partners Italia S.r.l. &middot; Via Vincenzo Monti, 74 &middot; 20832 Desio (MB)
      &middot; Tel +39 0362 1636293 &middot; <a href="mailto:commerciale@tp-italia.com">commerciale@tp-italia.com</a></span>
    <span>P.IVA e C.F. 05660080960 &middot;
      <a href="https://www.privacylab.it/informativa.php?13064379882">Informativa privacy</a></span>
  </div>
</div></div>

</body>
</html>
"""

# ---------------------------------------------------------------- AI
ai_body = """
<h2>L'intelligenza artificiale arriva con il gestionale, non come progetto a parte</h2>
<p>&Egrave; la differenza che conta per un'impresa che non ha un reparto dati: le funzioni di intelligenza
artificiale sono gi&agrave; dentro le soluzioni Zucchetti, e si attivano sui processi che state gi&agrave;
usando. Zucchetti lo dice cos&igrave;: <em>&laquo;l'Intelligenza Artificiale non &egrave; pi&ugrave; una tecnologia
del futuro: &egrave; uno strumento concreto che oggi supporta aziende, studi professionali e
associazioni&raquo;</em>.</p>
<p>Le funzioni si muovono su tre direzioni: <b>assistere</b> chi lavora nelle decisioni quotidiane,
<b>arricchire</b> i dati che l'azienda gi&agrave; produce, <b>automatizzare</b> le attivit&agrave; ripetitive
che oggi occupano tempo di persone qualificate.</p>

<h2>Dove &egrave; gi&agrave; operativa</h2>
<div class="tpGrid">
  <div>
    <h4>Personale e selezione</h4>
    <p>Pubblicazione degli annunci e screening dei curricula, previsione del fabbisogno di personale,
      interpretazione delle norme contrattuali, controllo delle anomalie e pianificazione delle attivit&agrave;.</p>
  </div>
  <div>
    <h4>Gestionale ed ERP</h4>
    <p>Algoritmi predittivi applicati ai processi aziendali e automazione delle attivit&agrave; a basso
      valore aggiunto, integrati nell'operativit&agrave; quotidiana del gestionale.</p>
  </div>
  <div>
    <h4>Amministrazione e contabilit&agrave;</h4>
    <p>Contabilizzazione assistita delle fatture, acquisizione automatica dei dati dall'Agenzia delle
      Entrate, riconciliazione bancaria.</p>
  </div>
</div>
<p>Dietro queste funzioni c'&egrave; l'<b>AI Factory</b> di Zucchetti, il centro interno che riunisce
i data scientist dedicati ai progetti di intelligenza artificiale.</p>

<h2>Che cosa facciamo noi</h2>
<p>Le funzioni predittive hanno bisogno di dati affidabili per produrre risultati credibili: un modello
che gira su dati incompleti d&agrave; risposte che nessuno usa. Il nostro lavoro sta esattamente l&igrave;
&mdash; nel far s&igrave; che i dati arrivino completi al sistema che li deve leggere: rilevazione alla fonte
in reparto, anagrafiche in ordine, processi che non saltano passaggi.</p>
<div class="tpBox">
  <p><b>Da verificare sul vostro impianto.</b> Quali funzioni di intelligenza artificiale siano
    effettivamente disponibili dipende dai moduli e dalle versioni che avete in uso. &Egrave; la prima
    cosa che guardiamo insieme, prima di qualsiasi proposta.</p>
</div>
"""

# ---------------------------------------------------------------- ESG
esg_body = """
<h2>La richiesta arriva dai clienti e dalle banche, prima che dalla norma</h2>
<p>Le imprese tenute alla rendicontazione di sostenibilit&agrave; devono dichiarare anche gli impatti della
propria catena di fornitura. Non potendoli inventare, li chiedono ai fornitori. Per una PMI
manifatturiera questo significa ricevere questionari con richieste sempre pi&ugrave; puntuali &mdash;
consumi, materiali, sicurezza, formazione &mdash; e tempi di risposta stretti.</p>
<p>Chi risponde compilando a mano un foglio di calcolo ci mette settimane e resta scoperto: quei numeri
non sono ricostruibili. Chi li estrae dai sistemi risponde in giornata e pu&ograve; dimostrarli.</p>

<h2>Le piattaforme Zucchetti, una per dimensione d'impresa</h2>
<div class="tpGrid">
  <div>
    <h4>Sostenibile.go</h4>
    <p>Per microimprese e PMI che muovono i primi passi: percorso guidato fino al report di
      sostenibilit&agrave; allineato allo standard VSME.</p>
  </div>
  <div>
    <h4>Sostenibile.cloud</h4>
    <p>Per PMI e studi professionali: piattaforma per la gestione della sostenibilit&agrave; aziendale
      e la rendicontazione.</p>
  </div>
  <div>
    <h4>ESG Zucchetti</h4>
    <p>Per le grandi aziende: gestione completa del processo che porta al bilancio di
      sostenibilit&agrave;, con controllo delle iniziative e degli indicatori.</p>
  </div>
  <div>
    <h4>ESG Datastore</h4>
    <p>Per PMI e grandi aziende: raccoglie in un unico punto i dati ESG che i software gi&agrave; in uso
      producono, e li organizza secondo i criteri ambientali, sociali e di governance.</p>
  </div>
</div>

<h2>Il nostro ruolo, detto con chiarezza</h2>
<p>Non facciamo consulenza di sostenibilit&agrave; e non redigiamo bilanci: quel lavoro resta al
professionista o alla societ&agrave; che ve lo segue. Noi ci occupiamo della parte che conosciamo &mdash;
i sistemi che producono i dati &mdash; e che &egrave; anche quella da cui dipende la tenuta di tutto il resto:
i consumi rilevati dalle macchine in reparto, gli acquisti e i materiali nel gestionale, la
tracciabilit&agrave; dei lotti in magazzino, i documenti conservati a norma.</p>
<div class="tpBox">
  <p><b>Da dove conviene partire.</b> Dall'ultimo questionario che vi ha mandato un cliente, o dal set
    di indicatori che vi chiede la banca. Si guarda quali di quei numeri i vostri sistemi sanno gi&agrave;
    produrre e quali no: &egrave; una verifica breve e dice subito quanto lavoro serve davvero.</p>
</div>
"""

# ---------------------------------------------------------------- FABBRICA 5.0
fab_body = """
<h2>Gli incentivi non premiano l'acquisto: premiano quello che si riesce a dimostrare</h2>
<p>Interconnessione al sistema gestionale, tracciabilit&agrave; della produzione, dati raccolti e
conservati: sono requisiti tecnici, e si soddisfano solo se il progetto nasce gi&agrave; pensato per
soddisfarli. Un impianto messo in funzione senza pensarci arriva alla scadenza con le fatture in
ordine e le evidenze tecniche mancanti.</p>
<p>&Egrave; la parte di cui ci occupiamo da anni, ben prima che si chiamasse 5.0: <b>EasyInd</b> ed
<b>EasyTime</b>, che abbiamo sviluppato noi, nascono proprio per far parlare le macchine con il
gestionale e per lasciare traccia di quello che succede in reparto.</p>

<h2>Che cosa producono, in concreto</h2>
<ul>
  <li><b>Interconnessione reale</b> &mdash; gli ordini di produzione creati nel gestionale arrivano in
    reparto e tornano indietro consuntivati: quantit&agrave;, tempi, work center.</li>
  <li><b>Dati macchina in tempo reale</b> &mdash; contatore, part-program, tempo ciclo e tempo di fermo,
    salvati e recuperabili. Il software si adatta alle diverse tipologie di macchinario, con
    integrazioni gi&agrave; realizzate verso DMG Mori Messenger e Fanuc.</li>
  <li><b>Tracciabilit&agrave; del lotto</b> &mdash; stampa da EasyLabel su etichette Zebra del lotto in
    produzione, con progressivo per ogni etichetta.</li>
  <li><b>Scarti e qualit&agrave;</b> &mdash; ogni scarto dichiarato con la sua causale, con un livello di
    controllo intermedio prima dello scarto definitivo.</li>
  <li><b>Schede tecniche versionate</b> &mdash; l'operatore vede sempre la revisione pi&ugrave; recente, e
    resta traccia di quale revisione era in uso.</li>
  <li><b>Storico consultabile</b> &mdash; lavorazioni, allarmi e scarti restano interrogabili nel tempo,
    con i grafici del modulo chart.</li>
</ul>
<p>Sono le stesse informazioni che servono a dimostrare un requisito di interconnessione e a
ricostruire, anche a distanza di anni, che cosa &egrave; stato installato e come ha funzionato.</p>

<h2>Fin dove arriviamo noi</h2>
<p>Ci occupiamo della parte tecnica: rendere le macchine interconnesse davvero, far s&igrave; che i dati
richiesti vengano prodotti e conservati, e mettere la documentazione tecnica a disposizione di chi
firma perizie e dichiarazioni. La presentazione della pratica e gli adempimenti fiscali restano al
vostro commercialista o al consulente specializzato.</p>
<div class="tpBox">
  <p><b>Perch&eacute; qui non trovate percentuali.</b> Le misure agevolative cambiano: aliquote, finestre
    temporali e requisiti vengono aggiornati e alcune si chiudono con l'esaurirsi delle risorse.
    Quali siano aperte quando il vostro progetto parte va verificato in quel momento, con chi vi segue
    sul piano fiscale. Quello che possiamo garantire noi &egrave; che l'impianto tecnico regga i requisiti.</p>
</div>
"""

PAGES=[
 dict(slug="ai.html", on="ai.html",
  title="AI nativa nei gestionali Zucchetti | Technology Partners Italia",
  desc="Le funzioni di intelligenza artificiale gi&agrave; presenti nelle soluzioni Zucchetti: personale e selezione, gestionale, contabilit&agrave;. Che cosa fanno e che cosa serve perch&eacute; funzionino.",
  crumb="AI nativa", kick="Area d'impatto 01",
  h1="L'intelligenza artificiale &egrave; gi&agrave; dentro i software che usate",
  lead="Non serve un progetto a parte n&eacute; un reparto dati: le funzioni predittive e di automazione arrivano con le soluzioni Zucchetti. Serve per&ograve; che i dati che le alimentano siano completi &mdash; ed &egrave; l&igrave; che lavoriamo noi.",
  body=ai_body,
  ctah="Vediamo che cosa &egrave; gi&agrave; disponibile sul vostro impianto",
  ctap="Prima di qualsiasi proposta guardiamo i moduli e le versioni che avete in uso, e quali funzioni si possono attivare senza cambiare sistema.",
  fonte='Fonte delle informazioni sulle funzioni di intelligenza artificiale: pagine ufficiali Zucchetti (<a href="https://www.zucchetti.it/it/cms/ai-software-zucchetti" rel="nofollow">zucchetti.it &mdash; AI</a>). Ultima verifica: agosto 2026.'),
 dict(slug="esg.html", on="esg.html",
  title="Dati ESG e software di sostenibilit&agrave; Zucchetti | Technology Partners Italia",
  desc="Sostenibile.go, Sostenibile.cloud, ESG Zucchetti ed ESG Datastore: le piattaforme Zucchetti per la rendicontazione, e i sistemi che producono i dati che vi verranno chiesti.",
  crumb="Sostenibilit&agrave; ESG", kick="Area d'impatto 02",
  h1="I dati di sostenibilit&agrave; che vi chiederanno nascono dai sistemi",
  lead="Clienti industriali e banche hanno smesso di accontentarsi delle dichiarazioni. Portiamo le piattaforme ESG di Zucchetti e colleghiamo i dati che i vostri sistemi gi&agrave; producono.",
  body=esg_body,
  ctah="Partiamo dal questionario che avete gi&agrave; ricevuto",
  ctap="Portatelo in un incontro: si vede subito quali indicatori i vostri sistemi sanno gi&agrave; produrre, quali richiedono un collegamento e quali oggi non esistono.",
  fonte='Fonte delle informazioni sulle piattaforme ESG: pagine ufficiali Zucchetti (<a href="https://www.zucchetti.it/it/cms/soluzioni/software-esg-sostenibilita" rel="nofollow">zucchetti.it &mdash; software ESG</a>). Ultima verifica: agosto 2026.'),
 dict(slug="fabbrica50.html", on="fabbrica50.html",
  title="Fabbrica 5.0: interconnessione e tracciabilit&agrave; per gli incentivi | Technology Partners Italia",
  desc="EasyInd ed EasyTime, sviluppati da Technology Partners Italia: interconnessione delle macchine, dati di produzione in tempo reale, tracciabilit&agrave; dei lotti. Le evidenze tecniche su cui si gioca l'accesso agli incentivi.",
  crumb="Fabbrica 5.0 e finanza agevolata", kick="Area d'impatto 03",
  h1="Le evidenze tecniche decidono la pratica, non le fatture",
  lead="Interconnessione, dati di produzione e tracciabilit&agrave; sono i requisiti su cui si gioca l'accesso agli incentivi. EasyInd ed EasyTime, che abbiamo sviluppato noi, li producono come normale attivit&agrave; di reparto.",
  body=fab_body,
  ctah="Avete un investimento in programma?",
  ctap="Conviene guardare i requisiti tecnici prima di ordinare le macchine: cambia il modo in cui l'impianto va collegato, e a volte cambia anche la scelta.",
  fonte='Le funzionalit&agrave; descritte sono quelle di EasyInd ed EasyTime, soluzioni sviluppate da Technology Partners Italia S.r.l. e gi&agrave; installate in produzione.'),
]

for p in PAGES:
    html=page(**p)
    open(os.path.join(OUT,p["slug"]),"w",encoding="utf-8").write(html)
    print(p["slug"], len(html),"byte")
