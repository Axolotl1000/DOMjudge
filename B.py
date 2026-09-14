CODES = {item: index for index, item in enumerate("-----,.----,..---,...--,....-,.....,-....,--...,---..,----.".split(","))}

for _ in range(int(input())):
    print("".join(list(str(CODES[i]) for i in input().split(" "))))
