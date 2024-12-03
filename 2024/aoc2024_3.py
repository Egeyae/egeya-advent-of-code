import re


def get_input():
    with open("./inputs/day3.txt") as f:
        data = f.read()
    return data


def part_1():
    data = get_input()

    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total = 0

    all_patterns = re.findall(mul_pattern, data)
    for pattern in all_patterns:
        total += int(pattern[0]) * int(pattern[1])
    print(total)


def find_start_pattern(pattern, text):
    return [(m.start(), pattern) for m in re.finditer(pattern, text)]


def part_2():
    data = get_input()
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    do_starts = find_start_pattern(do_pattern, data)
    dont_starts = find_start_pattern(dont_pattern, data)

    all_starts = sorted(do_starts + dont_starts, key=lambda x: x[0])
    if all_starts[-1][1] == do_pattern:
        all_starts.append((len(data), dont_pattern))
    do = True
    last_index = 0
    new_text = ""

    for idx, pattern in all_starts:
        if do and pattern == dont_pattern:
            do = False
            new_text += data[last_index:idx]
            last_index = idx
        elif not do and pattern == do_pattern:
            do = True
            last_index = idx

    total = 0

    all_patterns = re.findall(mul_pattern, new_text)
    for pattern in all_patterns:
        total += int(pattern[0]) * int(pattern[1])
    print(total)


if __name__ == "__main__":
    part_1()
    part_2()
