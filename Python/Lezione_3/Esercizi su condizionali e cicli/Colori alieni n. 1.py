"""immagina che un alieno sia stato appena abbattuto in un gioco. 
Crea una variabile chiamata alien_color e assegnale un 
valore di "verde", "giallo" o "rosso".
• Scrivi un'istruzione if per verificare se il colore dell'alieno è verde. 
Se lo è, stampa un messaggio che il giocatore ha appena guadagnato 5 punti.
• Scrivi una versione di questo programma che superi il test if e un'altra che fallisca. 
(La versione che fallisce non avrà alcun output.)"""




colore= str(input("Inserisci un alieno da colpire:\n"))
if colore =="verde":
        print("Complimenti, Hai colpito l'alieno ed hai ottenito 5 punti!!!")
else:
    print("alieno non trovato ritenta!!")
while colore !="verde":
        colore= str(input("Inserisci un alieno da colpire"))
        if colore =="verde":
         print("Complimenti, Hai colpito l'alieno ed hai ottenito 5 punti!!!")
         
        
        else:
            print("alieno non trovato ritenta!!")