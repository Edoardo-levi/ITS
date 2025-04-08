"""scrivi una funzione chiamata make_shirt() 
che accetti una taglia e il testo di un messaggio che dovrebbe essere stampato sulla maglietta. 
La funzione dovrebbe stampare una frase che riassuma la taglia della maglietta e 
il messaggio stampato su di essa. Chiama la funzione una volta usando argomenti posizionali per 
creare una maglietta. Chiama la funzione una seconda volta usando argomenti per parole chiave."""


def make_shirt(taglia:str, testo:str):
    print(f"la taglia selezionata per la maglietta e': {taglia}\n\
e il testo da stampare e': {testo} ")
    
misura=str(input("inserisci una misura per la maglietta:\n"))
frase=str(input("inserisci una frase da far stampare sulla maglietta:\n"))

#funzione che passa argomenti per posizione: 
maglietta=make_shirt(misura, frase)

#funzione che passa argomenti per parola chiave
make_shirt(taglia=misura, testo=frase)