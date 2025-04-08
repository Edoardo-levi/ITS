''' lavorando con uno dei programmi degli Esercizi 3, usa len() 
per stampare un messaggio che indica il numero di persone che stai invitando a cena.'''






lista = ["Andrea", "Francesca", "Giorgia"]

for index in range(3):
    print(f"Caro/a {lista[index]}, sei invitato alla mia festa. \n\
TI ASPETTO")
print(f"\n{lista[2]} putroppo non riesce a venire.")
lista.pop(2)
print("\nil nome invitato sara': Sara\n")
lista.append("Sara")
for index in range(3):
    print(f"Caro/a {lista[index]}, sei invitato alla mia festa. \n\
TI ASPETTO")

print("\nCARI AMICI HO TROVATO UN TAVOLO PIU' GRANDE. INVITO ALTRE PERSONE\n")

lista.insert(0, "Max")
lista.insert(3, "Edoardo")
lista.append("Rebecca")

for index in range(6):
    print(f"Caro/a {lista[index]}, sei invitato alla mia festa. \n\
TI ASPETTO")

lunghezza=len(lista)
print (f"\nla lunghezza della lista e': \n{lunghezza}")