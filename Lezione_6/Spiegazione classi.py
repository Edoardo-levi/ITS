'''CLASSI E ISTANZE
Le classi sono uno strumento che ci permette di immagazzinare variabili e funzini in maniera efficiente e riutilizzabile.
Supponiamo di dover scrivere un applicazione che gestisca l'iscrizione ai corsi di alcuni studenti, ogni studente ha attributi come:
nome, cognome e corso associato, e alcune funzioni che chiameremo 'metodi'.
Ogni studente potrà essere associato ad un modello generico chiamato 'classe'.
Una classe può essere metaforizzata come una fabbrica di oggetti e ogni oggetto creato a partire da una classe si dice 'istanza'.
Quindi, nel nostro esempio, avremo una classe Studente e ogni studente creato darà un istanza di questo modello''' 


class Studente:  #parole chiave per creare una classe
    '''per aggiungere le caratteristiche nome, cognome e corso, ci serve una funzione speciale (metodo) chiamata 'init' : metodo inizializzatore -> costruisce gli oggetti
        e mettiamo all'interno degli algomenti la parola "self"'''
    def _init_(self, nome, cognome, corso):    # self rappresenta l'oggetto a cui dovranno essere associate le proprietà, è la referenza e ciascun oggetto della classe
        self.nome = nome
        self.cognome = cognome
        self.corso = corso
    
    def schedapersonale(self):
        print(f"Scheda studente:\nNome: {self.nome}\nCognome: {self.cognome}\nCorso: {self.corso}\n")

studente1=Studente("Paolo", "Brosio", "Cybersecurity")
studente2=Studente("Luisa", "Pistolesi", "Scienze politiche") # andiamo a dichiare due entità 'studente' in cui passiamo i parametri che abbiamo prestabilito
print(studente1)
print(studente2) # stampando le due entità vediamo due codici di allocazione di memoria => sono varibili diverse

studente1.schedapersonale()
studente2.schedapersonale()  # invocando l'apposito metodo della classe riesco a visualizzare i dati

# in alternativa avremmo potuto scrivere:

Studente.schedapersonale(studente1) 