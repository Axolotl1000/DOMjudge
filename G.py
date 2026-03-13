rm = [i for i in "aoyeui"]
res = list("." + n for n in list(i if i not in rm else "" for i in input().lower()) if n != "")
print("".join(res))