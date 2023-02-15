# name = 'Mukund'
# company_name = 'Tech Amplifiers'
# id = 15.5
#
# # print('Hello ' + name + '\nCongratulations! \nyou got selected for' + company_name + 'your id', id, 'Welcome Onboard.')
# print(f'Hello {name}, \nCongratulations! \nyou got selected for {company_name}, your id {id} Welcome Onboard.')
''' 
Hi Mukund ,
Congratulations! 
you got selected for ...... . your id ......1 welcome onboard 
'''

''' 
Hi Deepak, 
Congratulations! 
you got selected to ...... . your id ......2 welcome onboard 
'''
''' 
Hi Shubham, 
Congratulations! 
you got selected to ...... . your id ......3 welcome onboard 
'''
# name = 'Mukund'
# company_name = 'Tech Amplifiers'
# # id = 15
#
# print(f'Hello {name}, \nCongratulations! \nyou got selected for {company_name}, your id {id}.')

# name = 'Deepak'
# company_name = 'Tech Amplifiers'
# id = 15.545445
# print(f'Hello {name}, \nCongratulations! \nyou got selected for {company_name}, your id {id}.')

# a = 10
# print('Memory Location of a : ', id(a))
#
# c = 10
# print('Memory Location of c : ', id(a))
#
# a = ['Mukund']
#






#
# b = 'Mukund'
# print('Memory Location of b' ,id(b))
#
# d = True
# a = a + 2
# print('The value of a is', a)           # 12
# print('Memory Location of a : ', id(a))
# a = 15


#  Immutable
# b = 'Mukund'
# print('The value of b is', b)
# print(id(b))
#
# b = b + ' Parve'
# print('The value of b is', b)
# print(id(b))

# a = 10
# print('value of a', a)
# print(id(a))
#
# a = a + 1
# print('value of a', a)
# print(id(a))


# IMMUTABLE
# l = [10, 12, 56, 79]
# print(l)
# print(id(l))
#
# l.append(10)
# l.pop(1)
# print(l)
# print(id(l))
# #

# a = 10
# print(a)
# print(id(a))
#
# b = 10      #
# print(b)
# print(id(b))
#
# c = 10
# c = c + 2 # 12
# d = 12
# print(c)
# print(id(c))
# print(d)
# print(id(d))
#
# a = b = c = 10
# print(id(a))
# print(id(b))
# print(id(c))

# l = [10, 20]
# l2 = [10, 20]
# print(l)
# print(id(l))
# print(l2)
# print(id(l2))
#
# l.append(10)
# print(l)
# print(id(l))
# print(l2)
# print(id(l2))

# print(l)
# print(id(l))
# print(l2)
# print(id(l2))
#
# l.append(10)
# print(l)
# print(id(l))
# print(l2)
# print(id(l2))
#
#
# print()



# print(name.upper())
# print(name.count('z'))      # count
# for i in name:
#     print(i)

# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.isupper())
# print(name.islower())
# print(name.isalpha())
# name = '12.5'
# print(name.isdigit())
# print(name.isalnum())

# l = l2 = [10, 20]
# del l
# print(l2)
# print(l)

# name = 'Mukund Parve'
# to find the first index of alpha in string
# print(name.index('n'))
# print(name.index('P'))
# # print(name.index('p'))   # error
# # find() - index        # No error if not found
# print(name.find('P'))
# print(name.find(' '))
# print(name.find('p'))


# removing letters
# name = '    Mukund Parve  '
# print(name.strip('    M'))
# print(name.strip('e'))
# print(name.strip('u'))
# print(name.strip('P'))
# print(name.strip('ve'), end='#')
# print()
# print(name.strip(), end='#\n')
# print(name.lstrip(), end='#\n')
# print(name.rstrip(), end='#\n')
# print(name.strip('Muku'))

# name = 'Mukund Parve'           # [start: end : step]
# print(name[0:6])
# print(name[0:6:3])
# print(name[0::2])
# print(name[::2])
# print(name[3::2])
# print(name[:-5]+'#')

# email = 'mukundparve@techamplifiers.com'


email = input('Enter your Email address: ')

user_name = email[0:email.index('@')]
print('User Name:', user_name)

raw_domain = email[email.index('@'):]
domain_name = raw_domain[1: raw_domain.index('.')]
print('Domain Name:', domain_name)


#
# a_zA_Z15 = 2.5          # this is a variable
# a = 'Mukund'
# A = 155
#
# print(id(a))
# print(id(A))
# print(type(a))
