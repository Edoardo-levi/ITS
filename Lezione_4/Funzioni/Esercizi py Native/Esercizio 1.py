"""sito esercizi =https://pynative.com/python-functions-exercise-with-solutions/"""



"""Creare una funzione in Python:
Scrivi un programma per creare una funzione che accetta due argomenti, nome ed età, e ne stampa il valore."""


def dati(nome:str, eta:int):

    return nome, eta



name,age=dati(input("inserisci il nome dell'utente:\n"),int(input("inserisci l'eta dell'utente:\n")))

print(f"I dati dell'utente sono: {name} {age}") 
