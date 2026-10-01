count, size = tuple(int(i) for i in input().split(" "))

oversize = 0
max_person = 0
current = 0

for i in range(1, count + 1):
    off, on = tuple(int(i) for i in input().split(" "))
    current -= off
    current += on
    if oversize == 0 and current > size:
        oversize = i
    max_person = max(max_person, current)

print(current, oversize, max_person)
