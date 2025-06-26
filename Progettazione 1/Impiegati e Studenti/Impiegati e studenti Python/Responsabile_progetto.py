from Impiegato import *
from Progetto import *

class ResponsabileProgetto:

    @classmethod
    def add(cls, impiegato: Impiegato, progetto: Progetto) -> None:
        l= cls._link(impiegato, progetto)
        impiegato.add_link_responsabile(l)  # deve essere un metodo in Impiegato
        progetto.add_link_responsabile(l)  # deve essere un metodo in Progetto

    class _link:
        _impiegato: Impiegato
        _progetto: Progetto

        def __init__(self, impiegato: Impiegato, progetto: Progetto) -> None:
            self._impiegato = impiegato
            self._progetto = progetto

        def progetto(self) -> Progetto:
            return self._progetto
        
        def impiegato(self) -> Impiegato:
            return self._impiegato
        
        