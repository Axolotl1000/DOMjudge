second = int(input())
minute = (second // 60)
hour = minute // 60
minute %= 60
second %= 60

print(hour, minute, second)