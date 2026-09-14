ALLOWED_CHARS = " ,;!."

for _ in range(int(input())):
    count = 0
    buf = False
    for i in input():
        if buf:
            if i in ALLOWED_CHARS:
                buf = False
                count += 1
        else:
            if i not in ALLOWED_CHARS:
                buf = True
    if buf:
        count += 1
    print(count)
