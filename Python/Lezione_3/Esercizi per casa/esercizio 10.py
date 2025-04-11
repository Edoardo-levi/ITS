"""Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti."""

numeri=[]
somma=0
sommaD=0
media=0
cont=0
frequenze={}


while True:
    num=int(input("inserisci un numero (0 per terminare il ciclo):\n"))

    if num==0:
        break

    numeri.append(num)

    if num %2==0:
        somma+=num

    else:
        sommaD+=num
        cont+=1


    if num in frequenze:                                # calcola quante volte i numeri sono stati inseriti
        frequenze[num] += 1
    else:
        frequenze[num] = 1


media= sommaD/cont
    
max_frequenza = max(frequenze.values())                                                                     # calcola il numero massimo 
numeri_frequenza_massima = [num for num, freq in frequenze.items() if freq == max_frequenza]                # calcola i numeri inseriti più volte 


print(f"la somma dei numeri pari e':\n{somma}\nLa media dei numeri dispari e':\n{media:.2f}")
for num in numeri_frequenza_massima:
    print(f"Numero più frequente: {num} ({max_frequenza} volte)")

