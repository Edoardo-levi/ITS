# dal modulo persona.py importo la classe Persona

from persona import Persona


# la classe studente eredita dalla classe persona
class Studente (Persona):


    '''
    Attributi della classe Persona in quanto Studnete eredita da Persona

    self.name:str
    self.lastname:str
    self.age:int

    Attributi della classe Studente:
    self.matricola:str
    '''

    # inizializzare un oggetto della classe Studente

    def __init__(self, name:str, lastname:str, age:int, matricola:str):
        # inizializzo la classe Persona chiamando il metodo init della superclasse 
        super().__init__(name, lastname, age,)

        # istruzioni che inizializzano l'oggetto della classe Studente

        self.setMatricola(matricola)

        # definire i metodi setter della classe Studente

        # metodo che imposta il valore dell'attributo self.matricola

    def setMatricola(self, matricola:str)-> None:

        if matricola:
            self.matricola = matricola
        else:
            print("\n Errore! La matricla non può essere rappresentata da una stringa vuota")

    # metodi getter
    # matodo che ritorna il valore dell'attributo self.matricola

    def getMatricola(self) -> str:
        return self.matricola
    

    # ridefinire il metodo __str__(overiding)

    def __str__(self) -> str:
        return f"\nNome:{self.name}\nCognome:{self.getLastname()}\nMatricola:{self.getMatricola()}"