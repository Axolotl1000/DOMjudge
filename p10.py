inp = input()

current = 0

while inp.find(bin(current)[2:]) != -1:
    current += 1

print(current - 1)