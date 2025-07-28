"""Scrivere un programma PYTHON che a partire da una stringa la cifra con la tecnica XOR
Successivamente mostrare che la stringa cifrata, riapplicando lo stesso XOR, torna la stringa originale
Per fare lo XOR utilizzate un solo valore: 57
Quindi data la stringa di esempio “Nel mezzo del cammin di nostra vita”, dovete fare per ogni carattere della stringa lo xor con il valore 57
“N” xor 57, “e” xor 57, …
Ottenendo una lista di numeri es: 78 (che è il codice asciii  della lettera N) xor (si indica con il simbolo ^) => 78 ^ 57 = 119
E così via per tutta la stringa.
Al termine stampare la lista di numeri ottenuti
In fondo a partire dalla lista di numeri, riapplicare lo xor sempre con 57 e quindi ottenere (ricostruendola) la stringa originale
NB: potreste utilizzare input(“…”) in modo da leggere sia la stringa da cifrare, sia il valore segreto da applicare come xor
"""

stringa:str=input("Inserisci una stringa da cifrare:\n")
numero_codifica=int(input("Inserisci un numero per la codifica ascii:\n"))
numeri_codificati:list=[]
carattere_decodificato:list=[]
stringa_decodificata=""

for index in stringa:
    carettere_codificato=ord(index)^numero_codifica
    numeri_codificati.append(carettere_codificato)

print(f"Numeri cifrati: {numeri_codificati}")

for index in numeri_codificati:
    numero_decodificato= index^numero_codifica
    carattere_decodificato.append(numero_decodificato)

print(f"Numeri decifrati: {carattere_decodificato}")

for index in carattere_decodificato:
    stringa_decodificata+=chr(index)
print(f"La parola decodificata è: {stringa_decodificata}")