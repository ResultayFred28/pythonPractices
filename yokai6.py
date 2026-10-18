def calculateTicketPrice(age):

    if age < 12:
        return 8
    elif age >= 65:
        return 10
    else:
        return 15


age = int(input("enter your age:"))

result = calculateTicketPrice(age)
print(result)