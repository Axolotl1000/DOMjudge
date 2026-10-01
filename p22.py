score: list[tuple[str, float]] = []

for _ in range(int(input())):
    name, first, second = tuple(i for i in input().split(" "))
    first = int(first)
    second = int(second)
    score.append((name, round((first + second) / 2, 2)))

score.sort(key=lambda x: x[0])
score.sort(key=lambda x: x[1], reverse=True)

for i in range(len(score)):
    print(f"{i + 1} {score[i][0]} {score[i][1]:.2f}")