def get_input():
    with open("inputs/day2.txt") as f:
        return [x.strip().replace("-", " ").replace(":", " ") for x in f.readlines()]


def count(s, letter):
    total = 0
    for c in s:
        if c == letter:
            total += 1
    return total


def part_1():
    data = get_input()
    total = 0
    for line in data:
        match line.split():
            case mx, mn, l, s:
                if int(mn) >= count(s, l) >= int(mx):
                    total += 1

    print(total)


def is_valid(pos0, pos1, letter, s):
    if s[pos0] != s[pos1] and (s[pos0] == letter or s[pos1] == letter):
        return True
    return False


def part_2():
    data = get_input()
    total = 0
    for line in data:
        match line.split():
            case mx, mn, l, s:
                if is_valid(int(mx) - 1, int(mn) - 1, l, s):
                    total += 1

    print(total)


part_2()
