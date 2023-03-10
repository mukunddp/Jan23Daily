# import zipfile
# from zipfile import *
from zipfile import ZipFile

# with ZipFile('techamplifiers.zip', 'w') as z:
#     z.write('mukund.txt')

# extracting files and reading file in zip
# with ZipFile('techamplifiers.zip', 'r') as z:   # w, x, a, r
#     # print(str(z.read('mukund.txt')))     # in default binary form
#     z.extractall("myZip")

# printing directory
# with ZipFile("techamplifiers.zip", 'a') as z:       # w, a, r, x
    # print('Directory')
    # z.write('Indian_flag.py')
    # z.write('rdj.py')
#     z.printdir()
#     z.extractall("mukundzip")        # to extract files from zip




# import os, zipfile
# def zipdir(path, ziph): # ziph is zipfile handle
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             ziph.write(os.path.join(root, file))


# zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
# zipdir('dec_basic.py', zipf)
# zipf.close()