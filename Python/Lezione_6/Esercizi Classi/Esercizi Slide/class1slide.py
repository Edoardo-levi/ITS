'''1. Create an if-statement that prints
the name of the oldest of the two
Persons

2. Create three other Persons. Make
a list called people with all 5
Persons.

3. Make a loop that finds and prints
the youngest person’s name'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
rache=Person("Rachele", 57)
mattia=Person("Mattia Ferrandino", 28)
edo=Person("Edo Levi", 20)
ricc=Person("Riccardo", 21)

people=[alice, bob, rache, mattia, edo, ricc]

giovane=120
for i in range(len(people)):
    if giovane>=people[i].age:
        giovane=people[i].age
print(f"La persona più giovane ha {giovane} anni")