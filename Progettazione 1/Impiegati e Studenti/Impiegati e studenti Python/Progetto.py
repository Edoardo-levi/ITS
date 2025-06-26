class Progetto:
    __nome:str

    def __init__(self, nome):
        self.set_nome()

    def set_nome(self, nome:str)->None:
        self.__nome=nome   
    

    def get_nome(self) ->str:
        return self.__nome