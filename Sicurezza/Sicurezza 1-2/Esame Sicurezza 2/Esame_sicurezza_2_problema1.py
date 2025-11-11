"""Crittografia

Sia dato il messaggio decifro (convertito in numero intero in base 10): 

204751668535
Il messaggio decifro è stato ottenuto cifrando il messaggio originale con algoritmo RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3
Provare a decifrare il messaggio decifro
NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente."""


# dati 
testo_decifro = 204751668535
modulo = 514948966453
esponente = 3

# variablie da usare se viene trovato il testo decifro 
testo_trovato = False

lettere_ricercate = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for carattere1 in lettere_ricercate:
    if testo_trovato == True:
        break
    for carattere2 in lettere_ricercate:
        if testo_trovato == True:
            break
        for carattere3 in lettere_ricercate:
            if testo_trovato == True:
                break
            for carattere4 in lettere_ricercate:
                if testo_trovato == True:
                    break
                for carattere5 in lettere_ricercate:
                    if testo_trovato == True:
                        break
                    parola = carattere1 + carattere2 + carattere3 + carattere4 + carattere5
                    try:
                       
                        testo = int(parola.encode("utf-8").hex(), 16) # prende la stringa parola e la trasforma in una sequenza di byte
                                                                      # .hex() crea una stringa esadecimale du byte 
                                                                      # ,16 converte la stringa esadecimale in un intero base 10
                        decifro = pow(testo, 3, modulo)               # decifro il messaggio con l'esponente pubblico = 3 e il modulo

                        if decifro == testo_decifro:                  # se il messaggio decifrato è = al testo_decifo
                            print(f"Testo trovato: {parola}")         # lo stampo 
                            testo_trovato = True

                    except:
                        # non faccio nulla
                        continue



if testo_trovato == False:
    print("Nessun testo trovato")

