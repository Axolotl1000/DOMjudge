inp = input().split(".")
result = ""

for i in inp:
    temp = format(int(i), "b")
    result += "0"*(8-len(temp))
    result += temp

print(result)