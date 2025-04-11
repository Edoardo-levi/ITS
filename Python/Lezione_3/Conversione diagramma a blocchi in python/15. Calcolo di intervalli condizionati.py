"""Progettare un algoritmo che chieda all’utente di inserire un valore intero n.
L'algoritmo deve:

Verificare se n è compreso tra 1 e 100:
se sì, calcolare e mostrare la somma di tutti i numeri pari compresi tra 1 e n.
Verificare se n è 0 o negativo:
Se sì, mostrare un messaggio di errore e terminare.
Altrimenti, calcolare e mostrare la somma di tutti i numeri dispari compresi tra 1 e n.
"""
n:int = int(input("inserisci un numero:\n"))
sumP = 0
sumD = 0


if n%1==0:
    if n > 0 and n<=100:
            for i in range (0, n+1, 2):
                sumP += i
            for x in range (1, n+1, 2):
                sumD += x    
    
    elif  n==0 or n<0:
        print("errore")
else:
    print("Errore! il numero deve essere intero")

print(f"la somma dei numeri pari compresi tra 1 e {n} e':{sumP}")
print(f"la somma dei numeri dispari compresi tra 1 e {n} e':{sumD}")