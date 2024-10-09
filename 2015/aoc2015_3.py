def get_input():
    with open("./inputs/day3.txt") as f:
        return f.readline().strip()

def part_1():
    data = get_input()
    x, y = 0, 0
    visited = {(0, 0)}

    for c in data:
        match c:
            case ">":
                x += 1
            case "v":
                y += 1
            case "<":
                x -= 1
            case "^":
                y -= 1

        visited.add((x, y))

    print(len(visited))


def part_2():
    data = get_input()
    x, y = 0, 0
    x2, y2 = 0, 0

    set_santa = {(0, 0)}
    set_robot = {(0, 0)}

    for i in range(len(data)):
        if i % 2 == 0:
            match data[i]:
                case ">":
                    x += 1
                case "<":
                    x -= 1
                case "^":
                    y -= 1
                case "v":
                    y += 1
            set_santa.add((x, y))
        else:
            match data[i]:
                case ">":
                    x2 += 1
                case "<":
                    x2 -= 1
                case "^":
                    y2 -= 1
                case "v":
                    y2 += 1
            set_robot.add((x2, y2))

    total_visited = set()
    total_visited.update(set_santa)
    total_visited.update(set_robot)

    print(len(total_visited))

part_2()