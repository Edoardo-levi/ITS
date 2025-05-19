"""Crea una funzione che definisca un prodotto con un nome, un prezzo e una quantità.
Crea funzioni che gestiscono il carrello della spesa, consentendo all'utente di aggiungere, rimuovere e visualizzare i prodotti nel carrello.
Crea una funzione che calcoli il totale del carrello e applichi eventuali sconti o tasse.
Crea una funzione per stampare un riepilogo dettagliato del carrello inclusi prodotti e totali.
Implementa un ciclo for per iterare sugli articoli nel carrello e stampare informazioni dettagliate su ciascun prodotto e sul totale."""

def crea_prodotto(nome: str, prezzo: float, quantita: int) -> dict:
    return {"nome": nome, "prezzo": prezzo, "quantita": quantita}

def aggiungi_prdotto(carrello: list, prodotto: dict):
    carrello.append(prodotto)

def rimuovi_prodotto(carrello: list, nome_prdotto: str):
    for elemento in carrello:
        if elemento["nome"] == nome_prdotto:
            carrello.remove(elemento)
            print(f"L'elemento {nome_prdotto}, e' stato rimosso dal carrello ")

def visualizza_prodotti(carrello: list):
    if not carrello:
        print("Il carrello e' vuoto")
    else:
        for prodotto in carrello:
            print(f" {prodotto['nome']} (x{prodotto['quantita']}) €{prodotto['prezzo']}")

def totale_carrello(carrello: list, sconto: float, tasse: float) -> float:
    totale = 0
    for prodotto in carrello:
        totale += prodotto["prezzo"] * prodotto["quantita"]
    sconto_applicato = totale * (sconto / 100)
    tasse_applicate = totale * (tasse / 100)
    prezzo_finale = totale - sconto_applicato + tasse_applicate
    return prezzo_finale

def riepilogo(carrello: list, sconto: float = 0, tasse: float = 0):
    if not carrello:
        print("Il carrello è vuoto")
    else:
        for prodotto in carrello:
            totale_prodotto = prodotto["prezzo"] * prodotto["quantita"]
            print(f" {prodotto['nome']} (x{prodotto['quantita']}) €{prodotto['prezzo']}")
            print(f"Totale: €{totale_prodotto}")
        
        finale_totale = totale_carrello(carrello, sconto, tasse)
        print(f"\nSconto applicato: {sconto}%")
        print(f"Tassa applicata: {tasse}%")
        print(f" Totale finale da pagare: €{finale_totale:.2f}")


# Creazione del carrello
carrello = []

# Aggiunta prodotti
aggiungi_prdotto(carrello, crea_prodotto("Laptop", 799.99, 1))
aggiungi_prdotto(carrello, crea_prodotto("Mouse", 25.50, 2))
aggiungi_prdotto(carrello, crea_prodotto("Zaino", 40.00, 1))

# Visualizzazione prodotti
visualizza_prodotti(carrello)

# Rimozione prodotto
rimuovi_prodotto(carrello, "Mouse")

# Riepilogo finale con sconto del 10% e tasse del 5%
riepilogo(carrello, sconto=10, tasse=5)
