# Инициализация двух списков
list1 = ["apple", "banana", "cherry"]
list2 = ["kiwi", "mango"]

# Расширение list1 элементами из list2
list1.extend(list2)
print(list1)  # Результат: объединение list1 и list2

# Удаление элемента "banana" из list1
list1.remove("banana")
print(list1)  # Результат: "banana" удаляется из списка

# Удаление элемента по индексу 0 (первый элемент) из list1
list1.pop(0)
print(list1)  # Результат: первый элемент списка удаляется

# Удаление элемента по индексу 2 из list1
del list1[2]
print(list1)  # Результат: элемент на индексе 2 удаляется

# Очистка всего списка list1
list1.clear()
print(list1)  # Результат: пустой список
