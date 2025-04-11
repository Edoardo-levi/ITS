"""crea un elenco contenente una serie di brevi messaggi di testo.
Passa l'elenco a una funzione chiamata show_messages(), che stampa ogni messaggio di testo."""


testo1=input("inserisci un testo breve:\n")

testo2=input("inserisci un testo breve:\n")

testo3=input("inserisci un testo breve:\n")

lista=[testo1,testo2,testo3]

def show_message():
    cont=0
    for x in lista:
        if cont < len(lista):
            print(lista[0 + cont])
            cont+=1
        else:
            break

show_message()