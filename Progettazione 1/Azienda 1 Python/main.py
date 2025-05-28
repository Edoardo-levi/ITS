from mytipes import *
from Impiegato import *
from Dipartimento import *
from datetime import date



tel1: NumeroTelefono = NumeroTelefono("3334445566")
tel2: NumeroTelefono = NumeroTelefono("3337778899")
ind: Indirizzo = Indirizzo("Viale Cesare Pavese", "205b",
                           CAP("00144"))

alice: Impiegato = Impiegato("Alice", "Alessi",
                             date(year=1990, month=12, day=31),
                             RealGez(18000))
print(f"Ho creato l'impiegata {alice.nome()} {alice.cognome()}")

bob: Impiegato = Impiegato("Bob", "Burnham",
                             date(year=1997, month=10, day=11),
                             RealGez(19000))
print(f"Ho creato l'impiegato {bob.nome()} {bob.cognome()}")


dip1: Dipartimento = Dipartimento("Vendite", tel1, ind)

print(f"Ho creato il dipartimento {dip1}")


dip2: Dipartimento = Dipartimento("Acquisti", tel2, None)
print(f"Ho creato il dipartimento {dip2}")

t: frozenset[NumeroTelefono] = dip1.telefoni()

print("dip1.telefoni() = " + str(dip1.telefoni()))

dip1.add_NumeroTelefono(NumeroTelefono("3481265413"))

print("dip1.telefoni() = " + str(dip1.telefoni()))