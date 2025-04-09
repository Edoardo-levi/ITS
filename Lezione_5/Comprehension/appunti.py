print("Lista da 1 a 20")
lista_numeri=[x for x in range(1,21) ]  # CREA UNA LISTA DA 1 A 20

print(*lista_numeri)

print("------------------------ \n")
print("Lista di numeri pari da 1 a 20")
lista_numeri_pari= [x for x in range (1,21) if x%2 ==0] # CREA UNA LISTA DA 1 A 20 SOLO DI NUMERI PARI

print(*lista_numeri_pari)

print("------------------------ \n")

numeri_pari_elevati_seconda= [x**2 for x in range(10) if x%2==0]  #CREA UNA LISTA DI NUMERI PARI ELEVATI ALLA 2 (0 ^2, 2^2, 4^2, 6^2, 8^2)

print(numeri_pari_elevati_seconda)

print("------------------------ \n")

print("LIsa con i nomi tutti in magliuscolo")

nomi:list=["edoardo", "mattia", "alessio"]

nomi_maiuscolo:list[str] = [names.upper() for names in nomi]
print(nomi_maiuscolo)

print("------------------------\n")

matrice:list [list[int]] = [[1, 2], [3, 4]]
flat:list[int]= [num for riga in matrice for num in riga]   # riga equivale a 1,2 e 3,4
                                                            # nel primo for itera sulle liste nel secondo for itera sui numeri (prende i numeri e li salva in flat)
print(flat)

print("------------------------\n")
print("Calcolo della lunghezza delle parole senza duplicati")

parole=["ciao", "ao", "bella", "daje"]
calcolo_lunghezza_parole= {len(word) for word in parole}        # calcola la lunghezza delle parole e se ci sono duplicati non li considera
print(calcolo_lunghezza_parole)

print("------------------------\n")
print("dizionario di chiave valore di numeri da 0 a 4 elevati alla 2")

numeri_elevati={x:x**2 for x in range(5)}                   # crea un dizionario con chiave valore di numeri da 0 a 4 elevati alla 2
#x: è la chiave mentre x**2 è il valore
print(numeri_elevati)
