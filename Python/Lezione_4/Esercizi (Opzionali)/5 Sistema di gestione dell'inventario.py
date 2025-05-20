"""Crea un elenco per archiviare gli articoli nell'inventario.
Crea una funzione che definisca un articolo con un codice, un nome, una quantità e un prezzo.
Implementa funzioni per aggiungere, rimuovere, cercare e aggiornare gli elementi nell'inventario.
Utilizzare per i cicli per gestire le varie operazioni di inventario.
"""

def inventario(nome:str, codice:int, quantita:int, prezzo:float)->dict:
  return{"Nome": nome, "Codice": codice, "Quantità":quantita, "Prezzo": prezzo}

def aggiungi_elemento(inventario:list,prodotto:dict):
  inventario.append(prodotto)

def rimuovi_elemento(inventario:list, nome_prodotto:str):
  for elemento in inventario:
    if elemento['Nome']==nome_prodotto:
      inventario.remove(elemento)
      print(f"L'elemento {nome_prodotto}, è stato rimosso dall'inventario")

def cerca_prodotto(inventario:list, prodotto_cercato:str):
  for elemento in inventario:
    if elemento['Nome']== prodotto_cercato:
      print(f"L'elemento {prodotto_cercato} si trova nel'inventario")
    else:
      print(f"L'elemento {prodotto_cercato}, non è presente nell'inventario")

def aggiorna_elemento(inventario: list, nome_prodotto: str, nuova_quantita: int = None, nuovo_prezzo: float = None):
    for elemento in inventario:
        if elemento['Nome']==nome_prodotto:
           if nuova_quantita is not None:
             elemento['Quantità'] = nuova_quantita
           if nuovo_prezzo is not None:
             elemento['Prezzo'] = nuovo_prezzo
           print(f"L'elemento {nome_prodotto}, è stato aggiornato")

    print(f"L'elemento '{nome_prodotto}' non è stato trovato.")




# 1. Creo la lista dell'inventario
inventario_lista = []

# 2. Aggiungo alcuni prodotti
p1 = inventario("Pane", 101, 20, 1.50)
p2 = inventario("Latte", 102, 10, 1.20)
p3 = inventario("Uova", 103, 30, 2.00)

aggiungi_elemento(inventario_lista, p1)
aggiungi_elemento(inventario_lista, p2)
aggiungi_elemento(inventario_lista, p3)

# 3. Stampo l'inventario iniziale
print("\nInventario iniziale:")
for prodotto in inventario_lista:
    print(prodotto)

# 4. Cerco un prodotto esistente
print("\nCerco il prodotto 'Latte':")
cerca_prodotto(inventario_lista, "Latte")

# 5. Cerco un prodotto inesistente
print("\nCerco il prodotto 'Burro':")
cerca_prodotto(inventario_lista, "Burro")

# 6. Aggiorno quantità e prezzo del prodotto 'Pane'
print("\nAggiorno 'Pane':")
aggiorna_elemento(inventario_lista, "Pane", nuova_quantita=50, nuovo_prezzo=1.80)

# 7. Rimuovo un prodotto
print("\nRimuovo 'Uova':")
rimuovi_elemento(inventario_lista, "Uova")

# 8. Stampo l'inventario finale
print("\nInventario finale:")
for prodotto in inventario_lista:
    print(prodotto)