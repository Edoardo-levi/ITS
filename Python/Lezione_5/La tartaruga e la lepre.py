import random

def posizioni_gara(position_tartaruga:int=0, position_lepre:int=0):
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    
    finish:int=70
    while True:
        percorso:list=["_"]*70
       
        position_tartaruga=mosse_tartaruga(position_tartaruga)
        position_lepre=mosse_lepre(position_lepre)
        percorso[position_tartaruga-1]= "T"
        percorso[position_lepre-1]="H"
        
        print(*percorso)
        

        if position_tartaruga==position_lepre:
            print("OUCH")



        if position_tartaruga>=finish and position_lepre>=finish:
            print("PAREGGIO")
            break

        if position_lepre >= finish:
            print("HA VINTO LA LEPRE")
            break
        if position_tartaruga >=finish:
            print("HA VINTO LA TARTARUGA")
            break



def mosse_tartaruga(posizione_tartaruga): 

    percentuale_mosse= random.randint(1,10)


    if 1<=percentuale_mosse<=5:
        posizione_tartaruga+=3
    
    if 6<=percentuale_mosse<=7:
        posizione_tartaruga -=6
        if posizione_tartaruga<0:
            posizione_tartaruga=0


    if 8<=percentuale_mosse<=10:
        posizione_tartaruga+=1
    
    return min(posizione_tartaruga,70)

    
        
def mosse_lepre(posizione_lepre):

    percentuale_mosse= random.randint(1,10)


    if 1<=percentuale_mosse<=2:
        posizione_lepre=posizione_lepre
    
    if 3<=percentuale_mosse<=4:
        posizione_lepre+=9

    if percentuale_mosse==5:
        posizione_lepre-=12
        if posizione_lepre<0:
            posizione_lepre=0
    
    if 6<=percentuale_mosse<=8:
        posizione_lepre+=1
    
    if 9<=percentuale_mosse<=10:
        posizione_lepre-=2
        if posizione_lepre<0:
            posizione_lepre=0
    return min(posizione_lepre,70)


posizioni_gara()