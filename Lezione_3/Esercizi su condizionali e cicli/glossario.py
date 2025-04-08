"""un dizionario Python può essere utilizzato per modellare un dizionario reale. Tuttavia, per evitare confusione, chiamiamola glossario.
• Pensa a cinque parole di programmazione che hai imparato nei capitoli precedenti. Usa queste parole come chiavi nel tuo glossario e memorizza i
 loro significati come valori.
• Stampa ogni parola e il suo significato come output formattato in modo ordinato. 
Potresti stampare la parola seguita da due punti e poi il suo significato, oppure stampare la parola su una riga e poi stampare 
il suo significato rientrato su una seconda riga. Usa il carattere di nuova riga (\n) per inserire una riga vuota tra ogni
 coppia parola-significato nel tuo output."""


Glossario= {"APPEND": "",\
            "aggiunge un elemnto alla fine di una lista": "",\
            "INSERT": "", \
            "aggiunge un elemento all'interno della lista nella posizione desiderata" : "",\
            "POP": "",\
            "elimina un elemneto desiderato all'interno di una lista": "",\
            "DEL": "",\
            "elimina tutti gli elementi della lista": "",\
            "SORT": "",\
            "ordina la lista in modo alfabetico": ""}

print ("DIZIONARIO:\n")

for chiave, valore in Glossario.items():
    print(f"{chiave}: {valore}")