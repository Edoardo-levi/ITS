'''crea un dizionario chiamato città.
Usa i nomi di tre città come chiavi nel tuo dizionario. 
Crea un dizionario di informazioni su ogni città e includi il paese in 
cui si trova la città, la sua popolazione approssimativa e un fatto su quella città.
Le chiavi per il dizionario di ogni città dovrebbero essere qualcosa come paese,
popolazione e fatto. Stampa il nome di ogni città e tutte le informazioni 
che hai memorizzato su di essa.'''

citta= {"Roma": 
            {"paese": "Italia", "popolazione": "2.8 milioni", "fatto": "Roma e' caput mundi"},
        "Milano":
            { "paese": "Italia", "popolazione": "1.4 milioni", "fatto": "Milano e' la citta della moda"},
        "Firenze":
            {"paese": "Italia", "popolazione": "62 mila", "fatto": "A firenze c'e' la torre di Pisa"}
        }
        
        
for città_nome, citta_info  in citta.items():
    print(f"Informazioni su {città_nome}:")
    print(f"- Paese: {citta_info['paese']}")
    print(f"- Popolazione: {citta_info['popolazione']}")
    print(f"- Fatto interessante: {citta_info['fatto']}")
    print ("----------------")
