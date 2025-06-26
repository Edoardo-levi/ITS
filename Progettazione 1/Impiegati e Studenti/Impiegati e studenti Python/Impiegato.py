from Persona import *
from mytipes import Ruolo


class Impiegato(Persona):
    __stipendio: RealeMaggioreDiZero
    __ruolo: Ruolo
    __is_responsabile: bool

    def __init__(self,*,nome, cognome, cf, genere, maternita = None, posizione_mil = None, nascita, stipendio: RealeMaggioreDiZero, ruolo: Ruolo, is_responsabile: bool = False) -> None:
        super().__init__(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita, posizione_mil=posizione_mil, nascita=nascita)


        self.set_stipendio()
        self.set_ruolo()
   

    def set_stipendio(self, stipendio: RealeMaggioreDiZero) -> None:
        if self.__stipendio <= 0:
            raise ValueError("Lo stipendio deve essere maggiore di zero")
        else:
            self.__stipendio = stipendio

    def get_stipendio(self) -> RealeMaggioreDiZero:
        return self.__stipendio
    
    def set_ruolo(self, ruolo: Ruolo) -> None:
        if self.__ruolo not in Ruolo:
            raise ValueError("Ruolo non valido")
        else:
            self.__ruolo = ruolo
        
    def get_ruolo(self) -> Ruolo:
        return self.__ruolo
    
    def is_responsabile(self) -> bool:
        return self.__is_responsabile
    
    