
## Consultare l'archivio in locale

I file CSS sono referenziati dall'HTML con un suffisso anti-cache (`index_html.css?h=2b9d5bd8`),
che un server statico ignora. Per rivedere il sito originale esattamente com'è online:

    python3 -m http.server 8000 --directory archivio/sito
