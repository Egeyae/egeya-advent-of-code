def get_input():
    with open("inputs/day2.txt") as f:
        in_ = f.readlines()
    return in_


def process_command(l, x, y):
    if l == "U":
        y -= 1
    elif l == "D":
        y += 1
    elif l == "R":
        x += 1
    elif l == "L":
        x -= 1
    else:
        raise Exception(f"Wrong input: {l}")

    return x, y


def process_line(line, x, y):
    for char in line.strip():
        # print(char, end=" ")
        x, y = process_command(char, x, y)

        x = max(min(x, 2), 0)
        y = max(min(y, 2), 0)
        # print(x, y, end=" || ")
    # print()
    return x, y


def get_num(x, y):
    nums = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    return nums[y][x]


def part_1():
    in_ = get_input()
    x, y = 1, 1
    password = ""

    for l in in_:
        x, y = process_line(l, x, y)
        password += str(get_num(x, y))

    print(f"The password is: {password}")


def part_2():
    in_ = get_input()
    keypad = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, "A", "B", "C", 0],
        [0, 0, "D", 0, 0]
    ]

    x, y = 0, 2
    password = ""
    for line in in_:
        for char in line.strip():
            nx, ny = process_command(char, x, y)
            nx = max(min(nx, 4), 0)
            ny = max(min(ny, 4), 0)

            if keypad[ny][nx] != 0:
                x, y = nx, ny
        password += str(keypad[y][x])

    print(f"The password is: {password}")


part_2()
