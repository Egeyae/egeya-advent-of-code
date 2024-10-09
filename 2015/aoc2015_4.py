from hashlib import md5


def get_input():
    with open("inputs/day4.txt") as f:
        return f.read().strip()


def part_1():
    prefix = get_input()

    i = 0
    hashhex = ""
    while not hashhex.startswith("0"*5):
        i += 1
        word = prefix + str(i)
        hashhex = md5(word.encode("utf-8")).hexdigest()


    print(i)


def part_2():
    prefix = get_input()

    i = 0
    hashhex = ""
    while not hashhex.startswith("0"*6):
        i += 1
        word = prefix + str(i)
        hashhex = md5(word.encode("utf-8")).hexdigest()


    print(i)

part_2()