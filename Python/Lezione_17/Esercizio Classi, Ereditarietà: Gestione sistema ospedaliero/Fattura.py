"""Creare un file chiamato "fatture.py".
In tale file, creare una classe chiamata Fattura.

- Definire i seguenti metodi:
init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}"""

from Dottore import *
from Paziente import *

class Fattura:
    def __init__(self,patient:list,doctor:Dottore):
        if doctor.isAValidDoctor() is True:
            self.__patient = patient
            self.__doctor = doctor
            self.__fatture = len(patient)
            self.__salary = 0
        else:
            self.__patient= None
            self.__doctor=None
            self.__fatture=None
            self.__salary=None
    
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        parcella=self.__doctor.getParcel()
        self.__salary=parcella*len(self.__patient)
        return self.__salary
    

    def getFatture(self):
        if self.__patient is not None:
            self.__fatture = len(self.__patient)
            return self.__fatture
        return None
    
    def addPatient(self, newPatient):
        
        if self.__patient is not None:
            self.__patient.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.__doctor.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}")
        else:
            print("Impossibile aggiungere pazienti: fattura non valida.")

    def removePatient(self,idCode):
        for paziente in self.__patient:
            if paziente.getIdCode()==idCode:
                self.__patient.remove(paziente)
        self.getSalary()
        self.getFatture()
        print(f"Alla lista del Dottor cognome è stato rimosso il paziente {idCode}")
