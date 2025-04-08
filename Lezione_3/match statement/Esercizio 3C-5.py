"""Scrivere un programma in Python che memorizzi il nome, 
il ruolo e l'età di un utente in un dizionario. Il nome, il ruolo e l'età devono essere inseriti 
in input dall'utente stesso. Il programma deve determinare il livello di 
accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"""

utente={"nome":"",\
        "ruolo":"",\
        "eta":""}

utente["nome"]=str(input("inserisci il nome dell'utente:\n"))
utente["ruolo"]=str(input("inserisci il ruolo dell'utente:\n"))
utente["eta"]=int(input("inserisci l'eta dell'utente:\n"))



match utente:
    case utente if utente["ruolo"]=="admin":
        print(f"l'utente ha l'accesso completo a tutte le funzionalita'")
    
    case utente if utente["ruolo"]=="moderatore":
        print(f"l'utente può gestire i contetnuti ma non modificare le impostazioni'")
    
    case utente if utente["ruolo"]== "utente adulto" or utente["eta"] >=18:
        print(f"l'utente ha l'accesso standard a tutti i servizi")
    
    case utente if utente["ruolo"]== "utente minorenne" or utente["eta"] <=18:
        print(f"l'utente ha l'accesso limitato e alcune funzioni sono bloccate")
    
    case utente if utente["ruolo"]=="ospite":
        print(f"l'utente ha l'accesso ristretto. solo visualizzazione dei contentuti")
    
    case _:
        print(f"Ruolo non riconosciuto per l'utente ACCESSO NEGATO:\n{utente}")

for chiave, valore in utente.items():
    print(f"{chiave}: {valore}")

    