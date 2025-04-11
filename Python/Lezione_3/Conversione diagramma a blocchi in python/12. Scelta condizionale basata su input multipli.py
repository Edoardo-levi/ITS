"""Progettare un algoritmo che richieda all’utente di inserire un numero variabile n di valori x e y. L'algoritmo deve:

calcolare il prodotto di x e y solo se entrambi i valori sono positivi;
calcolare la somma di x e y solo se uno dei due valori è negativo;
mostrare il risultato dell’operazione effettuata o un messaggio di errore altrimenti."""

n= int(input("quante coppie di valore x e y vuoi inserire? "))

i=0
for i in range (n):
    x=int(input("inserisci un numero X: "))
    y=int(input("inserisci un numero y: "))

    if x>0 and y>0:
        result=x*y
        print(result)
    else:
        if x<0 and y<0:
            print("Erorre")
        else:
            result=x-y
            print(result)
    i+=1
