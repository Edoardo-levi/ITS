"""Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"
"""

oggetti=[]
cont=1

for index in range(3):
    oggetto=str(input("inserisci un oggetto:\n"))
    cont+=1
    oggetti.append(oggetto)

match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale Scolastico")
    
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    
    case ["telefono", "computer", "armadio"]:
        print("Dispositivi Elettronici")
    
    case _: 
        print("Categoria Sconosciuta ")
        