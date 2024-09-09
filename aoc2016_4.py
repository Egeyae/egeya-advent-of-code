from string import ascii_lowercase


def get_input():
    with open("inputs/day4.txt") as f:
        lines = f.readlines()

    to_return = []
    for line in lines:
        line = line.strip().split("[")
        check = line[1][:-1]

        line = line[0].split("-")
        rid = int(line[-1])

        letters = " ".join(line[:-1])
        to_return.append([letters, check, rid])

    return to_return


def get_letters(letters):
    to_return = {}
    for l in letters:
        if l == " ":
            continue
        if l in to_return:
            to_return[l] += 1
        else:
            to_return[l] = 1

    return to_return.items()


def sort_letters(lettersitems):
    sli = sorted(lettersitems, key=lambda x: x[0])
    return sorted(sli, key=lambda x: x[1], reverse=True)


def compare_check_letters(check, letters):
    for c in check:
        if not c in letters:
            return False
    return True


def part_1():
    in_ = get_input()

    s = 0
    for line in in_:
        l = sort_letters(get_letters(line[0]))
        l = [x[0] for x in l[:5]]

        if compare_check_letters(line[1], l):
            s += line[2]
    print("Total sum:", s)


def convert(line, shift):
    to_return = ""
    for c in line:
        if c == " ":
            to_return += " "
        else:
            to_return += ascii_lowercase[(ascii_lowercase.index(c) + shift) % len(ascii_lowercase)]
    return to_return


def part_2():
    in_ = get_input()

    s = 0
    for line in in_:
        l = sort_letters(get_letters(line[0]))
        l = [x[0] for x in l[:5]]

        if compare_check_letters(line[1], l):
            str_ = convert(line[0], line[2])
            print(str_)
            if "northpole" in str_:
                s = line[2]
                break
    print("Total sum:", s)


part_2()
