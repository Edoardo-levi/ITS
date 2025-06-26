from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from Impiegato import Impiegato
    from Progetto import Progetto

class Coinvolto:
    # é una classe 'factory': non ha oggetti suoi:
    # serve solo a creare oggetti di un'altra classe (in questo caso di _link)
    @classmethod 
    def add(cls, impiegato:Impiegato, progetto:Progetto, data_inizio:date)->None:
         #crea il link l (impiegato proggetto)
         l= cls._link(impiegato,progetto,data_inizio)
         impiegato.add_link_coinvolto(l) # deve essere un metodo in Impiegato che registra il link nell'impiegato 
         progetto.add_link_coinvolto(l)  # deve essere un metodo in Proggetto che registra il link nel Progetto
    class _link:
        # ogni oggetto di questa class rappresenta un link 
        # dell'associazione 'coinvolto', cioè una coppia 
        # (Impiegato, Progetto)
        _impiegato: Impiegato   # immutabile
        _progetto: 'Progetto'   # immutabile
        _data_inizio: date

        def __init__(self,imp:Impiegato, prog:'Progetto', data_inizio:date)->None:
            self.setdate(data_inizio)
            self._impiegato=imp
            self._progetto=prog


        def progetto(self)-> 'Progetto':
                return self._progetto
            
        def impiegato(self)->Impiegato:
                return self._impiegato
        

        def data_inizio(self)->date:
            return self.data_inizio
        
        
        def setdate(self,data_inizio)->None:
            self._data_inizio:date=data_inizio

    