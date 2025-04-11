"""Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi."""


frase= str(input("inserisci una frase:\n"))

match frase:
    case frase if len(frase) % 2 == 0 and frase[-1]== "?":
        print("SI")
    case frase if len(frase) % 2 !=0 and frase[-1]== "?":
        print("NO")
    case frase if len(frase[-1]) == "!":
        print("WOW")
    case _:
        print(f'Tu dici "{frase}"')