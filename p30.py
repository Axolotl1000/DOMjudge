houses = [int(i) for i in input().replace(" ", "").split(",")]

prev, prev2 = houses[0], 0

for i in range(1, len(houses)):
    current = max(prev, prev2 + houses[i])
    prev, prev2 = current, prev

print(prev)
