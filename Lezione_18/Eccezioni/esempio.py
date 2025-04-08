num=int(input("inserisci un numero:\n"))
if num !=5:
    raise Exception(f"il numero inserito ({num}) è diverso da 5 ")
else:
    print(f"Numero corretto ({num})")

