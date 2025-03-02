import string

# Получаем список букв от A до Z
text_list = list(string.ascii_uppercase)

# Создаем файлы
for letter in text_list:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}")
