def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        print("Файл не найден.")
        return 0

filename = input("Введите имя файла: ")
lines_count = count_lines(filename)
print(f"Количество строк в файле: {lines_count}")
