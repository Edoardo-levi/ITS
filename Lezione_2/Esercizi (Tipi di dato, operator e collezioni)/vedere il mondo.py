''' pensa ad almeno cinque posti nel mondo che vorresti visitare.
• Memorizza le posizioni in un elenco. Assicurati che l'elenco non sia in ordine 
alfabetico.
• Stampa il tuo elenco nel suo ordine originale.
Non preoccuparti di stampare l'elenco in modo ordinato; 
stampalo semplicemente come un elenco Python grezzo.
• Usa sorted() per stampare il tuo elenco in ordine 
alfabetico senza modificare l'elenco effettivo.
• Mostra che il tuo elenco è ancora nel suo ordine originale stampandolo.
• Usa sorted() per stampare il tuo elenco in ordine alfabetico 
inverso senza modificare l'ordine dell'elenco originale.
• Mostra che il tuo elenco è ancora nel suo ordine originale stampandolo di nuovo.
• Usa reverse()  per cambiare l'ordine del tuo elenco. 
Stampa l'elenco per mostrare che il suo ordine è cambiato.
• Usa reverse() per cambiare di nuovo l'ordine del tuo elenco.
Stampa l'elenco per mostrare che è tornato al suo ordine originale.
• Usa sort() per cambiare il tuo elenco in modo che sia memorizzato in ordine 
alfabetico. Stampa l'elenco per mostrare che il suo ordine è stato cambiato.
• Usa sort() per modificare la tua lista in modo che venga 
archiviata in ordine alfabetico inverso.
Stampa la lista per mostrare che il suo ordine è cambiato.'''



luoghi: list= ["NewYor", "Londra", "Lapponia", "Amsterdam","Los Angeles"]

print (*luoghi)

luoghi.sort()                  # ordina la lista in ordine alfabetico
print (*luoghi, sep=", ")      # con questa scrittura possiamo separare gli elementi di una lista con un carattere a nostra scelta.
luoghi.sort() 

luoghi.reverse()
print(*luoghi, sep=", ")       # ordina la lista in ordine alfabetico al contrario

luoghi.reverse()
print(*luoghi, sep=", ")