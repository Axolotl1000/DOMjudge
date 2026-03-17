inp = input()

result = ""

for i in range(0, len(inp) - 1):
    result += str(abs(ord(inp[i]) - ord(inp[i+1])))

print(result)