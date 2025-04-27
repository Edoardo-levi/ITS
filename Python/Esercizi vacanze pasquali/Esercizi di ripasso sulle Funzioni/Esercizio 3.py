"""Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario.
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori."""

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:  
     risultato = lista.copy()
     for elemento, conteggio in da_rimuovere.items():
        for i in range(conteggio):
            if elemento in risultato:
                risultato.remove(elemento)
            else:
                break  

     return risultato
