def get_input():
    with open("inputs/day1.txt", "r") as f:
        i = f.read()

    i = i.split(", ")
    return i
                                                                                                                                                    

def switch_dir(curr, side):
    if side == "R":
        return (curr + 1) % 4
    elif side == "L":
        return (curr - 1) % 4
    else:
        raise Exception(f"Wrong input: {side}")


def move(curr, x, y, amount=1):
    if curr == 0:
        y += amount
    elif curr == 1:
        x += amount
    elif curr == 2:
        y -= amount
    elif curr == 3:
        x -= amount
    else:
        raise Exception(f"Wrong input: {curr}")
    return x, y


input_ = get_input()
current_dir = 0  # North
posx, posy = 0, 0
positions = {}
finished = False

for in_ in input_:

    current_dir = switch_dir(current_dir, in_[0])

    for i in range(int(in_[1:])):
        posx, posy = move(current_dir, posx, posy)

        if posx in positions:
            if posy in positions[posx]:
                finished = True
                break
            else:
                positions[posx].append(posy)
        else:
            positions[posx] = [posy]
    if finished:
        break

print(posx, posy)
print(f"Distance = {abs(posx) + abs(posy)}")
