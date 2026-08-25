# tp-italia.com — rifacimento sito

Progetto di rifacimento di **www.tp-italia.com** (Technology Partners Italia, Desio MB).
Regola di base: **non si perde nulla**. Il sito attuale è archiviato integralmente prima
di qualsiasi modifica; i contenuti vengono riscritti e ampliati partendo da quell'archivio.

## Struttura

| Cartella | Contenuto |
|---|---|
| `archivio/sito/` | Copia integrale del sito online al 25/08/2026: 47 pagine HTML, CSS, ~490 immagini, 6 video MP4, 2 PDF. Non va modificata: è la fonte di verità. |
| `archivio/contenuti/` | Testo di ogni pagina estratto in Markdown (`.md` per pagina) + `_index.json` con titoli, keyword e conteggi. È il materiale da cui riscrivere. |
| `INVENTARIO.md` | Tabella pagina per pagina, raggruppata per area, con la colonna *Destino* da compilare. |

## Com'è fatto il sito oggi

- Sito **statico** generato con **RocketCake**, ospitato su Register.it. Tutte le pagine
  sono in root (`/nomepagina.html`), nessuna sottocartella, nessun CMS.
- Menu unico in cima a tutte le pagine: Home · Chi Siamo · Prodotti · Contattaci · Lavora con Noi.
- 47 pagine, ~22.500 parole. Aree: ERP Mago, ERP Ad Hoc Infinity, suite Zucchetti Infinity
  (CRM, DMS, HR, Portal, BI, fatturazione elettronica, presenze), soluzioni proprie
  (ITEK4, OPERA MES, W.App, EasyTime, EasyInd 4.0, MO.TI., RFID), sistemistica, news, azienda.
- Contatti: Via Vincenzo Monti 74, 20832 Desio (MB) · commerciale@tp-italia.com ·
  Tel +39 0362 163 6293 · Fax +39 0362 632 343.
- Social collegati: LinkedIn, Facebook, Instagram, YouTube.

## Cosa è emerso dall'analisi (da correggere nel rifacimento)

0. **Due pagine erano invisibili a qualsiasi crawler**: `azienda.html` (Chi siamo — Mission e
   Company Profile) e `contatti.html` non sono linkate da nessun `href` nell'HTML. I menu a
   tendina sono costruiti in JavaScript, quindi quelle pagine esistono online ma nessun motore
   di ricerca le raggiunge. È il caso più grave: la pagina che racconta chi siete non è
   indicizzabile.
1. **Nessuna `meta description`** su nessuna pagina, e **8 pagine hanno lo stesso `<title>`**
   ("Technology Partners Italia"): Google non ha modo di distinguerle.
2. **Nessuna sitemap.xml e nessun robots.txt** (entrambi 404).
3. **6 pagine sono praticamente vuote di testo** — il contenuto sta dentro le immagini o in un
   PDF: `presenzeweb`, `smplice`, `ztravel`, `ruckus`, `bussinessapps`, `hr`. Per i motori di
   ricerca quelle pagine non esistono.
4. **Nessun form nativo**: "Richiedi informazioni" e "Lavora con noi" sono iframe di Google Forms.
   Nessuna tracciabilità dei lead, nessuna conferma via mail.
5. **Google Analytics obsoleto**: due snippet Universal Analytics duplicati con lo stesso ID
   `UA-37003217-1`, dismesso da Google nel 2023 — non sta raccogliendo più nulla. Il primo
   snippet è per giunta corrotto (apici tipografici al posto di quelli dritti: non gira).
6. **6 video MP4 caricati direttamente** (fino a 15 MB l'uno) e immagini fino a 1772 px non
   ottimizzate: pagine pesanti, penalizzate sul mobile.
7. **Refusi nei titoli e negli URL**: "Tecnology Partners News", "Le Bussiness Apps",
   "LAvora con Noi", `bussinessapps.html`.
8. Coppie di pagine sovrapposte da consolidare: `news`/`newsnew`, `gestionali`/`gestionalix`.

Tutte cose risolvibili nella ricostruzione, senza perdere un rigo dei contenuti attuali.

## Verifica di completezza dell'archivio

Il mirror iniziale via `wget` aveva scaricato solo ciò che è referenziato nell'HTML. Le pagine usano
però slideshow JavaScript che caricano le immagini a runtime, e i menu a tendina sono generati in
JavaScript: mancavano **243 immagini** e **2 pagine intere** (`azienda.html`, `contatti.html`).
Recuperate aprendo tutte le pagine in un browser headless, registrando ogni 404 e riscaricandolo.
Secondo giro di verifica: **0 richieste fallite**.

## Consultare l'archivio in locale

I file CSS sono referenziati dall'HTML con un suffisso anti-cache (`index_html.css?h=2b9d5bd8`),
che un server statico ignora. Per rivedere il sito originale esattamente com'è online:

    python3 -m http.server 8000 --directory archivio/sito

## Il sito in lavorazione

`sito/` è la copia di lavoro: parte identica all'archivio e viene modificata pagina per pagina
secondo `STRATEGIA.md` e la colonna *Destino* di `INVENTARIO.md`. Si confronta con l'originale
servendo le due cartelle su due porte diverse.

## Prossimo passo

Definire il **nuovo intento** del sito e compilare la colonna *Destino* di `INVENTARIO.md`,
poi progettare la nuova architettura delle pagine (vecchie riscritte + nuove) e la mappa
dei redirect 301 dai vecchi URL.

## Anteprima navigabile

`anteprima/archivio-live.html` è una copia autonoma dell'intero sito in un unico file:
tutte le 47 pagine con CSS e JavaScript originali, le immagini incorporate come data URI
(WebP, per stare sotto il limite di peso) e i link interni che funzionano. Serve a rivedere
il sito com'era senza dipendere dal dominio online. Video e contenuti esterni (mappe Google,
Google Forms, YouTube) sono sostituiti da segnaposto: i file originali restano in `archivio/sito/`.

Si rigenera con gli script in `strumenti/`.
