from persona import Persona
from alieno import Alieno

# creare un oggetto p della classe Persona

p: Persona = Persona("Edoardo", "Levi", 20)

# visualizzare le informazioni dell'oggetto p

print(p)

# creare un oggetto et della classe Alieno

et: Alieno =Alieno("Andromeda")

# visualizzare le informazione dell'oggetto et

print(et)

# l'oggetto p invochi il metodo speak()

p.speak()

# invochiamo il metodo speak() dall'ggetto et

et.speak()