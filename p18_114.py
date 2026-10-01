# WA

count, mod = (int(i) for i in input().split(" "))

def hash(s: str) -> int:
    result = 0
    for i in range(len(s)):
        result += ord(s[i]) * (31 ** i)

    return result % mod

inputs = set(input() for _ in range(count))

hashs = {}

for i in inputs:
    value = hash(i)
    if value in hashs:
        hashs[value].append(i)
    else:
        hashs[value] = [i]

result = sorted(hashs.items(), key=lambda x: len(x[1]), reverse=True)[0]

if len(result[1]) == 1:
    print("No collision")
else:
    print(f"Collision at hash {result[0]}: {", ".join(result[1])}")