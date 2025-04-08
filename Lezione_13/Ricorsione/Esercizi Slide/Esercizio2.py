"""Scrivi una funzione chiamata `sum` che prenda come input un intero positivo `n` e 
restituisca la somma dei numeri da 0 a `n`.
Se il numero di input `n` è negativo, mostra un messaggio di errore e la funzione deve restituire `None`.
Per implementare la funzione `sum`, devi usare esclusivamente un ciclo `while` e il parametro
`n` passato come input alla funzione.
È consentito dichiarare solo una variabile all'interno della funzione per gestire la somma.
Poi, chiama la funzione `sum` per `n = -5` e `n = 5`."""
"""

def sum (n:int) -> int:
    if n<=0:
        print("Errore!")
        return None
    else:
        sum=0
        while n:
            print(n)
            sum+=n
            n-=1
    print(f"la somma dei numeri e':{sum}")
    return int(sum)
           


sum(5)"""


# STESSA FUNZIONE FATTA IN MODO RICORSIVO

def recorsive_sum(n:int) ->int:
    if n<0:
        print("Errore!")
        return None
    
    elif n==0:
        return 0
    
    else:
        return int (n+ recorsive_sum (n-1))
    

print(recorsive_sum(int (input("inserisci un numero: "))))