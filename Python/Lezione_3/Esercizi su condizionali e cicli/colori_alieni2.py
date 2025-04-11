
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



if colore=="verde":
    print("hai ottenuto 5 punti")
else: 
    print("hai ottenuto 10 punti")