'''Creare una funzione con lunghezza variabile degli argomenti
Scrivi un programma per creare func1()una funzione che accetti argomenti di lunghezza variabile e ne stampi il valore.
creare una funzione in modo tale che sia possibile passare un numero qualsiasi di argomenti a questa funzione, 
e la funzione dovrebbe elaborarli e visualizzare il valore di ciascun argomento.'''

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)
