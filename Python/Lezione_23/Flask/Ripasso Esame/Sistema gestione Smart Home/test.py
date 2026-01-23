import json
import requests


BASE_URL = "http://127.0.0.1:5000"

HEADERS= {
    "Content-type": "application/json",
    "Accept": "application/json"
}

new_device={
    "type":"bulb",
    "serial_number":"123456789",
    "brand":"Tapo",
    "room":"salotto",
    "installation_year":2026,
    "status":"online",
    "brightness_lumens":800,
    "color_capability":False
}
update_device={
    "type":"bulb",
    "serial_number":"123456789",
    "brand":"Tapo",
    "room":"salotto",
    "installation_year":2026,
    "status":"error",
    "brightness_lumens":800,
    "color_capability":False
}



if __name__== '__main__':
    # Test GET/
    response = requests.get(f"{BASE_URL}/", headers=HEADERS)
    print("GET /", response.status_code, response.json())

    # Test GET/devices

    response=requests.get(f"{BASE_URL}/devices",headers=HEADERS)
    if response.status_code==200:
        device=response.json()
        if len(device)>0:
            print(f"La lista contiene {len(device)} dispositivi")
        else:
            print("la lista è vuota")
    
    # Test POST/devices

    id_disp=new_device["serial_number"]
    response=requests.post(f"{BASE_URL}/devices",json=new_device,headers=HEADERS)

    # Test GET/devices/<serial_number

    response=requests.get(f"{BASE_URL}/devices/{id_disp}",headers=HEADERS)
    print(f"verifica {response.status_code}")

    # Test PATCH/devices/<serial_number>/status

    aggiorna_status={"status":"offline"}
    response=requests.patch(f"{BASE_URL}/devices/{id_disp}/status",json=aggiorna_status,headers=HEADERS)
    print (f"aggiorno {response.status_code}")

    # Test PUT/devices/<serial_number> 
    sostituisci_dispositvo= {
        "type":"bulb",
        "serial_number":"123456789",
        "brand":"alexa",
        "room":"camera",
        "installation_year":2026,
        "status":"online",
        "brightness_lumens":800,
        "color_capability":False
    }
    response=requests.put(f"{BASE_URL}/devices/{id_disp}",json=sostituisci_dispositvo,headers=HEADERS)
    print(f"sostituisco {response.status_code}")

    # Test DELETE/devices/<serial_number>

    response=requests.delete(f"{BASE_URL}/devices/{id_disp}",headers=HEADERS)
    print(f" dispositivo {id_disp}, eliminato{response.status_code}")

    # Test GET/devices/<serial_number>

    response= requests.get(f"{BASE_URL}/devices/{id_disp}",headers=HEADERS)
    print(f"il dispositivo {id_disp}, non è presente {response.status_code}")