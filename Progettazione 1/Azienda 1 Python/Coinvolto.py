from __future__ import annotations
from Impiegato import *
from Progetto import *

class Coinvolto:
    _impiegato:Impiegato
    _progetto: 'Progetto'
    _data_inizio:date

    def __init__(self,imp:Impiegato, prog:'Progetto', data_inizio:date):
        self.setdate(data_inizio)

    def data_inizio(self)->date:
        return self.data_inizio
    
    def progetto(self)-> 'Progetto':
        return self._progetto
    
    def impiegato(self)->Impiegato:
        return self._impiegato
    
    def setdate(self,data_inizio)->None:
        self._data_inizio:date=data_inizio

    
