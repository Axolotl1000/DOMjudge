def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

inp = int(input())

def find_nearest_prime(n: int) -> int:    
    step = 1
    while True:
        higher = n + step
        lower = n - step
        
        has_higher = is_prime(higher)
        has_lower = (lower >= 2) and is_prime(lower)

        if has_lower and has_higher:
            return lower
        elif has_lower:
            return lower
        elif has_higher:
            return higher
            
        step += 1

print(find_nearest_prime(inp))