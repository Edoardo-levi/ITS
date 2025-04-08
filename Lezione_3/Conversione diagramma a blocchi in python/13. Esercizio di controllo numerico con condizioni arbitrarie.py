"""Progettare un algoritmo che verifichi se tre numeri interi positivi x, y, z rispettano le seguenti regole:

la somma di x+y+z deve essere pari;
x deve essere divisibile per 3, y divisibile per 5 e z divisibile per 7;
se entrambe le condizioni sono vere, mostrare: “Regole rispettate”. Altrimenti, mostrare: “Regole non rispettate”."""


while True:
    x= int(input("inserisci un numero x:\n"))
    y= int(input("inserisci un numero y:\n"))
    z=int(input("inserisci un numero z:\n"))

    if x>0:
        if y>0:
            if z>0:
                if (x+y+z) %2==0 and x%3==0 and y%5==0 and z%7==0:
                    print("Regole rispettate")
                else:
                    print("Regole non rispettate")
            else:
                print(f"il numero Z ({z}) deve essere positivo")
        else:
            print(f"il numero y ({y}) deve essere positivo")
    else:
        print(f"il numero x ({x}) deve essere positivo")