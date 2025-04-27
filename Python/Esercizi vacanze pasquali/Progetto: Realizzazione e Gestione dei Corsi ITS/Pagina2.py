"""### Classi Person, Student e Lecturer:
La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
Le classi Student e Lecturer ereditano da Person.
Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
    - set_group(group): Associa un gruppo di studio allo studente
    
Classe Group:
La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), una lista di studenti (students) e una lista di docenti (lecturers).
- Metodi:
    - get_name(): Restituisce il nome del gruppo
    - get_limit(): Restituisce il limite di studenti nel gruppo
    - get_students(): Resituisce la lista di studenti nel gruppo
    - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti. Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
    - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
    - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto."""

class Person:
    def __init__(self, cf:str, name:str, surname:str, age:int):
        self.setCf(cf)
        self.setName(name)
        self.setSurname(surname)
        self.setAge(age)
    
    def setCf(self, cf:str) -> None:
        self.cf = cf
    def setName(self, name:str) -> None:
        self.name = name
    def setSurname(self, surname:str) -> None:
        self.surname = surname
    def setAge(self, age:int) -> None:
        self.age = age
    

    def getCf(self)->str:
        return self.cf
    def getName(self)->str:
        return self.name
    def getSurname(self)->str:
        return self.surname
    def getAge (self)->int:
        return self.age
    

class Student(Person):
    def __init__(self, cf, name, surname, age, group:str = None):
        super().__init__(cf, name, surname, age)
        self.set_group(group)
    
    def set_group(self, group:str) -> None:
        self.group = group

    def getGroup(self) -> str:
        return self. group
    
class Lecturer (Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)

class Group :
    def __init__(self, name:str, limit:int):
        self.name=name
        self.limit= limit
        self.students= []
        self.lecturers=[]
    
    def setNmae(self, name:str)->None:
        self.name=name
    
    def setLimit(self,limit:int) -> None:
        self.limit=limit
    def setStudents (self, students:list[str]) -> None:
        self.students=students
    
    def setLecturers (self, lecturers:list[str]) -> None:
        self.lecturers=lecturers
    

    def get_name(self) ->str:
        return self.name
    def get_limit(self) ->int:
        return self.limit
    def get_students(self)->list:
        return self.students
    def get_limit_lecturers(self)->int:
        return max(1,(len(self.students)//10)+1)  # grazie a questa linea di codice posso calcolare quanti professori possono essere assegnati ad un gruppo di studenti
    
    def add_student(self, student: Student):
        if len(self.students) < self.limit:
            self.students.append(student)
    
    def add_lecturer(self, lecturer:Lecturer) ->None:
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
