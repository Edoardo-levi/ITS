from bid import Bid
from asta import Asta

class asta_bid:
    #classe factory
    @classmethod
    def add(cls, asta: Asta, bid: Bid) -> None:
        # crea il link (impiegato, bid)
        l = cls._link(asta, bid)
        asta.add_link_AstaBid(l)
        bid.add_link_AstaBid(l)
        asta.remove_link(l)
        bid.remove_link(l)
    
    class _link:
        # ogni oggetto di questa class rappresenta un link di associazione AstaBid
        # ovvero una coppia (Impiegato, bid)
        _asta: Asta
        _bid: Bid
        def __init__(self, asta: Asta, bid: Bid):
            self._asta=asta
            self._bid=bid

        def impiegato(self):
            return self._asta

        def bid(self):
            return self._bid