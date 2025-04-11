"""Scrivi una funzione ricorsiva chiamata `recursiveSumInRange` che calcola la somma di tutti 
gli interi tra `a` e `b`, inclusi, dove `a` e `b` vengono passati come input alla funzione.
Assumi che il valore di `b` sia sempre maggiore del valore di `a`. Pertanto, se `a`
è maggiore di `b`, è necessario scambiare i valori per garantire che `a` sia il più piccolo dei due.
Poi, chiama la funzione `recursiveSumInRange` per `a = 5`, `b = 10` e per `a = 10`, `b = 5`."""


def recursiveSumInRange(a: int, b:int) ->int:
    sum:int=0
    if a > b:
        var= a      #variabile temporanea
        a=b
        b=var
    while b>=a:
        sum+=b
        b-=1
    return(sum)

print(recursiveSumInRange(5,10))
print(recursiveSumInRange(10,5))


#FUNZIONE RICORSIVA 

def recursiveSumInRange(a:int, b:int) -> int:
    if a>b:
        a,b=b,a
    
    if a==b:
        return a
    
    else:
        return int(b+recursiveSumInRange(a,b-1))


print(recursiveSumInRange(5,10))
print(recursiveSumInRange(10,5))
