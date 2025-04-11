""": i numeri ordinali indicano la loro posizione in un elenco, come 1° o 2°.
La maggior parte dei numeri ordinali termina in th, eccetto 1, 2 e 3.
• Memorizza i numeri da 1 a 9 in un elenco.
• Esegui un ciclo nell'elenco.
• Utilizza una catena if-elif-else all'interno del ciclo per stampare l
a corretta terminazione ordinale per ciascun numero. Il tuo output dovrebbe essere 
"1° 2° 3° 4° 5° 6° 7° 8° 9°" e ogni risultato dovrebbe essere su una riga separata."""



lista= [x for x in range(1,11)]

print (lista)

for num in lista:
    if num==1:
        print(f"{num}°")
    elif num==2:
         print(f"{num}°")
    elif num==3:
         print(f"{num}°")
    else:
         print(f"{num}th")