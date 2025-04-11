i=1
somma=0
while i<=10:
    somma+=i
    i+=1
print(f"Sum of integers from 1 to 10 is {somma}")


i=20
somma=0
while i<=37:
    somma+=i
    i+=1
print(f"Sum of integers from 20 to 37 is {somma}")


i=35
somma=0
while i<=49:
    somma+=i
    i+=1
print(f"Sum of integers from 35 to 49 is {somma}")


'''svolgendo questi esercizi ci accorgiamo che risultano essere molto ripetitivi e, 
sebbene operino su numeri differenti, fanno la stessa identica cosa.
Una funzione in python serve a questo: a semplificare la scrittura di un codice in modo da
scrivere le ocse in maniera meno ripetitiva'''


# sintassi di una funzione:
# ----> def functionName(list of parameters):
#           instruction

'''rifacendo l'esercizio con una funziona posso scrivere:'''

def somma(a:int, b:int):
    result:int = 0
    for i in range(a,b+1):
        result+=i
        
    return result
    
'''dopo aver definito la funzione, la posso richiamare dentro al mio codice'''

print(f"Sum from 1 to 10 is {somma(1, 10)}")
print(f"Sum from 20 to 37 is {somma(20, 37)}")
print(f"Sum from 14 to 370 is {somma(14, 370)}")

'''una funzione, quindi, ci permette di scrivere codice in modo più corto, più flessibile e riusabile'''

def operations(a: int, b: int) -> tuple[int, int]:   # specifico che il risultato ritornato dev essere di tipo tupla[int, int]
    sum_result:int = a+b
    diff_result:int = a-b
    
    return sum_result, diff_result     # ---> si può fare in modo che una funzione ritorni due valori dentro ad una tupla


'''una funzione può non prendere nulla come argomenti (es: funzioni che stampano qualcosa o che devono ritornare un valore prestabilito)
e una funzione può restituire sia una lista che un dizionario'''
