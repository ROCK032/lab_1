# Создание словаря
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)  # Вывод полного словаря

# Доступ к значениям по ключам
print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])

# Если в словаре несколько одинаковых ключей, сохраняется последнее значение
thisdict2 = {
  "brand": "BMW",
  "model": "M6",
  "year": 2016,
  "year": 2020  # Перезапишет предыдущее значение "year"
}
print(thisdict2)

# Итерация по значениям словаря
for i in thisdict2:
    print(thisdict2[i])

# Итерация по ключам словаря
for i in thisdict2:
    print(i)

# Итерация по ключам и значениям одновременно
for x, y in thisdict2.items():
    print(x, y)

# Длина словаря
print(len(thisdict))
print(len(thisdict2))

# Тип данных словаря
print(type(thisdict))

# Создание словаря с использованием конструктора dict()
thisdict3 = dict(name="John", age=36, country="Norway")
print(thisdict)

# Получение списка ключей
x = thisdict.keys()
y = thisdict3.keys()
print(x)
print(y)

# Добавление нового ключа и значения в словарь
thisdict["color"] = "black"
print(thisdict)

# Получение всех значений и пар ключ-значение
print(thisdict.values())
print(thisdict.items())

# Обновление значения существующего ключа
thisdict.update({"color": "red"})
print(thisdict)

# Удаление элемента с использованием pop()
thisdict.pop("color")
print(thisdict)

# Удаление последней добавленной пары ключ-значение с использованием popitem()
thisdict.popitem()
print(thisdict)

# Удаление элемента по ключу с использованием del
del thisdict["brand"]
print(thisdict)

# Полная очистка словаря
thisdict.clear()
print(thisdict)

# Копирование словаря
car = thisdict2.copy()
print(car)

# Создание вложенного словаря
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}

# Итерация по вложенному словарю
for x, obj in myfamily.items():
    print(x)  # Имя ключа (например, "child1")

    # Итерация по внутренним ключам и значениям
    for y in obj:
        print(y + ':', obj[y])  # Вывод внутреннего ключа и значения
    print()
