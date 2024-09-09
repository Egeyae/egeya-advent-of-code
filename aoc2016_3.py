def get_input():
    with open("inputs/day3.txt") as f:
        in_ = f.readlines()
    to_return = []
    for l in in_:
        x = l.strip().split(" ")
        to_return.append([])
        for j in x:
            if j:
                to_return[-1].append(int(j))

    return to_return


def get_input_2():
    in_ = get_input()

    to_return = []

    for i in range(0, len(in_), 3):
        for k in range(3):
            to_return.append([])
            for j in range(3):
                to_return[-1].append(in_[i + j][k])
    print(to_return)
    return to_return


def part_1():
    input_ = get_input()
    poss = 0

    for t in input_:
        maxi = t.index(max(t))
        s = 0
        for i in range(3):
            if maxi != i:
                s += t[i]
        if t[maxi] < s:
            poss += 1

    print(f"Total = {poss}")


def part_2():
    input_ = get_input_2()
    poss = 0

    for t in input_:
        maxi = t.index(max(t))
        s = 0
        for i in range(3):
            if maxi != i:
                s += t[i]
        if t[maxi] < s:
            poss += 1

    print(f"Total = {poss}")


part_2()
