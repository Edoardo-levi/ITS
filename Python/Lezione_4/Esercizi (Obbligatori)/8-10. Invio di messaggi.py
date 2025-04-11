'''inizia con una copia del tuo programma dall'esercizio 8-9. 
Scrivi una funzione chiamata send_messages() che stampa ogni messaggio di testo e sposta ogni messaggio 
in una nuova lista chiamata sent_messages mentre viene stampata. Dopo aver chiamato la funzione, 
stampa entrambe le tue liste per assicurarti che i messaggi siano stati spostati correttamente.'''


testo1=input("inserisci un testo breve:\n")

testo2=input("inserisci un testo breve:\n")

testo3=input("inserisci un testo breve:\n")

list1 = [testo1,testo2,testo3]
print("\n\n")
def show_messages():
    for i in list1:
        print(i)
show_messages()


def sent_messages(testo1, testo2, testo3, testo4):
    print(sent_messages)

list2 = []

for i in list1:
    list2.append(i)
print("\n")
print(*list1)

print(*list2)