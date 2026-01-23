# ---------------------------------------------------------
# PARTE 1: LOGICA DEL SISTEMA (Questa parte è già pronta)
# ---------------------------------------------------------
from abc import ABC, abstractmethod
from flask import *

# Sezione classi (Vehicle, Car, Van, FleetManager)
# Incolla qui le classi che abbiamo scritto prima, oppure usa queste:

class Vehicle(ABC):
    def __init__(self, plate_id: str, model: str, driver_name: str, registration_year: int, status: str):
        self.plate_id = plate_id
        self.model = model
        self.driver_name = driver_name
        self.registration_year = registration_year
        self.status = status

    @abstractmethod
    def vehicle_type(self) -> str:
        pass

    @abstractmethod
    def base_cleaning_time(self) -> int:
        pass

    @abstractmethod
    def wear_level(self) -> int:
        pass

    def info(self) -> dict:
        return {
            "id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "vehicle_type": self.vehicle_type(),
            "registration_year": self.registration_year,
            "status": self.status,
        }

    def estimated_prep_time(self, factor: float = 1.0) -> int:
        return int(self.base_cleaning_time() * factor + self.wear_level() * 15)

class Car(Vehicle):
    def __init__(self, plate_id, model, driver_name, registration_year, status, doors, is_cabrio):
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self) -> str: return "car"
    def base_cleaning_time(self) -> int: return 30
    def wear_level(self) -> int: return 2
    def info(self) -> dict:
        data = super().info()
        data.update({"doors": self.doors, "is_cabrio": self.is_cabrio})
        return data

class Van(Vehicle):
    def __init__(self, plate_id, model, driver_name, registration_year, status, max_load_kg, require_special_license):
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self) -> str: return "van"
    def base_cleaning_time(self) -> int: return 60
    def wear_level(self) -> int: return 4
    def info(self) -> dict:
        data = super().info()
        data.update({"max_load_kg": self.max_load_kg, "require_special_license": self.require_special_license})
        return data

class FleetManager:
    def __init__(self):
        self.vehicles = {}
    def add(self, vehicle: Vehicle) -> bool:
        if vehicle.plate_id in self.vehicles: return False
        self.vehicles[vehicle.plate_id] = vehicle
        return True
    def get(self, plate_id: str) -> Vehicle:
        return self.vehicles.get(plate_id)
    def update(self, plate_id: str, new_vehicle: Vehicle) -> None:
        self.vehicles[plate_id] = new_vehicle
    def patch_status(self, plate_id: str, new_status: str) -> None:
        if plate_id in self.vehicles: self.vehicles[plate_id].status = new_status
    def delete(self, plate_id: str) -> bool:
        if plate_id in self.vehicles:
            del self.vehicles[plate_id]
            return True
        return False
    def list_all(self) -> list:
        return [v.info() for v in self.vehicles.values()]

# Inizializzazione dati di esempio
fleet_manager = FleetManager()
fleet_manager.add(Car("HA014AS", "Fiat Panda", None, 2020, "available", 5, False))
fleet_manager.add(Van("CC216FG", "Peugeot Partner", "Mario Rossi", 2018, "rented", 800, False))


# ---------------------------------------------------------
# PARTE 2: APP FLASK (CORRETTA)
# ---------------------------------------------------------


app = Flask(__name__)

# --- ROUTE GET ---

@app.route('/', methods=['GET'])
def welcome():
    links = {
        "vehicles_list": url_for("vehicles"),
        "vehicle_sample": url_for("get_plate", plate_id = "HA014AS" ),
        "estimate_sample": url_for("devices", plate_id= "HA014AS", factor = 2.0)
    }
    return jsonify ({
        "message": "Welcome to Rent Center API",
        "links": links
    })

@app.route('/vehicles', methods=['GET'])
def vehicles():
    return jsonify(fleet_manager.list_all())

@app.route('/vehicles/<string:plate_id>', methods=['GET'])
def get_plate(plate_id: str):
    vehicle = fleet_manager.get(plate_id)
    if not vehicle:
        return jsonify({"message": "Errore: il veicolo non esiste"}), 404
    return jsonify(vehicle.info()), 200

# CORREZIONE QUI: <float:factor> invece di float:factor
@app.route('/vehicles/<string:plate_id>/prep-time/<float:factor>', methods=['GET'])
def device(plate_id: str, factor: float):
    vehicle = fleet_manager.get(plate_id)
    if not vehicle:
        return jsonify({"message": "Errore: il veicolo non esiste"}), 404
    
    info = vehicle.info()
    info["tempo_attesa"] = vehicle.estimated_prep_time(factor)
    return jsonify(info), 200

# --- ROUTE POST ---

@app.route('/vehicles', methods=['POST'])
def create_vehicles():
    data = request.get_json()
    # CORREZIONE: Uso .get('plate_id') per matchare il test
    pid = data.get('plate_id') 
    
    new_vehicle = None
    if data.get('type') == 'car':
        new_vehicle = Car(
            plate_id=pid,
            model=data['model'],
            driver_name=data.get('driver_name'),
            registration_year=data['registration_year'],
            status=data['status'],
            doors=data['doors'],
            is_cabrio=data['is_cabrio']
        )
    elif data.get('type') == 'van':
        new_vehicle = Van(
            plate_id=pid,
            model=data['model'],
            driver_name=data.get('driver_name'),
            registration_year=data['registration_year'],
            status=data['status'],
            max_load_kg=data['max_load_kg'],
            require_special_license=data['require_special_license']
        )
    else:
        return jsonify({"message": "Veicolo non supportato"}), 400

    if fleet_manager.add(new_vehicle):
        return jsonify(new_vehicle.info()), 201
    else:
        return jsonify({"errore": "Veicolo già esistente"}), 400

# --- ROUTE PUT ---

@app.route('/vehicles/<plate_id>', methods=['PUT'])
def update_vehicles(plate_id: str):
    data = request.get_json()
    if fleet_manager.get(plate_id) is None:
        return jsonify({"message": "Errore veicolo non trovato"}), 404
    
    new_vehicle = None
    # L'ID nell'oggetto deve corrispondere all'URL
    pid = plate_id 

    if data.get("type") == "car":
        new_vehicle = Car(pid, data['model'], data.get('driver_name'), data['registration_year'], data['status'], data['doors'], data['is_cabrio'])
    elif data.get("type") == "van":
        new_vehicle = Van(pid, data['model'], data.get('driver_name'), data['registration_year'], data['status'], data['max_load_kg'], data['require_special_license'])
    else:
        return jsonify({"message": "Errore tipo veicolo"}), 400

    fleet_manager.update(plate_id, new_vehicle)
    return jsonify(new_vehicle.info()), 200     

# --- ROUTE PATCH ---

@app.route('/vehicles/<string:plate_id>/status', methods=['PATCH'])
def patch_vehicle_status(plate_id):
    data = request.get_json()
    if fleet_manager.get(plate_id) is None:
        return jsonify({"Message": "Veicolo non trovato"}), 404
    
    if "status" not in data:
        return jsonify({"message": "Status non trovato nel body"}), 400
    
    # CORREZIONE: passiamo plate_id, non la funzione stessa
    fleet_manager.patch_status(plate_id, new_status=data["status"])
    return jsonify(fleet_manager.get(plate_id).info())

# --- ROUTE DELETE ---

@app.route('/vehicles/<plate_id>', methods=["DELETE"])
def delete_vehicle(plate_id):
    if fleet_manager.get(plate_id) is None:
        return jsonify({"message": "il veicolo non esiste"}), 404
    
    fleet_manager.delete(plate_id)
    return jsonify({"message": "il veicolo è stato rimosso", "id": plate_id}), 200

if __name__ == "__main__":
    app.run(debug=True)