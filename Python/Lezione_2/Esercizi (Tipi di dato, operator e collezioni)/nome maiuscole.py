''' usa una variabile per rappresentare il nome di una persona 
e poi stampa il nome di quella persona in 
minuscolo, maiuscolo e maiuscolo iniziale.'''
nome = str(input("inserisci un nome"))

print (f"Ecco il nome nei formati richiesti:\n \
        Nome in minuscolo: {nome.lower()} \n \
        Nome in Maiuscolo: {nome.upper()} \n \
        Nome con solo l\'iniziale maiuscola: {nome.title()}")
