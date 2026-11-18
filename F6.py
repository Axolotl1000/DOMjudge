for _ in range(int(input())):
    N, R = map(int, input().split())
    
    if N == 0:
        print(0)
        continue
        
    digits = []
    while N > 0:
        rem = N % R
        if rem < 10:
            digits.append(str(rem))
        else:
            digits.append(chr(ord('A') + rem - 10))
        N //= R
        
    print("".join(reversed(digits)))