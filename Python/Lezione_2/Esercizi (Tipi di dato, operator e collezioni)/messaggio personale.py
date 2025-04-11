''' usa una variabile per rappresentare il nome di una persona e 
stampa un messaggio per quella persona.
Il tuo messaggio dovrebbe essere semplice, 
come "Ciao Eric, vuoi imparare un po' di Python oggi?"'''

nome= str (input("inserisci un nome al quale mandare un messaggio: "))
messaggio = str (input("\ninserisci un messaggio da inviare: "))

print(f"il messaggio inviato e': {messaggio} ed e' stato inviato a: {nome}")