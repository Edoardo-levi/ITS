from persona import Persona
from studente import Studente

# creo oggetto p della classe Persona

p:Persona = Persona("Edoardo", "Levi", 20)


# visualizzare le informazioni dell'oggetto p

print(p)



# creare un oggetto studente1 della classe Studente

studente1: Studente = Studente("Matio", "Rossi", 20, "0123456")

# visualizzare le informazioni relatica all'oggetto studente 1

print(studente1)


# controllare se studente1 è istanza della classe Studnete

# usa la funzione isisntance(obj, Class) -> controlla se l'oggetto obj è istanza della classe Class
# in caso affermativo ritorna True
# altrimenti ritorna False

if isinstance(studente1, Studente) :
    print("\nstudente1 è istanza della classe Studente")


# controllo se studente1 è un'istanza della classe Persona

if isinstance(studente1,Persona):
        print("\nstudente1 è un oggetto della classe Studente ma anche della classe Persona")


# controllo se l'oggeto p sia un istanza della classe Persona

if isinstance(p,Persona):
     print("\np è istanza della classe Persona")



# controllo se l'oggeto p sia un istanza della classe Studente

if isinstance(p,Studente):
     print("\np è istanza  della classe Persona ma anche della classe Studente")
else:
      print("\np è un oggetto della classe Persona ma non della classe Studente")


# controllare se una classe è sottoclasse di un'altra 

# controllo che la classe Studente sia sottoclasse della classe Persona

# utilizzo la funzione issubclass (class 1, class2) controlla se la calsse 1 è sottoclasse della classe 2 
# in caso affermatico ritorna True
# altrimenti False


if issubclass(Studente, Persona):
      print("\nLa classe Studente è sottoclasse della classe Persona")