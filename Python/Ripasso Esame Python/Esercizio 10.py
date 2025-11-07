"""Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%.
"""

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    new_dict:dict={}
    for nome, prezzo in prodotti.items():
        if prezzo>20:
            new_dict[nome]=prezzo*0.9
    return new_dict