"""Progetta un algoritmo per ottenere la misura di un cateto c 
in un triangolo rettangolo, conoscendo quelle dell’ipotenusa a e dell’altro cateto b."""

import math 

a=int(input("inserisci una misura per a: \n"))
b=int(input("inaerisci una misura per b:\n"))

if a>b:
    c= math.sqrt(a**2 - b**2)
    print(f"{c:.2f}")
else:
    print("Errore")


