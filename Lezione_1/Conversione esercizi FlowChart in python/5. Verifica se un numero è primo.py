"""Progetta un algoritmo per determinare se un numero intero positivo inserito dall'utente è un numero primo."""


n=int(input("inserisci un numero:\n"))

if n<2:
   print("il numero non e' primo ")
else:
   div =2
   primo=True
   while div <n:
      if n%div ==0:
         primo=False
         break
      div +=1
   if primo:
      print("il numero e' primo")
   else:
      print("il numero non e' primo")

# altro modo di farlo 

import math

n=int(input("inserisci un numero:\n"))

if n<2:
   print("il numero non e' primo")
else:
   div =2
   primo=True
   limite=math.sqrt(n)
   while div<=limite:
      if n%div==0:
         primo=False
         break
      div +=1
   if primo:
      print("il numero e' primo")
   else:
      print("il numero non e' primo")