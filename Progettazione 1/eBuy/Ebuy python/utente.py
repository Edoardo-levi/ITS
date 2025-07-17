from mytipes import *
from bid import *
from asta_bid import * 
from asta_bid import *

class Utente:
    _username:str #<<immutable>>
    _registrazione:datetime #<<immutable>>

    def __init__(self, username, registrazione):
        self.set_username(username)
        self.set_registrazione(registrazione)

    def set_username(self, username):
        self._username = username

    def set_registrazione(self, registrazione):
        self._registrazione = registrazione

    def username(self):
        return self._username

    def registrazione(self):
        return self._registrazione
    



"""ultimo_bid(i:datetime): Bid|None
    max_b = None
        per ogni l in this.asta_bid:
            se l.bid.istante <= :
                se l.bid.istante > max_b.istante OR max_b = None:
                    max_b = b
        return max_b
    """


def ultimo_bid(self, i:datetime) -> Bid | None:
    max_b = None
