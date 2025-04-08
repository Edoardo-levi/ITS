#eserici con stringhe
# stringa scritta su una solo riga
stringA= "hello world!"

#stringa scritta su più righe 
stringB = "This is a \
    multiple \
    line \
    string"         #questa è una stringa scritta su più righe
    
print (stringA[0])
print(stringA[3])
print(stringA[10])

#lowcase = minuscolo  
#stampo e converto tutti i caratteri di stringA in minuscolo
print (stringA.lower())

#uppercase = maiuscolo
#stampo e converto tutti i caratteridi stringA in maiuscolo
print(stringA.upper())
#title titlecase rende maiuscole la prima lettra della stringa e la prima lettera dopo lo spazio
print(stringA.title())