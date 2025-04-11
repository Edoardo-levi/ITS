'''
Le comprehension sono metodi compatti per creare sequenze,
migliora la leggibilità e ci fanno risparmiare molte righe di codice (risparmiandoci i loop).
es:
    [x+1 for x in range(20) if x%2==0]
(output)     (loop)       (condizione [opzionale])
"Fai questo" - "per questa collection" - "in questa rituazione" 
'''

lista=[]
for x in range(10):
    if x%2==0:
        lista.append(x**2)

print(*lista, sep=", ")

#lo stesso codice compresso sarebbe ['expression' for 'item' in 'iterable' if 'condition']:

listaComppressa=[x**2 for x in range(10) if x%2==0]
print(*listaComppressa, sep=", ")


#altro esempio:

name=["andrea", "giulia", "alessio"]
uppercase_name={i.upper() for i in name}

print(*uppercase_name, sep=" - ")


# altro esempio:

lista=[[1, 2], [3, 4]]   # lista che contiene due liste, voglio fare in modo che ci sia un unica lista
flat=[num for riga in lista for num in riga]

# se immaginiamo la lista come una matrice composta da due righe e due colonne:
# | 1 2 |
# | 3 4 |
# prima viene esplorata la prima riga, poi la seconda riga
# il primo for itera sulle righe, il secondo for itera sugli elementi delle righe

print(flat)


# altro esempio
#immaginiamo di voler creare un set con le lunghezze de alcune parole:

parole=["ciao", "come stai?", "benvenuto"]
lunghezze={len(stringa) for stringa in parole}

print(lunghezze)


#altro esempio:
#immaginiamo di voler creare un dizionario:

dizionario={x: x**2 for x in range(5)}  #questa riga crea delle coppie chiave-valore uguali
print(dizionario)