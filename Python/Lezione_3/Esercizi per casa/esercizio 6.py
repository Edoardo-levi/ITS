"""Scrivere un programma che acquisisca 
in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente."""

n1=int(input("inserisci n1:\n"))
n2=int(input("inserisci n2:\n"))
prodotto=1
if n1 > n2:                                         # se il primo numero è maggiore del secondo, scabio i numeri 
    n1, n2 = n2, n1
for index in range (n1,n2+1):                       #cicolo che include gli estremi nei calcoli 
    prodotto*=index

print(f"il prodotto tra {n1} e {n2} e': {prodotto}")