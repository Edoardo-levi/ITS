from Dottore import Dottore
from Paziente import Paziente
from Fattura import Fattura

# ======== Creazione Dottori ========
dottore_1 = Dottore("Mario", "Rossi", "Cardiologia", 150.0)
dottore_2 = Dottore("Luigi", "Verdi", "Pediatria", 200.0)

# Imposto l'età affinché i dottori siano validi
dottore_1.setAge(45)
dottore_2.setAge(50)

# Presentazione dei medici
dottore_1.doctorGreet()
dottore_2.doctorGreet()

# ======== Creazione Pazienti ========
# Lista 1 - 3 pazienti
pazienti_1 = [
    Paziente("Anna", "Bianchi", "P001"),
    Paziente("Luca", "Neri", "P002"),
    Paziente("Sara", "Rossi", "P003")
]

# Lista 2 - 1 paziente
pazienti_2 = [
    Paziente("Marco", "Verdi", "P004")
]

# ======== Creazione Fatture ========
fattura1 = Fattura(pazienti_1, dottore_1)
fattura2 = Fattura(pazienti_2, dottore_2)

# Stampa salario iniziale
print(f"Salario Dottore1: {fattura1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

# ======== Trasferimento Paziente ========
# Rimuovo il primo paziente dalla lista del dottore 1
paziente_da_trasferire = pazienti_1[0]  # P001
fattura1.removePatient(paziente_da_trasferire.getIdCode())

# Aggiungo lo stesso paziente alla lista del dottore 2
fattura2.addPatient(paziente_da_trasferire)

# Stampa salario aggiornato
print(f"Salario Dottore1: {fattura1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

# ======== Guadagno totale dell'ospedale ========
totale = fattura1.getSalary() + fattura2.getSalary()
print(f"In totale, l'ospedale ha incassato: {totale} euro!")
