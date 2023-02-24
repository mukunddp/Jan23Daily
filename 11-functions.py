# print('Printing ')
# input('Enter ')
# print(name.count('M'))
# name.count()
# print(f'u apeared {2} and at indexes of {1, 3}')
#
# name = 'uMUkuudu'
# check = 'u'
# each_index = 0
# indexes = []
# for i in name:      #
#     if check == i.lower():
#         indexes.append(each_index)
#     each_index += 1
# print(f'{check} apeared {len(indexes)} times and at indexes of {indexes}')

# name = 'Deepak'
# # print(name.count('u'))
#
#
# def count_index(check):     # check is parameter
#     each_index = 0
#     indexes = []
#     for i in name:  #
#         if check == i.lower():
#             indexes.append(each_index)
#         each_index += 1
#     return f'{check} appeared {len(indexes)} times and at indexes of {indexes}'
#
# count_index('a')
# print(count_index('u'))
# print(count_index('m'))
# print(count_index('k'))
# print(count_index('p'))


# def add(a, b):                  # a , b are parameters
#     c = a + b
#     print('value of a', a, '\nvalue of b', b)
#     return c
#
#
# add(10, 15)                     # calling the function
# add(2, 3)
# print(add(7, 10))               # calling the function and printing return value

# adding
# adding
# adding...
# 17


# def add(a, b, c):                  # a , b are parameters
#     print('\nvalue of a', a, '\nvalue of b', b, '\nvalue of c', c)
#     return
# add(10, 15, 12)                     # positional arguments
# add(a=15, c=10, b=9)                # Keyword arguments
# add(c=5, b=10, a=15)                # Keyword Argument
# add(10, b=9, c=5)

# add(10, 9, a=5)                     # error
# add(10, b=15, 12)                   # positional argument should not follows keyword argument


# factorial of a number
# 4! = 4 * 3 * 2 * 1
# num = int(input('Enter Number:'))
# fact = 1
# for i in range(num, 0, -1):
#     fact = fact * i
#
# print(fact)


# def factorial_number(num):
#     fact = 1
#     for i in range(num, 0, -1):
#         fact = fact * i
#     print(fact)
#
#
# factorial_number(0)
# factorial_number(2)
# factorial_number(3)


# 4! = 4 * 3 * 2 * 1
# 4! = 4 * 3!
# 5! = 5 * 4!
# 3! = 3 * 2 * 1
# def factorial_number(num):
#     fact = 1
#     for i in range(num, 0, -1):
#         fact = fact * i
#     print(fact)


def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    return num * factorial(num-1)

def add(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    return num * factorial(num-1)
# num = 4
# 4 * (3 * (2 * (1 * 1)))
# print(factorial(0))
# print(factorial(1))
print(factorial(4))
print(factorial(10))

# which function is preferable for writing a code Recursion function or normal function????

