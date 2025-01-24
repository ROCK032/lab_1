# Создать множество
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Повторяющиеся значения будут автоматически игнорироваться
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True и 1 считаются одним и тем же значением
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False и 0 также считаются одним и тем же значением
thisset = {"apple", "banana", "cherry"}

# Получить количество элементов в множестве
print(len(thisset))

# Проверить тип данных множества
print(type(thisset))

# Создание множества с использованием конструктора set()
fruits = set(("papaya", "banana", "pineapple"))
print(fruits)

# Итерация по элементам множества
for i in thisset:
    print(i)

# Проверка наличия элемента в множестве
print("banana" in thisset)
print("banana" not in fruits)

# Добавление элемента в множество
thisset.add("kiwi")
print(thisset)

# Объединение двух множеств с использованием метода update()
thisset.update(fruits)
print(thisset)

# Удаление элемента с использованием remove()
thisset.remove("apple")
print(thisset)

# Удаление элемента с использованием discard()
thisset.discard("banana")
print(thisset)

# Удаление случайного элемента с использованием pop()
x = thisset.pop()
print(x)
print(thisset)

# Очистка множества
thisset.clear()
print(thisset)

# Удаление множества
del fruits

# Объединение двух множеств с использованием union() и оператора |
x = {"lion", "cat", "dog"}
y = {1, 2, 3}
z = x.union(y)
q = x | y
print(z)
print(q)

# Поиск пересечения двух множеств
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# Поиск разности двух множеств
set4 = set1.difference(set2)
print(set4)

# Поиск симметрической разности двух множеств
set5 = set1.symmetric_difference(set2)
print(set5)
