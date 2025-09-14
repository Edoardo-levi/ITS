"""aggiungi un attributo chiamato login_attempts alla tua classe utente dall'esercizio 9-3. Scrivi un metodo chiamato increment_login_attempts() che incrementa il valore di login_attempts di 1. Scrivi un altro metodo chiamato reset_login_attempts() che ripristina il valore di login_attempts a 0. Crea un'istanza della classe User e chiama increment_login_attempts() più volte. Stampa il valore di login_attempts per assicurarti che sia stato incrementato correttamente, quindi chiama reset_login_attempts(). Stampa di nuovo login_attempts per assicurarti che sia stato ripristinato a 0."""
class Utente:
    def __init__(self, nome, cognome, eta, sesso, login_attempts=0):
        self.nome= nome
        self.cognome=cognome
        self.eta= eta
        self.sesso=sesso
        self.login_attempts=login_attempts
    
    def descible_user(self):
        print(f"Nome: {self.nome}\nCognome: {self.cognome}\nEtà: {self.eta}\nSesso: {self.sesso}")

    def greet_user(self):
        print(f"Ciao {self.nome} {self.cognome}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts=0
    

print("\n\n")

nome1 = input("Inserisci il primo nome:\n")
cognome1 = input("Inserisci il primo cognome:\n")
eta1:int =int(input("Inserisci la prima eta':\n"))
sesso1=input("Inserisci il primo sesso (M/F):\n")


print("----------------------------------")

utente= Utente(nome1, cognome1, eta1, sesso1)
utente.increment_login_attempts()
utente.increment_login_attempts()
utente.increment_login_attempts()

utente.descible_user()
utente.greet_user()

print(f"Tentativo di accesso: {utente.login_attempts}")


utente.reset_login_attempts()

print(f"I tentativi di accesso sono stati ripristinati a: {utente.login_attempts}")