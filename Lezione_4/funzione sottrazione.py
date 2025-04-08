"""
Proviamo a definire noi stessi una funzione chiamata sottrarre:
● Dovrebbero essere necessari 2 parametri.
● All'interno della funzione, dovrebbe sottrarre i due.
● Quindi, restituire il risultato.
Dopo averlo definito, chiama la funzione con alcuni argomenti!"""







def sottrazione(x,y):                   # definisco la funzione
    risultato= x-y                      # faccio la sottrazione 
    return risultato                    # restituisco il risultato
num1=int(input("numero1:\n"))           # faccio inserire all'utente il primo numero da sottrarre
num2= int(input("numero2:\n"))          # faccio inserire all'utente il secondo numero da sottrarre 
funzioe = sottrazione(num1, num2)       # chiamo la funzione
print(f"il risultato della sottrazione tra {num1} e {num2} e': {funzioe}")        # stampo il risultato

