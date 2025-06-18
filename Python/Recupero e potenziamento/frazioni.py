"""8.A Si Scriva in Python in un file frazioni.py una classe Frazione, i cui attributi privati siano rispettivamente numeratore e denominatore.

Si definiscano i metodi __init__, setter, getter, __str__, value.
In particolare:
il metodo value(), deve restituire il valore della frazione, ovvero numeratore / denominatore arrotondato a 3 cifre decimali;
il metodo __str__ deve mostare in output la frazione nel seguente modo: "numeratore / denominatore ";
i metodi setter devono controllare che il valore inserito sia un intero, in caso contrario il numeratore ed il denominatore devono essere impostati per default rispettivamente a 13 e 5. Inoltre, il metodo setter relativo al denominatore deve assicurarsi che questo non sia mai uguale a 0. Nel caso in cui il denominatore passato sia 0, impostarlo per default a 5.
Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la funzione is_integer()."""

import math

class Frazione:
    __numeratore:int
    __denominatore:int
    def __init__(self,numeratore:int, denominatore:int)-> None:
        
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)
        
    
    def is_integer(self,value)->bool:
        return isinstance(value,int)
    
    def set_numeratore(self,numeratore:int)->None:
        if self.is_integer(numeratore):
            self.__numeratore= numeratore
        else:
            self.__numeratore = 13
       
    
    def set_denominatore(self,denominatore:int)->None:
        if self.is_integer(denominatore):
            if denominatore== 0:
                self.__denominatore = 5
            else:
                self.__denominatore = denominatore
        else:
            self.__denominatore = 5
        
    
    def get_numeratore(self)->int:
        return self.__numeratore

    def get_denominatore(self)->int:
        return self.__denominatore
    
    def value(self)->float:
        return round(self.__numeratore / self.__denominatore, 3)
    
    def __str__(self) ->str:
        return f"{self.__numeratore}/{self.__denominatore}"
    

    def MCD (x:int, y:int) ->int:
       return math.gcd(x,y)             # funzione vista su web3schools
    

    def semplifica(lista: list["Frazione"]):
        lista_semplificata: list[Frazione] = []

        for i in lista:
            numeratore: int = i.get_numeratore()
            denominatore: int = i.get_denominatore()

            d: int = 2
            d1: int = 2  # Spostati all'interno del ciclo for

            while numeratore > 1:
                if numeratore % d == 0:
                    numeratore //= d
                else:
                    d += 1

            while denominatore > 1:
                if denominatore % d1 == 0:
                    denominatore //= d1
                else:
                    d1 += 1

            lista_semplificata.append(Frazione(numeratore, denominatore))  # Ordine corretto

        return lista_semplificata


def fractionCompare(lista:list[Frazione], lista_semplificata:list[Frazione]):
    for i in lista:
        for j in lista_semplificata:
            if i.value() == j.value():
                print(f"Valore frazione originale: {i.value} --- Valore frazione ridotta: {j.value}")