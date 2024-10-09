def get_input():
    with open("inputs/day6.txt") as f:
        return f.read().replace(",", " ").split("\n")  # removes \n and splits the coords for later use

def part_1():
    WIDTH, HEIGHT = 1000, 1000
    led_matrix = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for command in get_input():
        parts = command.split()

        match parts:
            case ["turn", "on", x1, y1, "through", x2, y2]:
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        led_matrix[x][y] = True

            case ["turn", "off", x1, y1, "through", x2, y2]:
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        led_matrix[x][y] = False

            case ["toggle", x1, y1, "through", x2, y2]:
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        led_matrix[x][y] = not led_matrix[x][y]

    count = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if led_matrix[x][y]:
                count += 1
    print(count)


def part_2():
    WIDTH, HEIGHT = 1000, 1000
    led_matrix = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for command in get_input():
        parts = command.split()

        match parts:
            case ["turn", "on", x1, y1, "through", x2, y2]:
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        led_matrix[x][y] += 1

            case ["turn", "off", x1, y1, "through", x2, y2]:
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        led_matrix[x][y] = max(led_matrix[x][y]-1, 0)

            case ["toggle", x1, y1, "through", x2, y2]:
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        led_matrix[x][y] += 2

    count = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            count += led_matrix[x][y]
    print(count)
part_2()
