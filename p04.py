from collections import Counter

inp = input()

while inp.find("  ") != -1:
    inp = inp.replace("  ", " ")

inp = inp.split(" ")

count = dict((i, len(i)) for i in inp)

sort = dict(sorted(count.items(), key=lambda x : x[1]))

print(" ".join(sort.keys()))