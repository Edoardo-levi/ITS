from bid import Bid
from utente_privato import UtentePrivato

class bid_ut:
    class _link:
        _bid:set[Bid]
        _privato:UtentePrivato

        def __init__(self, bid, privato):
            self.set_bid(bid)
            self.set_privato(privato)

        def set_bid(self, bid:set[Bid]):
            self._bid = bid

        def set_privato(self, privato:UtentePrivato):
            self._privato = privato

        def bid(self):
            return frozenset[self._bid]

        def privato(self):
            return self._privato