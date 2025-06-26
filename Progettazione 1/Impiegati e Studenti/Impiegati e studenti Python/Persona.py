from __future__ import annotations
from mytipes import *

class Persona:
    _nome: str
    _cognome: str
    _cf: list[CodiceFiscale]  # almeno uno
    _genere: Genere
    _maternita: PositiveInt | None  # solo se donna
    _posizione_mil: PosizioneMilitare | None  # solo se uomo
    _nascita: date

    def __init__(self, *, nome: str, cognome: str,cf: list[CodiceFiscale],genere: Genere,maternita: PositiveInt | None = None,posizione_mil: PosizioneMilitare | None = None,nascita:date) -> None:
        self._nome = nome
        self._cognome = cognome
        self._nascita = nascita

        
        if not cf:
            raise ValueError("La persona deve avere almeno un codice fiscale!")
        self._cf = cf
        self._genere = genere
        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("È obbligatorio fornire il numero di maternità per le donne")
            self._maternita = maternita
            self._posizione_mil = None
        else:
            # uomo
            self._posizione_mil = posizione_mil
            self._maternita = None

    def diventa_donna(self, maternita: PositiveInt) -> None:
        if self._genere == Genere.donna:
            raise RuntimeError("La persona era già una donna!")
        self._genere = Genere.donna
        self._maternita = maternita
        self._posizione_mil = None

    def diventa_uomo(self, posizione_mil: PosizioneMilitare | None = None) -> None:
        if self._genere == Genere.uomo:
            raise RuntimeError("La persona era già un uomo!")
        self._genere = Genere.uomo
        self._posizione_mil = posizione_mil
        self._maternita = None

    def set_maternita(self, maternita: PositiveInt) -> None:
        if self._genere != Genere.donna:
            raise RuntimeError("Solo le donne possono avere un numero di maternità")
        self._maternita = maternita

    def set_posizione_mil(self, posizione: PosizioneMilitare | None) -> None:
        if self._genere != Genere.uomo:
            raise RuntimeError("Solo gli uomini possono avere una posizione militare")
        self._posizione_mil = posizione
    
    def nascita(self) -> date:
        return self._nascita
