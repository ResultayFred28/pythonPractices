def calculateScore(kills,deaths,assists):

    totalScore = (kills * 100) - (deaths * 25) + (assists * 50)

    if totalScore < 0:
        return 0
    else:
        return totalScore


kills = int(input("enter how many kills: "))
deaths = int(input("enter how many deaths: "))
assists = int(input("enter how many assists: "))

print(calculateScore(kills,deaths,assists))