from Dipartimento import Dipartimento
from Impiegato import Impiegato
from datetime import *


class Afferenza:

    @classmethod
    def add(cls, imp: Impiegato, dip: Dipartimento, data: date) -> None:
        l = cls._link(imp, dip, data)
        imp.add_link_afferenza(l)  # deve essere un metodo in Impiegato
        dip.add_link_afferenza(l)  # deve essere un metodo in Dipartimento

    class _link:
        _impiegato: Impiegato   # immutabile
        _dipartimento: Dipartimento   # immutabile
        _data_inizio: date

        def __init__(self, imp: Impiegato, dip: Dipartimento, data: date):
            self.setdate(data)
            self._impiegato = imp
            self._dipartimento = dip

        def dipartimento(self) -> Dipartimento:
            return self._dipartimento

        def impiegato(self) -> Impiegato:
            return self._impiegato

        def data_inizio(self) -> date:
            return self._data_inizio

        def setdate(self, data: date) -> None:
            self._data_inizio = data
