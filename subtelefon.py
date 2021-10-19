import re


def read_file():
    f = open("files\\produkte2.txt", "r")
    lines = f.read().split("\n")
    f.close()
    return lines


def find_and_replace_number(lines):
    sub = []
    for line in lines:
        result = re.sub("\d+/\d+\s+", "xxxx/xxxx ", line)
        if result:
            print("gefunden!\nResult: " + result)
            sub.append(result)
        else:
            print("nicht gefunden!")
    return sub


def write_file(sub):
    f = open("files\\telefon_sub.txt", "w")
    for line in sub:
        print(str(line))
        f.write(str(line) + "\n")
    f.close()


lines = read_file()
sub = find_and_replace_number(lines)
write_file(sub)
