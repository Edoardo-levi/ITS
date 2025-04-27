"""In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2), e corsi (parte 3).
 
### Classe Room:
La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area). L'area è calcolata come il doppio dei posti.
- Metodi:
    - get_id(): Restituisce l'ID dell'aula.
    - get_floor(): Restituisce il piano dell'aula.
    - get_seats(): Restituisce il numero di posti dell'aula.
    - get_area(): Restituisce l'area dell'aula.

### Classe Building:
La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address), un intervallo di piani (floors), e una lista di aule (rooms).
- Metodi:
    - get_floors(): Restituisce l'intervallo di piani dell'edificio.
    - get_rooms(): Restituisce la lista delle aule nell'edificio.
    - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
    - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.
    
### Classe Course:
La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
- Metodi:
    - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
    - get_groups(): Restituisce la lista dei gruppi nel corso.
    - add_group(group): Aggiunge un gruppo al corso."""


class Room:
    def __init__(self, id:str, floor:int, seats:int):
        self.setId(id)
        self.setFloor(floor)
        self.setSeats(seats)
        self.setArea()
    
    def setId(self, id:str) -> None:
        self.id= id
    def setFloor(self, floor:int) -> None:
        self.floor=floor
    def setSeats(self, seats:int)-> None:
        self.seats=seats
    def setArea(self,) -> None:
        self.area= self.seats*2
    
    def get_id(self)->str:
        return self.id
    def get_floor(self)->int:
        return self.floor
    def get_seats(self) -> int:
        return self.seats
    def get_area(self)-> int:
        return self.area
        
class Building:
    def __init__(self, name: str, address: str, floors: range, rooms:list= None):
        if rooms is None:
            rooms:list=[]
        
        self.setName(name)
        self.setAddress(address)
        self.setFloors(floors)
        self.setRooms(rooms)

    def setName(self, name:str) ->None:
        self.name= name
    def setAddress(self, address:str) ->None:
        self.address= address
    def setFloors(self, floors:range) -> None:
        self.floors = floors
    def setRooms (self, rooms:list) -> None:
        self.rooms= rooms
    def get_floors(self) ->range:
        return self.floors
    def get_rooms(self)->list:
        return self.rooms
    def add_room(self, room):
        if room.get_floor() <= self.floors[1] and room.get_floor() >= self.floors[0]:
                if room not in self.rooms:
                    self.rooms.append(room)
    
    def area(self):
        x = 0
        for i in self.rooms:
            x+=i.get_area()
        return x



