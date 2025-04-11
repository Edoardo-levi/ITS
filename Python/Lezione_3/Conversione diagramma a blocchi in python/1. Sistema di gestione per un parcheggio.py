'''Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli da un 
parcheggio con un numero massimo di posti dati in input. L'utente può inserire una '
'delle seguenti opzioni "ingresso", "uscita", "stato", "esci". Per ogni opzione:

se l'utente inserisce "ingresso", verifica se ci sono posti disponibili, quindi incrementa il numero di posti occupati;
se l'utente inserito "uscita", verifica che ci siano veicoli nel parcheggio, quindi decrementa il numero di posti occupati;
se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
se l'utente inserito "esci", termina l'algoritmo.
Torna all'inserimento di un'opzione finché l'utente non seleziona "esci".'''




print("inserisci una parola:\n\
Ingresso per occupare un posto ,\n\
Uscita per liberare il posto,\n\
Stato per mostrare il numero dei posti liberi e occupati,\n\
Esci per uscire dall'operazione\n")


max_posti=int(input("inserisci i posti massimi disponibili:\n"))

liberi=max_posti
while True:
    opzione=(input("Opzione: ")).lower()

    match opzione:
        case "ingresso":
            if liberi>0:
                liberi-=1
                print(f"hai prenotato un posto!\nPosti disponibili:{liberi}")
            
            else:
                print("Non ci sono posti liberi")
            
        case "uscita":
            if liberi < max_posti:
                liberi+=1
                print(f"hai liberato un posto!\nPosti disponibili:{liberi}")
            
            else:
                print("tutti i posti sono gia' disponibili")
            
        case "stato":
            print(f"i posti liberi sono: {liberi}\nI posti occupati sono: {max_posti-liberi}")
        
        case "esci":
            break
        
        case _: 
            print("operazione non valida")