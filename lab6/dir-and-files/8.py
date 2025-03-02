import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f"Файл '{file_path}' успешно удалён.")
            except Exception as e:
                print(f"Ошибка при удалении файла: {e}")
        else:
            print(f"Нет прав на удаление файла '{file_path}'.")
    else:
        print(f"Файл '{file_path}' не существует.")

file_path = input("Введите полный путь к файлу: ")
delete_file(file_path)
