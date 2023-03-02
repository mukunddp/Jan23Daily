# from abc import ABC, abstractmethod
#
#
# class Bank(ABC):                # Abstract Base Class
#     def __init__(self):
#         print('I am constructor')
#
#     @abstractmethod
#     def cashier(self):          # abstract method
#
#         pass
#
#     @abstractmethod
#     def cashier1(self):  # abstract method
#         pass
#
#     def clark(self):
#         print('Something')
#
# class Manager(Bank):                    # Abstract Class
#     def cashier(self):
#         print('All Cashier functions ')
#
#     @abstractmethod
#     def cashier2(self):  # abstract method
#         pass
#
#
# # m = Manager()
# # m.cashier()
#
# class Working(Manager):
#     def cashier(self):
#         print('Working of Cashier')
#
#     def cashier1(self):
#         print('Working of Cashier')
#
#     def cashier2(self):
#         print('Working of Cashier')
#
# # b = Bank()
# # b.cashier()
#
# w = Working()
# w.cashier()
# w.cashier2()
#
# # b = Manager()
# # b.cashier()


class Father:
    a = 10
    print(a)
    def __init__(self):
        self.bank_account = '4563131'
        self._atm = 'ATM'
        self._credit = 'Credit Card'
        self.__pin = 4646

class Son(Father):
    def __access(self):
        print(self.bank_account)
        print(self._atm)
        print(self.__pin)


s = Son()
# s.__access()

print(s._credit)
print(s.__pin)








