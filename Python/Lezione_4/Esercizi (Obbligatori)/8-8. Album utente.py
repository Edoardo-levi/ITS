"""inizia con il tuo programma dall'esercizio 8-7. 
Scrivi un ciclo while che consenta agli utenti di immettere l'artista e il titolo di un album. 
Una volta ottenute queste informazioni, chiama make_album() 
con l'input dell'utente e stampa il dizionario creato. Assicurati di includere un valore quit nel ciclo while."""


def make_album (nome_artista:str, titolo_album:str, brani=None):
    album:dict={'Artista': nome_artista,\
                'Canzone': titolo_album}
    if brani==0:
        brani=None
    
    album["Numero di brani"]= brani
    
    return album
parola_quit=""
while True:
    print("inserisci il dati per il PRIMO artista")

    artista1=input("inserisci il nome dell'artista:\n")
    if artista1=="quit":
        break

    album1=input("inserisci il nome dell'album:\n")

    if album1=="quit":
        break
    n_brani1=int(input("inserisci il numero di brani presente nell'album:\n"))
    dict1=make_album(artista1, album1, n_brani1)
   

    print("inserisci i dati per il SECONDO artista:")

    artista2=input("inserisci il nome dell'artista:\n")

    if artista2=="quit":
        break

    album2=input("inserisci il nome dell'album:\n")

    if album2=="quit":
        break

    n_brani2=int(input("inserisci il numero di brani presente nell'album:\n"))
    dict2=make_album(artista2, album2,n_brani2)



    print("inserisci i dari per il TERZO artista:")

    artista3=input("inserisci il nome dell'artista:\n")

    if artista3=="quit":
        break

    album3=input("inserisci il nome dell'album:\n")

    if album3=="quit":
        break

    n_brani3=int(input("inserisci il numero di brani presente nell'album:\n"))
    dict3=make_album(artista3, album3, n_brani3)
    
    


def print_album(album):                                 # questa funzione serve per far stampare i dizionari senza parentesi e apici 
    for key, value in album.items():
        print(f"{key}: {value}")
print("\n1° Album:")
print_album(dict1)
print("\n2° Album:")
print_album(dict2)
print("\n3° Album:")
print_album(dict3)