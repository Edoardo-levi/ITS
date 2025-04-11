"""Scrivere un programma che acquisisca una 
stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. Il risultato deve essere visualizzato in output."""

stringa= str(input("inserisci una stringa:\n"))
conta=0
for spazi in stringa:
    if spazi==" ":
        conta+=1

print(conta)