"""scrivi una funzione validate_password(password)
che controlla se una password soddisfa determinati criteri 
(ad esempio, lunghezza minima di 20 caratteri, almeno tre caratteri maiuscoli e almeno quattro caratteri speciali). 
Genera un'eccezione personalizzata (ad esempio, InvalidPasswordError) per le password non valide."""

def validate_password (password:str):
    cont=0
    cont_special=0
    
    for i in password:
        if i.isupper:
            cont+=1
        if i.isalnum:
            cont_special+=1
    if len(password) < 20 and cont < 3 and cont_special < 4:
        raise Exception("InvalidPasswordError:(Password non valida)")
    
    
    


parola_chiave= validate_password(input("Inserisci la Passwor:\n"))

print(parola_chiave)