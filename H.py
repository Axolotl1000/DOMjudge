inp = input().replace(" ", "")

rules = [
    "BT",
    "TC",
    "CW",
    "WB",
]

if inp in rules:
    print(1)
elif inp[::-1] in rules:
    print(2)
else:
    print(0)