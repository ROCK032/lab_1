import os

file_path = input("Enter the file path")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        line_count = sum(1 for i in file)
    print("Number of lines:", line_count)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
