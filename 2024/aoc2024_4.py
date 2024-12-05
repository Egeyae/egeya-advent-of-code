import re
from _ast import pattern


def get_input():
    with open('./inputs/day4.txt') as f:
        return f.read().splitlines()


def get_normal_strings(lines):
    return "|".join(lines)

def get_vertical_strings(lines):
    new_lines = ["" for _ in range(len(lines[0]))]
    for line in lines:
        for c in range(len(line)):
            new_lines[c] += line[c]

    return get_normal_strings(new_lines)

def get_diagonals(lines):
    rows = len(lines)
    cols = len(lines[0])

    diagonals_bl_tr = ["" for _ in range(rows + cols - 1)]
    for r in range(rows):
        for c in range(cols):
            diagonals_bl_tr[r + c] += lines[r][c]

    diagonals_tl_br = ["" for _ in range(rows + cols - 1)]
    for r in range(rows):
        for c in range(cols):
            diagonals_tl_br[c - r + (rows - 1)] += lines[r][c]

    return diagonals_bl_tr, diagonals_tl_br

def get_diagonal_strings(lines):
    diagonals_bl_tr, diagonals_tl_br = get_diagonals(lines)
    return "|".join([get_normal_strings(diagonals_bl_tr), get_normal_strings(diagonals_tl_br)])

def part_1():
    data = get_input()

    all_data = "|".join([get_normal_strings(data), get_vertical_strings(data), get_diagonal_strings(data)])
    all_data += "|" + all_data[::-1]

    pat = r"XMAS"
    print(len(re.findall(pat, all_data)))


def find_As(line):
    pat = r"A"
    return [m.start() for m in re.finditer(pat, line)]


def check_cross(data, row, column):
    if (row < 1 or row > len(data)-2) or (column < 1 or column > len(data[row])-2):
        return False # No cross as it is not possible

    lines = [
        data[row-1][column-1:column+2],
        data[row][column-1:column+2],
        data[row+1][column-1:column+2],
    ]
    bl_tr, tl_br = get_diagonals(lines)
    bl_tr = bl_tr[2]
    tl_br = tl_br[2]

    pat = r"MAS"
    bl_tr += "|" + bl_tr[::-1]
    tl_br += "|" + tl_br[::-1]

    if re.search(pat, bl_tr) and re.search(pat, tl_br):
        return True
    else:
        return False


def part_2():
    data = get_input()

    a_pos = []
    for line in data:
        a_pos.append(find_As(line))
    total = 0
    for row in range(len(data)):
        for column in a_pos[row]:
            if check_cross(data, row, column):
                total += 1
    print(total)


if __name__ == '__main__':
    part_1()
    part_2()