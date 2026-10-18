def calculatePrintCost(page,color_type):

    if page > 50:
        if  color_type == "BW":
            return page * 1
        else:
            return page * 4
    else:
        if color_type == "BW":
            return page * 2
        else:
            return page * 5





page = int(input("how many pages: "))
colorType = input("anong kulay boss: ")

color = colorType.upper()

presyo = calculatePrintCost(page,color)

print(presyo)
