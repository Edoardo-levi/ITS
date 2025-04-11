"""Scrivere un programma che consenta 
all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). 
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali)."""

numeri=[]
somma=0
cont=0
massimo= 0
minimo=float('inf')



sentinella=0

while True:
    num=float(input("inserisci dei numeri:\n"))
    
    

    if num<0:
        sentinella=num
        break

    numeri.append(num)
    
    if num.is_integer():
        somma+=num
        cont+=1

    if num>massimo:
        massimo=num
    
    if num<minimo:
        minimo=num
    
    
    
  
    
media=somma/cont
print(f"il numero negativo inserito che ha fatto terminare il ciclo e': {sentinella}")
print(f"la somma e':{somma}")
print(f"la media e': {media:.2f}")
print(f"il numero massimo e': {massimo}")
print(f"il numero minimo e': {minimo}")