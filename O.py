def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

for _ in range(int(input())):
    inp = int(input())
    rev_inp = int(str(inp)[::-1])
    if is_prime(inp):
        if is_prime(rev_inp) and inp != rev_inp:
            print(inp, "is an emirp number.")
        else:
            print(inp, "is a prime number.")
    else:
        print(inp, "is not a prime number.")
