'''fai un elenco dei tuoi frutti preferiti, quindi scrivi una serie di istruzioni 
 if indipendenti che controllano determinati frutti nel tuo elenco.
• Fai un elenco dei tuoi tre frutti preferiti e chiamalo favorite_fruits.
• Scrivi cinque istruzioni if. Ognuna dovrebbe controllare se un certo tipo di 
frutto è nel tuo elenco. Se il frutto è nel tuo elenco, il blocco if dovrebbe s
tampare un'istruzione, come Ti piacciono molto le mele!'''


frutti=["mele", "banane", "fragole"]
if "mele" in frutti:
    print("Ti piacciono molto le mele!")
elif "banane" in frutti:
    print("ti piacciono molto le banane")
else:
    print("ti piacciono le fragole")
    
