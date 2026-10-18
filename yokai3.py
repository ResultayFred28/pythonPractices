def calculateStar(capital, ):
    star = 0

    for match in capital:
        if match == "W":
            star = star + 1
        else:
            if match == "L":
                if star == 0:
                    continue
                else:
                    star = star - 1
    return star








matches = input("match result(W/L): ")
capital = matches.upper()

star = calculateStar(capital)
print(star)