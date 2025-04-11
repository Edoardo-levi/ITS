"""scrivi una funzione chiamata city_country() 
che prenda il nome di una città e del suo paese. 
La funzione dovrebbe restituire una stringa formattata in questo modo: "Santiago, Cile". 
Chiama la tua funzione con almeno tre coppie città-paese e stampa i valori restituiti."""


def city_country(citta:str, paese:str):
    print(f"{citta}, {paese}")

cont=0


while cont!=3:
    city=input("inserisci una citta':\n")
    country=input("inserisci un paese:\n")
    citta_paese=city_country(city, country)
    cont+=1

