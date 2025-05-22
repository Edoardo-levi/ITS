from enum import *
from typing import Any, Self
import re


class Genere(StrEnum):
    uomo=auto()
    donna=auto()


class CodiceFiscale:
    def __init__(self, codice):
        controllo=bool(re.fullmatch(r"^[A-Z]{6}\d{2}[A-Z]{1}\d{2}[A-Z]\d{3}[A-Z]", codice))
        if controllo==False:
            raise ValueError("Codice fiscale non corretto")
        self.codice=codice
    
    def __str__(self):
        return self.codice


class Città:
    def __init__(self, nomeC):
        self.nomeC=nomeC
    def __hash__(self) -> int:
        return hash(self.nomeC)
    
class Regione: 
    def __init__(self, nomeR):
        self.nomeR=nomeR
    def __hash__(self) -> int:
        return hash(self.nomeR)


class Nazione: 
    def __init__(self, nomeN):
        self.nomeN=nomeN
    def __hash__(self) -> int:
        return hash(self.nomeN)
    

class Indirizzo:
    _via:str
    _civico:str
    def __init__(self, via:str, civ:str):
        if not via or via.isdigit()==True:
            raise TypeError("La via non può essere vuota e non può contenere solo numeri")
        elif len(civ)>6:
            raise ValueError("Civico inesistente")
        self._via=via
        self._civico=civ
    
    def via(self) -> str:
        return self._via
    
    def civico(self) -> str:
        return self._civico


class Voto(int):
    def __new__(cls, v:int|float|Self) -> Self:
        if v<18 or v>30:
            raise ValueError("Il voto deve essere compreso tra 18 e 30")
        return int.__new__(cls, v)


class Studente:
    def __init__(self, matricolaS: str, nome: str, genere:Genere, indirizzo: Indirizzo, codicefiscale:CodiceFiscale):
        self.matricolaS=matricolaS
        self.nome=nome
        self.genere=genere
        self.indirizzo=indirizzo
        self.codicefiscale=codicefiscale

    def __hash__(self) -> int:
        return hash(self.matricolaS)
    

class Posizione:
    ricercatore=auto()
    profAssociato=auto()
    profOrdinario=auto()


class Professore:
    def __init__(self, cf: CodiceFiscale, nome:str, cognome:str, matricolaP:str, ruolo: Posizione):
        self.cf= cf
        self.nome=nome
        self.cognome=cognome
        self.matricolaP=matricolaP
        self.ruolo=ruolo
    
    def __hash__(self) -> int:
        return hash(self.matricolaP)


indirizzo1=Indirizzo("Via Mattia Battistini", "52")
indirizzo2=Indirizzo("Via del Forte Boccea", "115")
st=Studente("12234", "pippo", "uomo", indirizzo1, "VLNDRD03S28H501I")
st1=Studente("2234", "pina", "donna", indirizzo2, "VLNDRD03S28H501I")

if hash(st)==hash(st1):
    raise ValueError("Due studenti non possono avere stesso numero di matricola")