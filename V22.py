inp = input().split(".")

code = []

for i in inp:
    raw = bin(int(i))[2:]
    code.append("0"*(8-len(raw)))
    code.append(raw)

print(*code, sep="")