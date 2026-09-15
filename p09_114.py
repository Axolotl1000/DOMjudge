data = [int(i) for i in input().split(",")]
data.sort()

print(len(str(bin(data.pop() - data.pop(0)))[2:].replace("0", "")))