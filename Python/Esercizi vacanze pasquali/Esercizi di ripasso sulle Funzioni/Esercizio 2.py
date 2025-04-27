"""Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3."""

def somma_condizionale(numeri: list[int]) -> int :
    somma=0
    for num in numeri:
        if num %2 ==0 and num %3 ==0:
            somma+= num
    
    return somma

print(somma_condizionale([1, 2, 3, 6, 12]))