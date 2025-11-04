"""Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori."""



def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    somma_dict=dict1
    for keys, value in dict2.items():
        if keys in somma_dict:
            somma_dict[keys]+=value
        else:
            somma_dict[keys]=value
    return somma_dict
