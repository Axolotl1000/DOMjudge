roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
total = 0
inp = input().upper()
n = len(inp)

for i in range(n):
    if i < n - 1 and roman_map[inp[i]] < roman_map[inp[i+1]]:
        total -= roman_map[inp[i]]
    else:
        total += roman_map[inp[i]]

print(total)