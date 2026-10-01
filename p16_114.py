users: dict[str, dict[int, str]] = {}

for _ in range(int(input())):
    user, time, ip = input().split(" ")
    time_split = time.split(":")
    time = int(time_split[0]) * 60 + int(time_split[1])
    if user in users:
        users[user][time] = ip
    else:
        users[user] = {time: ip}

sus = []

for name in users:
    logs = sorted(users[name].items())
    oldTime = None
    oldIP = None
    is_suspect = False
    
    for time, ip in logs:
        if oldTime is None:
            oldTime = time
            oldIP = ip
            continue
        if (time - oldTime) < 10 and oldIP != ip:
            is_suspect = True
            break
        oldTime = time
        oldIP = ip
        
    if is_suspect:
        sus.append(name)

print("\n".join(sorted(sus)))