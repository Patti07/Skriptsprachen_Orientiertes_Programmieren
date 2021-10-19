operator = 0

while operator <= 0 or operator > 4:
    operator = int(input("Bitte geben Sie eine Zahl von 1 bis 4 an: "))

    if operator > 4 or operator < 1:
        print("Zahl muss zwischen 1 und 4 sein!")

zahl1 = float(input("Bitte geben Sie eine Zahl ein: "))
zahl2 = float(input("Bitte geben Sie eine zweite Zahl ein: "))


def addition(zahl1, zahl2):
    return zahl1 + zahl2


def subtraktion(zahl1, zahl2):
    return zahl1 - zahl2


def multiplikation(zahl1, zahl2):
    return zahl1 * zahl2


def division(zahl1, zahl2):
    return zahl1 / zahl2


switch_with_dictionary = {
    1: addition(zahl1, zahl2),
    2: subtraktion(zahl1, zahl2),
    3: multiplikation(zahl1, zahl2),
    4: division(zahl1, zahl2)
}

print(switch_with_dictionary.get(operator))