# i decorator sono funzioni che prendono in input altre funzioni

def cronometro(fun):    # prende in ingresso una funzione 
    def wrapper(*arg):       # una funzione dentro una funzione si chiama inner function()
        import time 
        start=time.time() # memorizzio il valore corrente nel quale è chiamata la funzione. Se chiamassi la funzione alle 15:09, start avrebbe come valroe 15:09
        fun(*arg)
        print(time.time()-start)
    return wrapper 


def prova():
    print("Ciao")


print(cronometro)    # quando ho un decorator, la funzione che va in stampa, deve essre seza parentesi

prova=cronometro(prova) #Equivale a scrivere  @cronometro

prova()