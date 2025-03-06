import shutil

file1 = input("Enter the file1 file path: ")
file2 = input("Enter the file2 file path: ")

try:
    shutil.copyfile(file1, file2)
    print("File copied successfully.")
except FileNotFoundError:
    print("Error: Source file not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")
