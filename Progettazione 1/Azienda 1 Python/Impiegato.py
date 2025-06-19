from __future__ import annotations

from typing import TYPE_CHECKING

from datetime import date
from mytipes import *
from Coinvolto import Coinvolto


if TYPE_CHECKING:
    from Progetto import Progetto
    


class Impiegato:
    _nome: str # noto alla nascita  
    _cognome: str # noto alla nascita
    _nascita: date # <<immutable>>, noto alla nascita
    _stipendio: RealGez # noto alla nascita
    _progetti:dict[Progetto, Coinvolto]


    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGez) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self._progetti = dict()

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGez:
        return self._stipendio

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_cognome(self, c: str) -> None:
        self._cognome: str = c

    def set_stipendio(self, s: RealGez) -> None:
        self._stipendio = s
    
    def add_progetto(self,progg:Progetto, date:date)->None:
        
        if progg in self._progetti:
            raise ValueError("Il progetto e' gia' presente")
        else:
            self._progetti[progg] = Coinvolto(self, progg, date)
            progg.add_impiegato(self, date)
            
    def progetti(self) -> frozenset['Coinvolto']:
        return frozenset(self._progetti)
    
if __name__ == "__main__":
    alice: Impiegato = Impiegato("Alice", "A", nascita=date.today(), stipendio=RealGez(0))
    from Progetto import Progetto
    pegaso: Progetto = Progetto("Pegaso", budget=RealGz(45_000))

    #alice.add_progetto(pegaso, date.today())
    pegaso.add_impiegato(alice, date.today())
    print(f"Progetti di alice: {alice.progetti()}")
    print(f"Impiegati di pegaso: {pegaso.impiegati()}")
