"""Progettare un algoritmo che chieda all’utente di inserire due valori interi positivi 
𝐴 e 𝐵 con 𝐴 < 𝐵. Se i valori non rispettano le condizioni, mostrare un messaggio di errore e terminare. 
Se i valori sono validi, calcolare la somma di tutti i numeri interi compresi tra 𝐴 e 𝐵 (inclusi) e mostrare il risultato."""

a=int(input("inserisci il numero A: "))
b=int(input("inserisci il numero B "))


if a<b:
    if a>0 and b>0:
        sum=0
        i=a
    else:
        print("A e B devono essere positivi")
else:
    print("il numero A deve essere minore di B")
for i in range (a, b+1):
    sum+=i

print(f"la somma e': {sum}")
