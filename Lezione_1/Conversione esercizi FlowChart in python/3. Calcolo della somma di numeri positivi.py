"""Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori inseriti dall'utente. 
Quindi, se un numero è negativo o zero, ignora quel valore nella somma."""


sum=0
cont=1
while True:
    n=int(input("inserisci un numero:\n"))

    if n>0:
        sum+=n
    
    cont+=1
    if cont==5:
        break
print(sum)
