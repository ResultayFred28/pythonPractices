# number = int(input("enter a number: "))
#
# def convert(num):
#     if num > 0:
#         convert(num // 2)
#         print(num % 2, end="")
#     else:
#         return
#
# convert(number)

# text = input("enter an text to reverse: ")
#
# def reverse(text):
#     return text[:: -1]
#
# print(reverse(text))

# my_array = [12, 22, 11, 90, 5] # [5, 11, 12, 22, 90]
#
# n = len(my_array) # 5
# for i in range(n-1): # 4
#     for j in range(n-i-1): # 1
#         if my_array[j] > my_array[j+1]:
#             my_array[j], my_array[j+1] = my_array[j+1], my_array[j]     #
#
# print("Sorted array:", my_array)

# print(0)
# print(1)
# count = 2
#
# def fibonacci(prev1, prev2):
#     global count
#     if count <= 19:
#         newFibo = prev1 + prev2
#         print(newFibo)
#         prev2 = prev1
#         prev1 = newFibo
#         count += 1
#         fibonacci(prev1, prev2)
#     else:
#         return
#
# fibonacci(1,0)

def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(5))