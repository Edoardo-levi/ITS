"""scrivi una funzione che memorizza informazioni su un'auto in un dizionario. 
La funzione dovrebbe sempre ricevere un nome di produttore e un modello. Dovrebbe quindi accettare un numero arbitrario di argomenti di parole chiave. 
Chiama la funzione con le informazioni richieste e altre due coppie nome-valore, come un colore o una caratteristica opzionale.
 La tua funzione dovrebbe funzionare per una chiamata come questa: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
 Stampa il dizionario che viene restituito per assicurarti che tutte le informazioni siano state memorizzate correttamente."""

def caratteristiche_auto(produttore: str, modello: str, **kwargs):
    auto: dict = {"produttore": produttore, "modello": modello}
    auto.update(kwargs)
    return auto

# Input per produttore e modello
produttore = input("Inserisci il produttore dell'auto:\n")
modello = input("Inserisci il modello dell'auto:\n")

# Chiamata corretta della funzione
macchina = caratteristiche_auto(produttore, modello, tow_package=True)
car=caratteristiche_auto(produttore,modello,tow_package=True )
# Stampa del risultato
for key, value in car.items():
    print(f"{key}: {value}")
