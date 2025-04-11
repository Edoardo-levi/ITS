"""Progetta un algoritmo che dati 10 numeri forniti dall'utente, conta quanti sono pari e quanti dispari."""


pari=0
dispari=0
cont=0


for i in range (0,10):
  
    
    n=int(input("inserisci un numero:\n"))

    if n%2==0:
        pari+=1
    else:
        dispari+=1
    
    cont+=1
    
print(f"i numeri pari sono :\n{pari}")
print(f"i numeri dispari sono:\n{dispari}")