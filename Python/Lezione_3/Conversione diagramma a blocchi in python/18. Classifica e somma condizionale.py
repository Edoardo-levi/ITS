"""Scrivere un algoritmo che consenta all’utente di inserire una numero variabile di numeri interi (la quantità è scelta dall’utente). L'algoritmo deve:

sommare i numeri pari e maggiori della media dei numeri inseriti fino a quel momento;
sommare i numeri dispari o minori della media dei numeri inseriti fino a quel momento;
Mostrare in output entrambe le somme e indicare quale somma è maggiore."""

n:int=int(input("Quanti numeri vuoi inserire? "))

somma=0
media=0
somma_pari=0
somma_dispari=0
for i in range (1,n+1):
    x:int=int(input(f"inserisci un numero {i}: "))
    somma+=x
    media= somma/(x+1)
    if x%2==0 and x>media:
        somma_pari+=x
    else:
        if x<media or x%2 !=0:
            somma_dispari+=x
    i+=1
print(f"La somma dei numeri pari e': {somma_pari}\n\
La somma dei numeri dispati e': {somma_dispari}")

if somma_pari > somma_dispari:
    print("La somma dei numeri pari e' maggiore della somma dei numeri dispari")
elif somma_dispari > somma_pari:
        print("La somma dei numeri dispari e' maggiore della somma dei numeri pari")
else:
    print("Le somme sono uguali")


# Modo di risolvere l'ultima sequenza di istruzioni con il Match Case (da riga 26 a riga 31)
somme = [somma_pari, somma_dispari]

match somme:
    case somme if somme[0] > somme[1]:
        print("La somma dei nuemri pari e' maggiore della somma dei numeri dispari")
    case somme if somme [1]> somme[0]:
        print("La somma dei numeri dispari e' maggiore della somma dei numeri pari")
    case _:
        print("le somme dei numeri sono uguali") 
