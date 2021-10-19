def read_file():
    f = open("files\\zahlen.txt", "r")
    lines = f.read().split("\n")
    f.close()
    return lines


def write_file(lines):
    f = open("files\\zahlen2.txt", "w")
    for line in lines:
        print(str(float(line)))
        f.write(str(float(line)) + "\n")
    f.close()


lines = read_file()
write_file(lines)



