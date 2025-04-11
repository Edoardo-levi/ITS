'''inizia con il tuo programma dall'esercizio 4-1. 
Crea una copia dell'elenco delle pizze e chiamalo friend_pizzas.
Quindi, fai quanto segue:
• Aggiungi una nuova pizza all'elenco originale.
• Aggiungi una pizza diversa all'elenco friend_pizzas.
• Dimostra di avere due elenchi separati. 
Stampa il messaggio Le mie pizze preferite sono:,
quindi usa un ciclo for per stampare il primo elenco. 
Stampa il messaggio Le pizze preferite del mio amico sono:,
quindi usa un ciclo for per stampare il secondo elenco. 
Assicurati che ogni nuova pizza sia archiviata nell'elenco appropriato'''



pizze:list= ["Margherita", "Boscaiola", "Bufala"]


for pizza in pizze:
    print(f"mi piace la pizza:{pizza}\n")
    
print ("MI PIACE TANTIISSIO LA PIZZA !!!!")

friend_pizzas= pizze[:]                                                 #faccio una copia della lista pizze
print(f"La copia della lista {pizze} e':\n{friend_pizzas}")


pizze.append("Capricciosa")


friend_pizzas.append("Napoli")
print("Le mie pizze preferite sono:")
for pizza in pizze:
    print(pizza)
print("Le pizze preferite del mio amico sono:")
for pizza in friend_pizzas:
    print(pizza)