"""Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold."""

def moltiplica(lista:list, threshold):
    totale=1
    for numero in lista:
        if numero<threshold:
            totale*=numero
    print (totale)


moltiplica((1,2,3,4,5,6,7,8,9,10), 5)