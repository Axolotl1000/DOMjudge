stage = int(input())

if stage == 1:
    print(1)
if stage == 2:
    print(2)

a, b, c = 1, 1, 2
for _ in range(3, stage + 1):
    current = c + b + a
    a, b, c = b, c, current

print(c)