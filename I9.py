DEFAULT = 10
LETTERS = "ABCDEFGHJKLMNPQRSTUVXYWZIO"
PRIORTY = "87654321"

inp = input().strip()
letter_code = list(LETTERS).index(inp[0]) + DEFAULT
check_code = (letter_code // 10) + (letter_code % 10) * 9
for i in range(1, 9):
    check_code += int(inp[i]) * int(PRIORTY[i-1])
check_code += int(inp[9])
print("Y" if check_code % 10 == 0 else "N")