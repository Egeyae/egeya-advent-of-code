SCREEN_SIZE = (50, 6)


def get_lines():
    with open("inputs/day8.txt") as f:
        return [l.strip() for l in f.readlines()]


def get_screen():
    return [
        [0 for _ in range(SCREEN_SIZE[0])] for _ in range(SCREEN_SIZE[1])
    ]


def show(screen):
    for row in screen:
        print("".join(["#" if row[i] == 1 else "." for i in range(SCREEN_SIZE[0])]))


def rect(screen, x, y):
    for xi in range(x):
        for yi in range(y):
            screen[yi][xi] = 1
    return screen


def down1(screen, x):
    nscreen = [
        screen[x].copy() for x in range(SCREEN_SIZE[1])
    ]

    for yi in range(SCREEN_SIZE[1] - 1, -1, -1):
        if screen[yi][x] == 1:
            nscreen[yi][x] = 0
            i = yi + 1
            if i >= SCREEN_SIZE[1]:
                i = 0
            nscreen[i][x] = 1

    return nscreen


def downx(screen, x, amount):
    for _ in range(amount):
        screen = down1(screen, x)
    return screen


def shift1(screen, y):
    nscreen = [
        screen[x].copy() for x in range(SCREEN_SIZE[1])
    ]

    for xi in range(SCREEN_SIZE[0] - 1, -1, -1):
        if screen[y][xi] == 1:
            nscreen[y][xi] = 0
            i = xi + 1
            if i >= SCREEN_SIZE[0]:
                i = 0
            nscreen[y][i] = 1

    return nscreen


def shiftx(screen, y, amount):
    for _ in range(amount):
        screen = shift1(screen, y)
    return screen


def parse_line_and_exec(line, screen):
    if line.startswith("rect"):
        dims = line.split(" ")[1].split("x")
        return rect(screen, int(dims[0]), int(dims[1]))
    elif line.startswith("rotate"):
        line = line[6:].strip()
        if line.startswith("column"):
            func = downx
        elif line.startswith("row"):
            func = shiftx
        else:
            raise ValueError("Unrecognized parameter")

        line = line.split("=")[1]
        line = line.split(" by ")

        x_or_y = int(line[0])
        amount = int(line[1])

        return func(screen, x_or_y, amount)
    else:
        raise ValueError("Unrecognized command")


def count_pixels(screen):
    count = 0
    for row in screen:
        for pixel in row:
            if pixel == 1:
                count += 1
    return count


def part_1():
    lines = get_lines()
    screen = get_screen()
    for line in lines:
        screen = parse_line_and_exec(line, screen)
    show(screen)
    print("Total pixels:", count_pixels(screen))


part_1()
