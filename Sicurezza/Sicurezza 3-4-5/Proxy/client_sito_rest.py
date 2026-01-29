import requests
import sys

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def login(self, username, password):
        url = f"{self.base_url}/login"
        payload = {'username': username, 'password': password}
        try:
            r = self.session.post(url, json=payload)
            r.raise_for_status() # Lancia errore se status è 4xx o 5xx
            return r.json()
        except Exception as e:
            # Ritorna l'errore per gestirlo nel main
            return {"esito": False, "errore": str(e)}

    def register(self, new_user, new_pass):
        url = f"{self.base_url}/register"
        payload = {'username': new_user, 'password': new_pass}
        r = self.session.post(url, json=payload)
        return r.json()

    def add_item(self, name, description):
        url = f"{self.base_url}/add_item"
        payload = {'name': name, 'description': description}
        r = self.session.post(url, json=payload)
        return r.json()

    def get_items(self):
        url = f"{self.base_url}/get_items"
        r = self.session.get(url)
        return r.json()

    def logout(self):
        url = f"{self.base_url}/logout"
        try:
            r = self.session.get(url)
            self.session.cookies.clear()
            return r.json()
        except:
            return {"esito": False}

# --- ESECUZIONE ---
if __name__ == "__main__":
    TARGET_URL = "http://127.0.0.1:32001"
    client = ApiClient(TARGET_URL)

    print(f"--- Connessione a {TARGET_URL} ---\n")

    try:
        # ==========================================
        # FASE 1: PREPARAZIONE (Admin crea Mario)
        # ==========================================
        print("[1] Login Admin...")
        resp = client.login("admin", "adminpass")
        
        if not resp.get("esito"):
            print(f"    [!] Errore Admin: {resp.get('dati') or resp.get('errore')}")
            sys.exit(1)
        
        print("    [OK] Admin loggato. Creo utente 'mario'...")
        reg_resp = client.register("mario", "12345")
        print(f"    Esito registrazione: {reg_resp.get('dati')}")

        print("    Logout Admin...")
        client.logout()
        print("    [OK] Admin disconnesso.\n")

        # ==========================================
        # FASE 2: OPERATIVITÀ (Mario lavora)
        # ==========================================
        print("[2] Login Mario...")
        resp_mario = client.login("mario", "12345")

        if not resp_mario.get("esito"):
            print("    [!] Login Mario fallito.")
            sys.exit(1)
        
        print("    [OK] Mario loggato.")

        print("[3] Aggiunta Oggetto...")
        item_resp = client.add_item("Smartphone", "iPhone 15")
        print(f"    Server: {item_resp.get('dati')}")

        print("[4] Recupero Lista...")
        items = client.get_items()
        print(f"    Oggetti: {items}")

    except Exception as e:
        print(f"\n[!] Eccezione imprevista: {e}")

    finally:
        # ==========================================
        # FASE 3: CHIUSURA (Logout sicuro)
        # ==========================================
        print("\n[5] Chiusura Sessione (Logout)...")
        logout_resp = client.logout()
        print(f"    [OK] Fine: {logout_resp.get('dati')}")