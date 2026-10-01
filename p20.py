def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

start, end = tuple(int(i) for i in input().split(" "))
print(sum(1 for i in range(start, end) if is_prime(i)))