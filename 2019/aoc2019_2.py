def get_input():
    with open("inputs/day2.txt") as f:
        return list(map(int, f.readline().split(",")))


def part_1():
    data = get_input()
    i = 0
    while True:
        match data[i]:
            case 99:
                break
            case 1:
                data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            case 2:
                data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            case _:
                raise ValueError(f"Unexpected input: {data[i]}")

        i += 4

    print(data[0])


def part_2():
    data = get_input()
    search = 19690720

    for noun in range(100):
        for verb in range(100):
            print(noun, verb)
            data_copy = data.copy()
            data_copy[1] = noun
            data_copy[2] = verb
            i = 0

            while True:
                match data_copy[i]:
                    case 99:
                        break
                    case 1:
                        data_copy[data_copy[i+3]] = data_copy[data_copy[i+1]] + data_copy[data_copy[i+2]]
                    case 2:
                        data_copy[data_copy[i+3]] = data_copy[data_copy[i+1]] * data_copy[data_copy[i+2]]
                    case _:
                        raise ValueError(f"Unexpected input: {data_copy[i]}")

                i += 4

            if data_copy[0] == search:
                print(100*noun + verb)
                return


part_2()
