def get_input():
    with open("inputs/day1.txt") as f:
        return f.readline().strip()


def part_1():
    data = get_input()
    total = 0

    for i in range(len(data)):
        j = (i + 1) % len(data)

        if data[i] == data[j]:
            total += int(data[i])

    print(total)


def part_2():
    data = get_input()
    total = 0
    shift = len(data) // 2

    for i in range(len(data)):
        j = (i + shift) % len(data)

        if data[i] == data[j]:
            total += int(data[i])

    print(total)


part_2()
