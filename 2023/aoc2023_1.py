def get_input():
    with open("inputs/day1.txt") as f:
        return f.readlines()


def part_1():
    data = get_input()
    total = 0

    for line in data:
        line = line.strip()
        a, b = None, None
        for i in range(len(line)):
            if not a and line[i].isdigit():
                a = line[i]
            if not b and line[-(i + 1)].isdigit():
                b = line[-(i + 1)]

            if a and b:
                break

        total += int(a + b)

    print(total)


def find_all_nums(s):
    valid_nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    nums = []

    for i in range(len(s)):
        if s[i].isdigit():
            nums.append(s[i])
        else:
            for n in valid_nums.keys():
                if s[i:].startswith(n):
                    nums.append(valid_nums[n])

    return nums


def part_2():
    data = get_input()
    total = 0

    for line in data:
        line = find_all_nums(line.strip())
        total += int(line[0] + line[-1])

    print(total)


part_2()
