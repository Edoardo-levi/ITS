"""Scrivere un programma in Python che richieda all'utente di inserire un numero 
intero rappresentante il numero di neonati e utilizzi lo statement match per fornire una risposta appropriata:

- Se il numero inserito è 1, stampare "Congratulazioni!"
- Se il numero inserito è 2, stampare "Wow! Gemelli!"
- Se il numero inserito è 3, stampare "Wow! Tre!"
- Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
- Se il numero inserito è 5, stampare "Incredibile! Cinque!"
- Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito.
"""


n_neonati= int(input("inserisci un numero:\n"))   # creo una variabile che mi permette di inserire da tastiera un numero di neonati

match n_neonati:                                  # creo il Match_statement
    case 1:                                       # verifico se il numero insertio è 1
        print("Congratulazioni")                  # stampo la condizione

    case 2:                                       # verifico se il numero insertio è 2
        print("Wow! Gemelli")                     # stampo la condizione
    
    case 3:                                       # verifico se il numero insertio è 3
        print("Wow! Tre!")                        # stampo la condizione
    
    case 4:                                       # verifico se il numero insertio è 4
        print("Mamma mia Quattro! Wow!")          # stampo la condizione
    
    case 5:                                       # verifico se il numero insertio è 5
        print("Incredibile! Cinque!")             # stampo la condizione
    
    case _:                                       # verifico se il numero insertio è diverso degli altri
        print(f"Non ci credo! {n_neonati} bambini!")# stampo la condizione