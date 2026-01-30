
# 1) Encoding Challenge

# Importiamo pwntools, una libreria molto usata nel CTF
# Serve per comunicare facilmente con servizi remoti (socket, exploit, ecc.)
from pwn import *  # pip install pwntools

# json serve per leggere e scrivere dati in formato JSON
import json

# Funzioni utili per convertire numeri grandi ↔ byte
# Servono quando i dati sono rappresentati come "bigint"
from Crypto.Util.number import bytes_to_long, long_to_bytes

# codecs serve per alcune codifiche testuali, come rot13
import codecs

# base64 serve per decodificare stringhe in Base64
import base64


# Ci connettiamo a un server remoto
# - 'socket.cryptohack.org' è l'host
# - 13377 è la porta
# - level='debug' stampa tutto ciò che viene inviato/ricevuto (utile per capire cosa succede)
r = remote('socket.cryptohack.org', 13377, level='debug')


# Funzione che:
# 1. riceve una riga dal server
# 2. la converte da bytes a stringa
# 3. la trasforma in un dizionario Python (JSON → dict)
def json_recv():
    line = r.recvline()              # riceve una riga dal socket
    return json.loads(line.decode()) # decode bytes → stringa, poi JSON → dict


# Funzione che:
# 1. prende un dizionario Python
# 2. lo trasforma in JSON
# 3. lo invia al server
def json_send(hsh):
    request = json.dumps(hsh).encode()  # dict → JSON → bytes
    r.sendline(request)                 # invia al server


# Variabile che conterrà la stringa decodificata
decoded = ""


# Il server manda 101 "sfide" da risolvere
for stage in range(101):

    # Riceviamo il messaggio dal server (è un dizionario)
    received = json_recv()

    # Reset della variabile decoded ad ogni round
    decoded = ""

    # In base al tipo di encoding ricevuto, scegliamo come decodificare

    # Caso Base64
    if received["type"] == "base64":
        # base64.b64decode restituisce bytes → li convertiamo in stringa
        decoded = base64.b64decode(received["encoded"]).decode()

    # Caso HEX
    elif received["type"] == "hex":
        # Converte una stringa esadecimale in bytes → poi in stringa
        decoded = bytes.fromhex(received["encoded"]).decode()

    # Caso ROT13
    elif received["type"] == "rot13":
        # Applica la codifica rot13 alla stringa
        decoded = codecs.encode(received["encoded"], "rot_13")

    # Caso BIGINT
    elif received["type"] == "bigint":
        # Il numero è una stringa tipo "0x...."
        # int(..., 0) capisce automaticamente la base (hex/dec)
        # long_to_bytes converte il numero in bytes
        decoded = long_to_bytes(int(received["encoded"], 0)).decode()

    # Caso UTF-8
    elif received["type"] == "utf-8":
        # received["encoded"] è una lista di numeri
        # Ogni numero rappresenta il codice ASCII/UTF-8 di un carattere
        for c in received["encoded"]:
            decoded += chr(c)  # chr converte numero → carattere


    # Prepariamo la risposta da inviare al server
    to_send = {
        "decoded": decoded
    }

    # Inviamo la risposta
    json_send(to_send)


# Dopo aver risolto tutte le 101 sfide,
# il server manda il messaggio finale (di solito la flag)
data = json_recv()





# 2) You either know, XOR you dont


# Importiamo solo la funzione xor da pwntools
# xor(a, b) fa l'operazione XOR byte-per-byte tra a e b
from pwn import xor


# Il ciphertext è una stringa esadecimale (hex)
# bytes.fromhex(...) la converte in una sequenza di byte reali
cipher = bytes.fromhex(
    "0e0b213f26041e480b26217f27342e175d"
    "0e070a3c5b103e2526217f27342e175d"
    "0e077e263451150104"
)


# Qui sfruttiamo un fatto importante:
# sappiamo che il plaintext inizia con "crypto{"
# XOR è reversibile:
#   plaintext XOR key = ciphertext
#   ciphertext XOR plaintext = key
#
# Quindi: cipher XOR "crypto{" → otteniamo la chiave
key = xor(cipher, "crypto{".encode())


# Stampiamo la chiave ottenuta
# .decode() serve per convertire bytes → stringa leggibile
print("I think this is the key: " + key.decode())


# Commento ironico: sappiamo (dal contesto della challenge)
# che la chiave termina con la lettera "y"
print("Obviously, please add the y")


# Convertiamo la chiave in stringa
# Prendiamo solo i primi 7 caratteri
# e aggiungiamo manualmente la "y" finale
key = key.decode()[:7] + "y"


# Ora che abbiamo la chiave completa,
# facciamo XOR tra ciphertext e chiave
# Questo restituisce il plaintext originale
print(xor(cipher, key.encode()))




# 3) Lemur xor

# Applicando un XOR tra le immagini e regolando opportunamente brightness e contrast, è possibile rendere visibili le differenze nei pixel. Questo permette di far emergere il messaggio nascosto nell’immagine, che risulta essere crypto{XORly_n0t!}



# 4) CERTainly not


# Importiamo il modulo RSA dalla libreria pycryptodome
# Serve per lavorare con chiavi RSA (pubbliche o private)
from Crypto.PublicKey import RSA


# Apriamo il file che contiene la chiave RSA in formato PEM
# "<PATH>/CERTIFICATE.pem" va sostituito con il percorso reale del file
# La modalità "r" indica che lo apriamo in lettura (read)
f = open(r"<PATH>/CERTIFICATE.pem", "r")


# Leggiamo tutto il contenuto del file e lo salviamo in una stringa
# In pratica, qui dentro c'è il testo della chiave PEM
key = f.read()


# Importiamo la chiave RSA a partire dal testo PEM
# RSA.importKey analizza il contenuto e crea un oggetto RSA
enc = RSA.importKey(key)


# Stampiamo il valore n della chiave RSA
# n è il modulo RSA, cioè il prodotto di due grandi numeri primi (p * q)
# È una delle informazioni fondamentali di una chiave RSA
print(enc.n)





# 5) SSH Keys

# Importiamo il modulo RSA dalla libreria pycryptodome
# Serve per leggere e usare chiavi RSA (pubbliche o private)
from Crypto.PublicKey import RSA


# Apriamo il file che contiene la chiave RSA in formato PEM
# <PATH>/RSA.pem va sostituito con il percorso reale del file
# "r" significa modalità lettura (read)
f = open(r"<PATH>/RSA.pem", "r")


# Leggiamo tutto il contenuto del file
# Il risultato è una stringa che contiene il testo PEM della chiave
key = f.read()


# Importiamo la chiave RSA a partire dal contenuto PEM
# RSA.importKey analizza il file e crea un oggetto RSA utilizzabile in Python
enc = RSA.importKey(key)


# Stampiamo il valore n della chiave RSA
# n è il modulo RSA, cioè il prodotto di due grandi numeri primi (p * q)
# È un valore pubblico ed è sempre presente sia nella chiave pubblica che privata
print(enc.n)
