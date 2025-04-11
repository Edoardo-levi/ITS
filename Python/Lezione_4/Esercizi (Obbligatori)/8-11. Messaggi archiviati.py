""" inizia con il tuo lavoro dall'esercizio 8-10. 
Chiama la funzione send_messages() con una copia dell'elenco dei messaggi. 
Dopo aver chiamato la funzione, stampa entrambi gli elenchi per mostrare che 
l'elenco originale ha mantenuto i suoi messaggi."""

 
sent_message=[]

def send_messages(*args):
    for i in args:
            print(i)
            sent_message.append(i)

send_messages("Alessio", "Mario", "Valentino", "Mirko", "Alfio")
print(*sent_message)