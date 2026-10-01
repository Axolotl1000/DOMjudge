import string

same = int(input())
inp = input()

def found() -> bool:
    current = ""
    count = 0
    for i in inp:
        if current != i:
            current = i
            count = 1
        else:
            count += 1

        if count >= same:
            return True
    return False

while found():
    for i in string.ascii_lowercase:
        inp = inp.replace(i * same, "")

if inp == "":
    print("EMPTY")
else:
    print(inp)