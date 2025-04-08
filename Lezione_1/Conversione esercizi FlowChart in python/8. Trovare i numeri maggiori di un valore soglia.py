"""Progetta un algoritmo che dati 7 numeri, trova e comunica i numeri maggiori di un valore soglia fornito dall'utente."""


soglia=int(input("inserisci un valore soglia:\n"))


cont=0

print("inserisci 7 numeri:\n")
for cont in range (1,7+1):
    n=int(input(f"numero {cont}:"))

    if n>soglia:
        print(f"il numero: {n}, e' maggiore del valore soglia: {soglia}\n")    
    else:
        cont+=1

