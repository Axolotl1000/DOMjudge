from collections import Counter

inp = input()

possible = set(inp[i:j] 
               for i in range(len(inp)) for j in range(i + 1, len(inp) + 1)
               if len(inp[i:j]) >= 4 
               and inp[i:j] == inp[i:j][::-1] 
               and len(Counter(inp[i:j])) >= 3)

print(len(possible))
