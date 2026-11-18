SEPC = "aoyeui"

raw = input()

result = []

for i in raw:
    if i.lower() in SEPC:
        continue
    result.append(i.lower())

print(f".{'.'.join(result)}")