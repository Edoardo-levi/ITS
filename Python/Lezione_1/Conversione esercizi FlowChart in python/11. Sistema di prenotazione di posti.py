'''Progetta un algoritmo per gestire la prenotazione dei posti in una sala che contiene 20 sedie libere. 
L'utente può inserire una delle seguenti opzioni "prenota", "libera", "visualizza", "esci". Per ogni opzione:

se l'utente inserisce "prenota", se ci sono ancora sedie libere, decrementa di uno il numero di posti liberi;
se l'utente inserisce "libera", incrementa di uno il numero di sedie libere;
se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati;
se l'utente inserisce "esci", termina l'algoritmo.
Torna all'inserimento di una opzione finché l'utente non seleziona "esci".'''

liberi=20
print("inserisci una parola:\n\
Prenota per prenotare il posto,\n\
Libera per liberare il posto,\n\
Visualizza per mostrare il numero dei posti liberi e occupati,\n\
Esci per uscire dall'operazione\n")




while True:
    operazione=input()
    match operazione:
        case "prenota":
            if liberi >0:
                liberi-=1
                print(f"hai prenotato un posto!\nPosti disponibili:{liberi}")
        
            else:
                print("Non ci sono posti disponibili")

        case "libera":
            if liberi < 20:
                liberi +=1
                print(f"hai liberato un posto!\nPosti disponibili:{liberi}")
            else:
                print("Tutti i posti sono gia' disponibili")
            
        case "visualizza":
            print(f"i posti liberi sono: {liberi}\n")
            print(f"i posti occupati sono: {20-liberi}")
        
        case "esci":
            break
        case _:
            print("operazione non valida ")

