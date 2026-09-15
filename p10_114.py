def is_pass(text: str) -> bool:
    cache = list()
    current = ""
    times = 1
    for i in text:
        if current != i:
            cache.append(current * times)
            current = i
            times = 1
        else:
            times += 1
    cache.append(current * times)
    return all(len(i) < 2 for i in cache)

inp = input().replace(" ", "").split(",")
print(sum(1 for i in inp if is_pass(i)))