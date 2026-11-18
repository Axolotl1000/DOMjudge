import ipaddress

for _ in range(int(input())):
    net = ipaddress.ip_network(input(), strict=False)
    print(f"{net.network_address}/{net.broadcast_address}")