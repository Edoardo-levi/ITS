"""Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, 

entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.
a[1] + b[n-1], a[2] + b[n-2], ...
Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c."""

a=[]
b=[]
c=[]


lunghezza=int(input("quanto deve essere lunga la lista?\n"))
print("\ninserisci i valori per la lista A:")
for index in range(lunghezza):
    a.append(int(input(f"a[{index+1}]: ")))                    # con questa scrittura, è possibile ariempire una stringa vuota con dei valori inseriti dall'utente.
                                                               # esempio : se la lunghezza inserita è 5, questa linea di codice mi permette di inserire 5 valori nella lisra a
                                                               # esempio: inserisco i valori 1,2,3,4,5. a[1] saraà 1, a[2] sarà 2, a[3] araà 3 e così via fino ad arrivare ad a[5] che sarà 5

print("\ninserisci i valori per la lisa B:")

for index in range(lunghezza):
    b.append(int(input(f"b[{index+1}]:")))

print(a,b)

for index in range(lunghezza):                                  # con questo ciclo ci andaimo a calcolare la somma incrocaita delle due liste. 
    c.append(a[index]+ b[lunghezza-1-index])                    # con il ciclo for prendiamo l'elemto di a in posizione [index] e lo sommiamo con l'elemento di b in ordine inverso 
                                                                # con la formula lunghezza -1, dove lunghezza -1 è l'ultimo elemento di b. 
                                                                # sottrando idex ci permette di muoverci all'indietro nella lista 

print(f"lista A: {a}\nLista B: {b}\nLista C (Somma Incrociata): {c}")

