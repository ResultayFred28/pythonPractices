def two_sum(num : list[num], target: int) -> list[int]:

    seen = {}

    for i,n in enumerate(num):
        complement = target - n
        if complement in seen:
            return [seen[complement],i]
        seen[n] = i

    return []


num = []
ilan = int(input("how many number you want to enter?: "))
for x in range(ilan):
    nums = int(input("enter a number: "))
    num.append(nums)

target = int(input("enter a target: "))

print(two_sum(num, target))