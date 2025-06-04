"""Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi."""


def liste_separate (lista:list) ->dict:
    lista_pos=[]
    lista_neg=[]

    for numero in lista:
        if numero>0:
            lista_pos.append(numero)
        else:
            lista_neg.append(numero)

    dizionario:dict={"Lista Positivi":lista_pos, "Lista Negativi": lista_neg}
    print(dizionario)
    return dizionario

liste_separate((1,-3,4,56,-56))