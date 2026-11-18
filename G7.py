STARS =[
("Aquarius", (1*30+21, 2*30+19)),
("Pisces", (2*30+20, 3*30+20)),
("Aries", (3*30+21, 4*30+20)),
("Taurus", (4*30+21, 5*30+21)),
("Gemini", (5*30+22, 6*30+21)),
("Cancer", (6*30+22, 7*30+22)),
("Leo", (7*30+23, 8*30+21)),
("Virgo", (8*30+22, 9*30+23)),
("Libra", (9*30+24, 10*30+23)),
("Scorpio", (10*30+24, 11*30+22)),
("Sagittarius", (11*30+23, 12*30+22))]

for _ in range(int(input())):
    m, d = tuple(int(i) for i in input().split("/"))
    days = m * 30 + d
    found = False
    for name, rang in STARS:
        if rang[0] <= days <= rang[1]:
            found = True
            print(name)
    if not found:
        print('Capricorn')
        