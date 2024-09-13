from math import floor


def get_info():
    with open("inputs/day1.txt") as f:
        return f.readlines()


def part_1():
    data = get_info()
    total = sum([floor(int(n) / 3) - 2 for n in data])

    print(total)


def get_fuel(mass):
    mass = max(floor(mass / 3) - 2, 0)
    return mass + get_fuel(mass) if mass else mass


def part_2():
    data = get_info()
    total = sum([get_fuel(int(n)) for n in data])

    print(total)


part_2()
