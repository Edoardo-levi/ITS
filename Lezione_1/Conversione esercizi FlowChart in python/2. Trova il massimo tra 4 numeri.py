"""Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente."""


# metodo con il while:
massimo=int(input("inserisci il primo numero che sara' inizialmente il nostro massimo:\n"))

cont=1

while cont<4:
    cont+=1
    n=int(input("inserisci un numero:\n"))
    if n>massimo:
        massimo=n

print(massimo)



# metodo con il for:


mass=int(input("inserisci il primo numero che sara' inizialmente il nostro massimo:\n"))

i=0
for i in range(0,4):
    i+=1
    n=int(input("inserisci un numero:\n"))
    if n>mass:
        mass=n
print(mass)


# metodo con il Repeat Untill

massimo= int(input("inserisci un numero che sara' inizialmente il nostro massimo:\n"))

cont=1
while True:
    
    

    n=int(input("inserisci un numero:\n"))

    if n>massimo:
        massimo=n
    cont+=1
    if cont==4:
         break
print(massimo)