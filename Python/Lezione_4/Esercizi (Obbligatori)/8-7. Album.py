'''scrivi una funzione chiamata make_album() che costruisca un dizionario che descriva un album musicale. 
La funzione dovrebbe accettare un nome di artista e un titolo di album e dovrebbe restituire un dizionario 
contenente queste due informazioni. Usa la funzione per creare tre dizionari che rappresentano album diversi. 
Stampa ogni valore restituito per mostrare che i dizionari stanno memorizzando correttamente le informazioni 
dell'album. Usa None per aggiungere un parametro facoltativo a make_album() che ti consente di memorizzare 
il numero di brani in un album. Se la riga di chiamata include un valore per il numero di brani, aggiungi 
quel valore al dizionario dell'album. 
Crea almeno una nuova chiamata di funzione che includa il numero di brani in un album.'''


def make_album (nome_artista:str, titolo_album:str, brani=None):
    album:dict={'Artista': nome_artista,\
                'Canzone': titolo_album}
    if brani==0:
        brani=None
    
    album["Numero di brani"]= brani
    
    return album


print("inserisci il dati per il PRIMO artista")

artista1=input("inserisci il nome dell'artista:\n")
album1=input("inserisci il nome dell'album:\n")
n_brani1=int(input("inserisci il numero di brani presente nell'album:\n"))
dict1=make_album(artista1, album1, n_brani1)


print("inserisci i dati per il SECONDO artista:")

artista2=input("inserisci il nome dell'artista:\n")
album2=input("inserisci il nome dell'album:\n")
n_brani2=int(input("inserisci il numero di brani presente nell'album:\n"))
dict2=make_album(artista2, album2,n_brani2)


print("inserisci i dari per il TERZO artista:")

artista3=input("inserisci il nome dell'artista:\n")
album3=input("inserisci il nome dell'album:\n")
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