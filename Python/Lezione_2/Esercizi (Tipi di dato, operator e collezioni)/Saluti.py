''' inizia con l'elenco che hai usato nell'esercizio 3-1,
ma invece di stampare solo il nome di ogni persona, stampa un messaggio per loro.
Il testo di ogni messaggio dovrebbe essere lo stesso,
ma ogni messaggio dovrebbe essere personalizzato con il nome della persona.'''

nomi= ["Lorenzo", "Matteo", "Rebecca", "Sofia"]
messaggio=str (input("inserisci un messaggio:\n"))

for index in range(4):
    print (f"{nomi[index]}: {messaggio}")