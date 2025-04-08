'''usa un dizionario per memorizzare informazioni su una persona che conosci.
Memorizza il suo nome, cognome, età e città in cui vive. 
Dovresti avere chiavi come nome, cognome, età e città. 
Stampa ogni informazione memorizzata nel tuo dizionario.'''


persona= {"nome":"Lorenzo",\
          "cognome":"Palcich",\
          "eta":19, \
          "citta":"Roma"}
          
print("i dati dell'utente sono:\n")
for chiave, valore in persona.items():
    print(f"{chiave}: {valore}")
          
          