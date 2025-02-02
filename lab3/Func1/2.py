def toCelsius(Fahrenheit ):
    C = (5 / 9) * (Fahrenheit - 32)
    return C
Fahrenheit = int(input("Fahrenheit: "))
print(toCelsius(Fahrenheit))