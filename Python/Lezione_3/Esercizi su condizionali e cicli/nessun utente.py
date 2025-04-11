"""crea un elenco di cinque o più nomi utente, incluso il nome "admin". 
Immagina di scrivere codice che stamperà un saluto a ogni utente dopo che avrà 
effettuato l'accesso a un sito web. Scorri l'elenco e stampa un saluto a ogni utente.
• Se il nome utente è "admin", stampa un saluto speciale, come Ciao admin, 
vuoi vedere un rapporto sullo stato?
• Altrimenti, stampa un saluto generico, come Ciao Jaden, grazie per aver
effettuato di nuovo l'accesso.
"""


elenco= ["Edoardo", "Francesca", "Andrea", "Admin","Max"]

for nomi in elenco:
    if nomi=="Admin":
        print(f"Ciao {nomi} un saluto speciale a te")
        
    else:
        print(f"Benvenuto {nomi}")
        


for index in range (len(elenco)):
    elenco.pop()
if len(elenco)==0:
    print("la tua lista e' vuota, dobbiamo trovare alcuni utenti")