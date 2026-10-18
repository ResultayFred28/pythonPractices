result = 0
num1 = int(input("please enter the first number:"))

operator = input("operation(+,-,*,/,^,%):")

num2 = int(input("please enter the second number:"))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    if num2 == 0:
        print("cannot divide by zero, UNDEFINED")
    else:
        result = num1 / num2
        print(result)
elif operator == "^":
    result = num1 ** num2
    print(result)
elif operator == "%":
    result = num1 % num2
    print(result)
else:
    print("enter the valid operator!(+,-,*,/)")



