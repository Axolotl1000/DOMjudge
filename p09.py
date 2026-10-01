lst = [int(i, 2) for i in input().replace(" ", "").split(",")]

print(sum(1 for i in bin(max(lst) - min(lst))[2:] if i == "1"))