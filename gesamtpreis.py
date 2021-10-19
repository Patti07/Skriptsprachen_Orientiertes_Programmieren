import re


def read_file():
    f = open("files\\produkte.txt", "r")
    lines = f.read().split("\n")
    f.close()
    return lines


def find_price_and_amount(lines):
    gesamtpreis = 0.0
    for line in lines:
        result = re.search("(\d+).*:\s(\d+\.\d+)", line)
        if result:
            amount = result.group(1)
            price = result.group(2)
            print("gefunden!\nPrice: " + price + "\nAmount: " + amount)
            tmp = int(amount) * float(price)
            gesamtpreis += tmp
        else:
            print("nicht gefunden!")
    return gesamtpreis

lines = read_file()
gesamtpreis = find_price_and_amount(lines)
print("Der Geamtpreis beträgt: " + str(gesamtpreis))
