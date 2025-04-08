my_list=[1,2,3,4,5]

print(my_list)      # stampa la lista con le parentesi e la virgola 

print(*my_list)     # stampa la lista senza le parentesi e la virgola 






# FUNZIONE PER CALCOLARE LA SOMMA ILLIMITATA DI NUMERI DI INPUT


def somma(*args):                            # mette gli elementi in una tupla e li devo richiamere per posizione
    totale=0
    for num in args:
        totale+=num
    return totale

print(f"la somma e': {somma(5,6,7,9)}")


# FUNZIONE KWARGS


def total_price(**kwargs):                      # kwargs permette di prendere in input altri tipi di parametri 
                                                # all'interno della funzione  
    total:float = 0
    for product, price in kwargs.items():
        print(f"{product}: {price}€")
        total += price 
    return round(total, 2)
print(total_price(coffee=2.99, cake=4.55, juice=2.99))