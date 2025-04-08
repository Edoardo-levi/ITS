"""Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso."""


numeri=[]

for index in range(5):
    numeri.append(int(input("inserisci un numero da 1 a 30:\n")))

for numero in numeri:
    print("*"* numero)
