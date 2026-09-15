cache = list()

current = ""
times = 1
for i in input():
    if current != i:
        cache.append(current * times)
        current = i
        times = 1
    else:
        times += 1

cache.append(current * times)

print(max(len(i) for i in cache))