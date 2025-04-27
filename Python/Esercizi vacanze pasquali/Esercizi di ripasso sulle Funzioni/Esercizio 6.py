"""PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome,
e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto."""

def create_contact(name: str, email: str = None, telefono: int = None) -> dict:
    contatto = {"profile": name, "email": email, "telefono": telefono
    }
    return contatto



"""
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, 
il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto."""


def update_contact(contatto: dict, name: str, email: str =None, telefono: int=None) -> dict:
    if contatto["profile"] == name:
        if email is not None:
            contatto["email"] = email
        if telefono is not None:
            contatto["telefono"] = telefono
    return contatto
