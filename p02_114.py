import string

CHARS = list("0123456789" + string.ascii_letters)

def is_increase(text: str) -> bool:
    prev = -1
    for i in text:
        if CHARS.index(i) <= prev:
            return False
        prev = CHARS.index(i)
    return True

inp = input()
if is_increase(inp):
    print(1)
elif is_increase(inp[::-1]):
    print(2)
else:
    print(3)