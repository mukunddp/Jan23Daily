# age = int(input('Enter your age: '))      # type int
#
# # age = 58
# if age >= 40:        # True
#     print('Inside if condition ')
#     print(f'age is {age} which is above 40 so marriage is not allowed')
# elif age > 21:
#     print('Inside elif condition ')
#     print(f'age is {age} which is above 21 so marriage is allowed')
# else:
#     print('Inside else condition ')
#     print(f'age is {age} which is below 21 so marriage is not allowed')

# check age for boy 21 and to girl 18 for marriage
# age = int(input('Enter your age: '))
# gender = input('Enter your gender: ')
#
# if age > 21 and gender == 'male':
#     print(f'age is {age} and he is a {gender} so marriage is allowed')
#
# elif age > 18 and gender == 'female':
#     print(f'age is {age} and she is a {gender} so marriage is allowed')
#
# else:
#     print('Inside else condition ')
#     print(f'age is {age} which is below 21 so marriage is not allowed')


# nested If
# age = int(input('Enter your age: '))
# gender = input('Enter your gender: ')
#
# if age > 18:  # True
#     if gender == 'male':        # true
#         if age > 21:            # False
#             print(f'age is {age} and he is a {gender} so marriage is allowed')
#         else:
#             print(f'age is {age} and he is a {gender} so marriage is not allowed')
#     elif gender == 'female':
#         print(f'age is {age} and she is a {gender} so marriage is allowed')
# else:
#     print('Inside else condition ')
#     print(f'age is {age} which is below 18 so marriage is not allowed')


# if age == 23:
#     print('age is 23 so marriage is allowed')
# else :
#     pass
#
# if age> 21:
#     print()
# elif age == 58:
#     pass
# else:               # False
#     print('Inside else condition ')
#     print('age is below 21 so marriage is not allowed')


#  01-02-2023
# You have to calculate the income after deducting tax on yearly income
# below 3 lac - NO TAX
# tax_percentage_1 = 5        # between 3 - 6 lac - 5% tax
# tax_percentage_2 = 10       # between 6 - 9 lac - 10% tax
# tax_percentage_3 = 15       # between 9 - 12 lac - 15% tax
# tax_percentage_4 = 20       # between 12 - 15 lac - 20% tax
# tax_percentage_5 = 30       # above 15 % - 30% tax
#
# income = int(input('Enter Your Income: '))
# Income_after_deduction = 0
# if 0 < income < 300000:             # True
#     print('There will be no Tax')
#     Income_after_deduction = income
#
# elif income <= 600000:
#     print(f'There will be {tax_percentage_1}% tax')
#     Income_after_deduction = income - income * tax_percentage_1 / 100
#
# elif income <= 900000:
#     print(f'There will be {tax_percentage_2}% tax')
#     Income_after_deduction = income - income * tax_percentage_2 / 100
#
# elif income <= 1200000:
#     print(f'There will be {tax_percentage_3}% tax')
#     Income_after_deduction = income - income * tax_percentage_3 / 100
#
# elif income <= 1500000:
#     print(f'There will be {tax_percentage_4}% tax')
#     Income_after_deduction = income - income * tax_percentage_4 / 100
#
# elif income >= 1500000:
#     print(f'There will be {tax_percentage_5}% tax')
#     Income_after_deduction = income - income * tax_percentage_5 / 100
#
# else:
#     print('Find a Job')
#
# print('Income After Tax Deduction: ', Income_after_deduction)




