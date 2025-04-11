"""Progetta un algoritmo che gestisca l'iscrizione degli studenti a corsi disponibili in una università. '
'Per ogni corso ci sono un massimo di 100 posti liberi. '
'Richiesto il nome del corso, mostra un menu con le seguenti opzioni "iscrivi", "annulla", "visualizza", '
'"elimina", ed "Esci".

se l'utente inserisce "iscrivi", verifica se ci sono posti disponibili per il corso, quindi incrementa'
' il numero di posti occupati;
se l'utente inserisce "annulla", decrementa il numero di posti occupati;
se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati nel corso;
se l'utente inserisce "elimina", elimina il corso e richiedi un nuovo corso;
se l'utente inserisce "esci", termina l'algoritmo."""



nome_corso=input("inserisci il nome del corso:\n")

max_posti=100
print("\ninserisci un opzione tra quelle richieste:\n\
Iscriviti: Per iscriversi al corso;\n\
Annulla: Per eliminare l'iscrizione al corso;\n\
Visualizza: mostrare il numero di posti liberi e occupati;\n\
Elimina: Eliminare la domanda di iscrizione al corso;\n\
Esci: Terminare l'operazione di registrazione\n")


while True:
    opzione=input()
    match opzione:
        case "iscriviti":
            if max_posti > 0:
                max_posti-=1
                print(max_posti)
            else: 
                print("NON CI SONO POSTI DISPONIBILI\n")
        case "annulla":
            if max_posti < 100:
                max_posti += 1
                print(max_posti)
            else:
                print("TUTTI I POSTI SONO GIA' DISPONIBILI\n")
            
        case "visualizza":
            print(max_posti)
            print( 100-max_posti)
        
        case "elimina":
            print("inserisci un opzione tra quelle richieste:\n")
        
        case "annulla":
            break

        case _:
            print("Opzione non valida")
            break
