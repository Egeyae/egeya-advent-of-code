def get_input():
    with open("inputs/day6.txt") as f:
        in_ = f.readlines()
    size = len(in_[0].strip())
    l = [[] for _ in range(size)]

    for line in in_:
        line=line.strip()
        for i in range(size):
            l[i].append(line[i])
    
    return l

def count_letters(col):
    to_return = {}
    for c in col:
        if c in to_return:
            to_return[c] += 1
        else:
            to_return[c] = 1
    return to_return.items()

def part_1():
    in_ = get_input()

    message = ""

    for col in in_:
        letters = count_letters(col)
        max_letter = sorted(letters, key=lambda x: x[1], reverse=True)[0][0]
        message += max_letter
    
    print(message)

def part_2():
    in_ = get_input()

    message = ""

    for col in in_:
        letters = count_letters(col)
        max_letter = sorted(letters, key=lambda x: x[1])[0][0]
        message += max_letter
    
    print(message)

part_2()