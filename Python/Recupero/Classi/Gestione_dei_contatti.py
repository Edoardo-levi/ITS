class ContactManager:
    def __init__(self, contacts: dict[str, list[str]]):
        self.contacts={}
        
    
    def create_contact(self, name: str, phone_numbers: list[str]):
        if name in self.contacts:
            raise ValueError("Errore! Il contatto esiste già")
        else:
            self.contacts[name]=phone_numbers
            return {name:phone_numbers}
    
    def add_phone_number(self, contact_name: str, phone_number: str) ->dict:
        if contact_name not in self.contacts:
            raise ValueError("Errore! Il contatto non esiste")
        elif phone_number in self.contacts[contact_name]:
            raise ValueError("Erorre! Il nomero di telefono esiste già ")
        else:

            
            self.contacts[contact_name].append(phone_number)

            return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Erorre! Il contatto non esiste")

        elif phone_number not in self.contacts:
            raise ValueError ("Il Numero di telefono non esiste")
        
        else:
            self.contacts[contact_name].remove(phone_number)
        return {contact_name:self.contacts[contact_name]}

    def update_phone_number(self, contact_name: str, old_phone_number: str,new_phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore! Il contatto non esiste")
        elif old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore! il numero di telefono non è presente")
        
        else:
            self.contacts[contact_name].remove(old_phone_number)
            self.contacts[contact_name].append(new_phone_number)
        return {contact_name: self.contacts[contact_name]}
    
    def list_contacts(self):
        key_list:list=[]
        for key in self.contacts:
            key_list.append(key)
        return key_list
    
    def list_phone_numbers(self, contact_name: str): 
        if contact_name not in self.contacts:
            raise ValueError("Errore! Il contatto non esiste")

        else:
            print(self.contacts[contact_name])
            return self.contacts[contact_name]
    
    def search_contact_by_phone_number(self, phone_number: str):
        new_list:list=[]
        for key in self.contacts:
            if phone_number in self.contacts[key]:
                new_list.append(key)
            
        if not new_list:
            raise ValueError("Nessun contatto trovato con questo numero di telefono.")
        return new_list