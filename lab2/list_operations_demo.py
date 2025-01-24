# Инициализация списка с повторяющимися элементами
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

# Вывод списка
print(thislist)

# Вывод типа данных переменной thislist
print(type(thislist))

# Доступ к элементу списка по индексу 1 (второй элемент)
print(thislist[1])

# Доступ к последнему элементу списка (отрицательный индекс)
print(thislist[-1])

# Изменение элемента списка на индексе 4 (пятый элемент)
thislist[4] = "mango"
print(thislist)

# Замена среза списка (с 1 по 2 индексы) на два новых элемента
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Вставка нового элемента на позицию с индексом 2
thislist.insert(2, "watermelon")
print(thislist)

# Добавление нового элемента в конец списка
thislist.append("apple")
print(thislist)
