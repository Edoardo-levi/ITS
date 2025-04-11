''' un numero elevato alla terza potenza è chiamato cubo. Ad esempio, 
il cubo di 2 è scritto come 2**3 in Python. 
Crea un elenco dei primi 10 cubi (ovvero, il cubo di ogni intero da 1 a 10) 
e usa un ciclo for per stampare il valore di ogni cubo.
'''

cubi= []
for i in range (1,11):
    cubo=i**3
    cubi.append(cubo)
print("la lista dei cubi e':\n")
print(*cubi)
