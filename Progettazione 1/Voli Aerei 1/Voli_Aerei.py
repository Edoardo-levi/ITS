from typing import Any, Self
import re
from mytipes import *


class Volo:
    def __init__(self, codice:str, durata:PositiveInt) ->None:
        self.codice=codice
        self.durata=durata

class Aeroporto:
    def __init__(self, codice:str, nome:str):
        self.codice=codice
        self.nome=nome

class Compagnia:
    def __init__(self, nome:str, anno:PositivaInt1900):
        self.nome=nome
        self.anno=anno


class Nazione:
    def __init__(self, nome:str):
        self.nome=nome
    def __hash__(self)->str:        # Restituisce l'hash (codice univoco associato alla stringa nome in questo caso) dell'oggetto nome (in questo caso)
        return hash(self.nome)

class Citta:
    def __init__(self, nome:str, abiatnti: PositiveInt):
        self.nome=nome
        self.abiatnti=abiatnti
