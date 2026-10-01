height, weight = tuple(int(i) for i in input().split(" "))
y, x = tuple(int(i) for i in input().split(" "))
commands = input()

def hit() -> bool:
    if x < 0 or y < 0:
        return True
    if x >= weight or y >= height:
        return True
    return False

for command in commands:
    if command == "U":
        y -= 1
    elif command == "D":
        y += 1
    elif command == "L":
        x -= 1
    elif command == "R":
        x += 1

    if hit():
        print("Game Over")
        break
else:
    print(y, x)