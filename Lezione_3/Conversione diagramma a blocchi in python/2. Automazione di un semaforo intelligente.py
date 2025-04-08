"""Progettare un algoritmo che simuli il comportamento di un semaforo intelligente. Questo sistema deve adattare i tempi di durata 
(espressi in percentuale) del verde in base al numero di veicoli presenti sulle principali direzioni di traffico: Nord-Sud ed Est-Ovest. 
Ogni direzione può ricevere una priorità se il numero di veicoli supera una soglia predefinita.

Requisiti:

Se il numero di veicoli in una sola direzione supera la soglia (es. 70 veicoli), quella direzione riceve un tempo minimo garantito per il verde (es. 60%) 
e il restante tempo è assegnato all'altra direzione.
Se entrambe le direzioni superano la soglia, il tempo è equamente suddiviso (50% per ciascuna direzione).
Se nessuna direzione supera la soglia, il tempo è calcolato proporzionalmente al numero totale di veicoli nelle due direzioni.
Stampare la percentuale del tempo assegnato al verde per ciascuna direzione.

"""


nord_sud=int(input("inserisci un valore pre le direzionei NORD-SUD:\n"))
est_ovest=int(input("inserisci un valore pre le direzionei EST-OVEST:\n"))
soglia=70
punti =[nord_sud, est_ovest]
match punti:
    case punti if punti [0] >soglia and punti [1]>soglia:
        time_ns=50
        time_eo=50 
    case  punti if punti[0] > soglia:
        time_ns=60
        time_eo=40

    case punti if punti [1] > soglia:
        time_ns=40
        time_eo=60

    case _:
        time_ns= (nord_sud / (nord_sud+ est_ovest)) * 100
        time_eo= (est_ovest / (nord_sud + est_ovest)) * 100

print(f"Il tempo assegnato alla direzione Nord-Sud è: {time_ns}")
print(f"il tempo assegnato alla direzione Est-Ovest e': {time_eo}")