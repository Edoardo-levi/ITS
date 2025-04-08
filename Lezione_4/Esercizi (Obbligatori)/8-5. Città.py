'''scrivi una funzione chiamata describe_city() che accetti il nome di una città e il suo paese. 
La funzione dovrebbe stampare una frase semplice, come Reykjavik è in Islanda. 
Assegna un valore predefinito al parametro per il paese. 
Chiama la tua funzione per tre città diverse, almeno una delle quali non si trovi nel paese predefinito.'''

cont = 0
city_dict = {} 

def describe_city(citta: str, paese: str):
    
   
    city_dict[citta] = paese

luogho = "Islanda"
name = input("Inserisci il nome di una città:\n")
describe_city(name, luogho)

while cont != 3:
    name = input("Inserisci il nome di una città diversa dalle altre:\n")
    luogho = input("Inserisci un Paese:\n")
    describe_city(name, luogho)
    cont += 1


print("\nLista dei paesi inseriti:\n")
for citta, paese in city_dict.items():
    print(f"{citta} sta in {paese}")
