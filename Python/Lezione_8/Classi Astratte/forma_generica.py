from abc import ABC, abstractmethod     # sono librerie che vengono utilizzate per le classi astratte

class FormaGenerica(ABC): # in questo modo definisco la classe FormaGenerica come una classe astratta
    
    @abstractmethod       # definisco il metodo draw come astratto
    def draw(self) -> None:
        pass

    
    def setShape(self, shape:str) ->None:
        if shape:
            self.shape=shape
        else:
            print("Errore! La stringa shape non può essere una stringa vuota")


    def getShape(self)->str:
        return self.shape
    