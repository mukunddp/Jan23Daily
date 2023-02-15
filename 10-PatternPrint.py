# 1
# 1  2
# 1  2  3
# 1  2  3  4
# 1  2  3  4  5

# 1 : Understand the Questions
# 2 : Break the Question small parts
# 3 : Write the logic
# 4 : implement step by step

        # numbers are from 1 to 5
        # How many lines - 5
        # every number is increasing by one in each line

#
# for i in range(1, 6):       # i = 1, 2, 3, 4, 5  lines
#     for j in range(1, i+1):   # j = 1, 2, 3, 4, 5
#         print(j, end=' ')
#     print()


# 1  2  3  4  5
# 1  2  3  4
# 1  2  3
# 1  2
# 1

# 1 : Understand the Questions
# 2 : Break the Question small parts
# 3 : Write the logic
# 4 : implement step by step

        # numbers are from 1 to 5
        # How many lines - 5
        # every number is decreasing by one on each line

# for i in range(5, 0, -1):           # i = 5, 4, 3, 2, 1 lines
#     for j in range(1, i+1):     # j = 1, 2, 3, 4, 5
#         print(j, end=' ')
#     print()

#           1
#         1  2
#       1  2  3
#     1  2  3  4
#   1  2  3  4  5

# numbers are from 1 to 5
# How many lines - 5
# every number is increasing by one on each line
# every space is decreasing by one on each line

# for i in range(1, 6):       # i = 1, 2, 3, 4, 5  lines
#     for k in range(6, i, -1):
#         print(' ', end='')
#     for j in range(1, i+1):   # j = 1, 2, 3, 4, 5
#         print('*', end=' ')
#     print()

# task :
#      *  *  *  *  *
#       *  *  *  *
#        *  *  *
#         *  *
#          *


# stars are from 1 to 5
# How many lines - 5
# every space is increasing by one on each line
# every star is decreasing by one on each line


# the number 3 digit and addition of cube of each digit is that number itself
# 153 = 1**3 + 5**3 + 3**3
#     = 1 + 125 +  27 = 153
#
# pick each digit of that number
# make a cube of each digit and add
# check that addition is equal to old number
original_num = int(input('Enter a number'))
num = original_num
new_num = 0

while num != 0:
    a = num % 10
    a **= 4
    num = num // 10
    new_num += a
    print('Changed orginal Number: ', num)
    print('New Number: ', new_num)

if new_num == original_num:
    print(f'{new_num} number is armstrong number')
else:
    print('Not armstrong number')


