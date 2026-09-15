inp = input().strip()

sort = "".join(sorted(list(inp)))

print(int(sort[::-1]) - int(sort))