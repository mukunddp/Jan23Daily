# users = [
#     {
#         'User_name': 'Mukund',
#         'mobile': 7972005157
#     },
#     {
#         'User_name': 'Deepak',
#         'mobile': 123456789
#     },
# ]
# while True:
#     name = input('Enter Your name: ')
#
#     for element in users:
#         if name == element['User_name']:        # True
#             print('Found the User', element['User_name'])
#             break
#     else:
#         print('Name not found!')
#         ask = input('Do you want to join batch ? type: Yes/No')
#         if ask == 'Yes':
#             admin_input = input('Want to add this new user? type: Yes/No')
#             if admin_input == 'Yes':
#                 ele = {
#                     'User_name': name,
#                     'mobile': 1234567890
#                 }
#                 users.append(ele)
#                 print(users)
#             else:
#                 print('Admin has rejected your application')
#         elif ask == 'No':
#             print('Thank you for showing interest!')
#         else:
#             print('Thank you')









def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(numbers):
    return [num for num in numbers if is_prime(num)]

# Example usage
numbers = [11, 12 , 16, 97, 12, 53, 51, 23, 27, 1, 2, 7]
print(find_primes(numbers))