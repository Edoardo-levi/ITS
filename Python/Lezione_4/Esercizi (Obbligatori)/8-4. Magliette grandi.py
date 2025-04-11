'''modifica la funzione make_shirt() in modo che le magliette siano grandi di default con un messaggio che recita
I love Python. Crea una maglietta grande e una maglietta 
media con il messaggio di default e una maglietta di qualsiasi taglia con un messaggio diverso.'''


def make_shirt(taglia:str, testo:str):
    print(f"la taglia selezionata per la maglietta e': {taglia}\n\
e il testo da stampare e': {testo} \n")
    
misura="L"
frase=("i love Python")
misura=make_shirt(misura, frase)
misura="M"
misura=make_shirt(misura, frase)
size=input("inserisci una taglia diversa dalle altre:\n")
text=input("inserisci un testo diverso dagli altri:\n")
misura=make_shirt(size, text)