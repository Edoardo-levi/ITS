from mytipes import * 
from Persona import Persona


class Studente(Persona):
    __matricola: int

    def __init__(self,nome, cognome, cf, genere, maternita=None, posizione_mil=None, nascita=None) -> None:
        super().__init__(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita, posizione_mil=posizione_mil, nascita=nascita)

        self.__setMatricola()

    
    def __setMatricola(self,matricola:int) -> None:
        if self.__matricola <0:
            raise ValueError("La matricola non può essere negativa")
        else:
            self.__matricola = matricola 
    
    def get_matricola(self) -> int:
        return self.__matricola