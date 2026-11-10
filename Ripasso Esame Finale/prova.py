nome = "Marco"

def saluta ():
    global saluta
    saluta="Edo"
    print("Ciao", nome)

saluta ()
print("fuori", saluta)