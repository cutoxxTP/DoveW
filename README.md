# tp-italia.com — rifacimento sito

Progetto di rifacimento di **www.tp-italia.com** (Technology Partners Italia, Desio MB).
Regola di base: **non si perde nulla**. Il sito attuale è archiviato integralmente prima
di qualsiasi modifica; i contenuti vengono riscritti e ampliati partendo da quell'archivio.

## Struttura

| Cartella | Contenuto |
|---|---|
| `archivio/sito/` | Copia integrale del sito online al 25/08/2026: 45 pagine HTML, CSS, 148 PNG, 78 JPG, 9 WebP, 6 video MP4, 2 PDF. Non va modificata: è la fonte di verità. |
| `archivio/contenuti/` | Testo di ogni pagina estratto in Markdown (`.md` per pagina) + `_index.json` con titoli, keyword e conteggi. È il materiale da cui riscrivere. |
| `INVENTARIO.md` | Tabella pagina per pagina, raggruppata per area, con la colonna *Destino* da compilare. |

## Com'è fatto il sito oggi

- Sito **statico** generato con **RocketCake**, ospitato su Register.it. Tutte le pagine
  sono in root (`/nomepagina.html`), nessuna sottocartella, nessun CMS.
- Menu unico in cima a tutte le pagine: Home · Chi Siamo · Prodotti · Contattaci · Lavora con Noi.
- 45 pagine, ~22.300 parole. Aree: ERP Mago, ERP Ad Hoc Infinity, suite Zucchetti Infinity
  (CRM, DMS, HR, Portal, BI, fatturazione elettronica, presenze), soluzioni proprie
  (ITEK4, OPERA MES, W.App, EasyTime, EasyInd 4.0, MO.TI., RFID), sistemistica, news, azienda.
- Contatti: Via Vincenzo Monti 74, 20832 Desio (MB) · commerciale@tp-italia.com ·
  Tel +39 0362 163 6293 · Fax +39 0362 632 343.
- Social collegati: LinkedIn, Facebook, Instagram, YouTube.

## Cosa è emerso dall'analisi (da correggere nel rifacimento)

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

## Prossimo passo

Definire il **nuovo intento** del sito e compilare la colonna *Destino* di `INVENTARIO.md`,
poi progettare la nuova architettura delle pagine (vecchie riscritte + nuove) e la mappa
dei redirect 301 dai vecchi URL.
