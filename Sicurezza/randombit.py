import sys
import random

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file name>")

# 1) devo leggere tutti i file
data = None
with open(sys.argv[1], "rb") as f:
    data = f.read()

# 2) prendo un byte casuale del file 
pos = random.randint(0,len(data)-1)

# 3) prendo un bit casuale del byte 
bit = random.randint (0,7)

# ora devo cambiare il valore del bit <bit> di data[pos]
# in sostanza devo costruire un byte di tutti 0 e un solo 1 nel posto giusto
byte = data[pos]
byte = byte ^ (1<<bit) # ho rovesciato il bit bit-esimo del byte

data = data[:pos] + bytes([byte]) + data[pos+1:]

with open(sys.argv[1], "wb") as f:
    f.write(data)

print(f"Modificato il bit {bit} al posto {pos} nel file {sys.argv[1]}")
