"""scrivi una funzione safe_sqrt(number)che calcola la radice quadrata di un numero usando math.sqrt(). 
GestisciValueErrorse l'input è negativo restituendo un messaggio informativo."""
import math

def safe_sqrt(num:int):
    
        if num<0:
            raise ValueError("Radice quadrata non calcolabile! Il numero inserito e' negativo")
        else:
              return math.sqrt(num)


numero=int(input("inserisci un numero:\n"))

funzione=safe_sqrt(numero)
print(f"La radice quadrata del numero {numero} e': {float(funzione):.2f}")
