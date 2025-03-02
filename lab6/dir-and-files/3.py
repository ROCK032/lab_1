import os

def check_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        print(f"Путь существует.")
        print(f"Каталог: {directory}")
        print(f"Имя файла: {filename}")
    else:
        print("Путь не существует.")

# Пример использования
path = input("Введите путь: ")
check_path(path)
