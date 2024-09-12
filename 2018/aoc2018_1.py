def get_input():
    with open("inputs/day1.txt") as f:
        return f.readlines()

def part_1():
    data = get_input()
    freq = 0

    for line in data:
        freq += int(line.strip())
    
    print(freq)

part_1()