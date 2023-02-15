# Text Type - String    - Iterable Data Type
# var = 'Mukund '
# var1 = "Mukund " + 'Parve'
# print(type(var1))

# Numeric Type - Int , Float , Complex
# var = -23
# print(type(var))

# var = 16/4  # 4.0
# print(type(var))        # float(2) int(6)

# find how to write a Complex(Imaginary Number) in Python

# Sequence Type - list , Tuple , Range
# List - Mutable
# l = [1, 2, 3]
# print('Location:', id(l))
# # l.append(4)
# # l.pop(2)
# l.reverse()
# print(l)



# print(l.count(1))
# print('List :',l)
# print('Location:', id(l))

# l1 = ['Mukund', 'Shubham', 'Nehal', 'Rajlaxmi', 'Vaibhav']
# l2 = [12.5, 23.6]
# l3 = ['Mukund', 'Shubham', 'Nehal', 2, 3, 23.6]
# l4 = [1, 2, 30, 15, 25.5]
# l5 = [None, True, False, 0]

# tuple - Immutable
# t = (1, 2, 3)
# print(type(t))
# print(id(t))
t1 = ('Mukund', 'Shubham', 'Nehal', 2, 3, 23.6)
t2 = ('Mukund', 'Shubham', 'Nehal', 'Rajlaxmi', 'Vaibhav')
t3 = (25.5, 26.5)
t4 = 1, 2, 3
t5 = 1           # tuple(5) int() NOTA(1)
# print(type(t5))
# print(t5)

#range()
# a = range(1, 5)  # (1, 3) (1 , n-1)
# for i in a:
#     print(i)
# print(type(a))


# Mapping Type : dist   - Mutable
# Key  = Value
# name = Mukund
# age = 26
# address = Pune
# d = {
#     'a': 20,
#     'b': 30
# }
# print(type(d))
# print(d)
# d = dict(a=15, b=55)
# print(id(d))
# print(d.get('a'))
# d['a'] = 25
# print(d)
# print(id(d))
# a = d.copy()
# print(id(a))
# print(d.pop('a'))
# print(d)


# Set Type : Set , frozen set

# s = {10, 25, 'Mukund', 25, 25, 10, 16, 10, 10}
# print(s)
# s.add(26)
# print(s)
# s.pop()
# print(s)
# print(s)
# print(s)
# s.pop()
# print(s)

# Boolean Type  - True and False

# a = bool(15>5)
# print(a)
# print(type(a))

# Binary Type
# a = bytes(50)
# print(a)
# v = bytes(550)
# print(v)
# print(type(a))

# None Type - None
# a = None
# print(type(a))


a = frozenset({"tech", "amplifiers", "pune"})
print(type(a))


l = ["tech", "amplifiers", "pune"]
fnum = frozenset(l)
print("frozenset Object is : ", fnum)


