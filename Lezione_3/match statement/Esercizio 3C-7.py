"""Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", 
mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement."""

moneta=1
testa=0
croce=0

while moneta <=8:
    print(f"risultato del lancio: {moneta}")
    lancio=input("insercisci t (testa) oppure c (croce):\n")
    moneta +=1
    match lancio:
        case "t" | "T":
            testa+=1
        
        case "c" | "C":
            croce +=1

print(f"il risultato Testa e' uscito: {testa} volte e la sua percentuale e': {((testa/8) *100):.2f}%")
print(f"il risultato Croce e' uscito: {croce} volte e la sua percentuale e': {((croce/8) *100):.2f}%")