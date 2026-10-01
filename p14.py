first, second = tuple(int(i) for i in input().split(" "))

if first == second:
    print("*" * first)
    exit(0)

dash = max(first, second)

positive = first > second

for i in range(first, second + (-1 if positive else 1), -1 if positive else 1):
    print("-" * int(dash - i), end="")
    print("*" * i)