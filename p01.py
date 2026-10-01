from collections import Counter

count = dict(Counter(input()))

count = dict(sorted(count.items(), key=lambda x : x[1], reverse=True))

max_time = list(count.items())[0][1]

print(sum(1 for i in list(count.items()) if i[1] == max_time))