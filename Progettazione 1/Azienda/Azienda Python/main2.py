from datetime import date
from mytipes import RealeMaggioreDiZero
from Impiegato import Impiegato

imp = Impiegato("Mario", "Rossi", date(1990, 1, 1), RealeMaggioreDiZero(2500.00))

print(imp.nome())               # Mario
print(imp.cognome())            # Rossi
print(imp.nascita())            # 1990-01-01
print(imp.stipendio())          # 2500.00



from Dipartimento import Dipartimento
from mytipes import NumeroTelefono, Indirizzo

tel1 = NumeroTelefono("0123456789")
indirizzo = Indirizzo("Via Roma 1", "Torino", "10100")
dip = Dipartimento("Informatica", tel1, indirizzo)

print(dip.nome())               # Informatica
print(dip.indirizzo())          # Indirizzo
print(dip.telefoni())           # frozenset with tel1




from Progetto import Progetto
from mytipes import RealeMaggioreDiZero

proj = Progetto("Apollo", RealeMaggioreDiZero(100000))
print(proj.nome())             # Apollo
print(proj.budget())          # 100000



from Coinvolto import Coinvolto
from Impiegato import Impiegato
from Progetto import Progetto
from datetime import date
from mytipes import RealeMaggioreDiZero, RealeMaggioreDiZero

imp = Impiegato("Lucia", "Verdi", date(1985, 5, 20), RealeMaggioreDiZero(3200))
proj = Progetto("Pegaso", RealeMaggioreDiZero(50000))

Coinvolto.add(imp, proj,date.today())

print(len(imp.progetti()))      # 1
print(proj.is_coinvolto(imp))   # True



from Afferenza import Afferenza
from Impiegato import Impiegato
from Dipartimento import Dipartimento
from datetime import date
from mytipes import RealeMaggioreDiZero, NumeroTelefono, Indirizzo

imp = Impiegato("Anna", "Bianchi", date(1988, 3, 15), RealeMaggioreDiZero(2800))
dip = Dipartimento("Fisica", NumeroTelefono("0111234567"), Indirizzo("Via Galileo", "Torino", "10125"))

Afferenza.add(imp, dip, date(2020, 1, 1))

# Se i metodi imp.add_link_afferenza e dip.add_link_afferenza sono implementati, questo test dovrebbe andare
print("Test Afferenza completato")





from Direzione import Direzione
from Impiegato import Impiegato
from Dipartimento import Dipartimento
from datetime import date
from mytipes import RealeMaggioreDiZero, NumeroTelefono, Indirizzo

imp = Impiegato("Luca", "Neri", date(1980, 7, 10), RealeMaggioreDiZero(4000))
dip = Dipartimento("Chimica", NumeroTelefono("0109876543"), Indirizzo("Via Mendeleev", "Genova", "16100"))

Direzione.add(imp, dip)

print("Test Direzione completato")
