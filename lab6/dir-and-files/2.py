import os

path = input("Enter the folder path\n")

if os.path.exists(path):
    print("Path exists")
    print("Readable", "Yes" if os.access(path, os.R_OK) else "No")
    print("Writable", "Yes" if os.access(path, os.W_OK) else "No")
    print("Executable", "Yes" if os.access(path, os.X_OK) else "No")
else:
    print("Path does not exist")
