import shutil

source = input("Enter the source file path: ")
destination = input("Enter the destination file path: ")

try:
    shutil.copyfile(source, destination)
    print("File copied successfully.")
except FileNotFoundError:
    print("Error: Source file not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")

