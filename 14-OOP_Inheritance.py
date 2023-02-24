# class CalculatorProgram:                        # Base Class/ Parent Class
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         print('I am a default constructor Base Class')
#
#     def add(self):
#         self.a = 10
#         return self.num1 + self.num2
#
#     def sub(self):
#         print(self.a)
#         return self.num1 - self.num2
#
#     def mul(self):
#         print(self.a)
#         return self.num1 * self.num2
#
#     def div(self):
#         print(self.a)
#         return self.num1 / self.num2
#
#
# class CalculatorUpdated(CalculatorProgram):         # Derived Class / Child Class
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         print('I am a default constructor Derived class')
#
#     def power(self):
#         return self.num1 ** self.num2
#
#
# obj_updated = CalculatorUpdated(10, 2)
#
# print(obj_updated.power())
# print(obj_updated.add())

#  Multiple Inheritance
# class Father:                       # Base Class 1
#     def __init__(self):
#         print('I am Father')
#
#     def math(self):
#         print('Father - I am good with Maths')
#
#
# class Mother:                       # Base class 2
#     def __init__(self):
#         print('I am Mother')
#
#     def cooking(self):
#         print('Mother - Very good with Cooking')
#
#
# class Sister:                       # Base class 3
#     def __init__(self):
#         print('I am Mother')
#
#     def something(self):
#         print('sister - Very good with Cooking')
#
#
# class Me(Father, Mother, Sister):           # Derived Class
#     def __init__(self):
#         print('I am Me')
#
#     def python(self):
#         print('Son - knows python')
#
# m = Me()
# m.cooking()
# m.math()
# m.python()
# m.something()

# MultiLevel Inheritance
# class Father:                                # Base Class 1
#     def __init__(self):
#         print('I am Father')
#
#     def math(self):
#         print('Father - I am good with Maths')
#
#
# class Sister(Father):                       # Derived Class 1
#     def __init__(self):
#         print('I am Mother')
#
#     def something(self):
#         print('sister - Very good with Cooking')
#
#
# class Me(Sister):           # Derived Class
#     def __init__(self):
#         print('I am Me')
#
#     def python(self):
#         print('Son - knows python')
#
# m = Me()
# m.math()
# m.python()
# m.something()

# Hierarchical Inheritance
# class Father:                                # Base Class 1
#     def __init__(self):
#         print('I am Father')
#
#     def motivation(self):
#         print('Father - I am good with Maths')
#
#
# class Sister(Father):                       # Derived Class 1
#     def __init__(self):
#         print('I am Mother')
#
#     def something(self):
#         print('sister - Very good with Cooking')
#
#
# class Me(Father):                       # Derived Class 1
#     def __init__(self):
#         print('I am Me')
#
#     def python(self):
#         print('Son - knows python')

# m = Me()
# m.python()
# m.motivation()
# m.something()

# Hybrid Inheritance
# class Father:                             # Base Class 1
#     def __init__(self):
#         print('I am Father')
#
#     def motivation(self):
#         print('Father - I am good with Maths')
#
#
# class Sister(Father):                       # Derived Class 1
#     def __init__(self):
#         print('I am Mother')
#
#     def something(self):
#         print('sister - Very good with Cooking')
#
#
# class Mother(Father):                       # Derived Class 1
#     def __init__(self):
#         print('I am Me')
#
#     def cooking(self):
#         print('Mother - very good with Cooking')
#
#
# class Me(Mother, Sister):
#     def python(self):
#         print('Son - Python')

# mother = Mother()
# mother.motivation()
# # mother.something()
# m = Me()
# m.motivation()
# m.something()
# m.cooking()

# class Father:                             # Base Class 1
#     def __init__(self):
#         # self.a = a
#         print('I am Father')
#
#     def motivation(self):
#         print('Father - I am good with Maths')
#
#
# class Sister(Father):                       # Derived Class 1
#     def __init__(self):
#         super(Father).__init__()
#         print('I am sister')
#
#     def something(self):
#         print('sister - Very good with Cooking')

# s = Sister()
# s.something()
# s.motivation()

class ParentCompany:                # Base Class
    def __init__(self):
        print('Constructor of Parent Company')
        self.n = 'Mukunda'
        self.mobile = 'Mobile'

    def reception(self):
        print('Reception')


class ChildCompany(ParentCompany):  # Derived Class
    def __init__(self, name, mob):
        super().__init__()
        print('Inside ChildCompany ', name, self.n)
        self.a = self.n
        self.b = mob


class SChildCompany(ChildCompany):
    def __init__(self, name, mob):
        ChildCompany.__init__(self, name, mob)
        print('Inside Schild ', name, self.n)
        self.a = self.n
        self.b = self.mobile


d = SChildCompany('Mukund', 84)
d.reception()
print(d.a)