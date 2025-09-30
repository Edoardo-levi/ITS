"""Problema 2: 10 punti, facoltativo
Premessa: nell'RSA, per calcolare con python l'esponente privato nota la chave pubblica e noti i due numeri primi p e q, si utilizza la sequente funzione
d = inverse(e, phi) dove ph = (p-1)*(q-1).

Sia dato n (pari a p*q) = 51151902024533551
e siano
e (esponente pubblico) = 3
C=10002041662569686 il messaggio cifrato (l'originale è una parola di sette caratteri alfanumerici)
Decifrare il messaggio
NB: un attacco forza bruta su 7 caratteri ha un costo computazionale pari a 62^6 = 56.800.235.584 (infattibile in python)
NB: ma n=p*q e quindi se riuscissi a trovare i due numeri primi che fattorizzano n, allora potrei applicare euclide inverso (la funzione inverse) per trovare la chiave privata..."""



from Crypto.Util.number import inverse

n = 51151902024533551
e = 3
c = 10002041662569686

# n = p*q ovvero p e q sono due numeri interi molto gradi e tramite il loro prodotto riusciamo a trovare il mod n 

#d è l'esponende privato e matematicamnete è uguale a (e**-1)%funzione di eulero(n)

#la funzione di Eulero = (p-1)*(q-1)

p = 1 #serve solamente per non dividere n per 0

for i in range(2, n): # cerca il primo divisore di n provando tutti gli interi da 2 fino a n-1
    #appena si trova il primo divisore di n che non da resto 0 sarà il nostro p e si interromperà il ciclo
    if n% i == 0: 
        p = i
        break

q = n // p #essendo n = p*q la fomula inversa è dividere n per p per trovare q 

print(f"Il numero primo p è: {p}")
print(f"Il n umero primo q è: {q}")

eulero = (p-1)*(q-1)
print(f"La funzione di Eulero è ugaule a: {eulero}")

d = inverse(e, eulero)  # per trovare l'esponente privato uso inverse e elevato alla -1 per il modulo di eulero

messaggio_decifrato = pow(c, d, n) # decifra il messaggio con la chiave privata 


length = (messaggio_decifrato.bit_length() + 7) // 8 #mi da la lunghezza di byte corrispondente al messaggio
msg_bytes = messaggio_decifrato.to_bytes(length, 'big')#trasforma il messaggio proprio in quella sequenza di byte di lunghezza = length e li ordina dal b yte più significativo
plaintext = msg_bytes.decode('utf-8') #tramite il metodo di codifica utf-8 trasforma questa sequenza di byte in stringa
print("Il Messaggio decifrato è:", plaintext)

# la funzione di eulero è una funzione che permette che per un determinato numero intero positivo n, di trovare i numeri che sono minori uguali di n tale che siano coprimi di n.

# i numneri coprimi sono i numeri che tra di loro hanno come massimo comun divisore 1