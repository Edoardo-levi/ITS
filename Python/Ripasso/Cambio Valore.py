"""Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sommato 1."""

x: int= int(input("inserisci un numero: "))

if x%2==0:
    divisione=x//2
    print(divisione)
else:
    moltiplicazione=(x*3)+1
    print(moltiplicazione)


# Risolvendolo con la funzione 
def collatz (x):
    if x%2==0:
        divisore=x//2
        return divisore
    else:
        moltiplicatore=(x*3)+1
        return moltiplicatore
    
prova=collatz(int(input("inserisci un numero: ")))
print(prova)
