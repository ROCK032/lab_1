# Инициализация кортежа
thistuple = ("apple", "banana", "cherry")

# Вывод длины кортежа
print(len(thistuple))

# Инициализация кортежа с одним элементом
list1 = ("aplle",)
print(type(list1))  # Кортеж с одним элементом

# Ошибка при создании кортежа без запятой
list2 = ("apple")
print(type(list2))  # Это не кортеж, а строка

# Доступ к элементам кортежа по индексу и с использованием отрицательных индексов
print(thistuple[1])
print(thistuple[-1])

# Итерация по кортежу с проверкой условия
for i in thistuple:
    if "apple" in i:
        print("Да это яблоко")
    else:
        print("Нет это не яблоко")

# Преобразование кортежа в список для изменения его содержимого
y = list(thistuple)
y[1] = "mango"  # Замена элемента
thistuple = tuple(y)  # Преобразование списка обратно в кортеж
print(thistuple)

# Добавление нового элемента в кортеж
a = list(thistuple)
a.append("banana")
thistuple = tuple(a)
print(thistuple)

# Объединение кортежей
thistuple2 = ("kiwi",)
thistuple += thistuple2  # Добавление второго кортежа
print(thistuple)

# Удаление элемента из кортежа (через преобразование в список)
rem = list(thistuple)
rem.remove("banana")
thistuple = tuple(rem)
print(thistuple)

# Удаление кортежа
del thistuple
#print(thistuple)  # Будет ошибка, так как кортеж удалён

# Пример работы с списком (не кортежем)
fruits = ["apple", "banana", "cherry"]

# Итерация через индекс и вывод всех элементов списка
for i in range(len(fruits)):
    print(fruits[i])

# Итерация через while и вывод всех элементов списка
print()
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1  # Инкремент индекса
