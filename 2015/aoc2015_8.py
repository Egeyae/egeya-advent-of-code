def get_input():
    with open('inputs/day8.txt') as f:
        return f.read().splitlines()


def part_1():
    data = get_input()
    total = 0

    for line in data:
        total += len(line)
        total -= len(bytes(line[1:-1], encoding='utf-8').decode('unicode_escape'))

    print(total)

def part_2():
    data = get_input()
    total = 0

    for line in data:
        total -= len(line)
        line2 = '"'
        for char in line:
            match char:
                case '"':
                    line2 += r'\"'
                case '\\':
                    line2 += r'\\'
                case _:
                    line2 += char
        line2 += '"'
        total += len(line2)

    print(total)
part_2()