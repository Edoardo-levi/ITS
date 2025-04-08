'''1. Write a class called Student with the attributes name (str) and
studyProgram (str)

2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.

3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!

4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too. '''

class Student:
    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age=age
        self.gender=gender
    
    def printInfo(self):
        print(F"{self.name}: {self.studyProgram}, anni: {self.age}, gender: {self.gender}")
    
rac = Student("Rachele", "ITS Cybersecurity", 5, "Mamma Pig")
edo = Student("Edoardo", "ITS Cybersecurity", 21, "Gender Fluidissimo")
andr = Student("Andrea", "ITS Cybersecurity", 30, "Spazzolino")

rac.printInfo()
edo.printInfo()
andr.printInfo()