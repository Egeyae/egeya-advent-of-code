def sep_brackets(line):
    inside = []
    out = [""]
    b = False
    for c in line:
        if c == '[':
            b = True
            inside.append("")
        elif c == ']':
            b = False
            out.append("")
        elif b:
            inside[-1] += c
        else:
            out[-1] += c

    return out, inside


def get_input():
    with open("inputs/day7.txt") as f:
        lines = f.readlines()

    for l in lines:
        yield sep_brackets(l.strip())


def has_abba(s):
    for i in range(len(s) - 3):
        if s[i] != s[i + 1]:
            s1 = s[i] + s[i + 1]
            s2 = s[i + 2] + s[i + 3]

            if s1[::-1] == s2:
                return True
    return False


def part_1():
    count = 0

    for outside, in_ in get_input():
        if any(has_abba(o) for o in outside) and not any(has_abba(i) for i in in_):
            count += 1
    print("Total IPS with TLS:", count)


def has_aba(s):
    a = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] and s[i] != s[i + 1]:
            a.append([s[i], s[i + 1]])
    if a:
        return a
    else:
        return False


def has_bab(s, bab_seq):
    for i in range(len(s) - 2):
        for seq in bab_seq:
            if s[i] == seq[1] and s[i + 2] == seq[1]:
                if s[i + 1] == seq[0]:
                    return True
    return False


def part_2():
    count = 0

    for outside, in_ in get_input():

        all_aba = []
        for o in outside:
            r = has_aba(o)
            if r:
                for seq in r:
                    all_aba.append(seq)
        for i in in_:
            if has_bab(i, all_aba):
                count += 1
                break
    print("Total IPS with SSL:", count)


part_2()
