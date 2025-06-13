from __future__ import annotations
from mytipes import *
from Impiegato import *
from Coinvolto import *

class Progetto:

    _nome:int
    _budget:RealeMaggioreDiZero
    _impiegati: dict[Impiegato, 'Coinvolto']
     

    def __init__(self,nome:str, budget:RealeMaggioreDiZero ):
       self.set_nome(nome)
       self.set_budget(budget)
       self._impiegato=dict()
    

    def nome(self)->str:
        return self._nome

    def budget(self)->int:
        return self._budget
    

    def set_nome(self,name:str)->str:
        self._nome:str=name
    
    def set_budget(self,budget:RealeMaggioreDiZero)->RealeMaggioreDiZero:
        self._budget:RealeMaggioreDiZero=budget

    def add_impiegato(self, impiegato:Impiegato, data_assunzione:date):
        self._impiegato:Impiegato=impiegato
        self._data_assunzione:date=data_assunzione
        if impiegato in self._impiegati:
            raise ValueError("L'impiegato è già presente") 
        else:
            self._impiegati[impiegato]=data_assunzione    
    def is_coinvolto(self, impiegato:Impiegato)->bool:
        if impiegato in self._impiegati:
            return True
        else:
            return False
    
 