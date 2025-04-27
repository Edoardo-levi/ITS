"""Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari, e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato."""

def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
    nuova_lista:list=[]
    for nums in lista_numeri:
        if nums %2==0:
            num_motiplicati=nums*fattore
            nuova_lista.append(num_motiplicati)
    return nuova_lista