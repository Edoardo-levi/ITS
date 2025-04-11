'''Scrivi un programma Python che conti alla rovescia da 10 a 1 e poi stampi "Time's
up!"'''
import time 

tempo=10
while tempo>0:
     print(tempo)
     tempo-=1
     time.sleep(1)
print ("il tempo è finito")
