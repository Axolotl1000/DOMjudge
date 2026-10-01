shift = int(input())
raw = input()
result = ""

for i in raw:
    if not i.isalpha():
        result += i
        continue
    base = ord('A') if i.isupper() else ord('a')
    
    new_value = base + (ord(i) - base + shift) % 26
    result += chr(new_value)

print(result)