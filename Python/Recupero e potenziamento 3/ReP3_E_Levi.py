import random


class Creatura:


    __nome:str

    def __init__(self, nome:str) -> None:

        self.setNome(nome)
    
    def setNome(self,nome:str) -> None:
        
        if isinstance(nome, str) and nome != "":
            self.__nome = nome
            print(f"La creatura inserita: {self.__nome} è una stringa valida.")
        else:
            self.__nome = "Creatura Generica"
    
    def get_nome(self) -> str:
        return self.__nome
    
    def __str__(self) -> str:
        return f"Creatura: {self.__nome}"
    



class Alieno(Creatura):

    __matricola:int
    __munizioni:list[int]

    def __init__(self, nome:str) -> None:
        super().__init__(nome)
        self.__setMatricola()
        self.__setMunizioni()
        
        if Creatura.get_nome(self) == "alieno".lower():
            self.setNome(f"Robot-{self.__matricola}")
        else:
            print("Attenzione! Tutti gli Alieni deveno avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione del nome Alieno in corso!")
            self.setNome(f"Robot")
        
        

    def __setMatricola(self) -> None:

        self.__matricola= random.randint(10000,90000)
    

    def __setMunizioni(self)->None:

        self.__munizioni:list[int] = [i**2 for i in range(15)]

    

    def get_matricola(self)->int:
        return self.__matricola
    
    def get_munizioni(self)->list[int]:
        return self.__munizioni
    

    def __str__(self):
        return f"Alieno: {self.get_nome().title()}"
    


class Mostro(Creatura):
    
    __urlo_vittoria:str
    __gemito_sconfitta:str
    __assalto:list[int]

    def __init__(self, nome:str, vittoria:str, sconfitta:str) -> None:
        super().__init__(nome)
        self.__setAssalto()
        self.__setVittoria(vittoria)
        self.__setSconfitta(sconfitta)

    def __setAssalto(self) -> None:
        self.__assalto:list[int]=[]
        for i in range (1,16):
            numeri_casuali= random.randint(1,100)
            self.__assalto.append(numeri_casuali)
    

    def __setVittoria(self, vittoria:str) -> None:
        if vittoria != "GRAAAHHH".upper():
            self.__urlo_vittoria = "GRAAAHHH".upper()
        else:
            print("L'urlo di vittoria è impostato correttamente.")
        
    def __setSconfitta(self, gemito_sconfitta:str) -> None:

        if gemito_sconfitta != "Uuurghhh".title():
            self.__gemito_sconfitta = "Uuurghhh".title()
        else:
            print("Il gemito di sconfitta è impostato correttamente.")

    def get_urlo_vittoria(self) -> str:
        return self.__urlo_vittoria

    def get_gemito_sconfitta(self) -> str:
        return self.__gemito_sconfitta

    def get_assalto(self) -> list[int]:
        return self.__assalto
    
    
    def __str__(self)-> str:
        nome_alternato= ""
        for i, char in enumerate(self.get_nome()):
            if i % 2 == 0:
                nome_alternato += char.lower()
            else:
                nome_alternato += char.upper()
        return f"Mostro:{nome_alternato}"
        



def pariUguali(a: list[int], b: list[int]) -> int:
    c= []
    lunghezza_minima = min(len(a), len(b))

    for i in range (lunghezza_minima):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)

    return c



def combattimento(a: Alieno, m: Mostro)-> Creatura | None:
    if not isinstance(a, Alieno):
        print("Il combattimento è stato interrotto: 'a' non è un Alieno valido.")
        return None
    if not isinstance(m, Mostro):
        print("Il combattimento è stato interrotto: 'm' non è un Mostro valido.")
        return None

    print("\n--- Combattimento ---")

    
    risultati_pari = pariUguali(a.get_munizioni(), m.get_assalto())

    
    count_uni = risultati_pari.count(1)

   
    if count_uni > 4:
        
        for _ in range(3):
            print(m.get_urlo_vittoria())
        return m
    else:
        
        print(m.get_gemito_sconfitta())
        return a
