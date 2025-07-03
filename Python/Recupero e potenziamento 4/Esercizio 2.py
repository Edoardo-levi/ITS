"""Elaborare uno schema che consenta di stampare in output in maniera ricorsiva gli elementi di una lista in ordine inverso.

Una volta elaborato lo schema, appena consentitovi dal docente, scrivere una funzione ricorsiva in Python, chiamata printListBackward() che stampi in output gli elementi di una lista in ordine inverso, sfruttando la ricorsione.
Infine, scrivere un codice driver che, date le seguenti liste, stampi ogni lista in ordine inverso sfruttando la funzione ricorsiva implementata.

lista1: 1, 2, 3, 4, 5
lista2: "Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"""




def printListBackward(lista:list[any]):


    
    if not lista:
        return
            

    else:
        printListBackward(lista[1:])
        print (lista[0])


printListBackward(lista=["ciao", "come", "stai"])

printListBackward(lista= [1,2,3,4,5,6,7,8,9,10])