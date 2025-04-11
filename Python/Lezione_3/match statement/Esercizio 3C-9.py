'''Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto 
(x, y) e salvi le coordinate inserite in una tupla. Utilizzare il  match statement per determinare 
la sua posizione del punto inserito nel piano cartesiano:

- Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
- Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X."
- Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
- Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
- Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
- Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
- Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."'''


x=int (input("inserisci le coordinate per l'asse x:\n"))
y=int (input("inserisci le coordinate per l'asse y:\n"))

punti_cartesiani=(x,y)

match punti_cartesiani:
    case (0, 0):
        print(f"il punto si trova nell'origine ({x} {y})")
    
    case (0, y):
        print(f"il punto si trova nell'asse delle X {x} {y}")
    
    case (x, 0):
        print(f"il punto si trova sull'asse delle Y {x} {y}")
    
    case punti_cartesiani if x > 0 and y > 0:
        print(f"il punto si trova nel primo quadrante {x} {y}")
    
    case punti_cartesiani if x<0 and y>0:
        print(f"il punto si trova nel secondo quadrante {x} {y}")
    
    case punti_cartesiani if x <0 and y <0:
        print(f"il punto si trova nel terzo quadrante {x} {y}")

    case _:
        print(f"il punto si trova nel quarto quadrante {x} {y}")

