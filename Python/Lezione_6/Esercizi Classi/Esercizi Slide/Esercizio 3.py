"""È data la classe Animal. Per ogni attività, testa le tue modifiche!
1. Crea due istanze realistiche di Animals
2. Stampa il nome di ogni oggetto
3. Modifica la quantità di zampe di un oggetto usando la notazione a punto
4. Aggiungi un metodo setLegs() per impostare le zampe di un oggetto e ripeti l'attività 3 ma
questa volta usando il metodo.
5. Aggiungi un metodo getLegs() per restituire la quantità di zampe
6. Aggiungi un metodo denominato printInfo che stampa tutti gli attributi di Animal"""


class Animal:
    def __init__ (self, nome:str, habitat:str, zampe:int):
        self.nome=nome
        self.habitat=habitat
        self.zampe=zampe
    
    def setLegs (self) ->int:
        self.zampe=int(input(f"Quante zampe ha l'animale {self.nome}: "))
        return self.zampe
    
    def getLegs (self): 
        print(f"L'animale {self.nome} ha {self.zampe} zampe")

    def printInfo(self):
        Animal.getLegs(self)
    
animale1= Animal("squalo","acqua", 10)
animale2= Animal("giraffa","savana",4 )
animale1.zampe=Animal.setLegs(animale1)
animale2.zampe=Animal.setLegs(animale2)
print("\n")

Animal.getLegs(animale1)
Animal.getLegs(animale2)
