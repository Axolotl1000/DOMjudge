a, b = input().replace(" ", "").upper().split(",")

a_char = a[0]
b_char = b[0]
a_loc = int(a[1:])
b_loc = int(b[1:])

print((abs(ord(a_char) - ord(b_char)) + 1) * (abs(a_loc - b_loc) + 1))