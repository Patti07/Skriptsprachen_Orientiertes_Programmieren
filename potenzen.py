import math
from math import sqrt as wurzel, pow as potenz


def function_wurzel():
    for i in range(1, 11):
        print("Das ist komplett math: " + str(math.sqrt(i)))
        print("Das ist nur mit sqrt Funktion: " + str(wurzel(i)))


def function_potenzen():
    for i in range(10, 110, 10):
        print("Das ist komplett math: " + str(math.pow(i, 2)))
        print("Das ist nur die potenz Funktion: " + str(potenz(i, 2)))


function_potenzen()
function_wurzel()




