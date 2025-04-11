'''CLASSI E ISTANZE
Le classi sono uno strumento che ci permette di immagazzinare variabili e funzini in maniera efficiente e riutilizzabile.
Supponiamo di dover scrivere un applicazione che gestisca l'iscrizione ai corsi di alcuni studenti, ogni studente ha attributi come:
nome, cognome e corso associato (che chiameremo "attributi" della classe), e alcune funzioni che chiameremo 'metodi'.
Ogni studente potrà essere associato ad un modello generico chiamato 'classe'.
Una classe può essere metaforizzata come una fabbrica di oggetti e ogni oggetto creato a partire da una classe si dice 'istanza'.
Quindi, nel nostro esempio, avremo una classe Studente e ogni studente creato darà un istanza di questo modello''' 


class Studente:  #parole chiave per creare una classe
    '''per aggiungere le caratteristiche nome, cognome e corso, ci serve una funzione speciale (metodo) chiamata 'init' : metodo inizializzatore -> costruisce gli oggetti
        e mettiamo all'interno degli argomenti la parola "self"'''
    def __init__(self, nome, cognome, corso):    # self rappresenta l'oggetto a cui dovranno essere associate le proprietà, è la referenza e ciascun oggetto della classe
        self.nome = nome
        self.cognome = cognome
        self.corso = corso
    
    def schedapersonale(self):
        print(f"Scheda studente:\nNome: {self.nome}\nCognome: {self.cognome}\nCorso: {self.corso}\n")
    
    
    #METODI SPECIALI

    def __str__(self):
        return f"{self.nome}, {self.cognome}"


p=Studente("Mario", "Rossi", "Cyber")
print(p)    # output = stringa ritornata dal metodo speciale __str__, non serve specificare altri metodi

studente1=Studente("Paolo", "Brosio", "Cybersecurity")
studente2=Studente("Luisa", "Pistolesi", "Scienze politiche") # andiamo a dichiare due entità 'studente' in cui passiamo i parametri che abbiamo prestabilito

studente1.schedapersonale()
studente2.schedapersonale()  # invocando l'apposito metodo della classe riesco a visualizzare i dati

# in alternativa avremmo potuto scrivere:

Studente.schedapersonale(studente1)


@classmethod   # --> ho definito un metodo di classe, che mi permette di accedere agli attributi di classe cls
def aggiungi_persona(cls, nome_persona:str):
    cls.nome_persona= nome_persona



'''====================================================='''
