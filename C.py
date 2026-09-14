for _ in range(int(input())):
    a, b = input().split("/")
    ip = [int(i) for i in a.split(".")]
    mask = [int(i) for i in b.split(".")]
    network = [str(ip[i] & mask[i]) for i in range(4)]
    print(".".join(network))
