try:
    1 / 0
except ZeroDivisionError as err:
    print("Zero Division error: {0}".format(err))
except ValueError as v:
    print("Wrong value:" + v)

