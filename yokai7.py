def calculateChessScore(wins,draw,lose):
    return (wins * 3) + (draw * 1) + (lose * 0)


win = int(input("how many win?:"))
draw = int(input("how many draw?:"))
lose = int(input("how many lose?:"))

result = calculateChessScore(win,draw,lose)

print(result)