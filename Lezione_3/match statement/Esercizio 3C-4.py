"""Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, 
utilizzando un match statement, identifichi a quale categoria esso appartiene. 
L'animale deve essere classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate,
mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie."""

animale= str(input("inserisci un animale:\n"))

mammiferi=["cane", "gatto","cavallo", "elefante", "leone"]
rettili=["serpente", "lucertola","tartaruga","coccodrillo"]
uccelli=["aquila","pappagallo","gufo","falco"]
pesci=["squalo", "trota", "salmone", "carpa"]


match animale:
    case animale if animale in mammiferi:
        print(f"l'animale inserito : {animale}, apparteine alla categoria dei Mammiferi")
    
    case animale if animale in rettili:
        print(f"l'animale inserito : {animale}, apparteine alla categoria dei rettili")
    
    case animale if animale in uccelli:
        print(f"l'animale inserito : {animale}, apparteine alla categoria dei uccelli")
    
    case animale if animale in pesci:
        print(f"l'animale inserito : {animale}, apparteine alla categoria dei pesci")
    
    case _:
        print(f"il programma non è in grado di classificare l'animale inserito ({animale})")