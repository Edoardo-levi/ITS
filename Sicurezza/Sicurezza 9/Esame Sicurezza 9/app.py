from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# File che fungerà da database dinamico per il server
DB_FILE = 'server_db.json'

def init_db():
    """Inizializza il database se non esiste"""
    if not os.path.exists(DB_FILE):
        default_data = {
            "users": {
                'admin': {'pass': 'admin999', 'role': 'admin', 'status': 'active', 'perms': 'Level 5'},
                'user': {'pass': 'password123', 'role': 'user', 'status': 'active', 'perms': 'Level 1'}
            },
            "logs": []
        }
        with open(DB_FILE, 'w') as f:
            json.dump(default_data, f)

def load_db():
    """Carica i dati dal file JSON"""
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(data):
    """Salva i dati nel file JSON"""
    with open(DB_FILE, 'w') as f:
        json.dump(data, f)

# Inizializza il DB all'avvio del server
init_db()

@app.route('/')
def index():
    """Rotte principale che serve la tua interfaccia HTML"""
    return render_template('index.html')

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    """API REST per sincronizzare il frontend con il backend Flask"""
    if request.method == 'POST':
        # Quando il frontend invia nuovi dati (nuovi utenti, log, ecc.), li salviamo
        data = request.json
        save_db(data)
        return jsonify({"status": "success"})
    else:
        # Quando il frontend richiede i dati all'avvio
        return jsonify(load_db())

@app.route('/api/login', methods=['POST'])
def login():
    """Endpoint per verificare le credenziali (Messo in Sicurezza Definitiva)"""
    user = request.form.get('username', '')
    pwd = request.form.get('password', '')
    
    # 1. SANITIZZAZIONE (Difesa Server): Blocca alla radice qualsiasi carattere illegale
    dangerous_chars = ["'", '"', "--", ";", "union", "select", "%27", "%2D"]
    for char in dangerous_chars:
        if char in pwd.lower() or char in user.lower():
            return jsonify({"status": "failure", "message": "Caratteri illegali rilevati dal Server"}), 403
            
    # 2. AUTENTICAZIONE STANDARD SICURA
    db = load_db()
    
    # --- CONTROLLO DI SICUREZZA E RIPARAZIONE DB ---
    # Se il database si è corrotto e manca la chiave 'users', lo ripariamo al volo
    if 'users' not in db:
        repaired_data = {
            "users": {
                'admin': {'pass': 'admin999', 'role': 'admin', 'status': 'active', 'perms': 'Level 5'},
                'user': {'pass': 'password123', 'role': 'user', 'status': 'active', 'perms': 'Level 1'}
            },
            "logs": db.get("logs", []) # Mantiene i log salvati, se esistono
        }
        save_db(repaired_data)
        db = repaired_data
    # -----------------------------------------------

    # Verifica finale delle credenziali
    if user in db['users'] and db['users'][user]['pass'] == pwd:
        role = db['users'][user]['role']
        return jsonify({"status": "success", "user": user, "role": role})
        
    return jsonify({"status": "failure", "message": "Credenziali errate"}), 401

if __name__ == '__main__':
    # Flask gira sulla 5020, il WAF sulla 32456
    app.run(host='0.0.0.0', port=5020, debug=True)