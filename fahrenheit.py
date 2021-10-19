celsius = float(input("Gib eine Temperatur in Celsius an: "))


def fahrenheit(celsius):
    return (celsius * 1.8) + 32


result = fahrenheit(celsius)
print("Das Ergebnis lautet: " + str(result))
print("Das Ergebnis lautet: %.2f" % result)
