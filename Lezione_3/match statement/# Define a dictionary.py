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

