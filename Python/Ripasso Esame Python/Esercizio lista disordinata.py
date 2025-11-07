"""scrivere una funzione che prende in input una lista disordinata, trovare il massimo e il minimo e metterli in una tupla"""


def riordino(lista:list=[]):
    if len(lista)==0:
        raise ValueError("Lista vuota")
    else:
        minimo= lista[0]
        massimo=lista[0]
        for num in lista:
            if num>massimo:
                massimo=num
            if num < minimo:
                minimo=num
        
        nuova_lista=[]
        nuova_lista.append((massimo, minimo))
    
    return (nuova_lista)

print(riordino([5, 2, 9, 1, 7,25]))
