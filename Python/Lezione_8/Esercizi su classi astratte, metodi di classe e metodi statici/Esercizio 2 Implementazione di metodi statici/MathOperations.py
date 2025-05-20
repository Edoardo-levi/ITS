"""Crea una classe chiamata MathOperations per raggruppare alcune funzionalità aritmetiche di base. All'interno di questa classe, definisci due metodi statici :

add , che accetta due parametri numerici e restituisce la loro somma .

multiply , che accetta anch'essa due parametri numerici e restituisce il loro prodotto .

Infine , scrivi un piccolo programma driver per testare la funzionalità dei metodi add e multiply . Questo dovrebbe comportare la chiamata di entrambi i metodi con input di esempio e la stampa dei risultati per verificarne il corretto funzionamento.
"""



class MathOperations:
    @staticmethod
    def add(x:int | float, y:int | float) -> int | float:
        return x + y
    @staticmethod

    def multiply(x:int | float, y:int | float) -> int | float:
        return x * y
    
    