import re
from unittest import case

SYMBOLS = [
    "^",
    ">",
    ",",
    "<"
]

def get_input():
    with open("./inputs/day6.txt") as f:
        return f.read().splitlines()

def find_starting_pos(lines):
    y = 0
    while y < len(lines):
        x = 0
        while x < len(lines[y]):
            if lines[y][x] in SYMBOLS:
                return x, y, lines[y][x]
            x += 1
        y += 1
    return None, None

def next_step(symbol, x, y):
    match symbol:
        case "^":
            return x, y - 1
        case ">":
            return x + 1, y
        case ",":
            return x, y + 1
        case "<":
            return x - 1, y
        case _:
            raise ValueError("Invalid symbol")

def move(lines):
    x, y, s = find_starting_pos(lines)
    x2, y2 = next_step(s, x, y)

    if x2 < 0 or x2 >= len(lines[0]):
        return None, None
    if y2 < 0 or y2 >= len(lines):
        return None, None

    match lines[y2][x2]:
        case "#":
            lines[y] = lines[y][:x] + SYMBOLS[(SYMBOLS.index(lines[y][x]) + 1) % len(SYMBOLS)]  + lines[y][x+1:]
            return x, y
        case _:
            lines[y] = lines[y][:x] + "X" + lines[y][x+1:]
            lines[y2] = lines[y2][:x2] + s + lines[y2][x2+1:]
            return x2, y2

def get_all_unique_pos():
    data = get_input()
    all_pos = set()
    x, y, _ = find_starting_pos(data)
    while x is not None and y is not None:
        all_pos.add((x, y))
        # for l in data:
        #    print(l)
        # print()
        x, y = move(data)
    return all_pos


def part_1():
    all_pos = get_all_unique_pos()
    print(len(all_pos))

if __name__ == "__main__":
    part_1()