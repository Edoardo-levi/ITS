"""Sviluppare un algoritmo che chieda all’utente di inserire 7 temperature (una per ogni giorno della settimana). L'algoritmo deve:

calcolare la temperatura media,
controllare se tutte le temperature sono comprese tra 10 e 30:
Se sì, mostrare “Temperatura nella norma”.
verificare se almeno una temperatura è maggiore di 35 o minore di 5:
Se sì, mostrare “Allerta temperatura”.
Mostrare in output la media, il giorno della temperatura più alta e il giorno della temperatura più bassa espresso numericamente (es. 1 per lunedì, 2 per martedì, ecc.)"""
import math 

t_max = float('-inf')
day_max = 0
t_min = float('inf')
day_min = 0
cont_norma = 0
t_media = 0
for i in range (1,8):
    temp:float=(float(input(f"inserisci una temperatura per il giorno {i}: ")))
    t_media+=temp
    if temp > t_max:
        t_max = temp
        day_max = i
    
    if temp < t_min:
        t_min = temp
        day_min = i
        
    if temp >= 10 and temp <= 30:
        cont_norma +=1

    else:
        if temp < 5 or temp >35:
            print("Allerta Temperatura")
   
     
    i+=1

t_media/=7
print(f"La temperatura media e': {t_media:.2f}°C\n\
La temperatura massima e': {t_max}°C\n\
La temperatura minima e': {t_min}°C\n\
Il giorno con la temperatura masisma e': {day_max}\n\
Il giorno con la temperatura minima e': {day_min}")

if cont_norma==7:
    print("Temperatura nella norma")