from math import gcd
from itertools import combinations

for _ in range(int(input())):
    print(max(gcd(i[0], i[1]) for i in combinations((int(i) for i in input().split(",")), 2)))
