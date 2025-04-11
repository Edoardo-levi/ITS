"""Progetta un algoritmo per calcolare il fattoriale di un numero intero positivo fornito dall'utente."""

while True:
    
    n=int(input("inserisci un numero:\n"))

    if n<0:
        print("il numero e' negativo. ")
        break
    else:
        fattoriale=1
    
    i=1

    for i in range (1,n+1):
        
        fattoriale*=i

        i+=1
       
        if i==n+1 :
            break
    
    print(fattoriale)

