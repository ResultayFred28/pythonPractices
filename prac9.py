my_nums = [2,4,6,8,3,7,9,1,10,12,13]

new_num = list(map(lambda num : num ** 2, my_nums))

print(new_num)

odds = list(filter(lambda num : num % 2 != 0, my_nums))

print(odds)