def get_input():
    with open("inputs/day1.txt") as f:
        return f.readline().strip()


def part_1():
    floor = 0
    data = get_input()

    for c in data:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1

    print(floor)


def part_2():
    floor = 0
    data = get_input()

    for c in range(len(data)):
        if data[c] == "(":
            floor += 1
        elif data[c] == ")":
            floor -= 1

        if floor == -1:
            break

    print(c + 1)


part_2()
