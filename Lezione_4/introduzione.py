"""Supponiamo di dover trovare la somma degli interi da
1 a 10, da 20 a 37 e da 35 a 49.
Scrivi un programma Python che calcola queste tre diverse somme."""


somma=0
for index in range (1,11):
    somma+=index

print(f"la somma dei numeri da 1 a 10 e': {somma}")
somma=0
for index in range (20, 38):
    somma+= index

print(f"la somma dei numeri da 20 a 37 e': {somma}")
somma=0
for index in range (35, 50):
    somma+=index

print(f"la somma dei numeri da 35 a 49 e': {somma}")




print("riscrivo il codice utilizzando le funzioni")



def sum(a:int, b:int):                      # definisco la funzione sum

    result = 0                              # inizializzo il risultato  a o

    for i in range(a,b+1):                  # faccio il for con i parametri della funzione per calcolare la somma 
        result = result + i                 

    return result                           # restituisco il risultato 

print(f"la somma da 1 a 10 e': {sum(1,10)}")       # richiamo la funzione per calcolare la somma dei numeri da 1 a 10

print(f"Sum from 20 to 37 is {sum(20,37)}")        # richiamo la funzione per calcolare la somma dei numeri da 20 a 37

print(f"Sum from 35 to 49 is {sum(35,49)}")        # richiamo la funzione per calcolare la somma dei numeri da 35 a 49