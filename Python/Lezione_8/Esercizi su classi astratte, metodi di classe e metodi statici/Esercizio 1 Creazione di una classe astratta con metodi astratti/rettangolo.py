from Shape import Shape


class Rettangolo (Shape):
    def __init__(self, base:float, altezza:float):
        self.__base= base
        self.__altezza=altezza

    def area(self)->float:
        return (self.__base *self.__altezza)
        
    def perimetro(self):
        return (self.__base * self.__altezza)*2
    
    def base(self) ->float:
        return self.__base
    
    def altezza(self)->float:
        return self.__altezza