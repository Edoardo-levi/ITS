"""Crea una funzione che simuli un bancomat.
Inizializza un conto con un saldo iniziale.
Consenti all'utente di eseguire transazioni come deposito, prelievo e controllo del saldo.
Convalida le transazioni rispetto al saldo del conto e ai fondi disponibili.
Fornire un feedback appropriato all'utente per ogni transazione"""

def bancomat(operazione:str, saldo:float):
    
    try:

        if operazione.lower()=='deposito':
            deposito:float=float(input("Quando vuoi depositare?\n€ "))
            saldo+=deposito
            print(f"Hai depositato €{deposito}. Il bilancio è di €{saldo}")
        elif operazione.lower()=='prelievo':
            
            try:
                if saldo >0:
                    prelievo:float=float(input("Quanto vuoi prelevare?\n€ "))
                    if prelievo<=saldo:
                        saldo-=prelievo
                        print(f"Hai effettuato un prelievo di €{prelievo}. Il bilancio è di €{saldo}")
                    else: 
                        
                        raise ValueError("Fondi non sufficienti")
            except ValueError:
                print("Non puoi effettuare l'operazione di prelievo. Fondi Insufficienti")
        else:
            if operazione.lower()=='estratto':
                print(f"Il tuo bilancio è di € {saldo}")

    except ValueError:
        print("Operazione non consentita. Inserisci un opzione valida!")
    return saldo


operazioni:list=['deposito','prelievo','estratto']
saldo:float=float(input("Quanto è il tuo saldo iniziale? € ")) 
while True:
    try:
        
        operazione:str=input("Che tipo di operazione vuoi effettuare? (deposito, prelievo o estratto)\n")
        if operazione.lower() == 'esci':
            print("Operazioni concluse. Arrivederci")
            break
        if operazione not in operazioni:
            raise ValueError("Operazione non valida. Inserisci un opzione valida\n")
        saldo=bancomat(operazione,saldo)
    except ValueError:
        
        print("Operazione non valida. Inserisci un opzione valida")