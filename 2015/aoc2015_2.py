def get_input():
    with open("inputs/day2.txt") as f:
        return f.readlines()


def part_1():
    data = sum([2*sum(x)+min(x) for x in map(lambda s: (s[0] * s[1], s[1] * s[2], s[2] * s[0]),
                                             [list(map(int, x.strip().split("x"))) for x in get_input()])])
    print(data)


def part_2():
    data = sum([sum(x) for x in map(lambda s: (s[0] * s[1] * s[2], 2 * sum(sorted(s)[:2])),
                                                 [list(map(int, x.strip().split("x"))) for x in get_input()])])
    print(data)


part_2()
