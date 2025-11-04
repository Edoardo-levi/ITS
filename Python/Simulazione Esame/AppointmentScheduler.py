class AppointmentScheduler:
    def __init__(self, appointments:dict[str,dict[str,str]]={}):
        self.appointments=appointments
    
    def schedule_appointment (self,app_id:str,data:str) -> dict | str:
        if app_id in self.appointments:
            return "Errore! appuntamento esiste gia"
        else:
            self.appointments[app_id]={"data":data, "programmato": True}
            return self.appointments[app_id]

    def reschedule_appointment(self,app_id:str,nuova_data:str)-> dict | str:
        if app_id not in self.appointments:
            return "Errore appuntamento non trovato"
        else:
            self.appointments[app_id] ["data"]= nuova_data
            return self.appointments[app_id]
    
    def cancel_appointment(self,app_id:str)-> dict|str:
        if app_id not in self.appointments:
            return "Errore: appuntamento non trovato"
        else:
            self.appointments[app_id]["programmato"]=False
            return self.appointments[app_id]
    
    def remove_appointment(self,app_id:str) -> dict|str:
        if app_id not in self.appointments:
            return "Errore appuntamento non trovato"
        else:
            appuntameto_rimosso=self.appointments.pop(app_id)
            return appuntameto_rimosso
    
    def list_appointment(self)->list[str]:
        lista:list=[]
        for app_id in self.appointments.keys():
            lista.append(app_id)
        return lista
    
    def get_appointment(self, app_id:str)-> dict|str:
        if app_id in self.appointments:
            return self.appointments[app_id]
        else:
            return "Errore appuntamento non trovato"