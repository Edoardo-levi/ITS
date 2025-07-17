from mytipes import *
from datetime import *

class Bid:
    _istante:datetime

    def __init__(self, istante:datetime):
        self.set_istante(istante)

    def set_istante(self, istante):
        self._istante = istante

    def get_istante(self):
        return self._istante