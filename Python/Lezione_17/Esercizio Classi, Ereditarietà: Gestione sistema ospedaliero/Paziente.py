from Persona import*

class Paziente(Persona):
    def __init__(self, first_name, last_name,idCode):
        super().__init__(first_name, last_name)

        self.__idCode = None

    def setIdCode(self, idCode):
        if isinstance(idCode, str):
            self.__idCode = idCode
        else:
            print("Il codice identificativo deve essere una stringa!")
    
    def getIdCode(self):
        return self.__idCode

    def patientInfo(self):
        print(f"Paziente: {self.getName()} {self.getLastName()}\nID: {self.__idCode}")