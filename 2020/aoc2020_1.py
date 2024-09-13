def get_input():
    with open("inputs/day1.txt") as f:
        return f.readlines()


def part_1():
    data = sorted(map(int, get_input()), reverse=True)
    for i in range(len(data)):
        for j in range(len(data) - 1, i, -1):
            if data[i] + data[j] == 2020:
                print(data[i] * data[j])
                return


def part_2():
    data = sorted(map(int, get_input()), reverse=True)
    for i in range(len(data)):
        for j in range(i, len(data)):
            for k in range(j, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    print(data[i] * data[j] * data[k])
                    return


part_2()
