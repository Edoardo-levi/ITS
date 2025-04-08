"""Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta
all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 
classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, 
oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. 
Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_
type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat 
inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra"""

animale= str(input("inserisci un animale:\n"))
habitats=["terra", "aria", "acqua"]
habitat= str(input("inserisci un habitat:\n"))


mammiferi:list[str]=["cane", "gatto","cavallo", "elefante", "leone", "balena", "delfino"]
rettili=["serpente", "lucertola","tartaruga","coccodrillo"]
uccelli=["aquila","pappagallo","gufo","falco", "cigno", "anatra", "gallina", "tacchino" ]
pesci=["squalo", "trota", "salmone", "carpa"]


match animale:
    case animale if animale in mammiferi:
        animal_type="mammiferi"
    
    case animale if animale in rettili:
        animal_type="rettili"
    
    case animale if animale in uccelli:
        animal_type="uccelli"
    
    case animale if animale in pesci:
        animal_type="pesci"
    
    case _:
        print(f"il programma non è in grado di classificare l'animale inserito ({animale})")
        animal_type= "unknown"

'''info_animale={"specie":animale, "categoria":animal_type, "habitat": habitat}'''
info_animale:dict={
    "terra": ["cane","gatto", "cavallo", "elefante","leone", "serpente", "lucertola", "targura", "coccodrillo", "tacchino"],
    "acqua": ["balena", "delfino", "cigno", "anatra", "coccodrillo", "tartaruge", "squalo", "trota", "salmone", "carpa" ], 
    "aria": ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
    }


match animale:
    case animale if animale in mammiferi:
        print("mammifero")

        match habitat:
            case habitat if habitat in info_animale and animale in info_animale[habitat]:
                print(f"animale di {habitat}")
    case animale if animale in rettili:
        print("rettili")

        match habitat:
            case habitat if habitat in info_animale and animale in info_animale[habitat]:
                print(f"animale di {habitat}")
    
    case animale if animale in uccelli:
        print("uccelli")

        match habitat:
            case habitat if habitat in info_animale and animale in info_animale[habitat]:
                print(f"animale di {habitat}")
    
    case animale if animale in pesci:
        print("pesci")

        match habitat:
            case habitat if habitat in info_animale and animale in info_animale[habitat]:
                print(f"animale di {habitat}")
    case _:
        print(f"non conosco quest'habitat:{habitat}")