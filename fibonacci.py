eingabe = int(input("Bitte geben Sie eine Zahl ein: "))

def fibonacci(eingabe):
    f = 0
    s = 1
    count = 0

    if eingabe < 0:
        print("Bitte gebe eine positize zahl ein!")
    elif eingabe == 0:
        print("fibonacci Folge bis " + str(eingabe))
        print(f)
    elif eingabe == 1:
        print("fibonacci Folge bis " + str(eingabe))
        print(s)
    else:
        print("fibonacci Folge bis " + str(eingabe + 1))
        while count <= eingabe:
            print("Element: ", count, " : ", f)
            tmp = f + s
            f = s
            s = tmp
            count += 1


fibonacci(eingabe)

def rekursion(eingabe):
    if eingabe == 0:
        return 0
    elif eingabe == 1:
        return 1
    else:
        return rekursion(eingabe - 1) + rekursion(eingabe - 2)


for i in range(0,eingabe):
    rek = rekursion(eingabe)
    print(str(rek))

