def get_input_yield():
    with open("./inputs/day2.txt") as f:
        lines = f.read().splitlines()

    for line in lines:
        yield [int(x) for x in line.split()]


def part_1():
    total = 0

    for report in get_input_yield():
        if report[0] > report[1]:
            comparison = lambda a, b: a > b
        else:
            comparison = lambda a, b: a < b

        for i in range(0, len(report) - 1):
            if comparison(report[i], report[i + 1]) and (1 <= abs(report[i + 1] - report[i]) <= 3):
                if i == len(report) - 2:
                    total += 1
            else:
                break

    print(total)


def is_safe(report):
    size = len(report)
    for i in range(size - 1):
        diff = report[i + 1] - report[i]
        if not (1 <= abs(diff) <= 3):
            return False
        if not (report[0] < report[1] and report[i] < report[i + 1]) and not (
                report[0] > report[1] and report[i] > report[i + 1]):
            return False
    return True


def part_2():
    total = 0
    for report in get_input_yield():
        if is_safe(report):
            total += 1
            continue

        safe_with_removal = False
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                safe_with_removal = True
                break

        if safe_with_removal:
            total += 1

    print(total)


if __name__ == "__main__":
    part_1()
    part_2()
