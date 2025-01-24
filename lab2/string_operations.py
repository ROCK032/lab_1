# Инициализация строки
a = "Hello World"

# Вывод строки
print(a)

# Символ на индексе 1
print(a[1])

# Длина строки
print(len(a))

# Последний символ строки
print(a[-1])

# Итерация по символам строки
for i in a:
    print(i)

# Проверка наличия подстроки
b = "The best things in life are free!"
print("free" in b)  # Проверка: подстрока "free" в строке
print("free" not in b)  # Проверка: подстрока "free" отсутствует

# Условие: проверка наличия "life"
if "life" in b:
    print("Yes, 'life' is present")
else:
    print("No, 'life' is present")
