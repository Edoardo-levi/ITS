'''
Lambda è una funzione che scriviamo quando vogliamo scrivere una funzione sempice con
compiti elementari e spesso viene usata com argomento di altre funzioni.
Sintassi:
lambda arguments: espression

Essendo lambda una funzione, questa è di tipo Callable --> occorrerà importare Callable:

from typing import Callable
Callable[[Argtype1, Argotype2, ...], ReturnType]
'''

from typing import Callable

multiply:Callable[[int, int], int] = lambda a, b: a*b
# questa scrittura prende in input due interi e respituisce l loro prodotto

square:Callable[[int], int] = lambda x:x**2
print(square(5))
# questa funzione prende in input un intero e ne restituisce il quadrato

valore:Callable[[int], str] = lambda x: "Positivo" if x>0 else "Zero o positivo"
# questa scrittura implemente l'utilizza di if e else dentro alla funzione lambda
print(valore(5))
print(valore(-5))


'''Come accennato, lambda può essere usato come argomento per altre funzioni'''

num:list[int]=(1, 2, 3, 4, 6, 9, 10)
listaPari:list[int]=list(filter(lambda x: x%2==0, num))
#applicare lambda alla lista num, significa applicare lambda ad ogni elemento della lista
print(listaPari)


name:list[str] = ["Marios", "Michele", "Pippo"]
ordina:list[str] = sorted(name, key=lambda name: len(name)) 
#sorted prevede come parametro la parola key=lambda. Come ultima cosa scriviamo il parametro che deve usare sorted pr ordinare: len = secondo lunghezza
print(ordina)  # viene stampata la lista con le stringa ordinate dalla stringa più corta alla più lunga


'''Quando usare lmbda? quando occorre creare una funzione semplie
o quand occorre passare determinati argomenti ad altre funzioni più complesse
E' preferibile non usare lambda quando viene meno la legibilità

Di solito Lambda e RegEz vengono utlizzati a braccetto
Esempio:
'''

import re

words:list[str] = {"abdc", "234", "fkmfm35454", "323464"}
# vogliamo fare in modo da considerare soltanto le stringhe numeriche
numerisolo:list[str] = list(filter(lambda x: re.fullmatch(r"\d+", x), words))
print(numerisolo)


testo:str="Prezzo: 100 dollari, Tassa: 20 dollari"
print(testo)
nuovo_testo:str = re.sub(r"\d+", lambda x: str(int(x.group())*2), testo)
# questa lambda, per ogni match (100, 20), converte il carattere in intero, lo moltiplica per 2 e lo riconverte in str
print(nuovo_testo)

