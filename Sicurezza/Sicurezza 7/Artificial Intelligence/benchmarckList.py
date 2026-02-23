import random
from datetime import datetime

# Warning: This uses ~3.6GB of RAM. 
# If your VM freezes, reduce 100,000,000 to 10,000,000.
lista = []
for i in range(100000000):
    lista.append(random.randint(0,10))

test = 1000000 # Increased test count to get a measurable average

# Benchmark Index 0
start = datetime.now()
tot = 0
for i in range(test):
    tot += lista[0]
end = datetime.now() # Fix: Added .now()
print("Tempo medio per posto 0:", (end - start).total_seconds() / test, "secondi")

# Benchmark Index 50,000,000
start = datetime.now()
tot = 0
for i in range(test):
    tot += lista[50000000]
end = datetime.now() # Fix: Added .now()
print("Tempo medio per posto 50M:", (end - start).total_seconds() / test, "secondi")