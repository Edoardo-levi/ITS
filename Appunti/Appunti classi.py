'''CLASSI: 

Una classe rappresenta un modo per definire un nuovo tipo di oggetti, caratterizzati d attributi e metodi
 e si di dichiara in questo modo: '''

class MyList:
    def __init__(self):   # __init__ è un "costruttore"
        self.arg = "arg"

    def aggiungi(self, val: int):
        self.lst.append(val)
        return val in self.lst


'''fino ad ora, gli oggetti che andavmo ad utilizzare non erano altro che un puntatori a un indirizzo di memoria,
'''

mylist=MyList()
mylist.aggiungi(10)
print(mylist)