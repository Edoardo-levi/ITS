"""utilizzando un programma che hai scritto e che contiene una funzione, 
memorizza quella funzione in un file separato. 
Importa la funzione nel tuo file di programma principale e chiama la funzione utilizzando ciascuno di questi approcci:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""

"""
import funzioni_semplici

nome=input("inserisci un nome:\n")
eta= int(input("inserisci un eta':\n"))

stampa= funzioni_semplici.stampa_nome(nome), funzioni_semplici.stampa_eta(eta)

print(f"il nome inserito e': {nome}\nL'eta' inserita e': {eta}")


from funzioni_semplici import stampa_nome, stampa_eta
nome=input("inserisci un nome:\n")
eta= int(input("inserisci un eta':\n"))

stampa= funzioni_semplici.stampa_nome(nome), funzioni_semplici.stampa_eta(eta)

print(f"il nome inserito e': {nome}\nL'eta' inserita e': {eta}")

from funzioni_semplici import stampa_nome as st
from funzioni_semplici import stampa_eta as se



nome=input("inserisci un nome:\n")
eta= int(input("inserisci un eta':\n"))

stampa= st(nome), se(eta)

print(f"il nome inserito e': {nome}\nL'eta' inserita e': {eta}")


import funzioni_semplici as fs


nome=input("inserisci un nome:\n")
eta= int(input("inserisci un eta':\n"))

stampa= fs.stampa_nome(nome), fs.stampa_eta(eta)

print(f"il nome inserito e': {nome}\nL'eta' inserita e': {eta}")

"""
from funzioni_semplici import *


nome=input("inserisci un nome:\n")
eta= int(input("inserisci un eta':\n"))

stampa= stampa_nome(nome), stampa_eta(eta)

print(f"il nome inserito e': {nome}\nL'eta' inserita e': {eta}")
