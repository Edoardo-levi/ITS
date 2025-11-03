"""Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1."""

def transform(x: int) -> int:
    if x%2== 0:
        divisione=x//2
        return divisione
    else:
        return (x*3)-1


proma= transform(x=8)
print(proma)