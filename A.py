for _ in range(int(input())):
    input()
    tasks = (int(i) for i in input().split(","))
    current = tasks.__next__()
    price = 0
    for task in tasks:
        if current == task:
            continue
        elif current < task:
            price += (task - current) * 20
        else:
            price += (current - task) * 10
        current = task
    print(price)
