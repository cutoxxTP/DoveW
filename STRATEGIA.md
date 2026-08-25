# Riposizionamento tp-italia.com — Brand Authority

## Il salto

| | Sito attuale | Sito nuovo |
|---|---|---|
| Chi parla | un rivenditore di software | un consulente di direzione |
| A chi | responsabile IT / amministrativo | amministratore delegato, direttore generale |
| Che cosa promette | funzionalità di prodotto | meno rischio, ritorno misurabile, investimento finanziato |
| Prima cosa che si vede | l'immagine di apertura, alta 900 px, e sotto le quattro card di prodotto | l'apertura ridotta e, subito sotto, le tre aree d'impatto |
| Prova d'autorità | logo dei partner nel footer, in grigio | Top Partner Zucchetti e le 11 certificazioni sopra la piega |
| Chiamata all'azione | "Scopri di più" ripetuto 12 volte | telefono e mail in fondo a ogni pagina nuova |

Il perimetro resta lo stesso: gli stessi prodotti, gli stessi partner, gli stessi contenuti.
Cambia l'ordine in cui vengono presentati e la lingua in cui sono scritti.

## Le tre aree d'impatto

Sono la porta d'ingresso del sito, non tre pagine in fondo al menu. Ognuna risponde a una domanda
che un amministratore delegato si pone davvero:

1. **AI nativa** → *quanto anticipo ho sui problemi?* Contenuto costruito **solo** sulle funzioni
   che Zucchetti dichiara sulle proprie pagine ufficiali: personale e selezione, algoritmi predittivi
   nell'ERP, contabilizzazione assistita. Più il nostro contributo reale: far arrivare dati completi
   al sistema che li deve leggere.
2. **Sostenibilità ESG** → *i miei dati reggono una verifica?* Qui non abbiamo esperienza diretta,
   e la pagina lo dice: presentiamo le quattro piattaforme ESG di Zucchetti (Sostenibile.go,
   Sostenibile.cloud, ESG Zucchetti, ESG Datastore) e ci prendiamo solo la parte che sappiamo fare,
   cioè i sistemi che producono i dati. Frase esplicita in pagina: *"Non facciamo consulenza di
   sostenibilità e non redigiamo bilanci"*.
3. **Fabbrica 5.0 e finanza agevolata** → *quanto dell'investimento può rientrare?* Interamente
   fondata su EasyInd ed EasyTime, che sono nostri e già installati: interconnessione, dati macchina,
   tracciabilità del lotto, scarti e qualità. Nessuna percentuale e nessuna promessa sulla pratica,
   che resta al commercialista.

## Regole di scrittura

**Fuori dalla homepage e da ogni pagina d'ingresso** il gergo tecnico. Esempi presi dal sito attuale
(`sistemi.html`), da non riproporre in apertura:

> "compatibile con una vasta scelta di dischi da 3,5 pollici o da 2,5 pollici ssd"
> "l'utilizzo di questi ultimi permette di aumentare la velocità di esecuzione"
> "3 anni di garanzia inclusa, con sostituzione del pezzo danneggiato entro il giorno successivo"

Il dettaglio tecnico non si cancella: **scende di un livello**, nelle schede di prodotto, dove chi
lo cerca lo trova. In homepage al suo posto va il beneficio: continuità operativa, rischio di fermo,
tempo di ripristino.

Altre regole:
- Ogni pagina apre con il **problema del cliente**, non con il nome del prodotto.
- **Si scrive solo ciò che esiste.** Niente metodi, processi o servizi che non pratichiamo davvero:
  nessun "assessment in due settimane", nessun business case garantito, nessun indicatore promesso.
- Dove il contenuto viene da un fornitore, **la fonte è citata in fondo alla pagina** con la data
  di verifica.
- Niente superlativi senza prova ("la migliore soluzione", "leader di mercato" riferito a noi).
- Voce attiva, frasi brevi, seconda persona plurale rivolta all'azienda.

## Nuova architettura

```
Home  ─┬─ Aree d'impatto ─┬─ AI nativa                    [nuova]
       │                  ├─ Sostenibilità ESG            [nuova]
       │                  └─ Finanza agevolata 5.0        [nuova]
       │
       ├─ Soluzioni ──────┬─ Sistema gestionale ERP       (gestionalix + gestionali, riscritte)
       │                  ├─ CRM e portali                (crm + portal)
       │                  ├─ Fabbrica connessa            (easytime + easyind40 + operames)
       │                  ├─ Logistica di magazzino       (wapp + rfid)
       │                  ├─ Documenti e conservazione    (dms + fepasos)
       │                  ├─ Assistenza e ticketing       (itek4 + mobileticketnew)
       │                  ├─ Persone e presenze           (hr + presenzeweb + smplice + ztravel)
       │                  └─ Continuità e sicurezza       (sistemi + ruckus + tecnologia)
       │
       ├─ Azienda ────────┬─ Chi siamo                    (azienda, riscritta ed esposta nel menu)
       │                  ├─ News                         (newsnew, da riattivare)
       │                  └─ Lavora con noi               (lavoraconnoi, con form vero)
       │
       └─ Contatti                                        (modulo + indicazioni + contatti, unite)
```

## Fase 2 — schede prodotto Zucchetti *(fatta)*

Riscritte 22 schede prodotto sulle **fonti ufficiali zucchetti.it**, non sui testi attuali (fermi a
Mago.net e a Infinity 4.2). Ogni pagina chiude con la fonte, il collegamento alla pagina ufficiale e
la data di verifica, più l'avvertenza che i moduli disponibili dipendono dalla licenza.
Fonti usate:

| Nostra pagina | Fonte ufficiale |
|---|---|
| `mago4.html`, `mago*.html` | zucchetti.it → Soluzioni → Software gestionali → Mago4 (descrizione, funzionalità, vantaggi) |
| `ahi*.html` | zucchetti.it → Ad Hoc Infinity (descrizione, funzionalità, vantaggi) + brochure ufficiale |
| `infinity.html` | zucchetti.it → Infinity Zucchetti |
| `crm.html`, `dms.html`, `portal.html`, `infobusiness.html` | schede dei moduli Infinity |
| `hr.html`, `presenzeweb.html`, `smplice.html`, `ztravel.html` | zucchetti.it → HR Infinity, ZTravel |
| `fepasos.html` | zucchetti.it → fatturazione elettronica e conservazione |

Regola per ogni scheda riscritta: **prima il problema aziendale, poi il prodotto**; funzionalità
verificate sulla fonte ufficiale; nessun dato di versione o requisito di sistema in apertura.

## Redirect *(fatti)*

Nessun URL è stato eliminato. Le sette pagine confluite restano online e rimandano alla nuova:
il `301` è in `sito/.htaccess`, e la pagina di riserva resta pubblicata nel caso in cui l'hosting
non legga il file.

| Vecchia | Nuova |
|---|---|
| `mago.html` | `mago4.html` |
| `gestionali.html` | `gestionalix.html` |
| `presenzeweb.html`, `smplice.html` | `hr.html` |
| `bussinessapps.html`, `cloudapp.html` | `infinity.html` |
| `news.html` | `newsnew.html` |

## Interventi tecnici che accompagnano il riposizionamento

1. ✅ `<title>` e `meta description` unici su tutte le pagine riscritte.
2. ✅ `sitemap.xml` (43 URL) e `robots.txt` creati.
3. ✅ Menu con link reali nell'HTML sulle pagine nuove: `azienda.html` e `contatti.html` non sono
   più invisibili ai motori di ricerca.
4. ✅ Script Universal Analytics rimosso da tutte e 20 le pagine che lo contenevano: era corrotto
   e il servizio è dismesso dal 2023. **Serve da voi l'ID di misurazione GA4** per rimetterne uno che funzioni.
5. ✅ Testo vero al posto delle immagini nelle pagine prima vuote (`presenzeweb`, `smplice`,
   `ztravel`, `bussinessapps`, `cloudapp`, `hr`).
6. ⬜ Form propri al posto degli iframe di Google Forms, con notifica e tracciamento dei contatti.
7. ⬜ Immagini in formato moderno e video su piattaforma esterna: la home pesa ancora decine di MB.
8. ✅ Riscritte le pagine sulle soluzioni nostre: `easytime`, `easyind40`, `wapp`, `itek4`,
   `mobileticketnew`, `rfid`, `operames`.
9. ⬜ Restano: sistemistica (`sistemi`, `tecnologia`, `ruckus`), `azienda`, `verticali`,
   e le news ferme al 2018.

### Due decisioni cambiate rispetto al piano iniziale

Nell'inventario `mobileticketnew` e `rfid` erano segnate come *da fondere*. Leggendo i contenuti
si è visto che non regge: **Mobile Ticket e iTek4 sono due prodotti diversi** (ticketing di assistenza
il primo, noleggio e manutenzione il secondo) e accorparli avrebbe confuso entrambi. E la pagina RFID
è stata riscritta come **pagina di scelta** — barcode o radiofrequenza, con che cosa serve davvero —
che è più utile di un paragrafo dentro W.App. Restano quindi pagine autonome, collegate fra loro.

## Che cosa NON compare sul sito, e perché

Regola di lavoro: se non esiste, non si scrive. Sono rimasti fuori:

- il metodo in fasi, il business case e gli indicatori concordati: non è un processo che l'azienda pratica;
- qualunque esperienza nostra in ambito ESG: non ce n'è, e la pagina lo dichiara apertamente;
- le percentuali degli incentivi: cambiano, e sbagliarne una costa più di quanto renda;
- numeri aziendali non verificati: clienti attivi, installazioni, anno esatto di fondazione.

Se e quando questi elementi ci saranno, le pagine sono pronte ad accoglierli — sono i punti in cui
oggi il testo resta più generico del necessario.
