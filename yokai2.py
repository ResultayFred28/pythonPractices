def checkDeficit(tdee,calories_eaten,calories_burned):

    netCalories = calories_eaten - calories_burned
    deficit = tdee - netCalories

    if deficit >= 500:
        print(f"Explanation:NetCalories {netCalories}. deficit: = {tdee} - {netCalories} = {deficit} since {deficit} is >= 500 it is ")
        return "Goal Met"
    elif 0 < deficit < 500:
        print(f"Explanation:NetCalories {netCalories}. deficit: = {tdee} - {netCalories} = {deficit} since {deficit} is between 0 and 500 it is ")
        return "Slight Deficit"
    else:
        print(f"Explanation:NetCalories {netCalories}. deficit: = {tdee} - {netCalories} = {deficit} since {deficit} less than 0 it is ")
        return "Surplus"




netCalories = 0
deficit = 0
tdee = int(input("enter you tdee(Total Daily Energy Expenditure): "))
calories_eaten = int(input("enter you calories_eaten: "))
calories_burned = int(input("enter you calories_burned: "))


result = checkDeficit(tdee,calories_eaten,calories_burned)
print(result)




