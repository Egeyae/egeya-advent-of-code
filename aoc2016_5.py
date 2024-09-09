import hashlib

def get_input():
    with open("inputs/day5.txt") as f:
        return f.read().strip()

def part_1():
    in_ = get_input()

    password = ""

    x = 0
    while len(password) < 8:
        s = in_+str(x)
        hash_hex = hashlib.md5(s.encode()).hexdigest()
        if hash_hex.startswith("00000"):
            password += hash_hex[5]
        x += 1

    print(password)

def part_2():
    in_ = get_input()

    password = [None for _ in range(8)]

    x = 0
    count = 0
    while count < 8:
        s = in_+str(x)
        hash_hex = hashlib.md5(s.encode()).hexdigest()
        if hash_hex.startswith("00000"):
            if hash_hex[5].isnumeric() and hash_hex[5] != "9" and hash_hex[5] != "8" and not password[int(hash_hex[5])]:
                print(hash_hex)
                password[int(hash_hex[5])] = hash_hex[6]
                count+=1
        x += 1

    print("".join([str(x) for x in password]))

part_1()