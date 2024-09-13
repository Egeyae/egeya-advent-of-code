def get_input():
    with open("inputs/day1.txt") as f:
        return f.read().split("\n\n")


def part_1():
    data = [sum(map(int, x.strip().split("\n"))) for x in get_input()]
    print(max(data))


def part_2():
    data = [sum(map(int, x.strip().split("\n"))) for x in get_input()]
    print(sum(sorted(data, reverse=True)[:3]))


part_2()
