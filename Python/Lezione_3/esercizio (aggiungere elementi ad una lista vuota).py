'''
1.Crea un elenco vuoto denominato numeri
2. Utilizzando il ciclo for, scrivere un programma Python che richieda all'utente
di inserire il file lunghezza dell'elenco 
e quindi riempie i numeri dell'elenco con i numeri da 1
alla lunghezza inserita dall'utente
'''


len= int (input("inserisci la lunghezza della lista"))
num= []
for i in range(1, len+1):               # lent +1 perchè così includo tutta la lunghezza
                                        # senza il +1 avrebbe aggiunto i numeri fino a 4 
                                        # mentre io avevo detto che la lunghezza deve essere 5
                                        #quindi aggiungendo il +1 mi aggiunge tutti i numeri quanti la lunghezza desiderata
    num.append(i)
    
print (num)