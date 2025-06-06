""" Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali."""

def prodotto (prodotti:dict) ->dict:

    new_dict={}
    for key, value in prodotti.items():
        if value<50:
            incremento= round(value + (value*10)/100,2)
            new_dict[key] = [incremento]
    print(new_dict)


prodotto({"pane":50, "carne":20, "pollo":25})