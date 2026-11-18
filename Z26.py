from datetime import datetime, timedelta

for _ in range(int(input())):
    target_date = datetime(1970, 1, 1) + timedelta(days=int(input()))
    result = target_date.strftime("%Y-%m-%d")
    print(result)