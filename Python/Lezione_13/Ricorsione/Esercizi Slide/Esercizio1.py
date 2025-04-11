"""Scrivi una funzione Python chiamata `countdown` che prenda come input un intero positivo `n` e
stampi un conto alla rovescia da `n` a zero.
Se il numero di input è negativo, mostra un messaggio di errore.
Per implementare la funzione, devi usare esclusivamente un ciclo `while` e il parametro `n` passato come input alla funzione.
Non è permesso dichiarare variabili aggiuntive all'interno della funzione.
Poi, chiama la funzione con `n = -5` e `n = 5`."""

"""def countdown (n:int) -> None:
    if n<0:
        print("Errore!!")
    else:
        while n>=0:
            print(n)
            n-=1


countdown(-5)
countdown(5)


"""

# FUNZIONE COUNTDOWN IN MODO RICORSIVO:


def countdown(n:int) ->None:
    if n <0:
        print("Errore!! Il numero deve essere positivo")
    
    elif n==0:
        print(0)
        
    else:
        print(n)
        countdown(n-1)

countdown(int(input("inserisci un numero: ")))