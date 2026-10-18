bilangNgNumber = int(input("how many number you want to enter?: "))

numbers = []

for _ in range(bilangNgNumber):
  num = int(input("enter a number: "))
  numbers.append(num)

print(numbers)

def highestFinder(numbers):
  if len(numbers) == 0:
    return None
  highest = numbers[0]
  for x in numbers:
    if highest < x:
     highest = x
  return highest

def lowestFinder(numbers):
  if len(numbers) == 0:
    return None
  lowest = numbers[0]

  for x in numbers:
    if lowest > x:
      lowest = x
  return lowest

print("the highest value is", highestFinder(numbers))
print("the lowest value is", lowestFinder(numbers))
