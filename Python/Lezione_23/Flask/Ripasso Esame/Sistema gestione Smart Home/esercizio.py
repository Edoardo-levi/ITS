from abc import ABC, abstractmethod
from flask import Flask, request, jsonify, url_for

# ---------------------------------------------------------
# PARTE 1: LOGICA DEL SISTEMA (Classi)
# ---------------------------------------------------------

class SmartDevice(ABC):
    def __init__(self, serial_number: str, brand: str, room: str, installation_year: int, status: str):
        self.serial_number = serial_number
        self.brand = brand
        self.room = room
        self.installation_year = installation_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        pass

    @abstractmethod
    def energy_consumption(self) -> float | int:
        pass

    @abstractmethod
    def connection_quality(self) -> int:
        pass

    def info(self) -> dict:
        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status,
            "device_type": self.device_type()
        }

    def diagnostics_time(self, factor: float = 1.0) -> int:
        result = self.energy_consumption() * factor + self.connection_quality() * 10
        return int(result)


class SmartBulb(SmartDevice):
    def __init__(self, serial_number, brand, room, installation_year, status, brightness_lumens: int, color_capability: bool):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability

    def device_type(self) -> str:
        return "bulb"

    def energy_consumption(self) -> float | int:
        return 12

    def connection_quality(self) -> int:
        return 3

    def info(self) -> dict:
        data = super().info()
        data.update({
            "brightness_lumens": self.brightness_lumens,
            "color_capability": self.color_capability
        })
        return data


class SecurityCamera(SmartDevice):
    def __init__(self, serial_number, brand, room, installation_year, status, resolution: str, night_vision: bool):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.resolution = resolution
        self.night_vision = night_vision

    def device_type(self) -> str:
        return "camera"

    def energy_consumption(self) -> float | int:
        return 50

    def connection_quality(self) -> int:
        return 9

    def info(self) -> dict:
        data = super().info()
        data.update({
            "resolution": self.resolution,
            "night_vision": self.night_vision
        })
        return data


class IoTHub:
    def __init__(self):
        self.devices = {}

    def add(self, device: SmartDevice) -> bool:
        if device.serial_number in self.devices:
            return False
        self.devices[device.serial_number] = device
        return True

    def get(self, serial_number: str) -> SmartDevice | None:
        return self.devices.get(serial_number)

    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_status: str) -> None:
        if serial_number in self.devices:
            self.devices[serial_number].status = new_status

    def delete(self, serial_number: str) -> bool:
        if serial_number in self.devices:
            del self.devices[serial_number]
            return True
        return False

    def list_all(self) -> list:
        return [dev.info() for dev in self.devices.values()]


# ---------------------------------------------------------
# INIZIALIZZAZIONE DATI
# ---------------------------------------------------------

iot_hub = IoTHub()

bulb_demo = SmartBulb("SN-101", "Philips Hue", "Kitchen", 2023, "online", 800, True)
camera_demo = SecurityCamera("SN-10293-X", "Nest", "Garden", 2022, "recording", "4K", True)

iot_hub.add(bulb_demo)
iot_hub.add(camera_demo)


# ---------------------------------------------------------
# PARTE 2: APP FLASK
# ---------------------------------------------------------

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    links = {
        "device_list": url_for('get_devices', _external=True),
        "device_sample": url_for('get_devices_details', serial_number="SN-101", _external=True),
        "estimate_sample": url_for("diagnostic_time", serial_number="SN-101", factor=1.0, _external=True)
    }
    return jsonify({
        "message": "Smart Home Hub API",
        "links": links
    })

@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify(iot_hub.list_all()), 200

# CORREZIONE: Nome parametro coerente (serial_number)
@app.route('/devices/<string:serial_number>', methods=['GET'])
def get_devices_details(serial_number: str):
    device = iot_hub.get(serial_number)
    if not device:
        return jsonify({"errore": "Il dispositivo non è presente"}), 404
    else:
        return jsonify(device.info()), 200

@app.route('/devices/<string:serial_number>/diagnostic/<float:factor>', methods=['GET'])
def diagnostic_time(serial_number: str, factor: float):
    device = iot_hub.get(serial_number)
    if not device:
        return jsonify({"error": "il dispositivo non esiste"}), 404 # Aggiunto 404
    else:
        time_estimate = device.info()
        time_estimate["tempo_attesa"] = device.diagnostics_time(factor)
        return jsonify(time_estimate), 200
    
@app.route('/devices', methods=['POST'])
def add_device():
    data = request.get_json()
    new_device = None
    
    # Validazione base per evitare crash se mancano campi
    if not data or 'serial_number' not in data:
        return jsonify({"error": "Dati mancanti"}), 400

    if data.get('type') == "bulb":
        new_device = SmartBulb(
                serial_number=data.get("serial_number"),
                brand=data["brand"],
                room=data["room"],
                installation_year=data["installation_year"],
                status=data["status"],
                brightness_lumens=data["brightness_lumens"],
                color_capability=data["color_capability"]
        )
        # CORREZIONE IMPORTANTE: Rimosso il return jsonify({}) qui!
        
    elif data.get('type') == "camera":
        new_device = SecurityCamera(
            serial_number=data.get("serial_number"), 
            # CORREZIONE: data["brand"] invece di ["brand"]
            brand=data["brand"], 
            room=data["room"], 
            installation_year=data["installation_year"], 
            status=data["status"],
            # CORREZIONE: resolution invece di brightness_lumens
            resolution=data["resolution"], 
            night_vision=data["night_vision"]
        )
    else:
        return jsonify({"message": "Tipo dispositivo non supportato"}), 400
    
    if iot_hub.add(new_device):
        return jsonify(new_device.info()), 201
    else:
        return jsonify({"errore": "dispositivo già esistente"}), 400
    
# CORREZIONE: <string:serial_number> invece di <stringa:...>
@app.route('/devices/<string:serial_number>', methods=['PUT'])
def update_device(serial_number: str):
    data = request.get_json()
    if iot_hub.get(serial_number) is None:
        return jsonify({"message": "Dispositivo non trovato"}), 404
    
    new_device = None
    if data.get("type") == "bulb":
        new_device = SmartBulb(
                serial_number=serial_number,
                brand=data["brand"],
                room=data["room"],
                installation_year=data["installation_year"],
                status=data["status"],
                brightness_lumens=data["brightness_lumens"],
                color_capability=data["color_capability"]
        )
    elif data.get("type") == "camera":
        new_device = SecurityCamera(
            serial_number=serial_number, 
            # CORREZIONE: data["brand"] invece di ["brand"]
            brand=data["brand"], 
            room=data["room"], 
            installation_year=data["installation_year"], 
            status=data["status"],
            # CORREZIONE: resolution invece di brightness_lumens
            resolution=data["resolution"], 
            night_vision=data["night_vision"]
            )
    else:
        return jsonify({"message": "Errore tipo"}), 400
    
    iot_hub.update(serial_number, new_device)
    return jsonify(new_device.info()), 200

# CORREZIONE: <string:serial_number> invece di string:<...>
@app.route('/devices/<string:serial_number>/status', methods=['PATCH'])
def update_status(serial_number: str):
    # CORREZIONE: request.get_json() invece di request.json()
    data = request.get_json()
    
    if iot_hub.get(serial_number) is None:
        return jsonify({"message": "error"}), 404
    if "status" not in data:
        return jsonify({"message": "status non trovato"}), 400
        
    iot_hub.patch_status(serial_number, new_status=data["status"])
    return jsonify(iot_hub.get(serial_number).info())

@app.route('/devices/<string:serial_number>', methods=['DELETE'])
def delete_devices(serial_number):
    if iot_hub.get(serial_number) is None:
        return jsonify({"message": "dispositivo non presente"}), 404
    
    iot_hub.delete(serial_number)
    return jsonify({"message": "Il dispositivo è stato rimosso", "numero_seriale": serial_number}), 200

if __name__ == "__main__":
    app.run(debug=True)