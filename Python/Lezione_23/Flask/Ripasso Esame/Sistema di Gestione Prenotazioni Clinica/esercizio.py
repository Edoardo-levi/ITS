from abc import ABC, abstractmethod
from flask import *

class Booking(ABC):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, 
                 department: str, date: str, time: str, status: str):
        self.booking_id = booking_id
        self.patient_name = patient_name
        self.doctor = doctor
        self.department = department
        self.date = date
        self.time = time
        self.status = status

    @abstractmethod
    def booking_type(self) -> str:
        """Restituisce il tipo di prenotazione (es. 'visit', 'exam')."""
        pass

    @abstractmethod
    def base_duration(self) -> int:
        """Restituisce la durata standard in minuti."""
        pass

    @abstractmethod
    def priority_level(self) -> int:
        """Restituisce la priorità da 1 a 10."""
        pass

    def info(self) -> dict:
        """Restituisce un dizionario con le informazioni comuni."""
        return {
            "booking_id": self.booking_id,
            "patient_name": self.patient_name,
            "doctor": self.doctor,
            "department": self.department,
            "date": self.date,
            "time": self.time,
            "status": self.status,
            "type": self.booking_type(),
            "priority": self.priority_level()
        }

    def estimated_wait(self, factor: float = 1.0) -> int:
        """Calcola l'attesa stimata: base_duration * factor + priority * 5."""
        return int(self.base_duration() * factor + self.priority_level() * 5)


class MedicalVisit(Booking):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, 
                 department: str, date: str, time: str, status: str, 
                 visit_reason: str, first_time: bool):
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.visit_reason = visit_reason
        self.first_time = first_time

    def booking_type(self) -> str:
        return "visit"

    def base_duration(self) -> int:
        return 20  # Durata standard per una visita

    def priority_level(self) -> int:
        reason = (self.visit_reason or "").lower()
        keywords = ["urgente", "dolore", "acuto", "svenimento"]
        for k in keywords:
            if k in reason:
                return 7
        return 5

    def info(self) -> dict:
        data = super().info()
        data.update({
            "visit_reason": self.visit_reason,
            "first_time": self.first_time
        })
        return data


class DiagnosticExam(Booking):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, 
                 department: str, date: str, time: str, status: str, 
                 exam_type: str, requires_fasting: bool):
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.exam_type = exam_type
        self.requires_fasting = requires_fasting

    def booking_type(self) -> str:
        return "exam"

    def base_duration(self) -> int:
        # Esempio: esami complessi durano di più
        et = (self.exam_type or "").lower()
        if et in ["rmn", "mri"]:
            return 45
        return 30

    def priority_level(self) -> int:
        et = (self.exam_type or "").strip().lower()
        if et in ["rmn", "mri", "tac", "ct"]:
            return 8
        return 7

    def info(self) -> dict:
        data = super().info()
        data.update({
            "exam_type": self.exam_type,
            "requires_fasting": self.requires_fasting
        })
        return data


class ClinicHub:
    def __init__(self):
        self.bookings: dict[str, Booking] = {}

    def add(self, booking: Booking) -> bool:
        if booking.booking_id in self.bookings:
            return False
        self.bookings[booking.booking_id] = booking
        return True

    def get(self, booking_id: str) -> Booking | None:
        return self.bookings.get(booking_id)

    def update(self, booking_id: str, new_booking: Booking) -> None:
        # Sostituzione totale (PUT logic)
        self.bookings[booking_id] = new_booking

    def patch_status(self, booking_id: str, new_status: str) -> bool:
        if booking_id in self.bookings:
            self.bookings[booking_id].status = new_status
            return True
        return False

    def delete(self, booking_id: str) -> bool:
        if booking_id in self.bookings:
            del self.bookings[booking_id]
            return True
        return False

    def list_all(self) -> list[dict]:
        return [b.info() for b in self.bookings.values()]
    

# Inizializzazione del sistema
hub = ClinicHub()

# 1. Creazione di un oggetto MedicalVisit
visit_1 = MedicalVisit(
    booking_id="BK-101",
    patient_name="Mario Rossi",
    doctor="Dr. Bianchi",
    department="Cardiologia",
    date="2026-02-10",
    time="14:30",
    status="scheduled",
    visit_reason="Dolore toracico",
    first_time=True
)

# 2. Creazione di un oggetto DiagnosticExam
exam_1 = DiagnosticExam(
    booking_id="BK-202",
    patient_name="Giulia Verdi",
    doctor="Dr. Neri",
    department="Radiologia",
    date="2026-02-12",
    time="09:15",
    status="scheduled",
    exam_type="RMN",
    requires_fasting=True
)

# Aggiunta degli oggetti all'Hub
hub.add(visit_1)
hub.add(exam_1)


app= Flask(__name__)

@app.route('/bookings', methods=['POST'])
def create_booking():
    info = request.get_json()
    
    if not info or "booking_id" not in info or "type" not in info:
        return jsonify({"error": "Dati incompleti"}), 400

    booking_id = info["booking_id"]
    
    try:
        if info.get("type") == "exam":
            new_booking = DiagnosticExam(
                booking_id=booking_id,
                patient_name=info["patient_name"],
                doctor=info["doctor"],
                department=info["department"],
                date=info["date"],
                time=info["time"],
                status=info["status"],
                exam_type=info["exam_type"],
                requires_fasting=info["requires_fasting"]
            )
        elif info.get("type") == "visit": # Corretto "vist" -> "visit"
            new_booking = MedicalVisit( # Corretto == -> =
                booking_id=booking_id,
                patient_name=info["patient_name"],
                doctor=info["doctor"],
                department=info["department"],
                date=info["date"],
                time=info["time"],
                status=info["status"],
                visit_reason=info["visit_reason"],
                first_time=info["first_time"]
            )
        else:
            return jsonify({"error": "Tipo prenotazione non valido"}), 400
        
        if hub.add(new_booking):
            return jsonify(new_booking.info()), 201
        else:
            return jsonify({"error": "Prenotazione già presente"}), 400
    except KeyError as e:
        return jsonify({"error": f"Campo mancante nel JSON: {str(e)}"}), 400

@app.route('/bookings/<string:booking_id>', methods=['PUT'])
def update_booking(booking_id: str):
    info = request.get_json()
    if booking_id not in hub.bookings:
        return jsonify({"error": "Prenotazione non esistente"}), 404
    
    # Costruiamo il nuovo oggetto (sovrascrittura totale)
    try:
        if info.get("type") == "visit":
            new_booking = MedicalVisit( # Corretto == -> =
                booking_id=booking_id,
                patient_name=info["patient_name"],
                doctor=info["doctor"],
                department=info["department"],
                date=info["date"],
                time=info["time"],
                status=info["status"],
                visit_reason=info["visit_reason"],
                first_time=info["first_time"]
            )
        elif info.get("type") == "exam":
            new_booking = DiagnosticExam( # Corretto: era MedicalVisit per errore
                booking_id=booking_id,
                patient_name=info["patient_name"],
                doctor=info["doctor"],
                department=info["department"],
                date=info["date"],
                time=info["time"],
                status=info["status"],
                exam_type=info["exam_type"],
                requires_fasting=info["requires_fasting"]
            )
        else:
            return jsonify({"error": "Tipo non valido"}), 400
            
        hub.update(booking_id, new_booking)
        return jsonify(new_booking.info()), 200
    except KeyError as e:
        return jsonify({"error": f"Dati incompleti: {str(e)}"}), 400

@app.route('/bookings/<string:booking_id>/status', methods=["PATCH"])
def update_partial_booking(booking_id: str):
    info = request.get_json()
    prenotazione = hub.get(booking_id)
    
    if prenotazione is None:
        return jsonify({"error": "Prenotazione non trovata"}), 404
    if "status" not in info:
        return jsonify({"error": "Campo 'status' mancante"}), 400
    
    hub.patch_status(booking_id, new_status=info["status"])
    return jsonify(prenotazione.info()), 200 # Rimosse le graffe extra

@app.route('/bookings/<string:booking_id>', methods=['DELETE'])
def delete_booking(booking_id: str):
    if hub.delete(booking_id):
        return jsonify({"message": "Prenotazione cancellata", "booking_id": booking_id}), 200
    else:
        return jsonify({"error": "Prenotazione non trovata"}), 404