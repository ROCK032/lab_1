import os

file_path = input("Enter the file path\n")

data = ["Apple", "Banana", "Chery", "Date", "Elderberry"]

try:
    with open(file_path, 'w') as file:
        for i in data:
            file.write(i + "\n")
        print("Data successfully written to the file.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
