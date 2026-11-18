for _ in range(int(input())):
    line = input()
    if line:
        clean_str = line.replace(" ", "")
        total = 0
        for i in range(0, len(clean_str), 4):
            chunk = clean_str[i : i + 4]
            total += int(chunk, 16)
        while total > 0xFFFF:
            total = (total & 0xFFFF) + (total >> 16)
        checksum = ~total & 0xFFFF
        print(f"{checksum:04x}")
