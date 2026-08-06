for _ in range(int(input())):
    inp = int(input())
    current = 2
    result = 0
    while current * current <= inp:
        while inp % current == 0:
            result += current
            inp //= current
        current += 1
    if inp > 1:
        result += inp
    print(result)
