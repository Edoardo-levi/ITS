"""Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati."""

def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    if len(x) != len(y) and (x%1 !=0 and y %1 !=0):
        return("Errore, le liste devono avere la stessa lunggezza e devono essere interi")
    
    else: 
        lista_somma=[]
        for i in range (len(x)):
            lista_somma.append(x[i]+y[i])
        return lista_somma

            


lista1=[1,2,3,4]
lista2=[1,1,1,1]

somma_elementi(lista1, lista2)

somma_elementi()

