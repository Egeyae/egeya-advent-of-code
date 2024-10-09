def get_input():
    with open("inputs/day5.txt") as f:
        return f.read().split("\n")


def check_nice1(s):
    vowels = ("a", "e", "i", "o", "u")
    bad_strings = ("ab", "cd", "pq", "xy")

    vowel, double = 1 if s[0] in vowels else 0, 0

    for i in range(1, len(s)):
        if s[i-2:i] in bad_strings:
            return False

        if s[i] in vowels:
            vowel += 1
        if s[i-1] == s[i]:
            double += 1
    if vowel >= 3 and double:
        return True
    return False

def part_1():
    data = get_input()
    count = 0
    for l in data:
        if check_nice1(l):
            count += 1

    print(count-1)

def check_nice2(s):
    pair_nooverlap = False
    for i in range(len(s) - 1):
        pattern = s[i:i + 2]
        if pattern in s[i + 2:]:
            pair_nooverlap = True
            break

    mirror = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            mirror = True
            break

    return pair_nooverlap and mirror

def part_2():
    data = get_input()
    count = 0
    for l in data:
        if check_nice2(l):
            count += 1

    print(count)

part_2()