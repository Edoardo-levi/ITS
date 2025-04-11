"""scrivi una funzione chiamata favorite_book() che accetta un parametro, titolo. 
La funzione dovrebbe stampare un messaggio, come "Uno dei miei libri preferiti è Alice nel paese delle meraviglie". 
Chiama la funzione, assicurandoti di includere un titolo di libro come argomento nella chiamata di funzione."""


def favorite_book(titolo:str):
    print(f"Uno dei miei libri preferiti e': {titolo}")


print("inserisci un titolo del libro:")

libro=favorite_book(input())
