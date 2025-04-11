"""Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, 
dove n è la lunghezza della lista. Tuttavia, alcuni numeri potrebbero mancare: 
la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.

Il tuo compito è individuare i numeri mancanti.

Scrivi una funzione che, data in input una lista, restituisca una nuova lista ordinata contenente 
tutti i numeri da 1 a n che non sono presenti nella lista originale."""

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    numeri_mancanti=[]
    n=len(nums)
    for i in range(1,n+1):
        if i not in nums:
            numeri_mancanti.append(i)
    return (numeri_mancanti)

numei=[2,3,4,5,6,7,8,9]

find_disappeared_numbers(numei)