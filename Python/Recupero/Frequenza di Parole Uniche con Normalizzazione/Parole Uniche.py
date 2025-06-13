"""Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.
Requisiti:
● Suddividi l’input sugli spazi bianchi per ottenere i token.
● Normalizza ogni token:
1. Converti in minuscolo.
2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip()
con un insieme di caratteri di punteggiatura).
● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della
punteggiatura.
● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi
interi."""

from string import ascii_lowercase, punctuation

def parole_uniche(text:str)-> dict[str:int]:
    dizionario:dict={}
    text.split(" ")         # con questa funzione posso ottente le parole dell text tutte separate eritorna una lista di stringhe 

    for token in text:      # il token sarebbe il singolo carattere della lista 
        token_loewwr:str=token.lower()
        clean_token:str=token_loewwr.strip(punctuation)
        if not clean_token:
            continue
        if clean_token in dizionario:
            dizionario[clean_token]+=1
        else:
            dizionario[clean_token]=1
    
    return dizionario
        