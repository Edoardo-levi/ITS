'''ripeti l'esercizio inserisci una citazione famosa, 
ma questa volta, rappresenta il nome della persona famosa
usando una variabile chiamata famous_person. 
Quindi componi il tuo messaggio e rappresentalo con una nuova 
variabile chiamata message. 
Stampa il tuo messaggio.'''

famous_person= str(input("inserisci il nome di chi ha fatto la citazione:\n"))
citazione= str (input("inserisci la citazione: \n"))
print (f"\n\nuna volta {famous_person.title()} disse:\n \"{citazione}\"")