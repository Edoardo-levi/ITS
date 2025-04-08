'''hai appena trovato un tavolo da pranzo più grande, 
quindi ora hai più spazio a disposizione. Pensa ad altri tre ospiti da invitare a cena.
• Inizia con il tuo programma dall'esercizio 3-4 o 3-5. 
Aggiungi una chiamata print() alla fine del tuo programma, 
informando le persone che hai trovato un tavolo più grande.
• Usa insert() per aggiungere un nuovo ospite all'inizio della tua lista.
• Usa insert() per aggiungere un nuovo ospite al centro della tua lista.
• Usa append() per aggiungere un nuovo ospite alla fine della tua lista.
• Stampa un nuovo set di messaggi di invito, uno per ogni persona nella tua lista.'''

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
