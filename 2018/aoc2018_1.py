def get_input():
    with open("inputs/day1.txt") as f:
        return f.readlines()


def part_1():
    data = get_input()
    freq = 0

    for line in data:
        freq += int(line.strip())

    print(freq)


def part_2():
    data = get_input()
    freq = 0
    frequencies = []
    result = None

    while result is None:
        for line in data:
            freq += int(line.strip())
            if freq in frequencies:
                result = freq
                break
            else:
                frequencies.append(freq)

    print(result)


part_2()
