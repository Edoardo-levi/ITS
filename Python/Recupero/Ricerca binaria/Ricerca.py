"""implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False."""

def ricerca_binaria(lista:list[int], num_cercato:int) ->bool:
    lista.sort()
    sinistra =0
    destra= len(lista)-1

    while sinistra <= destra:
        centro= (sinistra+destra)//2
        if lista[centro]==num_cercato:
            return True
        elif lista[centro] > num_cercato:
            destra=centro-1
        else:
            sinistra=centro-1
    return False

print(ricerca_binaria([1,5,9,8,6,5,78,8,22,55,42,18],18))