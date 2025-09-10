"""1-1. Si scriva un programma che dimostri la natura approssimativa dei numeri in virgola mobile effettuando le seguenti attività:

Memorizzare un numero in virgola mobile nella variabile x.
Calcolare 1.0/x memorizzare il risultato nella variabile y.
Visualizzare il valore di x, y e il prodotto tra x e y.
Sottrarre x dal prodotto tra x e y e mostrarne il risultato."""


x: float =float(input("Inserisci un numero: "))

y =1.0/x
print(f"il valore di x e': {x}, il valore di y e': {y}")

z= x*y
print(f"il prodotto tra x e y e': {z}")

Sottrazioe = z-x
print(f"La sottrazione tra il prodotto di x e y e x e': {Sottrazioe}")
