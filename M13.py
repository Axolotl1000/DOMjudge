from itertools import permutations

inp = int(input())

result = sorted([int("".join(map(str, i))) for i in list(permutations(range(1, inp + 1), inp))], reverse=True)

for i in result:
    print(i)