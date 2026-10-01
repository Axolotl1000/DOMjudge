from math import comb

line = int(input())

if line == 1:
    print(1)
    exit(0)

line -= 1

row = [str(comb(line, i)) for i in range(line + 1)]

print(" ".join(row))