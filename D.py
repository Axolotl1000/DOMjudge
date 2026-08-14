for _ in range(int(input())):
    a, b = (input().split(" "), input().split(" "))
    a.pop(0)
    b.pop(0)
    print(len(list(i for i in a if i in b)))
