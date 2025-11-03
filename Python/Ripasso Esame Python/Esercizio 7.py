"""Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari."""


def classifica_numeri(lista: list[int]) -> dict[str:list[int]]:
   dizionario:dict={"pari":[],"dispari":[]}
   for num in lista:
        if num%2==0:
            dizionario["pari"].append(num)
        else:
            dizionario["dispari"].append(num)
   return dizionario