from collections import Counter

times = Counter(input()).most_common()

print(1 if times.pop(0)[1] == times.pop(0)[1] else 0)