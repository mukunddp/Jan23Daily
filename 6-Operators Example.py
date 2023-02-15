# a + (b + c * d )- a / 5 ** 5
# a = 1
# b = 2
# c = 5
# d = 2
#
# print(a + (b + c * d) - a / 5 ** 5)
# print(1 + (2 + 5 * 2) - 1 / 5 ** 5)
# print(1 + 12 -0.00032 - 51 - 25)

# a = 10
# b = 2
# c = 3
# print(a ** b ** c)
# print(10 ** 8)
# print(100 ** 3)

# & , | , ^ , ~
# &
# print(3 & 2)
#
# # print(1  and 1)
# # |
# print(2 | 3)
#
# # ~         # task
# print(~3)
#
# #  ^        # task
# print(2 ^ 3)
#

def add_nums(num1, num2):
    while num2 != 0:
        data = num1 & num2
        num1 = num1 ^ num2
        num2 = data << 1
        return num1
print(add_nums(11, 2))