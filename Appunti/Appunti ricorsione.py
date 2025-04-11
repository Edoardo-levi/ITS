'''Write a Python function called countdown that takes a positive integer n as input and prints a countdown from n to zero.
If the input number is negative, display an error message.
To implement the function, you must exclusively use a while loop and the parameter n passed as input to the function.
Declaring any additional variables inside the function is not allowed.
Then, call the function with n = -5 and n = 5.'''

'''def countdown(num:int) -> None:
    if num>=0:
        while num:
            print(num)
            n-=1
    else:
        print("Errore")

countdown(5)
print("---------")
countdown(-5)'''


'''Per ora abbiamo usato funzioni che svolgono un determinato task,
per risolvere alcuni problemi spesso è neessario usare funzioni che richiamano loro stesse.
Funzioni di questo tipo si chiamano funzioni ricorsive'''


'''proviamo a rifare l'esercizio precedente in maneira ricorsiva'''

def countdown(n:int) -> None:
    if n<0:         # caso in cui n sia negativo
        print("Errore, numero negativo")
    elif n>0:        # condizione di ripetizione
        print(n)
        countdown(n-1)     # la funzione richiama se stessa con un valore decrementato di 1
    else:       # per fermare la ricorsione e per fare in modo che anche 0 venga stampato
        print(0)


countdown(5)
print("--------------")
countdown(-5)



'''Sequenza di Fibonacci'''


def fibonacci(n:int) -> int:
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return int(fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(50))
