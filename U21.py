inp = list(input())

code = []

for idx, char in enumerate(inp):
    if idx == 0:
        continue
    code.append(abs(ord(char) - ord(inp[idx - 1])))

print(*code, sep="")