POSSIBLE = {
    "B": "T",
    "T": "C",
    "C": "W",
    "W": "B"
}

a, b = tuple(input().upper().split())

if POSSIBLE[a] == b:
    print(1)
elif POSSIBLE[b] == a:
    print(2)
else:
    print(0)