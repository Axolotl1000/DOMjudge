for _ in range(int(input())):
    amount, first, second, total = tuple((int(i) for i in input().split(",")))
    b = total // second
    a = amount - b
    less = total - first * a - second * b
    while less != 0:
        a += 1
        b -= 1
        less = total - first * a - second * b
    print(f"{a},{b}")

