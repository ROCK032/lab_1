def copy_file():
    source_file = input("Введите путь к исходному файлу: ")
    destination_file = input("Введите путь к файлу назначения: ")

    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            with open(destination_file, 'w', encoding='utf-8') as dest:
                dest.write(src.read())
        print("Файл успешно скопирован.")
    except FileNotFoundError:
        print("Ошибка: исходный файл не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")


copy_file()
