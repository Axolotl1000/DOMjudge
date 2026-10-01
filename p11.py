lst = [int(i) for i in input().split(" ")]

if len(lst) == 1:
    print("YES")
    exit(0)

seq = lst[0] - lst[1]

for i in range(1, len(lst) - 1):
    seq_local = lst[i] - lst[i + 1]
    if seq != seq_local:
        print("NO")
        break
    seq = seq_local
else:
    print("YES")