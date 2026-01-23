import json
import requests

# Assumiamo che l'app Flask di rentFleet.py giri su questa base URL
BASE_URL = "http://127.0.0.1:5000"

HEADERS= {
    "Content-type": "application/json",
    "Accept": "application/json"
}

veicolo_nuovo={
    "type":"car",
    "plate_id": "GM732RY",
    "model": "Ford-Fiesta",
    "driver_name": "Edoardo Levi",
    "registration_year":2024,
    "status":"available",
    "doors": 5,
    "is_cabrio":False
}

veicolo_aggiornato={
    "type":"car",
    "plate_id": "GM732RY",
    "model": "Ford-Fiesta-st",
    "driver_name": "Edoardo Levi",
    "registration_year":2024,
    "status":"cleaning",
    "doors": 5,
    "is_cabrio":False
}

if __name__== '__main__':
    # Test GET
    response= requests.get(f"{BASE_URL}/", headers=HEADERS)
    print ("GET/",response.status_code)

    # Test GET/vehicles
    response= requests.get(f"{BASE_URL}/vehicles",headers=HEADERS)
    if response.status_code==200:
        veicoli=response.json()
        if len(veicoli)>0:
            print(f"La lista contiente {len(veicoli)} veicoli")
        else:
            print("La lista è vuota")
    
    # Test POST /vehicles
    targa= veicolo_nuovo["plate_id"]
    response = requests.post(f"{BASE_URL}/vehicles", json=veicolo_nuovo, headers=HEADERS)
    print(f"veicolo inserito {response.status_code}")

    # Test GET/vehicles/<plate_id> 
    response= requests.get(f"{BASE_URL}/vehicles/{targa}",headers=HEADERS)
    print(f"verifica {response.status_code}")


    # Test PATCH /vehicles/<plate_id>/status 

    aggiornamento_status= {"status": "cleaning"}
    response = requests.patch(f"{BASE_URL}/vehicles/{targa}/status",json=aggiornamento_status,headers=HEADERS)
    print(f"aggiorno {response.status_code}")

    # Test PUT /vehicles/<plate_id> 

    sostitusci_veicolo= {
        "type": "car",             
        "plate_id": "GM732RY",      
        "model": "Jeep-Compass",
        "driver_name": "Edoardo Levi",
        "registration_year": 2013,  
        "status": "maintenance",
        "doors": 5,                 
        "is_cabrio": False
        }
    response= requests.put(f"{BASE_URL}/vehicles/{targa}", json=sostitusci_veicolo, headers=HEADERS)
    print(f"sostituisco {response.status_code}")

    # Test DELETE /vehicles/<plate_id>

    response=requests.delete(f"{BASE_URL}/vehicles/{targa}",headers=HEADERS)
    print(f"veicolo {targa} eliminato{response.status_code}")

    # Test GET /vehicles/<plate_id> 

    response= requests.get(f"{BASE_URL}/vehicles/{targa}",headers=HEADERS)
    print(f"il veicolo {targa} non è presente {response.status_code}")
    