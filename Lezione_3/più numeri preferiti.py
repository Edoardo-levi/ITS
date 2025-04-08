'''usa un dizionario per memorizzare i numeri preferiti delle persone. 
Pensa a cinque nomi e usali come chiavi nel tuo dizionario. 
Pensa a un numero preferito per ogni persona e memorizza ciascuno come 
valore nel tuo dizionario. Stampa il nome di ogni persona e il suo numero preferito. 
Per divertirti ancora di più, fai un sondaggio tra alcuni amici e ottieni 
alcuni dati reali per il tuo programma.'''

num_preferiti={"Edoardo": [12,344],
                "Mattia": [7,19],
                "Lorenzo":[8,45],
                "Totti":[10,69],
                "Leonardo":[4,90]}
print ("I numeri preferiti delle persone della lista sono:\n")
for chiave, valore in num_preferiti.items():
    a = ""     #creo una stringa vuota
    for v in valore:    # itero il valore della lista 
        a += f"{v}, " #concatena alla stringa un'altra stringa che contiene l'elemento della lista v , spazio 
    print(f"{chiave}: {a[:-2]}") #stampo la chiave della lista e i valori della stringa eccetto gli ultimi du quindi la virgola e lo spazio 