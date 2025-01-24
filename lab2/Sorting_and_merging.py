# Генерация списка чисел от 1 до 20
list1 = [i for i in range(1, 21)]

# Сортировка списка по убыванию
list1.sort(reverse=True)
print(list1)

# Сортировка списка по возрастанию
list1.sort()
print(list1)

# Сортировка по возрастанию, по убыванию и вывод противоположного списка
thislist = ["apple", "banana", "cherry"]

# Копирование списка через метод copy()
mylist = thislist.copy()
print(mylist)

# Очистка списка mylist и копирование списка через list()
mylist.clear()
mylist = list(thislist)
print(mylist)

# Объединение двух списков через оператор "+"
x = ["a", "b", "c"]
y = [1, 2, 3]
c = x + y
print(c)

# Объединение списков через цикл for с использованием метода append()
for i in y:
    x.append(i)
print(x)

# Объединение списков через метод extend()
d = [4, 5, 6]
y.extend(d)
print(y)
