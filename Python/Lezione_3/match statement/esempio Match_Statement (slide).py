# Define a dictionary
user = {"nome": "Luca", "ruolo": "admin"}
# match statement
match user:
    case {"nome": name, "ruolo": "admin"}:
        print(f"Benvenuto amministratore {user['nome']}")
    case {"nome": name, "ruolo": "utente"}:
        print(f"Benvenuto utente {name}")
    case _:
      print("Ruolo non riconosciuto")

# Define a tuple
point = (3,5)
# match statement
match point:
    case (0, 0):
        print("Origine")
    case (x, 0):
        print(f"Punto sull'asse X: ({x}, 0)")
    case (0, y):
        print(f"Punto sull'asse Y: (0, {y})")
    case _:
       print(f"Punto generico: {(point[0],point[1]) }")


