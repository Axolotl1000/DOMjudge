from math import gcd
from functools import reduce

for _ in range(int(input())):
    print(reduce(gcd, (int(i) for i in input().split(","))))
