"""Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. 
Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
Mostri quanti buoni sconto avanzano al termine dell'acquisto."""





barrette = int(input("Inserisci il numero di barrette che vuoi acquistare:\n"))

buoni = barrette            # Ogni barretta contiene un buono
barrette_totali = barrette  # inizialmente, il numero totale di barrette è uguale a quelle acquistate

while buoni >= 6:
    barrette_omaggio = buoni // 6        # Calcolo delle barrette gratuite che si possono ottenre 
    barrette_totali += barrette_omaggio  # Aggiungiamo le barrette omaggio al totale
    buoni = buoni % 6 + barrette_omaggio # buoni avanzati + quelli ottenuti dalle barrette nuove  

#numero totale di barrette e i buoni avanzati
print(f"Numero totale di barrette: {barrette_totali}")
print(f"Buoni sconto avanzati: {buoni}")
