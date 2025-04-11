""" scrivi una serie di test condizionali. Stampa un'istruzione
che descrive ogni test e la tua previsione per i risultati di ogni test. Il tuo codice
dovrebbe assomigliare a questo:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Guarda attentamente i tuoi risultati e assicurati di aver capito perché ogni riga
viene valutata come True o False.
• Crea almeno 10 test. Fai in modo che almeno 5 test vengano valutati come True e altri
5 come False."""

car= str(input("inserisci una marca di una macchhina"))
print("Is car == 'subaru'? I predict True.")
a:bool=True
if car == "subaru":
    print(car == 'subaru')
elif car=="audi":
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')
    