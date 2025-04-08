''' crea un elenco dei numeri da uno a un milione, 
quindi usa min() e max() per assicurarti che l'elenco inizi effettivamente 
da uno e finisca a un milione. Inoltre, usa la funzione sum() 
per vedere quanto velocemente Python può sommare un milione di numeri.'''

numeri = list(range(1, 1000001))

minimo= min(numeri)
massimo= max(numeri)
print(f"il numero massimo e': {massimo}\nil numeor minimo e': {minimo}\n")

# Somma dei numeri
somma = sum(numeri)
print(f"La somma dei numeri è: {somma}")



