"""Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista."""


def frequency_dict(elements: list) -> dict:
    freq = {}
    for elem in elements:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1
    return freq