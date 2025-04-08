"""Progettare un algoritmo che consenta di inserire all'utente un elenco di voti '
'non negativi relativi ad un esame, calcolandone la media. L'algoritmo deve chiedere all'utente se vuole inserire un voto. 

Se la risposta è "SI", allora l'utente può procedere ad inserire il voto. '
'L'algoritmo deve consentire all'utente di inserire voti fin quando la risposta dell'utente sarà "NO". 

Infine, mostrare in output il valore medio dei voti inseriti."""


cont=0
sum=0
while True:
    scelta=input("SI o NO?\n").lower()
    match scelta:
        case "si":
            voto=int(input("inserisci un voto:\n"))

            if voto > 0:
                cont+=1
                sum+=voto
                
            else:
                print("Erorre")
        case "no":
            
            if cont >0:
                media=sum/cont
                print(f"la media e': {media} e la somma e': {sum}")
                break
                
            
            else:
                print("nessun voto inserito")
        case _:
            print("Dati non validi")
            break
