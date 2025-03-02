import os


def main(path):
    result = {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
    return result


if __name__ == "__main__":
    path = input("Введите путь: ")
    access_info = main(path)

    print("Результаты проверки пути:")
    print(f"Существует: {'Да' if access_info['exists'] else 'Нет'}")
    print(f"Доступен для чтения: {'Да' if access_info['readable'] else 'Нет'}")
    print(f"Доступен для записи: {'Да' if access_info['writable'] else 'Нет'}")
    print(f"Доступен для выполнения: {'Да' if access_info['executable'] else 'Нет'}")
