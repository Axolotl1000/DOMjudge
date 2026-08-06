import math

for _ in range(int(input())):
    inp = input().split(" ")
    a = int(inp[0])
    b = int(inp[1])
    start = math.ceil(a ** 0.5)
    end = int(b ** 0.5)
    print(max(0, end - start + 1))

