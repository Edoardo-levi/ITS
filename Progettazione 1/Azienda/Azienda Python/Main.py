from datetime import date

from mytipes import *

from Impiegato import Impiegato
from Dipartimento import Dipartimento
from Progetto import Progetto
from Coinvolto import Coinvolto
from Afferenza import Afferenza
from Direzione import Direzione


imp = Impiegato("Mario", "Rossi", date(1990, 1, 1), RealeMaggioreDiZero(2500.00))

print(imp.nome())               # Mario
print(imp.cognome())            # Rossi
print(imp.nascita())            # 1990-01-01
print(imp.stipendio())          # 2500.00



tel1 = NumeroTelefono("0123456789")
indirizzo = Indirizzo("Via Roma 1", "Torino", "10100")
dip = Dipartimento("Informatica", tel1, indirizzo)

print(dip.nome())               # Informatica
print(dip.indirizzo())          # Indirizzo
print(dip.telefoni())           # frozenset with tel1






proj = Progetto("Apollo", RealeMaggioreDiZero(100000))
print(proj.nome())             # Apollo
print(proj.budget())          # 100000





imp = Impiegato("Lucia", "Verdi", date(1985, 5, 20), RealeMaggioreDiZero(3200))
proj = Progetto("Pegaso", RealeMaggioreDiZero(50000))

Coinvolto.add(imp, proj,date.today())

print(len(imp.progetti()))      # 1
print(proj.is_coinvolto(imp))   # True



imp = Impiegato("Anna", "Bianchi", date(1988, 3, 15), RealeMaggioreDiZero(2800))
dip = Dipartimento("Fisica", NumeroTelefono("0111234567"), Indirizzo("Via Galileo", "Torino", "10125"))

Afferenza.add(imp, dip, date(2020, 1, 1))

# Se i metodi imp.add_link_afferenza e dip.add_link_afferenza sono implementati, questo test dovrebbe andare
print("Test Afferenza completato")







imp = Impiegato("Luca", "Neri", date(1980, 7, 10), RealeMaggioreDiZero(4000))
dip = Dipartimento("Chimica", NumeroTelefono("0109876543"), Indirizzo("Via Mendeleev", "Genova", "16100"))

Direzione.add(imp, dip)

print("Test Direzione completato")
