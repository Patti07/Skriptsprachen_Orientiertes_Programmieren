import re

strings = [
    "Python",
    "#Ich bin #cool",
    "Python 15-.10.21 test 192.168.0.1 hallo",
    "Python 15.10.21 test 192.168.0.1 # + 6& hallo",
    "Python 15-.10.21 test 192.168.0.1 hallo",
    "Python 15.10.21 test 192.168.0.1 hallo",
    "a/5",
    "Das sind meine Daten: 11.04.2012, 03.02.20212, 01.02.12",
    "Das ist meine gültige Email: hanspeter.ulrich@hotmail.com",
    "Die negative Zahl lautet: -33.7689",
    "Python 15-.10.21 *0201/87543* test 192.168.0.1 hallo"
]

muster = [
    "^[p,P]ython",
    "#.*",
    "\d|\+|-",
    "[^a-zA-Z]",
    "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",
    "(\d{1,3}\.){3}\d{1,3}",
    "^...$",
    "(\d{1,2}\.){2}\d{1,4}.*",
    "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
    "-\d+\.\d{4}",
    "\*\d{3,6}/\d+\*"
]

count = 0

for s, m in zip(strings, muster):
    count += 1
    print("\nAufgabe " + str(count))
    print("String: " + s + "\nSuchmuster: " + m)
    result = re.search(m, s)
    if result:
        res = result.group()
        print("gefunden!\nErgebnisstring: " + res)
    else:
        print("nicht gefunden!")
