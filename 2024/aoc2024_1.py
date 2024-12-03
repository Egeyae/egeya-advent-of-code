from itertools import count


def get_input_lists():
    with open("./inputs/day1.txt") as f:
        data = f.read().splitlines()

    col_to_list = lambda lines, col: [int(x.split()[col]) for x in lines]

    return col_to_list(data, 0), col_to_list(data, 1)

def part_1():
    list1, list2 = get_input_lists()
    list1, list2 = sorted(list1), sorted(list2)

    dist = 0
    for i in range(len(list1)):
        dist += abs(list1[i] - list2[i])

    print("Total distance:", dist)

def part_2():
    list1, list2 = get_input_lists()
    list1, list2 = sorted(list1), sorted(list2)

    similarity = 0
    for i in range(len(list1)):
        similarity += list1[i] * list2.count(list1[i])

    print("Total similarity:", similarity)

if __name__ == "__main__":
    part_1()
    part_2()