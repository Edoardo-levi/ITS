import json
import requests

BASE_URL = "http://127.0.0.1:5000"

HEADERS = {
    "Content-type": "application/json",
    "Accept": "application/json"
}

# Usiamo un ID nuovo per evitare conflitti con quelli pre-caricati
ID_TEST = "BK-999"

nuova_prenotazione = {
    "type": "exam",
    "booking_id": ID_TEST,
    "patient_name": "Giulia Verdi",
    "doctor": "Dr. Neri",
    "department": "Radiologia",
    "date": "2026-02-12",
    "time": "09:15",
    "status": "scheduled",
    "exam_type": "RMN",
    "requires_fasting": True
}

if __name__ == '__main__':
    # 1. Test GET /
    response = requests.get(f"{BASE_URL}/", headers=HEADERS)
    print(f"GET /: {response.status_code}")

    # 2. Test GET /bookings (corretto refuso 'bookigs')
    response = requests.get(f"{BASE_URL}/bookings", headers=HEADERS)
    if response.status_code == 200: 
        bookings = response.json()
        print(f"La lista contiene {len(bookings)} prenotazioni")

    # 3. Test POST /bookings (invio tutto il dizionario, non solo l'ID)
    response = requests.post(f"{BASE_URL}/bookings", json=nuova_prenotazione, headers=HEADERS)
    print(f"POST /bookings: {response.status_code}")

    # 4. Test GET /bookings/<id>
    response = requests.get(f"{BASE_URL}/bookings/{ID_TEST}", headers=HEADERS)
    print(f"Verifica prenotazione creata: {response.status_code}")

    # 5. Test PATCH /status
    aggiornamento_status = {"status": "checked_in"}
    response = requests.patch(f"{BASE_URL}/bookings/{ID_TEST}/status", json=aggiornamento_status, headers=HEADERS)
    print(f"PATCH status: {response.status_code}")

    # 6. Test PUT (Sostituzione con dati coerenti per 'visit')
    sostituzione_prenotazione = {
        "type": "visit",
        "booking_id": ID_TEST,
        "patient_name": "Giulia Verdi",
        "doctor": "Dr. Neri",
        "department": "MST",
        "date": "2026-02-12",
        "time": "09:15",
        "status": "scheduled",
        "visit_reason": "Controllo post-operatorio",
        "first_time": False
    }
    response = requests.put(f"{BASE_URL}/bookings/{ID_TEST}", json=sostituzione_prenotazione, headers=HEADERS)
    print(f"PUT sostituzione: {response.status_code}")

    # 7. Test DELETE
    response = requests.delete(f"{BASE_URL}/bookings/{ID_TEST}", headers=HEADERS)
    print(f"DELETE prenotazione: {response.status_code}")

    # 8. Verifica finale (deve essere 404)
    response = requests.get(f"{BASE_URL}/bookings/{ID_TEST}", headers=HEADERS)
    print(f"Verifica post-cancellazione (atteso 404): {response.status_code}")