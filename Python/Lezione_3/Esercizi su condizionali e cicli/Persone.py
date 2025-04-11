"""Persone: inizia con il programma che hai scritto per l'esercizio 6-1. Crea due nuovi dizionari che rappresentano persone 
diverse e memorizza tutti e tre i dizionari in un elenco chiamato persone. 
Esegui un ciclo nell'elenco di persone. Mentre esegui un ciclo nell'elenco, stampa tutto ciò che sai su ciascuna persona."""





persona1= {"nome":"Lorenzo",\
          "cognome":"Palcich",\
          "eta":19, \
          "citta":"Roma"}
persona2= {"nome": "Edoardo",\
           "cognome": "Valentini",\
            "eta": "21"}
persona3= {"nome": "Mattia",\
           "cognome": "Ferrandino",\
            "eta": "19"}


lista_persona =[persona1,persona2,persona3]
          
print("i dati degli utetni sono:\n")
for item in lista_persona:
    print(f"nome: {item['nome']}\ncognome: {item['cognome']}\neta: {item['eta']}\n")
          
          