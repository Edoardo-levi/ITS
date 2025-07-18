import re 

def controllo_stringa(seq:str):
    seq = seq.upper()
    if re.fullmatch(r'[ACGT]+',seq):
        return True
    else:
        return False

def frammenti_DNA(s1:str, s2:str):
    try:
        if  controllo_stringa(s1) or  controllo_stringa(s2):
            lunghezza_max= min(len(s1), len(s2))
            sovrapposizione=0
            for i in range (1, lunghezza_max +1):
                if s1[-i:] == s2[:i]:
                    sovrapposizione = i
            print (s1)
            print(" " * (len(s1) - sovrapposizione) + s2)
            print(f"La massima lunghezza di sovrapposizione è {sovrapposizione}\n")
            
            
    except ValueError as error:
        print("La stringa inserita non è valida")
    

frammenti_DNA(s1= "TTGACCAGGTCA", s2="AACCGGTTAA")
