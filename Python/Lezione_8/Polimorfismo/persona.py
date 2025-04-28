class Persona:
    def __init__(self, name:str, lastname:str, age:int):
        self.setName(name)
        self.setLastname(lastname)
        self.setAge(age)
    
    
    # metodo speciale che ritorna una stringa e che viene chiamata automaticamente quando si usa l'istruzione print(obj),
    # dove obj è un oggetto della classe Persona
    # funzione che mi mostri in output i dati relativi ad una persona 
    def __str__(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
    # il metodo __call__ mi consente di usare l'oggetto della classe Persona istanziato come una funzione.
    # Quindi, un oggetto della classe Persona si comporta come una funzione
    def __call__(self):
        if self.age < 18:
            print(f"{self.name} {self.lastname} e' minorenne!")
        elif 18 <= self.age < 30:
            print(f"{self.name} {self.lastname} e' maggiorenne!")
        elif 30<= self.age < 80:
            print(f"{self.name} {self.lastname} e' una persona adulta!")
        else:
            print(f"{self.name} {self.lastname} e' una persona anziana!")
    
    # __call__ non deve necessarimanete printare o ritornare un valore. Ritorna un valore se tale valore deve essere riutilizzato nel codice. 
    # printa un valore se il metodo deve eseguire un'azione senza dover restituire nulla
    # Ovviamente, il metodo __call__ può ricevere parametri in input e parametri con valori di default.

    # funzione che mi consenta di impostare il valore di self.name 
    def setName(self, name:str) -> None:
        self.name = name
    
    # funzione che mi consenta di impostare il valore di self.lastname
    def setLastname(self,lastname:str) -> None:
        self.lastname = lastname
    
    # funzione che mi consenta di impostare il valore di self.age
    def setAge(self, age:int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age
    
    # funzione che mi consenta di ritornare il valore di self.name
    def getName(self) -> str:
        return self.name
    
    # funzione che mi consenta di ritornare il valore di self.lastname 
    def getLastname(self) -> str:
        return self.lastname
    
    # funzione che mi consenta di ritornare il valore di self.age
    def getAge(self) -> int:
        return self.age
    # metodo speak () per la classe Persona che consente di simulare un saluto 

    def speak(self) ->None:
        print(f"\nHello my name is  {self.getName()}!")