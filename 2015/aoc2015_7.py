addresses = {}


def get_input():
    with open("./inputs/day7.txt") as f:
        return f.read().splitlines()


def bitwise_not(n, nbits=16):
    return ((1 << nbits) - 1) ^ n


def compute(addr):
    if addr.isdigit():
        return int(addr)

    if isinstance(addresses[addr], int):
        return addresses[addr]

    command = addresses[addr]

    if isinstance(command, list):
        match command:
            case [x]:
                addresses[addr] = compute(x)
            case [x, "AND", y]:
                addresses[addr] = compute(x) & compute(y)
            case [x, "OR", y]:
                addresses[addr] = compute(x) | compute(y)
            case ["NOT", x]:
                addresses[addr] = bitwise_not(compute(x))
            case [x, "LSHIFT", amount]:
                addresses[addr] = compute(x) << int(amount)
            case [x, "RSHIFT", amount]:
                addresses[addr] = compute(x) >> int(amount)

    return addresses[addr]


def part_1():
    lines = get_input()

    for line in lines:
        command, addr = line.split(" -> ")
        command = command.split(" ")
        if addr in addresses:
            raise ValueError(f"Duplicate address: {addr}")
        addresses[addr] = command

    print("a:", compute('a'))

def part_2():
    lines = get_input()

    for line in lines:
        command, addr = line.split(" -> ")
        command = command.split(" ")
        if addr in addresses:
            raise ValueError(f"Duplicate address: {addr}")
        addresses[addr] = command
    addresses['b'] = 16076
    print("a:", compute('a'))

part_2()
