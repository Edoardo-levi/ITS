"""Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori."""


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    copia=dict1.copy()
    for key, value in dict2.items():
        if key in copia:
            copia[key]+=value
        else:
            copia[key]=value
    return copia
