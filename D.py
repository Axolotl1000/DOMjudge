for _ in range(int(input())):
    inp = input().split()
    (start, end) = (int(inp[0]), int(inp[1]))
    print(sum((i if i % 2 == 1 else 0) for i in range(start, end + 1)))