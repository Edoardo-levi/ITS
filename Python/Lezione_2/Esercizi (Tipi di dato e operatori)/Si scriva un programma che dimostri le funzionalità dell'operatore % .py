'''Si scriva un programma che dimostri le funzionalità dell'operatore % effettuando le seguenti attività:

Memorizzare un numero in virgola mobile nella variabile x.
Calcolare x%2.0 e memorizzare il risultato nella variabile y.
Visualizzare in maniera distinta x e y.
Si esegua il programma con valori positivi e negativi di x. 
Che cosa cambia nel comportamento dell’applicazione quando i valori di x sono positivi o negativi?'''

x = float(input("inserisci un numero:\n"))  # definisco come float la viariabile x
y= x%2.0    #eseguo la divisione tra x e 2.0

print (f"il valore della variabile x e':\n{x}\nIl valore della variabile y e': {y:.2f}") # visualizzio a schermo il valore di x e y (y con solo due cifre dopo la virgola)

print("Nel comportamento dell'applicazione notiamo che mettendo sia negativi che positivi il risultato è sempre positivo")