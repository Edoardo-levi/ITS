"""Scrivi una funzione check_length(), che accetta una stringa come argomento.
Usando if / else, controlla se la lunghezza della stringa è maggiore, minore o uguale a 10
caratteri."""


def check_length (parola:str):
    if len(parola)>10:
        print("la lunghezza della stringa e' maggiore di 10")
    
    elif len(parola)<10:
        print("la lunghezza della stringa e' minore di 10")
    else:
        print ("la lunghezza della stringa e' uguale a 10")

    
stringa= check_length('ciao')