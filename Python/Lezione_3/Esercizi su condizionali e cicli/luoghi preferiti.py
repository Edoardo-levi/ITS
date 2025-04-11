'''crea un dizionario chiamato luoghi_preferiti.
Pensa a tre nomi da usare come chiavi nel dizionario e memorizza da uno a tre luoghi 
preferiti per ogni persona. Per rendere questo esercizio un po' più interessante, 
chiedi ad alcuni amici di nominare alcuni dei loro luoghi preferiti. 
Scorri il dizionario e stampa il nome di ogni persona e i suoi luoghi preferiti.'''

luoghi_preferiti= {"Edoardo": ["Piramide", "Palma de Mallorca"], 
                   "Mattia": ["Tenerife", "Amsterdam"],
                   "Gino": ["Thailandia", "Mikonos"]}

for persona, luoghi in luoghi_preferiti.items():
    print(f"{persona} ama andare nei seguenti luoghi:")
    for luogo in luoghi:
        print(f"- {luogo}")
    print("---------")