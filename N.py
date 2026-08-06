points = []

for _ in range(int(input())):
    inp_split = input().split(" ")
    points.append((int(inp_split[0]), int(inp_split[1])))

points.sort()

for a, b in points:
    print(a, b)

