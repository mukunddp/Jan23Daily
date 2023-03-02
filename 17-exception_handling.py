# a = 10
# b = int(input('Write a number :'))
#
# c = a + b
# print(c)

# try, Except, else, raise , finally
# if a > 2:
# #     print('A is greater ')
#
# try:
#     print('This is running ')
#
# finally:
#     print('This is finally')

# except:
#     pass

# b = int(input('Write a number :'))
# a = 10
# c = a + b
# print(c, 'This is running')

# try, Except, else, raise, finally
#

try:
    b = int(input('Write a positive number :'))
    if b <= 0:
        raise ZeroDivisionError('This value should not be zero')
    a = 10
    c = a / b
    print(c, 'This is running')
    print()

except ZeroDivisionError as z:
    print(z)

else:
    print('If we don\'t get exception then it will run\n')
finally:
    print('This is finally')
