from Cerchio import cerchio
from rettangolo import Rettangolo

if __name__ =='__main__':
    c=cerchio(20)
    print(f"Area e perimetro del cerchio con raggio = {c.raggio():.2f}, area = {c.area():.2f}, perimetro ={c.perimetro():.2f}")
    r=Rettangolo(10,30)
    print(f"Area e perimetro del rettangolo con base = {r.base():.2f}, altezza = {r.altezza():.2f}, area = {r.area():.2f} perimetro ={r.perimetro():.2f}")
