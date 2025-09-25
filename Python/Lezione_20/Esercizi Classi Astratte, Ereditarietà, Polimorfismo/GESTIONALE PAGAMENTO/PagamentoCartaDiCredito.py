from Pagamento import *



class PagamentoCartaDiCredito(Pagamento):
    def __init__(self,importo,nome,data_scadenza,numero_carta):
        super().__init__()
        self.setimporto(importo)
        self.nome=nome
        self.data_scadenza=data_scadenza
        self.numero_carta=numero_carta

    def dettagliPagamento(self):
        print(f"Pagamento con carta di credito di {self.getimporto():.2f} €\n \
Nome Titolare Carta: {self.nome}\n \
Data scadenza Carta: {self.data_scadenza}\n \
Numero Carta: {self.numero_carta}")
        

p = PagamentoCartaDiCredito(
    250.50, 
    "Mario Rossi", 
    "12/25", 
    "1234 5678 9012 3456"
)
p.dettagliPagamento()