'''Si scriva un programma che dimostri la natura approssimativa dei numeri in virgola mobile effettuando le seguenti attività:

#Memorizzare un numero in virgola mobile nella variabile x.
#Calcolare 1.0/x memorizzare il risultato nella variabile y.
#Visualizzare il valore di x, y e il prodotto tra x e y.
#Sottrarre x dal prodotto tra x e y e mostrarne il risultato.'''



x= float(input("inserisci un numero:\n"))
y= 1.0/x

print (f"il valore di x e': {x}\nil valore di y e': {y:.2f}")
z= x*y

print (f"il valore del prodotto fra {x} e {y:.2f} e':\n{z:.2f}")

k= z-x

print (f"il valore della differenza tra {z:.2f} e {x} e':\n{k:.2f}")

