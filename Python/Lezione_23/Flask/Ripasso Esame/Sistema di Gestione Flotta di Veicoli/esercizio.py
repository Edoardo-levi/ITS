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
# PARTE 2: APP FLASK (Qui devi scrivere tu)
# ---------------------------------------------------------

# TODO: Importa Flask, request, jsonify e url_for
# ...

# TODO: Crea l'istanza dell'applicazione Flask
# app = ...

# --- ROUTE GET ---

@app.route('/', methods=['GET'])
def welcome():
    links={
        "vehicles_list":url_for("vehicles"),
        "vehicle_sample":url_for("get_plate",plate_id='HA014AS'),
        "estimate_sample":url_for("device",plate_id='HA014AS', factor=2.0)
    }
    return jsonify ({
        "messaggio":"Welcome to Rent Service API",
        "links":links
    })



# TODO: Route '/vehicles' (Lista veicoli)
# Deve restituire la lista JSON di tutti i veicoli (usa fleet_manager.list_all())
# @app.route( ... )
# def get_vehicles():
@app.route('/vehicles',methods=['GET'])
def vehicles():

    return jsonify(fleet_manager.list_all())

# TODO: Route '/vehicles/<plate_id>' (Dettaglio singolo veicolo)
# Cerca il veicolo con fleet_manager.get().
# Se esiste: restituisci il JSON con info().
# Se NON esiste: restituisci errore {"error": ...} e status code 404.
# @app.route( ... )
# def get_vehicle(plate_id):
@app.route('/vehicles/<string:plate_id>', methods=['GET'])
def get_plate(plate_id:str):
    vehicle=fleet_manager.get(plate_id)
    if not vehicle:
        return jsonify({"message": "Errore il veicolo non esiste"}),404
    else:
        return jsonify(vehicle.info()), 200

# TODO: Route '/vehicles/<plate_id>/prep-time/<factor>' (Tempo preparazione)
# Leggi factor come float.
# Chiama estimated_prep_time(factor) sull'oggetto veicolo.
# Restituisci il JSON con il calcolo. Gestisci il 404 se il veicolo non c'è.
# @app.route( ... )
# def get_prep_time(plate_id, factor):
@app.route('/vehicles/<string:plate_id>/prep-time/float:factor',methods=['GET'])
def device (plate_id:str,factor:float):
    vehicle=fleet_manager.get(plate_id)
    if not vehicle:
        return jsonify({"message":"Errore il veicolo non esiste"}),404
    else:
        info:dict=vehicle.info()
        info["tempo_attesa"]=vehicle.estimated_prep_time(factor)
        return jsonify (info),200

# --- ROUTE POST ---

# TODO: Route '/vehicles' (Aggiungi veicolo)
# 1. Leggi il JSON dal body (request.get_json()).
# 2. Controlla se 'type' è 'car' o 'van' e istanzia la classe corretta.
# 3. Chiama fleet_manager.add().
# 4. Se add() restituisce True -> return JSON conferma, status 201.
# 5. Se add() restituisce False (già esiste) -> return errore, status 400.
# @app.route( ... )
# def create_vehicle():
@app.route('/vehicles', methods =['POST'])
def create_vehicles():
    data = request.get_json()
    new_vehicle: dict = None
    if data.get('type') == 'car':
        new_vehicle = Car(
            plate_id=data['id'],
            model=data['model'],
            driver_name=data['driver_name'],
            registration_year=data['registration_year'],
            status=data['status'],
            doors=data['doors'],
            is_cabrio=data['is_cabrio']
        )
    elif data.get('type') == 'van':
        new_vehicle = Van(
            plate_id=data['id'],
            model=data['model'],
            driver_name=data['driver_name'],
            registration_year=data['registration_year'],
            status=data['status'],
            max_load_kg=data['max_load_kg'],
            require_special_license=data['require_special_license']
        )
    else:
        return jsonify({
            "message": "Veicolo non supportato"
        }),404
    if fleet_manager.add(new_vehicle)== True:
        return jsonify(new_vehicle.info()),201
    else:
        return jsonify({"errore":"Veicolo già esistente"}),400

# --- ROUTE PUT ---

# TODO: Route '/vehicles/<plate_id>' (Sostituisci veicolo)
# 1. Leggi JSON.
# 2. Crea il nuovo oggetto Car o Van.
# 3. Chiama fleet_manager.update().
# 4. Restituisci conferma (es. il nuovo veicolo info).
# @app.route( ... )
# def update_vehicle(plate_id):
@app.route('/vehicles/<plate_id>',methods=['PUT'])
def update_vehicles(plate_id:str):
    data =request.get_json()
    if fleet_manager.get(plate_id) is None:
        return jsonify ({"message": "Errore veicolo non trovato"}),404
    new_vehicle:dict=None

    if data.get("type") == "car":
            new_vehicle= Car(
            plate_id=data['id'],
            model=data['model'],
            driver_name=data['driver_name'],
            registration_year=data['registration_year'],
            status=data['status'],
            doors=data['doors'],
            is_cabrio=data['is_cabrio']
        )
    elif data.get("type") == "van":
            new_vehicle = Van(
            plate_id=data['id'],
            model=data['model'],
            driver_name=data['driver_name'],
            registration_year=data['registration_year'],
            status=data['status'],
            max_load_kg=data['max_load_kg'],
            require_special_license=data['require_special_license']
        )
    else:
        return jsonify ({"message":"Erorre"}),400

    fleet_manager.update(plate_id,new_vehicle)
    return jsonify(new_vehicle.info()),200     


# --- ROUTE PATCH ---

# TODO: Route '/vehicles/<plate_id>/status' (Aggiorna solo status)
# 1. Leggi JSON (es. {"status": "cleaning"}).
# 2. Controlla se il veicolo esiste.
# 3. Chiama fleet_manager.patch_status().
# 4. Restituisci info veicolo aggiornato o conferma.
# @app.route( ... )
# def patch_vehicle_status(plate_id):
@app.route('/vehicles/<string:plate_id>/status')
def patch_vehicle_status(plate_id):
    data=request.get_json()
    if fleet_manager.get(plate_id) is None:
        return jsonify({"Message": "Veicolo non trovato"}), 404
    if "status" not in data:
        return jsonify ({"message":"Status non trovato"}),404
    else:
        fleet_manager.patch_status(patch_vehicle_status,new_status=data["status"])
        return jsonify(fleet_manager.get(plate_id).info())


# --- ROUTE DELETE ---

# TODO: Route '/vehicles/<plate_id>' (Cancella veicolo)
# Chiama fleet_manager.delete().
# Se True -> conferma cancellazione.
# Se False -> errore 404.
# @app.route( ... )
# def delete_vehicle(plate_id):
@app.route('/vehicles/<plate_id>', methods= ["DELETE"])

def delete_vehicle(plate_id):
    if fleet_manager.get(plate_id) is None:
        return jsonify ({"message": "il veicolo non esiste"}),404
    else:
        fleet_manager.delete(plate_id)
        return jsonify({"message": "il veicolo è stato rimosso", "id": plate_id}), 200


# Avvio del server
if __name__ == "__main__":
    # TODO: Avvia l'app in modalità debug
    # ...
    pass