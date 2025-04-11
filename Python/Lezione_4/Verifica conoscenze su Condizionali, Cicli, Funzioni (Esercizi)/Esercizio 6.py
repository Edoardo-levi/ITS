"""Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a 
seconda del parametro to_fahrenheit. 
Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit."""

def convert_temperature(temperatura:float, to_fahrenheit:bool=True) -> float:
    if to_fahrenheit:
        return (temperatura * 9/5)+32
    else:
        return (temperatura - 32)*5/9