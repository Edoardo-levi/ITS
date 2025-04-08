'''Si scriva un programma che legge tre numeri interi e visualizza la media dei tre numeri.'''


x= int(input("inserisci un numero:\n"))
y= int(input("inserisci un numero:\n"))
z= int(input("inserisci un numero:\n"))

somma= x+y+z

print (f"la somma tra {x}, {y} e {z} e':\n{somma}")

media= somma/3

print (f"la media tra {x}, {y} e {z} e':\n{ media}")