"""crea una classe chiamata Utente. Crea due attributi chiamati first_name e last_name, quindi crea diversi altri attributi che sono tipicamente memorizzati in un profilo utente. Crea un metodo chiamato describe_user() che stampa un riepilogo delle informazioni dell'utente. Crea un altro metodo chiamato greet_user() che stampa un saluto personalizzato all'utente. Crea diverse istanze che rappresentano utenti diversi e chiama entrambi i metodi per ogni utente."""



class Utente:
    def __init__(self, nome, cognome, eta, sesso):
        self.nome= nome
        self.cognome=cognome
        self.eta= eta
        self.sesso=sesso
    
    def descible_user(self):
        print(f"Nome: {self.nome}\nCognome: {self.cognome}\nEtà: {self.eta}\nSesso: {self.sesso}")

    def greet_user(self):
        print(f"Ciao {self.nome} {self.cognome}!")

print("\n\n")

nome1 = input("Inserisci il primo nome:\n")
cognome1 = input("Inserisci il primo cognome:\n")
eta1:int =int(input("Inserisci la prima eta':\n"))
sesso1=input("Inserisci il primo sesso (M/F):\n")

print("----------------------------------")

utente= Utente(nome1, cognome1, eta1, sesso1)

utente.descible_user()
utente.greet_user()