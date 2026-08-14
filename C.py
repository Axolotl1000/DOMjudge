for _ in range(int(input())):
    a, b = (input(), input())
    same = list(set(i for i in a if i in b))
    same.sort()
    print("".join(same) if len(same) != 0 else "N")
