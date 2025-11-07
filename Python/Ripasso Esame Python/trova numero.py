
"""data una lista disordinata scrivere una funzione che permetta di trovare all'interno della lista un determinato elemento (senza usare in)
"""

def trova_numero(nums: list, element: int | float | str):
    if len(nums) == 0:
        raise ValueError("Lista vuota")

    i = 0
    while i < len(nums):
        if nums[i] == element:
            print(f"L'elemento {element} è presente nella lista (posizione {i}).")
            return True
        i += 1

    print(f"L'elemento {element} NON è presente nella lista.")
    return False

    
    
numeri = [5, 2, 9, 1, 3]

trova_numero(numeri, 9)   # trovato
trova_numero(numeri, 7)   # non trovato
