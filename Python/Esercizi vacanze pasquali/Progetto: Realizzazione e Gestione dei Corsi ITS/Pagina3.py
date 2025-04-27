"""### Classe Course:
La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
- Metodi:
    - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
    - get_groups(): Restituisce la lista dei gruppi nel corso.
    - add_group(group): Aggiunge un gruppo al corso."""


from Pagina2 import Group

class Course:
    def __init__(self, name:str):
        self.setName(name)
        self.groups=[]
    
    def setName(self, name:str) ->None:
        self.name=name
    
    def setGroups(self,groups:list[str]) ->None:
        self.groups=groups
    
    def get_groups(self) ->list:
        return self.groups

    def add_group(self, group:Group)->None:
        self.groups.append(group)
    
    def register(self, student):
         for group in self.groups:                               # con questa linea di coddice provo ad aggiungere lo studente al primo gruppo con spazio disponibile.
            if len(group.get_students())< group.get_limit():
                group.add_student(student)
                return
