"""Progettare un algoritmo che chieda all'utente di inserire un valore x positivo. Se x è negativo, '
'l'algoritmo mostra un messaggio di errore e termina. Se x  è positivo, il programma deve consentire 
all'utente di inserire 10 numeri sia positivi che negativi. 

Se x è pari, allora dei numeri inseriti devono essere sommati solamente i numeri che sono maggiori della metà di x. 
Se, invece, x è dispari, dei numeri inseriti devono essere sommati solo i numeri che sono minori di x. 
"""

x=int(input("inserisci un valore X:\n"))
somma_pari:int=0
somma_dispari:int=0

if x>0:
    for i in range (10):
        n=int(input("Inserisci un numero: "))
        if n%2 ==0:
            if n >(x/2):
                somma_pari +=n
        else:
            if n<x:
                somma_dispari+=n
else:
    print("Errore! X deve essere positivo")

print(f"la Somma dei numeri pari e': {somma_pari}\nLa somma dei numeri dispari e': {somma_dispari}")