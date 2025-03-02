my_list = ["apple", "banana", "cherry"]

with open("myfile.txt", "a", encoding="utf-8") as f:
    for item in my_list:
        f.write(item + "\n")

print("Список успешно записан в файл.")
