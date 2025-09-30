from Crypto.Cipher import AES
import base64

#Genero chiave privata forzando esponente pubblico a 3:
#openssl genrsa -out FAprivkey.pem -3 2048

#Genero chiave pubblica a partire da quella privata:
#openssl rsa -in FAprivkey.pem -out FApubkey.pem -pubout -RSAPublicKey_out

#Per leggere la chiave privata:
#openssl rsa -in FAprivkey.pem -noout -text

#Per leggere la chiave pubblica:
#openssl rsa -in FApubkey.pem -pubin -noout -text


modulo = """00:d2:8f:3e:9c:c1:b8:23:5e:55:7b:c1:e0:c0:ac:
    17:a6:4e:43:7f:2e:a1:7c:d9:b0:58:d6:37:96:cc:
    74:33:88:9c:32:8e:8f:82:b7:9e:fb:e8:ab:b1:12:
    20:d0:e5:61:74:b0:84:60:91:d5:7d:89:3e:e7:39:
    44:c6:9c:35:e7:ab:cb:f2:ba:4a:01:f9:eb:c1:38:
    52:b6:63:80:36:52:ef:c8:3c:8d:27:3a:8d:5f:c6:
    06:1a:83:31:02:53:6b:31:af:b0:1e:f4:62:b5:9e:
    11:82:a9:b4:16:ac:13:33:ef:fd:fe:44:ad:55:c7:
    aa:68:b9:1b:63:16:b7:ce:81:d6:c0:bf:6c:f9:86:
    b9:3e:3b:42:97:e6:3c:ea:e4:f5:c9:16:7c:cd:1f:
    b8:e8:b8:a6:47:e1:05:6e:62:5e:fc:4c:20:bb:9d:
    f1:ea:3b:57:58:77:35:9c:2f:39:fd:04:be:34:9e:
    8f:9d:88:65:ec:aa:26:02:8b:26:48:84:2f:56:53:
    fb:7b:ae:8b:9b:be:41:13:12:89:f2:65:ca:68:53:
    35:ae:41:6b:58:0c:38:f6:b9:88:0e:38:39:a0:fa:
    cc:a4:14:a9:9f:b9:8e:4c:e6:47:d0:b9:f1:e1:f3:
    5d:61:02:c9:dc:ba:70:a7:cb:bb:3b:c7:08:f2:dd:
    26:55"""

modulo = modulo.replace(" ", "").replace(":", "").replace("\n", "") # tolgo tutti gli spazi i due punti e gli a capo
modulo = int(modulo, 16) # converto in hex

print("\nModulo:", modulo, "\n")

plain_text = int("Messaggio segreto 123".encode("utf-8").hex(), 16) # creo il plain_text già convertito in hex

print("Messaggio in hex (da stringa a bytes e da bytes a hex):", plain_text, "\n")

messaggio_cifrato = pow(plain_text, 3, modulo) # cifro il messaggio con esponente pubblico (3) e il modulo 

print("Messaggio cifrato pow(messaggio, esponente_pubblico (3), modulo):", messaggio_cifrato, "\n")

# Function to pad the message to be multiple of 16 bytes
def pad(text):
    while len(text) % 16 != 0:
        text += " "
    return text


# Encryption
def encrypt(plain_text, key):
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode("utf-8"))
    return base64.b64encode(encrypted_text).decode("utf-8")


# Decryption
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    decrypted_text = (
        cipher.decrypt(base64.b64decode(encrypted_text)).decode("utf-8").strip()
    )
    return decrypted_text

key = "itscybersecurity"

# cifro il messaggio con AES
messaggio_cifrato = encrypt(str(messaggio_cifrato), key)

print("Messaggio cifrato due volte (RSA+AES):", messaggio_cifrato, "\n")

# decifro con AES (rimane cifrato con RSA)
messaggio_cifrato = decrypt(messaggio_cifrato, key)

print("Messaggio decifrato AES (ancora cifrato RSA:)", messaggio_cifrato, "\n")

priv_exponent = """00:8c:5f:7f:13:2b:d0:17:94:38:fd:2b:eb:2b:1d:
    65:19:89:82:54:c9:c0:fd:e6:75:90:8e:cf:b9:dd:
    a2:cd:05:bd:77:09:b5:01:cf:bf:52:9b:1d:20:b6:
    c0:8b:43:96:4d:cb:02:eb:0b:e3:a9:06:29:ef:7b:
    83:2f:12:ce:9a:72:87:f7:26:dc:01:51:47:d6:25:
    8c:79:97:aa:ce:e1:f5:30:28:5e:1a:27:08:ea:84:
    04:11:ac:cb:56:e2:47:76:75:20:14:a2:ec:79:14:
    0b:ac:71:22:b9:c8:0c:cd:4a:a9:54:2d:c8:e3:da:
    71:9b:26:12:42:0f:25:34:55:59:5a:b8:ed:02:bd:
    93:94:94:81:c2:68:98:41:69:bd:14:f3:d5:ad:50:
    38:b1:eb:6f:aa:64:2b:39:5a:b8:99:8d:72:cc:c4:
    69:46:18:3d:e9:07:27:b1:80:f6:95:f2:ac:d0:45:
    df:cb:ca:dd:b8:fa:25:cb:4b:9f:bb:fd:7d:3f:95:
    19:e2:4d:ef:19:23:54:25:3a:ae:74:93:06:6e:c3:
    73:57:f2:a3:3c:86:3a:b7:fe:b2:ea:90:18:73:83:
    eb:a8:e1:14:52:88:61:20:bd:b2:43:8a:b4:ef:a3:
    f7:de:4c:b2:8f:cf:d7:a6:7c:98:b7:66:3f:94:ee:
    20:f3"""

priv_exponent = priv_exponent.replace(" ", "").replace("\n", "").replace(":", "") # tolgo tutti gli spazi i due punti e gli a capo
priv_exponent = int(priv_exponent, 16) # converto in hex

print("Esponente privato in hex:", priv_exponent, "\n")

messaggio_decifrato = pow(int(messaggio_cifrato), priv_exponent, modulo) # decifro il messaggio con esponente privato e modulo

print("Messaggio decifrato pow(messaggio cifrato, esponente privato, modulo):", messaggio_decifrato, "\n")

print("Il messaggio originale (in hex) è uguale al messaggio decifrato (sempre in hex)?", plain_text == messaggio_decifrato, "\n")



# converisone da hex ad ascii fatta da chatgpt non spiegata dal prof
length = (messaggio_decifrato.bit_length() + 7) // 8
msg_bytes = messaggio_decifrato.to_bytes(length, "big")
plaintext = msg_bytes.decode("utf-8")
print(plaintext)