'''Progettare un algoritmo che, 
richiesto allo studente il reddito familiare e la media dei voti, 
se il reddito è inferiore a 20.000 € e la media è superiore a 27 approva la borsa di studio, 
altrimenti rifiuta la richiesta visualizzando il messaggio 
"Borsa di studio rifiutata. (Motivo: reddito o media insufficiente)".'''



r=int(input("inserisci il reddito:\n"))
m=float(input("inserisci la media dei voti:\n"))

if r<20000 and m > 27:
    print("Borsa di studio approvata")

else:
    print("Borsa di sudio rifiutata.\n(Motivo: Reddito o media insufficiente.)")