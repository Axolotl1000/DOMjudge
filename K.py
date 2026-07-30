LETTERS = "ABCDEFGHJKLMNPQRSTUVXYWZI"
PRIORTY = "876543211"

inp = input()

maybe = []

check_code = 0

for i in range(len(PRIORTY)):
    check_code += int(inp[i]) * int(PRIORTY[i])

default_number = 10

for i in LETTERS:
    first_num, second_num = (default_number // 10, default_number - default_number // 10 * 10)
    if (first_num * 1 + second_num * 9 + check_code) % 10 == 0:
        maybe += i
    default_number += 1

maybe.sort()

print("".join(maybe))
