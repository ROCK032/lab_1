import os

path = input("Enter the path: ")
if os.path.exists(path):
    print("Path exists")
    directory, filename =os.path.split(path)
    if os.path.isdir(path):
        print('It is a directory')
    elif os.path.isfile(path):
        print('It is a file')
    if directory:
        print("Directory:", directory)
    else:
        print("This is a root directory")

    if filename:
        print("Filename:", filename)
    else:
        print("No filename (this is a directory)")
else:
    print("Path does not exist")
