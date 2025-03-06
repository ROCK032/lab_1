import os
import string

directory = input("Enter the directory to save files: ")

if not os.path.exists(directory):
    os.makedirs(directory)
for i in string.ascii_uppercase:
    file_path = os.path.join(directory, f'{i}.txt')
    with open(file_path, "w") as file:
        file.write(f"This is file {i}.txt\n")
print("26 FILES created")
