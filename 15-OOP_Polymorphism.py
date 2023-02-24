# a = 10
# b = 20
# c = a + b
# print(c)
# s = 'I am gonig to learn'
# p = 'Polymorphism'
# l = [12, 'sd']
# print(len(s))
# print(len(l))

class A:
    def add(self):
        print('Adding')
    def sub(self):
        print('Subtracting')

class B(A):
    def add(self):
        print('Adding into B')

b = B()
b.add()
b.add()
# a = A()
# a.add()

# while running the code it will run top to bottom
#
# class A:
#     # def add(self, a, b):
#     #     print(a+b)
#
#     def add(self, x, y, z=0):
#         print(x+y+z)
#
# a = A()
# a.add(10, 20)
# a.add(10, 20, 30)
#
#
#
#
#
#
#
