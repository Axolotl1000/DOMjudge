CHARS = "DEFGHIJKLMNOPQRSTUVWXYZABC"
BIN = { "00": 0, "01": 1, "100": 2, "101": 3, "1100": 4, "1101": 5, "11100": 6, "11101": 7, "111100": 8, "111101": 9 }

for _ in range(int(input())):
    inp = input()
    buf = ""
    loc_buf = ""
    for char in inp:
        buf += char
        if buf in BIN:
            loc_buf += str(BIN[buf])
            buf = ""
    print(CHARS[abs(int(loc_buf) - 1)])

