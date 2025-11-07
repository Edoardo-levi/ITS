class Ticket:
    def __init__(self, ticket_id:str, movie:str, seat:str, is_booked:bool=False):
        self.ticket_id=ticket_id
        self.movie=movie
        self.seat=seat
        self.is_booked=is_booked
    
    def book(self)->None:
        if self.is_booked==False:
            self.is_booked=True
        else:
            print(f"Il biglietto per {self.movie} posto {self.seat} è già prenotato")
    
    def cancel(self)->None:
        if self.is_booked==True:
            self.is_booked=False
        else:
            print(f"Il biglietto per {self.movie} posto {self.seat} non risulta prenotato")
    

class Viewer:
    def __init__(self, viewer_id:str,name:str,booked_tickets:list[Ticket]=[]):
        self.viewer_id=viewer_id
        self.name=name
        self.booked_tickets=booked_tickets
        

    def book_ticket(self,ticket:Ticket) ->None:
        if ticket.is_booked==False:
            ticket.book()
            self.booked_tickets.append(ticket)
        else:
            print(f"Il biglietto per {ticket.movie} non è disponibile")
    
    def cancel_ticket(self, ticket:Ticket)->None:
        if ticket in self.booked_tickets:
            self.booked_tickets.remove(ticket)
            ticket.cancel()
        else:
            print(f"il biglietto per {ticket.movie} non è stato prenotato da questo spettatore")


class Cinema:
    def __init__(self,tickets:dict[str,Ticket]={}, viewers:dict[str,Viewer]={}):
        self.tickets=tickets
        self.viewers=viewers
    
    def add_ticket (self,ticket_id:str, movie:str, seat:str) ->None:
        if ticket_id in self.tickets:
            print(f"il biglietto con ID {ticket_id} esiste già")
        else:
            self.tickets[ticket_id]=Ticket(ticket_id,movie,seat)
    
    def register_viewer(self,viewer_id:str,name:str)->None:
        if viewer_id in self.viewers:
            print(f"Lo spettatore con ID {viewer_id} è già registrato")
        else:
            self.viewers[viewer_id]=Viewer(viewer_id,name)
    
    def cancel_ticket(self, viewer_id: str, ticket_id: str) -> None:
        if viewer_id in self.viewers and ticket_id in self.tickets:
            viewer = self.viewers[viewer_id]
            ticket = self.tickets[ticket_id]
            viewer.cancel_ticket(ticket)
        else:
            print("Spettatore o biglietto non trovato.")
    
    def list_available_tickets(self)->list[str]:
        ticket_disponibili=[]
        for ticket_id, ticket in self.tickets.items():
            if ticket.is_booked ==False:
                ticket_disponibili.append(ticket_id)
        return ticket_disponibili

    def list_viewer_bookings(self, viewer_id: str) -> list[str] | str:
        if viewer_id not in self.viewers:
            return "Errore: spettatore non trovato."
        else:
            spettatore = self.viewers[viewer_id]
            prenotazioni = []
            for ticket in spettatore.booked_tickets:
                prenotazioni.append(ticket.ticket_id)
            return prenotazioni
