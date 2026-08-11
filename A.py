def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

for _ in range(int(input())):
    inp = input().split(",")
    first, second = (int(inp[0]), int(inp[1]))
    if abs(first - second) != 2:
        print("N")
        continue
    if is_prime(first) and is_prime(second):
        print("Y")
    else:
        print("N")
