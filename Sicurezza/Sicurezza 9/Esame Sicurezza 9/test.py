import requests
import json
import sys

TARGET_URL = "http://127.0.0.1:32456"

def test_get_data():
    print(f"\n[1] TEST: Lettura dati (GET {TARGET_URL}/api/data)")
    try:
        response = requests.get(f"{TARGET_URL}/api/data", timeout=3)
        print(f"  -> Status Code : {response.status_code}")
        # Stampiamo solo un pezzo per non intasare il terminale
        print(f"  -> Risposta    : {response.text[:60]}...")
    except requests.exceptions.ConnectionError:
        print("  [!] ERRORE: Impossibile connettersi.")
        sys.exit(1)

def test_post_legitimate_data():
    print(f"\n[2] TEST: Dati LEGITTIMI nel Body (POST {TARGET_URL}/api/data)")
    payload = {"status": "clean"}
    response = requests.post(f"{TARGET_URL}/api/data", json=payload)
    print(f"  -> Status Code : {response.status_code}")

def test_post_malicious_data():
    print(f"\n[3] TEST: Attacco nel Body (POST {TARGET_URL}/api/data)")
    payload = {"pass": "' UNION SELECT * FROM users --"}
    response = requests.post(f"{TARGET_URL}/api/data", json=payload)
    print(f"  -> Status Code : {response.status_code}")
    print(f"  -> Risposta    : {response.text}") # <--- AGGIUNGI QUESTA RIGA!

def test_get_malicious_url():
    print(f"\n[4] TEST: Attacco Diretto via URL (GET {TARGET_URL}/api/data?query='UNION_SELECT--)")
    # Inseriamo l'attacco SQLi direttamente nella barra degli indirizzi!
    response = requests.get(f"{TARGET_URL}/api/data?query='UNION_SELECT--")
    print(f"  -> Status Code : {response.status_code}")
    print(f"  -> Risposta    : {response.text}")

if __name__ == "__main__":
    print(f"Inizio test verso {TARGET_URL}...\n")
    test_get_data()
    test_post_legitimate_data()
    test_post_malicious_data()
    test_get_malicious_url()
    print("\n--- Test Conclusi ---")