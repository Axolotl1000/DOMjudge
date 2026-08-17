times = int(input())
targets = input().split(",")
for _ in range(times):
    hits = { 2: 0, 3: 0, 4: 0, 5: 0 }
    selected = input().split(",")
    for i in range(6):
        skip = selected[i]
        build = (i for i in selected if i != skip)
        hit = sum(1 for i in build if i in targets)
        try:
            hits[hit] = hits[hit] + 1
        except KeyError:
            pass
    print(f"{hits[2]},{hits[3]},{hits[4]},{hits[5]}")

