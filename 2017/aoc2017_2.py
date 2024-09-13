def get_input():
    with open('inputs/day2.txt') as f:
        return f.readlines()


def part_1():
    data = get_input()
    total = 0

    for line in data:
        total += max([int(x) for x in line.strip().split()]) - min([int(x) for x in line.strip().split()])

    print(total)


def part_2():
    data = get_input()
    total = 0

    for line in data:
        line = sorted([int(x) for x in line.strip().split()], reverse=True)
        f = False
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if line[i] % line[j] == 0:

                    total += line[i] // line[j]
                    f = True
                    break
            if f:
                break

    print(total)


part_2()