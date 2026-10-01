import math

lst = []

for _ in range(2):
    [lst.append(int(i)) for i in input().split(", ")]

lst.sort()

print(lst[int(math.floor(len(lst) / 2))])