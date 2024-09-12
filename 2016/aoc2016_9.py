def get_input():
    with open("inputs/day9.txt") as f:
        return f.readline().strip()
    
def decompress(file):
    to_return = ""
    i = 0

    d = False
    nletters = ""
    ntimes = ""
    while i < len(file):
        if d:
            if nletters and nletters[-1] == "x":
                if ntimes and ntimes[-1] == ")":
                    nletters = int(nletters[:-1])
                    ntimes = int(ntimes[:-1])
                    
                    s = file[i:i+nletters] * ntimes
                    i += nletters-1
                    to_return += s

                    d = False
                    nletters = ""
                    ntimes = ""
                else:
                    ntimes += file[i]
            else:
                nletters += file[i]
                
        else:
            if file[i] == "(":
                d = True
            else:
                to_return += file[i]
    
        i += 1
    return to_return

def split_file(file):
    to_return = []
    i = 0

    d = False
    nletters = ""
    ntimes = ""
    count = 0
    while i < len(file):
        if d:
            if nletters and nletters[-1] == "x":
                if ntimes and ntimes[-1] == ")":
                    nletters = int(nletters[:-1])
                    ntimes = int(ntimes[:-1])
                    
                    to_return.append((nletters, ntimes))

                    d = False
                    nletters = ""
                    ntimes = ""
                else:
                    ntimes += file[i]
            else:
                nletters += file[i]
                
        else:
            if file[i] == "(":
                if count > 0:
                    to_return.append(count)
                    count = 0
                d = True
            else:
                count += 1
    
        i += 1
    if count > 0:
        to_return.append(count)
    print(to_return)

def get_tree(size, l):
    tree = [0]
    i = 0
    def get_size(item):
        if type(item) == int:
            return item
        else:
            return len(str(item))
    while size > 0:
        next_size = get_size[l[i]]

        if next_size <= size:
            
            size = size - next_size

def compute(l):
    if len(l) == 1:
        return l[0]
    i = 0
    total = 0
    while i < len(l):
        if type(l[i]) == int:
            total += l[i]
        else:
            


def part_1():
    d = get_input()

    for i in range(100):
        d = decompress(d)
    print(d)
    print("Taille:", len(d))

def part_2():
    i = get_input()
    d = split_file(i)
    # print(d)
    # print("Taille:", len(d))

part_2()