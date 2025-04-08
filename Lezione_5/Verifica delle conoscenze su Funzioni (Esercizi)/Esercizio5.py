"""Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:

tutti i numeri pari vengano prima di tutti i numeri dispari;

l’ordine relativo tra pari e dispari va mantenuto;

l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi."""

def even_odd_pattern(numbers:list[int]) -> list[int]:
    numeri_pari=[]
    numeri_dispari=[]
    lista_ordinata=[]
    for i in (numbers):
        if i %2==0:
            numeri_pari.append(i)
        if i%2 !=0:
            numeri_dispari.append(i)
    lista_ordinata = numeri_pari+numeri_dispari
    return lista_ordinata




