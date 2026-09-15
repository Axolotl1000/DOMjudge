inp = input()
for c in ",.!?":
    inp = inp.replace(c, " ")
while inp.find("  ") != -1:
    inp = inp.replace("  ", " ")

result = [i for i in inp.split(" ") if len(i) >= 4]
result.reverse()
print(" ".join(result))