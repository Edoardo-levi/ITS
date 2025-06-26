from Dipartimento import Dipartimento
from Impiegato import Impiegato
from datetime import *



class Direzione:
   

    @classmethod
    def add (cls, imp:Impiegato, dip:Dipartimento)->None:
        l= cls._link(imp, dip)
        imp.add_link_afferenza(l)  # deve essere un metodo in Impiegato
        dip.add_link_afferenza(l)   # deve essere un metodo in Dipartimento

    class _link:
        _impiegato: Impiegato   # immutabile
        _dipartimento: Dipartimento   # immutabile
        
        def __init__(self, imp:Impiegato, dip:Dipartimento):
            
            self._impiegato = imp
            self._dipartimento = dip
        
        def dipartimento(self) -> Dipartimento:
            return self._dipartimento
        
        def impiegato(self) -> Impiegato:
            return self._impiegato
    