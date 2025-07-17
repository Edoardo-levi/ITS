from mytipes import *
from post_oggetto import PostOggetto
from datetime import *
from bid import *

class Asta(PostOggetto):
    _prezzo_bid:RealeMaggioreDiZero
    _scadenza:datetime
   

    def __init__(self, prezzo, anni_garanzia, descrizione, is_nuovo, condizione, prezzo_bid, scadenza):
        super().__init__(prezzo, anni_garanzia, descrizione, is_nuovo, condizione)
        self.set_prezzo(prezzo)
        self.set_scadenza(scadenza)

    def set_prezzo(self, prezzo_bid):
        self.prezzo_bid = prezzo_bid
    
    def set_scadenza(self, scadenza):
        self.scadenza = scadenza
    
    def get_prezzo(self):
        return self.prezzo_bid
    
    def get_scadenza(self):
        return self.scadenza
