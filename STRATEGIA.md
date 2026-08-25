# Riposizionamento tp-italia.com — Brand Authority

## Il salto

| | Sito attuale | Sito nuovo |
|---|---|---|
| Chi parla | un rivenditore di software | un consulente di direzione |
| A chi | responsabile IT / amministrativo | amministratore delegato, direttore generale |
| Che cosa promette | funzionalità di prodotto | meno rischio, ritorno misurabile, investimento finanziato |
| Prima cosa che si vede | quattro card "Soluzioni Gestionali / Sistemistiche / CRM / Documentali" | le tre aree d'impatto: AI nativa, ESG, Finanza agevolata 5.0 |
| Prova d'autorità | logo dei partner nel footer, in grigio | Top Partner Zucchetti e le 11 certificazioni sopra la piega |
| Chiamata all'azione | "Scopri di più" ripetuto 12 volte | "Prenota un confronto riservato", telefono e mail sempre visibili |

Il perimetro resta lo stesso: gli stessi prodotti, gli stessi partner, gli stessi contenuti.
Cambia l'ordine in cui vengono presentati e la lingua in cui sono scritti.

## Le tre aree d'impatto

Sono la porta d'ingresso del sito, non tre pagine in fondo al menu. Ognuna risponde a una domanda
che un amministratore delegato si pone davvero:

1. **AI nativa** → *quanto anticipo ho sui problemi?* Previsione della domanda, manutenzione
   predittiva, qualità e scarti, anomalie sui documenti. Dentro i sistemi già in uso.
2. **Sostenibilità ESG** → *i miei dati reggono una verifica?* Energia, filiera, sicurezza,
   governance: estratti dai sistemi, non compilati a mano.
3. **Finanza agevolata (Fabbrica 5.0)** → *quanto dell'investimento me lo finanzia lo Stato?*
   La parte tecnica che fa passare la pratica: interconnessione, tracciabilità, evidenze conservate.

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
- Ogni affermazione di beneficio porta con sé **come si misura**.
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

## Fase 2 — schede prodotto Zucchetti

Le pagine che descrivono prodotti Zucchetti vanno riscritte sulle **fonti ufficiali**, non sui testi
attuali (fermi a Mago.net e a Infinity 4.2). Fonti di riferimento:

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

## Redirect

Nessun URL viene eliminato: le pagine che si fondono restano online e rimandano alla nuova, con
`301` lato server. La mappa completa vecchio → nuovo si compila insieme all'inventario, in
`INVENTARIO.md`, colonna *Destino*.

## Interventi tecnici che accompagnano il riposizionamento

1. `<title>` e `meta description` unici su ogni pagina (oggi 8 pagine condividono lo stesso titolo).
2. `sitemap.xml` e `robots.txt` (oggi assenti).
3. Menu con link reali nell'HTML: oggi è costruito in JavaScript e nasconde `azienda.html` e
   `contatti.html` ai motori di ricerca.
4. Form propri al posto degli iframe di Google Forms, con notifica e tracciamento dei contatti.
5. Google Analytics 4 al posto di Universal Analytics (fermo dal 2023, e con lo snippet corrotto).
6. Testo vero al posto delle immagini nelle 6 pagine oggi vuote.
7. Immagini in formato moderno e video su piattaforma esterna: oggi la home pesa decine di MB.

## Da confermare prima della pubblicazione

Sul sito nuovo compaiono solo affermazioni verificabili dai vostri materiali. Queste invece
servono a voi per rafforzare le pagine, e le aspettiamo da voi:

- **Numeri aziendali**: clienti attivi, installazioni, anno esatto di fondazione, dipendenti.
- **Casi reali**: due o tre clienti disposti a essere citati, con il risultato ottenuto in numeri.
- **Finanza agevolata**: quali misure seguite davvero, con quali professionisti, e se avete
  pratiche concluse da citare. Sulla pagina non compare nessuna percentuale proprio perché
  le misure cambiano: vanno verificate all'avvio di ogni progetto.
- **AI**: quali funzioni predittive avete già installato in produzione presso un cliente.
- **ESG**: se avete già assistito qualcuno nella raccolta dati per un questionario o un bilancio.
