import os

path = input("Enter the file path to delete\n")

if os.path.isfile(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File deleted.")
else:
    print("Cannot delete file.")

