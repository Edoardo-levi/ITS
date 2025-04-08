"""crea una classe chiamata Ristorante. 
Il metodo __init__() per Ristorante dovrebbe memorizzare due attributi: 
un restaurant_name e un cuisine_type. Crea un metodo chiamato describe_restaurant() 
che stampi queste due informazioni e un metodo chiamato open_restaurant() 
che stampi un messaggio che indica che il ristorante è aperto. 
Crea un'istanza chiamata ristorante dalla tua classe. '
'Stampa i due attributi singolarmente e poi chiama entrambi i metodi.

"""
class Ristorante:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    
    def describe_restaurant(self):
        print(f"Il nome del ristorante e': {self.restaurant_name} e la tipologia di cucina e': {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"il ristorante {self.restaurant_name} e' aperto") 

restaurant_name=(input("Inserisci il nome del ristorante:\n"))
cuisine_type= (input("Inserisci la tipologia di cucina:\n"))

ristorante=Ristorante( restaurant_name, cuisine_type)
ristorante.describe_restaurant()
ristorante.open_restaurant()