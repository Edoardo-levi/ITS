'''hai appena saputo che uno dei tuoi ospiti non può venire a cena, 
 quindi devi inviare un nuovo set di inviti. 
 Dovrai pensare a qualcun altro da invitare.
• Inizia con il tuo programma dall'esercizio 3-4. 
Aggiungi una chiamata print() alla fine del tuo programma, 
indicando il nome dell'ospite che non può venire.
• Modifica la tua lista, sostituendo il nome dell'ospite che non può venire
con il nome della nuova persona che stai invitando.
• Stampa un secondo set di messaggi di invito, uno per ogni persona che
è ancora nella tua lista.'''

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
