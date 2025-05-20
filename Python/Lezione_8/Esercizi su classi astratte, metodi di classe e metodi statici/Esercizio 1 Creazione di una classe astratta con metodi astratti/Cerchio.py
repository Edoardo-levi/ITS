from Shape import Shape
import math


class cerchio (Shape):
    def __init__(self, raggio:float):
        super().__init__()
        self.__raggio:float=raggio

    def area(self)->float:
        return math.pow(self.__raggio,2)*math.pi

    def perimetro(self):
        return 2*math.pi*self.__raggio

    def raggio(self) ->float:
        return self.__raggio

if __name__=='__main__':
    c=cerchio(10.3)
    print(f"L'area del cerchio è: {c.area():.2f}")
    print(f"Il perimetro del cerchio è: {c.perimetro():.2f}")
