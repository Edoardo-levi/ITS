'''In python un'eccezione è una condizione che fa in modo che il programa termini
una volta che succede una determinata cosa.
Per creare un 'eccezione dobbimo utilizzare la parola "Raise". 
'''

number=10
if number>5:
    raise Exception("Numero troppo grande")

'''possiamo gestire le eccezioni con "try" e "except".
Dentro try mettiamo la parte di codice che vogliamo verificare,
dentro except mettiamo una parte di codice che viene eseguito
se si verifica un'eccezione.
Infine con "finally" inseirmao porzione di codice che viene eseguita a prescindere'''


'''asserzioni: porzioni di codice che, ad un certo punto del codice,
verifica che tutto stia procedendo nel verso giusto.
Servono per fare debugging del codice durante l'esecuzione del codice'''

#sintassi:

x=5
assert x>0, "x must be positive" #messaggio opzionale

'''non è previsto l'uso per verificare l'input dell'utente.'''