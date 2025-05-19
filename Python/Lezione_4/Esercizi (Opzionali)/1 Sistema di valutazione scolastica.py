"""Crea una funzione che prenda il nome di uno studente e i suoi punteggi in diverse materie come input.
La funzione calcola il punteggio medio e stampa il nome dello studente, la media e un messaggio che indica 
se lo studente ha superato l'esame (media >= 60) o non è stato superato.
Crea un ciclo for per iterare su un elenco di studenti e punteggi, chiamando la funzione per ogni studente."""

def calcolaMedia(nome:str, punteggi:list[float]) -> dict:
    punteggio_medio = sum(punteggi)/ len(punteggi)

    if punteggio_medio >= 60:
        messaggio= f"Lo studente {nome}, ha superato l'esame con punteggio medio pari a {punteggio_medio:.2f}"
        esito = "Superato"
    else:
        messaggio= f"Lo studente {nome}, non ha superato l'esame con punteggio medio pari a {punteggio_medio:.2f}"
        esito= "Non superato"
    print(messaggio)

    

    return {"Nome": nome, "Media": punteggio_medio, "Esito": esito}


studenti = [
    ("Luca", [75, 80, 65]),
    ("Anna", [55, 60, 58]),
    ("Marco", [90, 85, 92]),
    ("Giulia", [45, 50, 40])
]

for nome, punteggi in studenti:
    calcolaMedia(nome, punteggi)