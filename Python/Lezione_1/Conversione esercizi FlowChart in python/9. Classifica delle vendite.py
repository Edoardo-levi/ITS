"""Progetta un algoritmo che forniti dall'utente 20 totali di vendita e i nomi dei venditori, '
'trova i due nomi dei venditori con il totale più alto e il totale più basso delle vendite."""

nome=input("iserisci un nome:\n")
vendite=int(input("inserisci un numero per le vendite:\n"))

max_nome=nome
max=vendite
min_nome=nome
min=vendite

cont=0
for cont in range (1,21):
    new_nome=input("inserisci un nuovo nome:\n")
    new_vendite= int(input("inserisci un nuovo numero per le vendite:\n"))


    if new_vendite > max:
        max_nome= new_nome
        max=new_vendite
    
    else:
        if new_vendite < min:
            min_nome=new_nome
            min=new_vendite
        
    cont+=1
    
print(f"il nome massimo e': {max_nome} e il numero massimo di vendite e': {max}")

print(f"il nome minimo e': {min_nome} e il numero minimo di vendite e': {min}")