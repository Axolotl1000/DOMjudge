first, opcode, second = tuple(i for i in input().split(" "))

if opcode == "+":
    print(int(first) + int(second))
if opcode == "-":
    print(int(first) - int(second))
if opcode == "*":
    print(int(first) * int(second))
if opcode == "/":
    print(f"{int(first) / int(second):.3f}")