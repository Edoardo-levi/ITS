"""Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, 
restituisca il risultato della potenza base^exponent. Supporre che base sia un numero intero e 
che l'esponente sia un valore intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!"""

def integerPower(base:int, esponente:int)->int:

    if esponente<0 and esponente==0:
        print("Errore! Il numero deve essere positivo e diverso da 0")
    
    else:
        for i in range (esponente):
            risultato= base**esponente
    return risultato

print(integerPower(3,3))