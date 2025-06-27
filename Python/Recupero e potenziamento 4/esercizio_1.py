import math

def tariffa_oraria(ore_parcheggio:float, macchina:str):
    tariffa_minima=2
    incremento_tariffa=0.50
    tariffa =0
 

    if ore_parcheggio <=3:
        tariffa = 2
    
    elif ore_parcheggio == 24:
        tariffa = 10
    
    else:
        if ore_parcheggio >3 and ore_parcheggio <24:
            tariffa = tariffa_minima +(math.ceil(ore_parcheggio)-3)*incremento_tariffa

    return(f"{macchina:<10} {ore_parcheggio:<10} €{tariffa:<10}")

print(f"{'Car':<10}{'Hours':<15}{'Charge'}")

totale_ore = 0
totale_tariffa = 0
clienti:list= [1,2.5,3,5,8,9]

for i in clienti:
    t= tariffa_oraria(i)
    


tariffa_oraria(2, "Fiat500")
tariffa_oraria(3, "Panda")
tariffa_oraria(5, "BMW")
tariffa_oraria(10, "Tesla")
tariffa_oraria(24, "Mercedes")
tariffa_oraria(23.5, "Audi")
