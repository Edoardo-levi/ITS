from Pagamento import *

class PagamentoContanti(Pagamento):
    def __init__(self, importo: float):
        super().__init__()
        self.setimporto(importo)
        
    def dettagliPagamento(self):
        print(f"Pagamento in contanti di {self.getimporto():.2f} €")
    
    def inPezziDa(self):
        tagli=[500,200,100,50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.01]
        importo = round(self.getimporto())  # recupero l'importo dalla classe Pagamento e dal metodo getimporto() 

        for taglio in tagli:
            quanti = int(importo // taglio)# calcolo quante banconote e monete con il teglio giusto servono
                                           # mettendo int ottengo il risultato in intero
            if quanti > 0:                 # cerco solo i tagli necessari
                if taglio >= 5:            # se mi occorre una banconota il taglio è intero
                    print(f"{quanti} banconote da {taglio:.0f} €")
                else:                      # se mi occorre una moneta il taglio può essere decimale   
                    print(f"{quanti} monete da {taglio:.2f} €")
                importo = round(importo - quanti * taglio, 2) # aggiorno l'importo da scomporre arrotondandolo a 2 cifre decimali

# Uso
p = PagamentoContanti(10000)
p.dettagliPagamento()
p.inPezziDa()
