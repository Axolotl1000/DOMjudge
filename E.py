for _ in range(int(input())):
    print(sum(1 for i in bin(int(input()))[2:] if i == "1"))
