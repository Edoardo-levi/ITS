"""Crea una funzione che generi un numero casuale all'interno di un intervallo specificato dall'utente.
Chiedere all'utente di indovinare il numero entro un numero massimo specificato di tentativi.
Fornire un feedback all'utente dopo ogni ipotesi, indicando se la sua ipotesi è troppo alta, troppo bassa o corretta.
Termina il ciclo quando l'utente indovina correttamente il numero o raggiunge il numero massimo di tentativi."""
import random


def gioco_numeri(max_tent:int) ->str:
    num_estratto= random.randint(0,20)
    tentativi=0
    while tentativi < max_tent:
        try:
            num_inserito = int(input(f"\nTentativo {tentativi + 1}: Inserisci il numero: "))
        except ValueError:
            print("Per favore, inserisci un numero valido.")
            continue
    
        tentativi += 1

        if num_inserito > num_estratto:
            print("Numero troppo alto.")
        elif num_inserito < num_estratto:
            print("Numero troppo basso.")
        
        else:
            print("Numero indovinato")
            print (f"Hai indovinaot il numero al {tentativi} tentativo")
            break
            
            
        
    return ("Hai esaurito i tentativi")

gioco_numeri(6)