'''trova una citazione di una persona famosa che ammiri. 
Stampa la citazione e il nome del suo autore. 
Il tuo output dovrebbe essere simile al seguente, 
comprese le virgolette: Albert Einstein una volta disse:
"Una persona che non ha mai commesso un errore non ha mai provato niente di nuovo".'''

nome= str(input("inserisci il nome di chi ha fatto la citazione:\n"))
citazione= str (input("inserisci la citazione: \n"))
print (f"\n\nuna volta {nome.title()} disse:\n \"{citazione}\"")