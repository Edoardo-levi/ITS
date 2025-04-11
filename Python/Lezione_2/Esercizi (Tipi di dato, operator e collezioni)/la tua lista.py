''' pensa al tuo mezzo di trasporto preferito, 
come una motocicletta o un'auto, e 
crea un elenco che memorizzi diversi esempi. 
Usa il tuo elenco per stampare una serie di affermazioni su questi elementi, 
come "Vorrei possedere una motocicletta Honda".'''

tipologia =["Auto", "Moto", "Treno", "Aereo"]
modello = ["Ford", "honda", "italo", "boing"]

for index in range(4): 
    print (f"vorrei possedere un/a {tipologia[index]} {modello[index]}")
