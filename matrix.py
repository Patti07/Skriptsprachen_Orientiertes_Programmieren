array = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]


def print_matrix(array):
    for i in range(len(array)):
        print(array[i])
    print()

    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=' ')
        print()


print_matrix(array)