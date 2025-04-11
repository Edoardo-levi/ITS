"""utilizzando uno dei programmi scritti in questo capitolo, 
aggiungi diverse righe alla fine del programma che eseguono le seguenti operazioni:
• Stampa il messaggio I primi tre elementi nell'elenco sono:. 
Quindi usa una slice per stampare i primi tre elementi dall'elenco di quel programma.
• Stampa il messaggio Tre elementi dal centro dell'elenco sono:. 
Quindi usa una slice per stampare tre elementi dal centro dell'elenco.
• Stampa il messaggio Gli ultimi tre elementi nell'elenco sono:. 
Quindi usa una slice per stampare gli ultimi tre elementi nell'elenco.
"""

pizze:list= ["Margherita", "Boscaiola", "Bufala","Capiricciosa", "Napoli", "Marinara"]


for pizza in pizze:
    print(f"mi piace la pizza:{pizza}\n")
    
print ("MI PIACE TANTIISSIO LA PIZZA !!!!")


print (f"i primi tre elementi della lista sono: {pizze[:3]}")
center= len(pizze) //2
if len(pizze) % 2 == 0:
    print(f"Tre elementi dal centro dell'elenco sono:{pizze[center-1]},{pizze[center]}")
else:
    print(f"Tre elementi dal centro dell'elenco sono:{pizze[center-1]} ,{pizze[center]} ,{pizze[center+1]}")
    
print(f"Gli ultimi tre elementi nell'elenco sono:{pizze[-3:]}")
