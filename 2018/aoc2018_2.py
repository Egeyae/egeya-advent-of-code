def get_input():
    with open("inputs/day2.txt") as f:
        return f.readlines()


def get_letters(line):
    letters = {}
    for c in line:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    return letters


def count(n2, n3, line):
    letters = get_letters(line)

    if 3 in letters.values():
        n3 += 1
    if 2 in letters.values():
        n2 += 1

    return n2, n3


def part_1():
    data = get_input()
    n2, n3 = 0, 0

    for line in data:
        n2, n3 = count(n2, n3, line)

    print(n2 * n3)


def compare(a, b):
    c = 0

    for i in range(len(a)):
        if a[i] != b[i] and c:
            return False
        elif a[i] != b[i]:
            c = 1

    if c:
        return True
    return False


def common(a, b):
    c = []
    for i in range(len(a)):
        if a[i] == b[i]:
            c.append(a[i])

    return c

def part_2():
    data = [x.strip() for x in get_input()]

    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            if compare(data[i], data[j]):
                print("".join(common(data[i], data[j])))
                return


part_2()
