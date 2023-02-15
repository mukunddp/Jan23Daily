# For Loop

# for variable in [1, 'Mukund', 3, 1, 'Mukund', 3, ]:
#     # print(variable)
#     print('My name is Mukund')
#
# # Function - range(start, end-1, step)
# for variable in range(0, 10, 2):  # 0, 0 + 2 = 2, 2 + 2 = 4,
#     print(variable)
#     print('My name is Mukund')
# even = []
# odd = []
# # in & not in - Membership operators
# for i in range(1, 101):     # increment of 1
#     if i % 2 == 0:          # i / 2 == 0 ()   i % 2 == 0 (4)  NOTA(1)
#         # print(i, 'This is even')
#         even.append(i)
#     else:
#         odd.append(i)
#         # print(i, 'This is Odd')
# print('Even Numbers from 1 to 100: ', even)
# print('\n\nOdd Numbers from 1 to 100: ', odd)


# Prime Numbers

# j = 0
# while True:
#     num = int(input('Enter Your Number: '))
#     for i in range(2, num):     # i = 2 , 3
#         print(j)
#         if num % i == 0:        # False
#             print('Not a prime number')
#             break   # break is a keyword to break the loop
#     else:
#         print('a prime number')


# i = -2
# while i < 0:        # True      i = -2 , -1, 0 (False)
#     i += 1          # i = i + 1 = -1 + 1 = 0
#     print(i)
#     print('None')


#
# def factorial(*args):
#     return args
#
#
# print(factorial(1, 2, 3, 4))
# list = [1, 2, 3, 4]
# print(factorial(*list))
# print(factorial(list))

# remove duplicated from list
# org_list = [11, 13, 15, 16, 13, 15, 16, 11]
# print("The list is: " + str(org_list))
#
# result = []
# for i in org_list:
#     if i not in result:
#         result.append(i)
# print(result)
a = {
    'a': 15,
    5: 55,
    52.5: 54,
    # # ['a', 'd']: 5,
    # {'a'}: {54, 4}
}
print(a)
