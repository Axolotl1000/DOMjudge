MAPPING = {1:5, 2:3, 3:9, 4:7, 5:0, 6:8, 7:2, 8:1, 9:4, 0:6}

def decode(raw: str) -> int:
    result = [str(MAPPING[int(i)]) for i in raw]
    return int("".join(result))

print(sum(decode(i) for i in input().split("+")))
