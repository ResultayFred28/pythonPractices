def calculateScore(kills,deaths,assists):
    score1 = 0
    score2 = 0
    score3 = 0
    kill = 100
    death = -25
    assist = 50
    for x in range(kills):
        score1 += kill
    for y in range(deaths):
        score2 += death
    for z in range(assists):
        score3 += assist

    return  score1 + score2 + score3

kills = int(input("enter number of kills: "))
deaths = int(input("enter number of deaths: "))
assists = int(input("enter number of assits: "))

total = calculateScore(kills,deaths,assists)

if total >= 0:
    print(total)
else:
    print(0)