"""inizia con la tua classe dall'esercizio 9-1. '
'Crea tre istanze diverse dalla classe e chiama describe_restaurant() per ogni istanza."""


class Ristorante:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    
    def describe_restaurant(self):
        print(f"Il nome del ristorante e': {self.restaurant_name} e la tipologia di cucina e': {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"il ristorante {self.restaurant_name} e' aperto") 

restaurant_name1=(input("Inserisci il nome del ristorante:\n"))
cuisine_type1= (input("Inserisci la tipologia di cucina:\n"))

restaurant_name2=(input("Inserisci il nome del ristorante:\n"))
cuisine_type2= (input("Inserisci la tipologia di cucina:\n"))

restaurant_name3=(input("Inserisci il nome del ristorante:\n"))
cuisine_type3= (input("Inserisci la tipologia di cucina:\n"))

ristorante1=Ristorante( restaurant_name1, cuisine_type1)
ristorante2=Ristorante( restaurant_name2, cuisine_type2)
ristorante3=Ristorante( restaurant_name3, cuisine_type3)

ristorante1.describe_restaurant()
ristorante1.open_restaurant()
print("-------------------------------")
ristorante2.describe_restaurant()
ristorante2.open_restaurant()
print("--------------------------------")
ristorante3.describe_restaurant()
ristorante3.open_restaurant()
