import re

inp = input()

check = [
    len(inp) >= 8,
    re.search(r"[0-9]", inp) is not None,
    re.search(r"[a-z]", inp) is not None,
    re.search(r"[A-Z]", inp) is not None,
    any(i in inp for i in "[]!@#$^&*(),.?\":{}|<>")
]

print(sum(1 for i in check if i))