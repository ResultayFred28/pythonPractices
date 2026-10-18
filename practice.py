def solution(fahrenheit):
    return (fahrenheit -32) * 5 / 9

def solve(celcuis):
    return (celcuis * 1.8) + 32

print("1. fahrenheit")
print("2. celcuis")
pili = int(input("choose:"))

match pili:
    case 1:
        fahrenheit = int(input("enter a fahrenheit so that we can convert it to celcuis:"))
        print(solution(fahrenheit),"C")
    case 2:
        celcuis = int(input("enter a celcuis so that we can convert it to fahrenheit:"))
        print(solve(celcuis),"F")

    case _:
        print("choose only on the two!(1,2)")


