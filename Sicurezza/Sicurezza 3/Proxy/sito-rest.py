import os
from flask import Flask, jsonify, request, session

SECRET_KEY = 'AAA' 

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# 1. Inizializzo con un admin per poter usare il sistema
utenti = {"admin": "adminpass"}
cose = {}

@app.route('/login', methods=['POST'])
def login():
    # LEGGO IL JSON DAL BODY
    data = request.get_json()
    if not data:
        return jsonify({"esito": False, "dati": "JSON mancante"}), 400

    username = data.get('username')
    password = data.get('password')

    if username in utenti and utenti[username] == password:
        session['username'] = username
        return jsonify({"esito": True, "dati": "Login effettuato con successo"})
    else:
        return jsonify({"esito": False, "dati": "Credenziali non valide"}), 401

@app.route('/register', methods=['POST'])
def register():
    # Controllo sessione
    if session.get('username') is None or session['username'] != "admin":
        return jsonify({"esito": False, "dati": "Utente non autorizzato"}), 403

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in utenti:
        return jsonify({"esito": False, "dati": "Utente già esistente"})

    utenti[username] = password
    return jsonify({"esito": True, "dati": f"Utente {username} registrato"})

@app.route('/add_item', methods=['POST'])
def add_item():
    # CORRETTO IL BUG: controllo 'username' invece di 'user_id'
    if 'username' not in session:
        return jsonify({"esito": False, "dati": "Devi fare login prima"}), 401

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    cose[name] = description
    return jsonify({"esito": True, "dati": "Elemento aggiunto"})

# --- Le route GET rimangono uguali (non hanno body) ---
@app.route('/getallusers', methods=['GET'])
def getall():
    # Per sicurezza, meglio non restituire le password, ma per debug va bene
    return jsonify(utenti)

@app.route('/get_items', methods=['GET'])
def get_items():
    return jsonify(cose)

@app.route('/logout') # Può rimanere GET o POST
def logout():
    session.clear()
    return jsonify({"esito": True, "dati": "Logout effettuato"})

if __name__ == '__main__':
    # Ascolta su tutte le interfacce per facilitare i test di rete
    app.run(host="0.0.0.0", port=32001, debug=True)