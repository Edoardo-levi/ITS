"""In questo esercizio, dovrai scrivere il codice per un sistema che gestisce le attrazioni di un parco divertimenti e che espone alcune informazioni tramite un’applicazione Flask. L’obiettivo è applicare i principi di ereditarietà e classi astratte, e sperimentare le richieste HTTP GET di Flask.

Specifiche del Problema

Classe Ride

La classe Ride rappresenta un’attrazione generica del parco. È una classe astratta e non può essere istanziata direttamente.
Ogni attrazione ha:

un identificativo (id) di tipo stringa;
un nome (name) di tipo stringa;
un’altezza minima richiesta (min_height_cm) di tipo intero.
Metodi:

category(): metodo astratto. Deve essere implementato nelle sottoclassi per restituire la categoria dell’attrazione (es. "roller_coaster", "family").
base_wait(): metodo astratto. Deve essere implementato nelle sottoclassi e deve restituire l’attesa base in minuti.
info(): metodo concreto che restituisce un dizionario con le informazioni principali dell’attrazione (id, nome, altezza minima, categoria e attributi specifici).
wait_time(crowd_factor: float = 1.0): metodo concreto che restituisce l’attesa stimata in minuti. L’attesa è calcolata come base_wait() * crowd_factor, arrotondata all’intero positivo.
Classe RollerCoaster

La classe RollerCoaster rappresenta una montagna russa e eredita da Ride.

Attributi aggiuntivi:

inversions: numero di inversioni presenti nel tracciato (ad esempio 3 o 5).
Metodi:

category(): restituisce la stringa "roller_coaster".
base_wait(): restituisce l’attesa base in minuti (ad esempio 40).
info(): estende il metodo della superclasse includendo anche il numero di inversioni.
Classe Carousel

La classe Carousel rappresenta una giostra con animali e eredita da Ride.

Attributi aggiuntivi:

animals: lista di animali presenti sulla giostra (ad esempio ["horse", "swan", "tiger"]).
Metodi:

category(): restituisce la stringa "family".
base_wait(): restituisce l’attesa base in minuti (ad esempio 10).
info(): estende il metodo della superclasse includendo la lista di animali.
Classe Park

La classe Park rappresenta il contenitore principale del sistema, che gestisce tutte le attrazioni presenti nel parco.

Attributi:

rides: dizionario che associa a ogni identificativo (id) l’oggetto Ride corrispondente.
Metodi:

add(ride): aggiunge un’attrazione al parco.
get(ride_id): restituisce l’attrazione corrispondente all’ID specificato oppure None se non esiste.
list_all(): restituisce una lista di tutte le attrazioni (puoi ordinare per categoria e nome, opzionale).
Nel codice principale dovrà essere creato un parco e dovranno essere create almeno due attrazioni, una di tipo RollerCoaster e una di tipo Carousel.

Applicazione Flask

Crea un’applicazione Flask che esponga alcune route GET per consultare i dati del parco. Le funzioni delle route devono restituire oggetti json. 

Route richieste

GET /

Restituisce un json con:

una breve descrizione del servizio (es. "Welcome to Park API"),
alcuni link testuali che indicano le altre route disponibili (es. "/rides", "/rides/rc1", "/rides/rc1/wait/4.0").
Devi generare i link dinamicamente con url_for() e poi inserirli nel json.
GET /rides

Restituisce un json di attrazioni presenti nel parco.
Ogni elemento del json può essere:

una stringa descrittiva (es. "rc1 - Vortex (roller_coaster) - min 140cm"), oppure
un dizionario con i campi principali dell’attrazione.
La scelta è libera, ma deve essere coerente in tutto il programma.

GET /rides/<ride_id>

Restituisce un json con un solo elemento che rappresenta i dettagli dell’attrazione con l’ID specificato.

GET /rides/<ride_id>/wait/<crowd>

Restituisce un json con le informazioni sull’attesa stimata per l’attrazione specificata.

Il parametro crowd indica un fattore di affollamento (valore di default 1.0).
L’output può essere, ad esempio, una json contenente una stringa "Attesa: 60 minuti" oppure un dizionario {"wait_min": 60}.
Cosa strutturare l'esercizio

Un file main.py contenente:
le classi Ride, RollerCoaster, Carousel, Park;
un parco popolato con almeno due giostre (una per tipo);
l’applicazione Flask con tutte le route richieste;
Il formato delle risposte deve essere coerente: tutte le route devono restituire oggetti json.
Esecuzione dell’applicazione

Il programma può essere eseguito in due modi:

da riga di comando:
flask --app main run --debug

oppure direttamente nel file Python:
app.run(debug=True, host="127.0.0.1", port=5000)
 """
from abc import ABC, abstractmethod
from flask import Flask, jsonify, url_for

# ==========================
# 1. Classi di Dominio (OOP)
# ==========================

class Ride(ABC):
    """
    Classe astratta che rappresenta un'attrazione generica.
    """
    def __init__(self, ride_id: str, name: str, min_height_cm: int):
        self.id = ride_id
        self.name = name
        self.min_height_cm = min_height_cm

    @abstractmethod
    def category(self) -> str:
        """Restituisce la categoria dell'attrazione."""
        pass

    @abstractmethod
    def base_wait(self) -> int:
        """Restituisce il tempo di attesa base in minuti."""
        pass

    def info(self) -> dict:
        """
        Restituisce un dizionario con le informazioni principali.
        Nota: Chiama il metodo astratto category() per ottenere il tipo.
        """
        return {
            "id": self.id,
            "name": self.name,
            "min_height_cm": self.min_height_cm,
            "category": self.category()
        }

    def wait_time(self, crowd_factor: float = 1.0) -> int:
        """
        Calcola il tempo di attesa stimato.
        Arrotonda il risultato all'intero più vicino.
        """
        estimate = self.base_wait() * crowd_factor
        return int(round(estimate))


class RollerCoaster(Ride):
    """
    Sottoclasse per le montagne russe.
    """
    def __init__(self, ride_id: str, name: str, min_height_cm: int, inversions: int):
        super().__init__(ride_id, name, min_height_cm)
        self.inversions = inversions

    def category(self) -> str:
        return "roller_coaster"

    def base_wait(self) -> int:
        return 40

    def info(self) -> dict:
        # Ottengo il dizionario base dalla superclasse e aggiungo il campo specifico
        data = super().info()
        data["inversions"] = self.inversions
        return data


class Carousel(Ride):
    """
    Sottoclasse per le giostre con animali.
    """
    def __init__(self, ride_id: str, name: str, min_height_cm: int, animals: list):
        super().__init__(ride_id, name, min_height_cm)
        self.animals = animals

    def category(self) -> str:
        return "family"

    def base_wait(self) -> int:
        return 10

    def info(self) -> dict:
        # Ottengo il dizionario base dalla superclasse e aggiungo il campo specifico
        data = super().info()
        data["animals"] = self.animals
        return data


class Park:
    """
    Classe contenitore (Manager) per gestire tutte le attrazioni.
    """
    def __init__(self):
        self.rides = {}  # Dizionario: id -> oggetto Ride

    def add(self, ride: Ride):
        """Aggiunge un'attrazione al parco."""
        self.rides[ride.id] = ride

    def get(self, ride_id: str):
        """Restituisce l'attrazione cercata o None."""
        return self.rides.get(ride_id)

    def list_all(self):
        """Restituisce una lista di tutte le attrazioni (oggetti)."""
        return list(self.rides.values())


# ==========================
# 2. Setup e Popolamento
# ==========================

app = Flask(__name__)
park = Park()

# Creazione delle attrazioni richieste
rc1 = RollerCoaster(
    ride_id="rc1", 
    name="Vortex", 
    min_height_cm=140, 
    inversions=5
)

c1 = Carousel(
    ride_id="c1", 
    name="Magic Horses", 
    min_height_cm=0, 
    animals=["horse", "unicorn", "lion"]
)

# Aggiunta al parco
park.add(rc1)
park.add(c1)


# ==========================
# 3. Route API (Flask)
# ==========================

# 1. GET / 
# Restituisce JSON con messaggio e link generati dinamicamente
@app.route('/', methods=['GET'])
def home():
    response_data = {
        "service": "Welcome to Park API",
        "links": {
            "all_rides": url_for('get_rides'),
            # Link di esempio generato con un ID esistente
            "example_ride_rc1": url_for('get_ride', ride_id='rc1'),
            # Link di esempio per l'attesa (nota come passo entrambi i parametri)
            "example_wait_rc1": url_for('get_wait', ride_id='rc1', crowd=1.5)
        }
    }
    return jsonify(response_data)


# 2. GET /rides
# Restituisce JSON lista di tutte le attrazioni
@app.route('/rides', methods=['GET'])
def get_rides():
    # Itero sugli oggetti del parco e chiamo .info() su ognuno
    # per ottenere una lista di dizionari
    rides_list = [ride.info() for ride in park.list_all()]
    return jsonify(rides_list)


# 3. GET /rides/<ride_id>
# Restituisce JSON dettaglio singola attrazione
@app.route('/rides/<string:ride_id>', methods=['GET'])
def get_ride(ride_id):
    # Cerco l'attrazione nel parco
    ride = park.get(ride_id)
    
    # Se esiste, restituisco il JSON delle info
    if ride:
        return jsonify(ride.info())
    
    # Se non esiste, restituisco un errore 404
    return jsonify({"error": "Ride not found"}), 404


# 4. GET /rides/<ride_id>/wait/<crowd>
# Restituisce JSON con tempo di attesa calcolato
# NOTA: crowd è definito come float nell'URL
@app.route('/rides/<string:ride_id>/wait/<float:crowd>', methods=['GET'])
def get_wait(ride_id, crowd):
    ride = park.get(ride_id)
    
    if not ride:
        return jsonify({"error": "Ride not found"}), 404
    
    # Calcolo usando il metodo della classe
    minutes = ride.wait_time(crowd)
    
    response = {
        "ride_id": ride.id,
        "ride_name": ride.name,
        "crowd_factor": crowd,
        "estimated_wait_minutes": minutes
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)