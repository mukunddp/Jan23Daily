# a = 10
# b = 20
# def add(a, b):
#     c = a + b
#     print('addition is', c)
#     return c
#
# add(16, 25)
#
# print(add(10, 15))
# print(add(15, 26))

# lambda arguments/parameters : expression
# x = lambda a, b, c, d: a + b + c + d
# # print(x)        # type of function
# #
# # print(x(10, 15, 12, 20))
# # print(lambda a : 15+ 2156+ a )
#
#
# def multiply(a, b):
#     return a * b
# for i in range(1,11):
#     multiply(i, 15)

# #
# # print(multiply(10, 15))
# # multiply(12, 15)
# # multiply(13, 15)
#
# def multi(n):       # n = 15
#     return lambda a: a * n  # a * 15
#
#
# multiple_15 = multi(15)     # lambda a: a * 15
#
# print(multiple_15(3))       # a = 3 : 3 * 15
# print(multiple_15(4))       # a = 4 : 4 * 15

# multiple_7 = multi(7)
#
#
# print(multiple_15(10))
# print(multiple_15(16))
#
#
# print(multiple_7(61))
# print(multiple_7(58))
# print(multi(15))


# x = lambda a, b: a + b


# for i in range(len(ls)):
#     print(x(ls[i], li[i]))

# def add(a, b):
#     return a + b
# #
#
# x = lambda a, b: a + b

# ls = [10, 15, 12, 15, 14, 19, 13]
# li = [12, 16, 13, 15, 18, 19, 17]

# print(list(map(add, ls, li)))
# add(10, 12)
#
# print(list(map(lambda a, b: a + b,  ls, li)))
#
# # y = map(lambda a, b: a + b, [10, 15, 12, 15, 14, 19, 13], [12, 16, 13, 15, 18, 19, 17])
#
#
# print(list(map(lambda a, b: a + b, [10, 15, 12, 15, 14, 19, 13], [12, 16, 13, 15, 18, 19, 17])))


ls = [10, 15, 12, 15, 14, 19, 13]


# square of ls :

# print(list(map(lambda n: n*n, ls)))
# print(lambda n: n*n)
# fun = lambda n: n*n
# print(type(fun))
# # map(function, iterator)
# m = map(fun, ls)
# print(map(fun, ls))
# print(type(m))
# sq = list(m)
# print(type(sq))


# Filter Function

# age = [8, 12, 15, 16, 19, 20, 25, 23, 65, 48]
# sorted_data = []
# for i in age:
#     if i >= 25:
#         sorted_data.append(i)
# print(sorted_data)


# def age_sorter(age):
#     if age >= 25:
#         return False
#     else:
#         return True
#
# print(10 >= 24)
#
# l_fun = lambda age: age <= 25

# age = [8, 12, 25, 15, 16, 19, 20, 25, 23, 65, 48]

# filter(function, Iterator)
# print(list(filter(lambda age: age >= 18, age)))    # If the return is True, it will get stored
# print(list(filter(if age <= 25: True, age)))


# age = 26

# if age <= 25: print('AGE'), print('Age is :', age)     # 15() or 17(2)
# else:print('Mukunda'), print('Mukund')

# print(age)
# var = 10
# print(var)
# print(type(var))
# a = 10, 'Mukund', 'Tech Amplifiers'
# print(a)
# print(type(a))

# t = (10, 12, 'Mukund')
# print(t, type(t))
# t1 = 10, 12, 15
# print(t1, type(t1))

# for i in range(1,10):print(i)

# def fun(a, b):print(a+b)
# fun(10,20)

# age = [8, 12, 25, 15, 16, 19, 20, 25, 23, 65, 48]
# for i in age: print()
# if 26 >= 25: print('')
#
# # def fun(age):for i in age: if i >=25: print(i)
#
# num = []
