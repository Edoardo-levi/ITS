"""Crea una funzione che prenda un paragrafo e conti il numero di occorrenze di ogni parola.
La funzione dovrebbe stampare un rapporto che mostra le parole più frequenti e il loro numero di occorrenze.
Puoi usare un ciclo for per iterare sulle parole nel testo e un dizionario per memorizzare le occorrenze."""

def analisi_testo(testo: str):
    testo = testo.lower()

    parole: list[str] = testo.split()

    conta_parole: dict[str, int] = {}

    for word in parole:
        if word in conta_parole:
            conta_parole[word] += 1
        else:
            conta_parole[word] = 1

    for word in conta_parole:
        print(f"La parola {word} compare {conta_parole[word]} volte ")

text: str = "Testo di prova: Ciao come stai?"
analisi_testo(text)