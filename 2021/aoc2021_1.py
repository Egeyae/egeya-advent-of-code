def get_input():
    with open('inputs/day1.txt') as f:
        return f.readlines()


def part_1():
    data = list(map(int, get_input()))
    total = 0

    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            total += 1

    print(total)


def part_2():
    data = list(map(int, get_input()))
    total = 0

    for i in range(len(data) - 3):
        if sum(data[i:i + 3]) < sum(data[i + 1:i + 4]):
            total += 1

    print(total)


part_2()
