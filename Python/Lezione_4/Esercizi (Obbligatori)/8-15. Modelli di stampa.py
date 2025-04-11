"""inserisci le funzioni per l'esempio printing_models.py in un file separato chiamato printing_functions.py. '
'Scrivi un'istruzione import all'inizio di printing_models.py e modifica il file per usare le funzioni importate."""

from printing_functions import caratteristiche_auto

nome="ford"
modello="fiesta"

stampa= caratteristiche_auto(nome, modello)

car= caratteristiche_auto (nome, modello)

for key, value in car.items():
    print(f"{key}: {value}")