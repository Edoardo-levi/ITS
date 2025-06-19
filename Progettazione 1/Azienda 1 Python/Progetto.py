from __future__ import annotations
from mytipes import *
from Impiegato import Impiegato
from Coinvolto import Coinvolto

class Progetto:

    _nome:int
    _budget:RealeMaggioreDiZero
    _impiegati: dict['Impiegato', 'Coinvolto']
     

    def __init__(self,nome:str, budget:RealeMaggioreDiZero ):
       self.set_nome(nome)
       self.set_budget(budget)
       self._impiegati=dict()
    

    def nome(self)->str:
        return self._nome

    def budget(self)->int:
        return self._budget
    

    def set_nome(self,name:str)->str:
        self._nome:str=name
    
    def set_budget(self,budget:RealeMaggioreDiZero)->RealeMaggioreDiZero:
        self._budget:RealeMaggioreDiZero=budget

    def add_impiegato(self, impiegato:Impiegato, data_assunzione:date):
        coinvolto=Coinvolto(self, impiegato,data_assunzione)
        if impiegato in self._impiegati:
            raise ValueError("L'impiegato è già presente") 
        else:
            self._impiegati[impiegato]=Coinvolto(self, impiegato, data_assunzione)


    def is_coinvolto(self, impiegato:Impiegato)->bool:
        if impiegato in self._impiegati:
            return True
        else:
            return False
    
    def ultimo_impiegato_coinvolto(self, impiegato:Impiegato, coinvolto:Coinvolto)-> Impiegato:
        if impiegato in coinvolto:
            return impiegato
        else:
            raise (ValueError("Errore"))
    

    def remove_impiegato(self, impiegato:Impiegato)->Impiegato:
        if impiegato in self._impiegati:
            self._impiegati.pop(impiegato)
            return "l'impiegato e' stato rimosso"
        else:
            raise ValueError(f"Errore, l'impiegato non e' presente")
        

    def impiegati(self) -> frozenset['Coinvolto']:
        return frozenset(self._impiegati)
 