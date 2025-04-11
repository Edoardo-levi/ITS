"""Progettare un algoritmo che richieda all’utente di inserire la sua età.
L'algoritmo deve:
controllare se l’età è compresa tra 18 e 65 anni. 
Se sì, mostrare un messaggio che indica che l’utente può partecipare all’attività;
se l’età non rientra nell’intervallo, verificare se è inferiore a 18 oppure maggiore di 65. 
Se sì, mostrare un messaggio che indica che l’utente non può partecipare perché 
ha superato l'età massima consentita o non ha raggiunto l'età minima consentita."""

eta=int(input("inserisci un eta': "))

if eta >= 18 and eta <=65:
    print("puoi partecipare all'attiva")

else:
    if eta<18:
        print("Non puoi partecipare alle attivita' perche' non hai raggiunto l'eta' minima richiesta")
    else:
        print("Non puoi partecipare alle attivita' perche' hai superato l'eta' minma consentita")

