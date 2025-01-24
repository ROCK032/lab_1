# Инициализация списка list1
list1 = ["apple", "banana", "cherry"]

# Использование цикла for для итерации по элементам списка
for i in list1:
    print(i)

# Использование цикла for с range для индексации элементов списка
for i in range(len(list1)):
    print(list1[i])

# Использование цикла while для итерации по элементам списка
i = 0
while i < len(list1):
  print(list1[i])
  i = i + 1

# Листовое выражение (list comprehension) для итерации по элементам списка
[print(i) for i in list1]

print("--------------")

# Фильтрация элементов списка, содержащих букву "a"
list2 = []
for i in list1:
    if "a" in i:
        list2.append(i)
print(list2)

# Листовое выражение для фильтрации элементов, содержащих букву "e"
newlist = [i for i in list1 if "e" in i]
print(newlist)

# Генерация нового списка с числами от 0 до 9
newlist2 = [i for i in range(10)]
print(newlist2)

# Очистка списка и создание нового списка с элементами списка list1, преобразованными в верхний регистр
newlist.clear()
newlist = [i.upper() for i in list1]
print(newlist)
