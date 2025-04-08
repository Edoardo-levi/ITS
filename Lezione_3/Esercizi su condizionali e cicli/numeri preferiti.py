'''usa un dizionario per memorizzare i numeri preferiti delle persone. 
Pensa a cinque nomi e usali come chiavi nel tuo dizionario. 
Pensa a un numero preferito per ogni persona e memorizza ciascuno come 
valore nel tuo dizionario. Stampa il nome di ogni persona e il suo numero preferito. 
Per divertirti ancora di più, fai un sondaggio tra alcuni amici e ottieni 
alcuni dati reali per il tuo programma.'''

num_preferiti={"Edoardo": 12,\
                "Mattia": 7,\
                "Lorenzo":8,\
                "Totti":10,\
                "Leonardo":4}
print ("I numeri preferiti delle persone della lista sono:\n")
for chiave, valore in num_preferiti.items():
    print(f"{chiave}: {valore}")