'''costruisci un profilo di te stesso chiamando build_profile(), 
usando il tuo nome e cognome e altre tre coppie chiave-valore che ti descrivono. 
Tutti i valori devono essere passati alla funzione come parametri. La funzione deve quindi restituire una stringa come 
"Eric Crow, 45 anni, capelli castani, peso 67"'''

def build_profile(nome:str, cognome:str, colore_capelli:str, peso:int):
    profilo:dict = {"nome": nome, "cognome": cognome, "capelli": colore_capelli, "peso": peso}
    return profilo


name=input("inserisci il tuo nome:\n")
surname=input("inserisci il tuo cognome:\n")
hair=input("inserisci il colore dei tuoi capelli:\n")
kg=int(input("inserisci il tuo peso:\n"))
profilo = build_profile(name, surname, hair, kg)
for key, value in profilo.items():
    print(f"{key}: {value}")