def calculateScore(kill,death,assist):
    return (100 * kill) - (50 * death) + (20 * assist)

kill = int(input("Enter your kill: "))
death = int(input("Enter your death: "))
assist = int(input("Enter your assist: "))

result = calculateScore(kill, death, assist)
if result > 0:
    print("your score is",result)
else:
    print("your score is",0)