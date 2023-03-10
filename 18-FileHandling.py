# Open a file
# f = open('rdj.py', 'r')
# # print(f)
# print('file opened\n')
#
# # Perform Operations
# print(f.read())
#
# # Close a file
# f.close()
# print('\nfile is closed')


# # opening a file and read
# with open('mukund.txt') as f:
#     # perform the operations
#     print(f.read())
#

    # at the end it will get closed

# # opening a file exclusive creation
# with open('mukund.txt', 'x') as f:
#     # create new file if already exist then show error
#     # perform the operations
#     # can't perform read operation
#     print(f.write('Mukund'))


# # opening a file for writing
# with open('mukund.txt', 'a+') as f:
#     # it will create if not exist and if exist then it truncates
#     # perform the operations
#     # can't read
#     print(f.write('Mukund Parve'))
#
#     print(f.tell())     # cursor position/index
#     f.seek(100)        # move the cursor the perticular index/position
#     print(f.tell())     # current cursor position after seek
#     print(f.read(200))
    # print('Read a file')






# # # opening a file
# with open('mukund.txt', 'x') as f:
#     # perform the operations
#     print(f.write('Mukund'))

# with open('mukund.txt', 'r+') as f:
#     # perform the operations
#     print(f.readlines())        # this methods returns a list containing all the lines
#     # for lines in f:           # can access all the lines
#     #     print(f.readline())   # this will return only one line
#     #     # print(lines, 'End of line')

# import os
#
# if os.path.exists("E:\\trac.JPG"):
#     os.remove("E:\\trac.JPG")
#     print("File deleted !")
# else:
#     print("File does not exist !")


# Truncate
# with open('mukund.txt', 'a+') as f: # a - append
#     # print(f.seek(15))
#     print(f.truncate(10))
#     print(f.tell())

import os

if os.path.exists("E:\change_seats.png"):
    os.rename("E:\change_seats.png", "E:\seats.png")
    print("File Renamed !")
else:
    print("File does not exist !")


