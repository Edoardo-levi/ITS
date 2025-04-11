"""Progettare un algoritmo che richieda all’utente di inserire un valore intero positivo n. 
Se n è negativo, il programma termina mostrando un messaggio di errore. Se n è positivo:

l’utente può inserire 10 numeri interi;
contare quanti di questi numeri sono divisibili per n.
Mostrare in output il risultato del conteggio.
"""


n=int(input("inserisci un numero:\n"))

if n>0:
    cont=0
    i=0
    for i in range (10):
        x=int(input("inserisci un numero X:\n"))
        if x%n==0:
            cont+=1
        else:
            i+=1
    print(f"i numeri divisibili per {n} sono: {cont}")
else:
    print("Il numero N deve essere positivo")
    