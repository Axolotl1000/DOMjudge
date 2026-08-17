from itertools import permutations

def find_possible(inp: list[int]) -> set[int]:
    perms = permutations(inp)
    return set(int("".join(map(str, p))) for p in perms)

for _ in range(int(input())):
    data, start, end = tuple(int(i) for i in input().split(","))
    possible = list(find_possible(list(int(i) for i in str(data))))
    possible.sort()
    print(possible[start-1] + possible[end-1])
    
