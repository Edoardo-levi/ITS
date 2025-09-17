"""Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome, ed un attributo privato di tipo int per l'età.

- La classe Persona deve avere i seguenti metodi:
init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo, impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio, "Il nome inserito non è una stringa!". Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; se first_name e last_name non sono due stringhe, allora assegnare None all'età.
setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".
setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".
setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passato al metodo un numero intero. In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".
getName(): consente di ritornare il nome di una persona.
getLastname(): consente di ritornare il cognome di una persona.
getAge(): consente di ritornare l'età di una persona.
greet(): stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"""
class Persona:
    def __init__(self, first_name, last_name):
        self.__first_name = None
        self.__last_name = None
        self.__eta = None

        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print("Il nome inserito non è una stringa!")

        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa!")

        if self.__first_name is not None and self.__last_name is not None:
            self.__eta = 0
        else:
            self.__eta = None

    def setName(self, first_name):
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print("Il nome inserito non è una stringa!")

    def setLastName(self, last_name):
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa!")

    def setAge(self, age):
        if isinstance(age, int):
            self.__eta = age
        else:
            print("L'età deve essere un numero intero!")

    def getName(self):
        return self.__first_name

    def getLastName(self):
        return self.__last_name

    def getAge(self):
        return self.__eta

    def greet(self):
        print(f"Ciao, sono {self.getName()} {self.getLastName()}! Ho {self.__eta} anni!")



persona = Persona("Edoardo", "Levi")
persona.setAge(30)
persona.setName(123) # Nome non valido -> Non viene cambiato e viene stamptao l'errore 
persona.setLastName("Levi")  

print(persona.getName())     
print(persona.getLastName())  
