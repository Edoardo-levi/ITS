"""Abbiamo un menù in un ristorante.
I piatti disponibili sono: pasta, pizza, insalata, vino, acqua
10.50, 9.00, 6.50, 4.00, 2.30
1. 2. 3. Salva queste informazioni in un dizionario chiamato menù.
Dal menù, accedi ai prezzi di pasta e vino. Salvali in variabili separate.
Stampa i prezzi di pasta e vino."""

menu:dict= {"pasta":10.50, \
            "pizza":9.00,\
            "insalata":6.50,\
            "vino":4.00,\
            "acqua":2.30}

prezo_pasta= menu["pasta"]
prezzo_vino= menu["vino"]

print(f"Il prezzo della pasta e' €{prezo_pasta:.2f}\nIl prezzo del vino e' €{prezzo_vino:.2f}")


menu["torta"]= 3.50

menu.pop("insalata")

menu["pasta"]=8.00

