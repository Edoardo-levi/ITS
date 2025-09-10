"""1-2. Si scriva un programma che dimostri le funzionalità dell'operatore % effettuando le seguenti attività:

Memorizzare un numero in virgola mobile nella variabile x.
Calcolare x%2.0 e memorizzare il risultato nella variabile y.
Visualizzare in maniera distinta x e y.
Si esegua il programma con valori positivi e negativi di x. Che cosa cambia nel comportamento dell’applicazione quando i valori di x sono positivi o negativi?"""



while True:
    try:
        # sostituisco la virgola con il punto per accettare anche "5,5"
        x: float = float(input("Inserisci un numero con la virgola: "))

        # controllo se è intero (cioè senza parte decimale)
        if x%1==0:
            raise ValueError("Errore: hai inserito un numero intero, devi usare la virgola!")

        # se arrivo qui, il numero è valido → calcolo il resto
        y = x % 2.0
        print(f"Valore di x: {x}")
        print(f"Valore di y (x % 2.0): {y}")
        break  # esco dal ciclo solo se va tutto bene

    except ValueError as e:
        print(e)
        print("Riprova!\n")
