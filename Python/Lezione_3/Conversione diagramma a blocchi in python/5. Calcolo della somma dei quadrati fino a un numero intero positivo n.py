"""Progettare un algoritmo che, dato un numero intero positivo n definito dall'utente, calcoli la somma:

12 + 22 + 32 + 42 + 52 + ... + n2,

mostrando in output il risultato. Se n è negativo, l'algoritmo mostra un messaggio di errore e termina. """

n=int(input("inserisci un numero:\n"))
if n%1==0 and n>0:
    sum=0
    i=0
    for i in range (1,n+1):
        sum+= i*i
        i+=1
    
    print(sum)

else:
    print("Errore!, N deve essre positivo")