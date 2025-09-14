"""inizia con il tuo programma dall'esercizio 9-1. Aggiungi un attributo chiamato number_served con un valore predefinito di 0. Crea un'istanza chiamata ristorante da questa classe. Stampa il numero di clienti che il ristorante ha servito, quindi modifica questo valore e stampalo di nuovo. Aggiungi un metodo chiamato set_number_served() che ti consente di impostare il numero di clienti che sono stati serviti. Chiama questo metodo con un nuovo numero e stampa di nuovo il valore. Aggiungi un metodo chiamato increment_number_served() che ti consente di incrementare il numero di clienti che sono stati serviti. Chiama questo metodo con qualsiasi numero che ti piace che potrebbe rappresentare quanti clienti sono stati serviti in, ad esempio, un giorno lavorativo."""


class Ristorante:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served= number_served
    
    def describe_restaurant(self):
        print(f"Il nome del ristorante e': {self.restaurant_name} e la tipologia di cucina e': {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"il ristorante {self.restaurant_name} e' aperto")
    
    def set_number_served(self, numero):
        self.number_served=numero
        print(f"Sono stati serviti: {self.number_served} clienti")

    def increment_number_served(self, numero_clienti):
        self.number_served += numero_clienti
        print(f"Clienti totali serviti:    {self.number_served}")


restaurant_name=(input("Inserisci il nome del ristorante:\n"))
cuisine_type= (input("Inserisci la tipologia di cucina:\n"))
number_served=int(input("Quanti clienti hai servito?    "))

ristorante=Ristorante( restaurant_name, cuisine_type)
ristorante.describe_restaurant()
ristorante.open_restaurant()
ristorante.set_number_served(number_served)

altri_clienti=input("Hai servito altri clietni (Si/No):    ")
if altri_clienti == "si".lower():
    numero_clienti= int(input("Quanti?  "))

ristorante.increment_number_served(numero_clienti)