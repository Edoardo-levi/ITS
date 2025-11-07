"""scrivere una funzione che data in input una lista disordinata ritorni una lista ordinata in ordine crescente"""


def lista_ordinata(nums:list=[]):
    if len(nums)==0:
        raise ValueError("Lista vuota")
    else:
        return sorted(nums)


numeri = [5, 2, 9, 1, 3]
lista_ordinata = lista_ordinata(numeri)
print(lista_ordinata)
