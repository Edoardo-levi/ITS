"""Tre ristoranti: inizia con la tua classe dall'esercizio 9-1. Crea tre diverse istanze dalla classe e chiama describe_restaurant() per ogni istanza."""


class Ristorante:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    
    def describe_restaurant(self):
        print(f"Il nome del ristorante e': {self.restaurant_name} e la tipologia di cucina e': {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"il ristorante {self.restaurant_name} e' aperto")
    

nome_ristorante1= input("Inserisci il nome del primo ristorante:\n")
tipo_cucina1= input("Inserisici la tipologia di cucina del primo ristorante:\n")

nome_ristorante2= input("Inserisci il nome del secondo Ristorante:\n")
tipo_cucina2= input("Inserisci la tipologia di cucina del secondo ristorante:\n")

nome_ristorante3= input("Inserisci il nome del terzo ristorante:\n")
tipo_cucina3= input("Inserisci la tipologia di cucina del terzo ristorante:\n")


ristorante1= Ristorante(nome_ristorante1,tipo_cucina1)
ristorante2 =Ristorante(nome_ristorante2,tipo_cucina2)
ristorante3= Ristorante(nome_ristorante3, tipo_cucina3)

print("-------------------------")
print("\n\n")

ristorante1.describe_restaurant()
ristorante1.open_restaurant()

print("-------------------------")

ristorante2.describe_restaurant()
ristorante2.open_restaurant()

print("-------------------------")

ristorante3.describe_restaurant()
ristorante3.open_restaurant()

