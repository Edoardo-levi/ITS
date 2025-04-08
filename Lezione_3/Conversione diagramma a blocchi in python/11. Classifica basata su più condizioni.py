"""Progettare un algoritmo che richieda all’utente di inserire un valore intero.
Il programma deve verificare:

se il numero è pari e maggiore di 10. Se sì, mostrare “Numero valido”;
se il numero è dispari o minore o uguale a 10. Se sì, mostrare “Numero non valido”."""



n=int(input("inserisci un numero:\n"))

if n%2==0 and n > 10:
    print(f"il numero inserito({n}), e' un numero valido")

else:
    print(f"il numero inserito ({n}), e' un numero non valido")