import sys

n=int(input("inserisci un numero: "))

if n==0:
    print("ERRORE")
    sys.exit()                                     # SE QUESTA ISTRUZIONE E' VERA, DOPO QUESTA LINEA DI CONDICE NON VIENE ESEGUITO NULLA  
    

if n==1:
    print(f"{n} ST")
elif n==2:
    print(f"{n} ND")
elif n==3:
   print(f"{n} HD")
else:
    print(f"{n} TH")



#esercizio svolto con il match statement:




n=int(input("inserisci un numero: "))

match n:

    case n if n==0:
        print("ERRORE")
        sys.exit()                                     # SE QUESTA ISTRUZIONE E' VERA, DOPO QUESTA LINEA DI CONDICE NON VIENE ESEGUITO NULLA  
    

    case n if n==1:
        print(f"{n} ST")
    case n if n==2:
        print(f"{n} ND")
    case n if n==3:
        print(f"{n} HD")
    case n:
        print(f"{n} TH")