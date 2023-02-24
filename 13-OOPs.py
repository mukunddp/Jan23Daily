# def factorial(num1):
#     if num1 == 0:
#         return 1
#     elif num1 == 1:
#         return 1
#     return num1 * factorial(num1 - 1)
#

# def add(num1, num2):
#     return num1 + num2
# print(add(10, 15))
#
#
# def sub(num1, num2):
#     return num1 - num2
# print(sub(10, 15))
#
#
# def mul(num1, num2):
#     return num1 * num2


# def calculator():
#     pass
#
#     def sub(self, num1, num2):
#         return num1 - num2
#
#     def mul(self, num1, num2):
#         return num1 * num2
#
# # class MyClass:
#     pass

#
# class CalculatorProgram:
#     a = 10                             # all attributes are public
#     # print('Value of a', a)             # yes (3)  no (1)
#     print(id(a))
#     def add(self, num1, num2):
#         return num1 + num2
#
# obj = CalculatorProgram()     # this object     # shubham
# print(obj.a)                # 10
# print(id(obj.a))
# obj.a = 15
# print(id(obj.a))
# print(obj.a)                # 15
#
# obj1 = CalculatorProgram()                      # payal
# print(obj1.a)               # 15 (1)  or 10 (1)
# print(id(obj1.a))
# obj = CalculatorProgram()       # Instance
# print(obj.num)          # 10
# obj.num = 15
# print(obj.num)          # 15
#
# obj1 = CalculatorProgram()      # Instance
# print(obj1.num)         # 15(v)     10(P)       NA(D)
# obj1.num = 12
# print(obj1.num)         # 12

class CalculatorProgram:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print('I am a default constructor')

    def add(self):
        self.a = 10
        return self.num1 + self.num2

    def sub(self):
        print(self.a)
        return self.num1 - self.num2

obj = CalculatorProgram(10, 12)
print(obj.add())
print(obj.sub())




# num1 = 10
# num2 = 12
# def add():
#     return num1 + num2
#
# def sub():
#     return num1 - num2
#
# print(add())




# You have create class containing all your personal details also a parameterized constructor and make use of object change the values into class and print