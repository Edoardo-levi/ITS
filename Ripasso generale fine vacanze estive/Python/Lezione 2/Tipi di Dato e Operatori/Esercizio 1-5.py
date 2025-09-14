"""Si scriva un programma che converta la temperatura da Fahrenheit a Celsius utilizzando la formula

gradiCelsius=5∗(gradiFahrenheit−32)/9

Si inizializzi una temperatura espressa in gradi Fahrenheit con un numero intero.

La temperatura deve essere convertita e visualizzata in gradi Celsius con un numero in virgola mobile con una precisione di un decimo di grado.

Un possibile esempio di output potrebbe essere il seguente:

72 gradi Fahrenheit corrispondono a 22.2 gradi Celsius."""

while True:
    try:
        temperatura_Fahrenheit: int = int(input("Inserisci una temperatura in gradi Fahrenheit:\n"))
        break  
    except ValueError:
        print("Errore: devi inserire un numero intero\n")

temperatura_Celsius = 5 * (temperatura_Fahrenheit - 32) / 9
print(f"Gradi Fahrenheit: {temperatura_Fahrenheit}\n\
Gradi Celsius: {temperatura_Celsius}")
