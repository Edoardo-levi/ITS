from mytipes import *
from datetime import *

class PostOggetto:
    _prezzo:RealeMaggioreDiZero
    _anni_garanzia:PositiveInt
    _descrizione:str
    _pubblicazione:datetime
    _is_nuovo:bool
    _condizione:Condizione

    def __init__(self, prezzo:RealeMaggioreDiZero, anni_garanzia:PositiveInt, descrizione:str, is_nuovo:bool, condizione:Condizione):
        self.set_prezzo(prezzo)
        self.set_anni_garanzia(anni_garanzia)
        self.set_descrizione(descrizione)
        self._pubblicazione = datetime.now()
        self._is_nuovo = is_nuovo
        self.set_condizione(condizione)

    def set_prezzo(self, prezzo):
        self._prezzo = prezzo

    def set_anni_garanzia(self, anni_garanzia):
        self._anni_garanzia = anni_garanzia

    def set_descrizione(self, descrizione):
        self._descrizione = descrizione

    def set_condizione(self, condizione):
        self._condizione = Condizione(condizione)
    
    def prezzo(self):
        return self._prezzo
    
    def anni_garanzia(self):
        return self._anni_garanzia
    
    def descrizione(self):
        return self._descrizione
    
    def pubblicazione(self):
        return self._pubblicazione
    
    def is_nuovo(self):
        return self._is_nuovo
    
    def condizione(self):
        return self._condizione