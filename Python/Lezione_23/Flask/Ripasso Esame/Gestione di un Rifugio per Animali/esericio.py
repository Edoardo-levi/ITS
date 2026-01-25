from abc import ABC, abstractmethod
from flask import *

class Animal(ABC):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float):
        self.id = animal_id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg

    @abstractmethod
    def species(self) -> str:
        """Restituisce la specie dell'animale."""
        pass

    @abstractmethod
    def daily_food_grams(self) -> float:
        """Calcola la quantità di cibo giornaliera."""
        pass

    def info(self) -> dict:
        """Restituisce le informazioni base comuni a tutti gli animali."""
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species(),
            "age_years": self.age_years,
            "weight_kg": self.weight_kg,
            "bmi_like": self.bmi_like()
        }

    def bmi_like(self) -> float:
        """Calcola un indice di forma fisica basato su peso ed età."""
        # Formula: peso / (età + 1) per evitare divisioni per zero
        return round(self.weight_kg / (self.age_years + 1), 2)


class Dog(Animal):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float, 
                 breed: str, is_trained: bool):
        super().__init__(animal_id, name, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained

    def species(self) -> str:
        return "dog"

    def daily_food_grams(self) -> float:
        # Formula: 200g base + 50g per ogni anno di età
        return float(200 + (self.age_years * 50))

    def info(self) -> dict:
        # Estende il dizionario della superclasse
        data = super().info()
        data.update({
            "breed": self.breed,
            "is_trained": self.is_trained
        })
        return data


class Cat(Animal):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float, 
                 indoor_only: bool, favorite_toy: str):
        super().__init__(animal_id, name, age_years, weight_kg)
        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy

    def species(self) -> str:
        return "cat"

    def daily_food_grams(self) -> float:
        # Formula: 100g base + 30g per ogni anno di età
        return float(100 + (self.age_years * 30))

    def info(self) -> dict:
        data = super().info()
        data.update({
            "indoor_only": self.indoor_only,
            "favorite_toy": self.favorite_toy
        })
        return data


class Shelter:
    def __init__(self):
        # Dizionario degli animali {id: oggetto_animale}
        self.animals = {}
        # Dizionario delle adozioni {id: nome_adottante}
        self.adoptions = {}

    def add(self, animal: Animal) -> bool:
        """Aggiunge un animale. Se l'ID esiste già, l'operazione viene ignorata."""
        if animal.id in self.animals:
            return False
        self.animals[animal.id] = animal
        return True

    def get(self, animal_id: str) -> Animal:
        """Restituisce l'oggetto Animal o None."""
        return self.animals.get(animal_id)

    def list_all(self) -> list[dict]:
        """Restituisce una lista di dizionari con le info di tutti gli animali."""
        return [animal.info() for animal in self.animals.values()]

    def is_adopted(self, animal_id: str) -> bool:
        """Controlla se l'animale è presente nel registro adozioni."""
        return animal_id in self.adoptions

    def set_adopted(self, animal_id: str, adopter_name: str) -> bool:
        """Registra un'adozione se l'animale esiste e non è già stato adottato."""
        if animal_id in self.animals and animal_id not in self.adoptions:
            self.adoptions[animal_id] = adopter_name
            return True
        return False
    # Inizializzazione del rifugio (Shelter)
shelter = Shelter()

# 1. Creazione di un oggetto Dog
dog_1 = Dog(
    animal_id="d1",
    name="Rex",
    age_years=2,
    weight_kg=18.5,
    breed="Border Collie",
    is_trained=True
)

# 2. Creazione di un oggetto Cat
cat_1 = Cat(
    animal_id="c1",
    name="Micia",
    age_years=3,
    weight_kg=4.2,
    indoor_only=True,
    favorite_toy="Pallina di lana"
)

# Aggiunta degli animali al rifugio
shelter.add(dog_1)
shelter.add(cat_1)


app= flash (__name__)

@app.route('/',methods=['GET'])
def welcome ():
    links={
        "animali":url_for("animal"),
        "animale":url_for("get_animal",animal_id=""),
        "cibo_animale":url_for("get_food",animal_id=""),
        "adozione":url_for("adoption_animals")
    }
    return jsonify({"message":"benveuto nel sito","link":links})

@app.route('/animals',methods=['GET'])
def animal():
    return jsonify({shelter.list_all()}),200

@app.route('/animals/<strinf:animal_id>',methods=["GET"])
def get_animal(animal_id:str):
    animale=shelter.get(animal_id)
    if not animale:
        return jsonify ({"error","animale non trovato"}),404
    else:
        return jsonify({animale.info()}),200

@app.route('/animals/<string:animal_id>/food',methods=['GET'])
def get_food(animal_id:str):
    animale =shelter.get(animal_id)
    if not animale:
        return jsonify ({"error":"l'animale non esiste"}),404
    else:
        cibo_animale=animale.daily_food_grams()
        grams_foot={"grammi_cibo":cibo_animale}
        return jsonify(grams_foot),200

@app.route('/animals/<string:animal_id>/adoption',methods=['GET'])
def adoption_animals(animal_id:str):
    animale=shelter.get(animal_id)
    if not animale:
        return jsonify ({"errore":"l'animale non esiste"}),404
    else:
        if shelter.is_adopted(animal_id):
            return jsonify ({"message":"animale adottato", "animale":animale.info()}),200
        else:
            return jsonify ({"message":"animale non adottato","animale":animale.info()}),200

@app.route('/animals/add',methods=['POST'])
def add_animale(animal_id:str):
    info=request.get_json()
    new_animale=None
    if animal_id not in shelter.animals:
        if info.get("type") == "dog":
            new_animale = Dog(
                animal_id=animal_id,
                name=info["name"],
                age_years=info["age_years"],
                weight_kg=info["weight_kg"],
                breed=info["breed"],
                is_trained=info["is_trained"]
            )
        elif info.get("type")== "cat":
            new_animale = Cat(
                animal_id=animal_id,
                name=info["name"],
                age_years=info["age_years"],
                weight_kg=info["weight_kg"],
                indoor_only=info["indoor_only"],
                favorite_toy=info["favorite_toy"]
            )
        else:
            return jsonify ({"error":"animale non consentito"}),404
    if shelter.add(new_animale):
        return jsonify ({"message":"animale creato correttamente"}),201
    else:
        return jsonify({"error":"animale non supportato"}),404
    

@app.route('/animals/<string:animal_id>/adopt',methods=['POST'])
def animal_adopted(animal_id:str):
    info=request.get_json()
    animale=shelter.get(animal_id)
    adopter_name=info.get("adopter_name")
    if not adopter_name:
        return jsonify({"message":"adopter_name non esistente"}),400
    if not animale:
        return jsonify({"message":"l'animale non esiste"}),404
    adottato=shelter.set_adopted(animal_id,adopter_name)
    if not adottato:
        return jsonify({"message":"l'animale non è stato adottato"}), 400
    return jsonify({"message":"adottato"}),201
        