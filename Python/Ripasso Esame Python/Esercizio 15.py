"""Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave."""

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    new_dict:dict={}
    for key,value in tuples:
        if key in new_dict:
            new_dict[key].append(value)
        else:
            new_dict[key]=[value]
    return new_dict