# Создание простого класса с атрибутом x
class MyClass:
    x = 5

# Создание объекта класса MyClass
p1 = MyClass()
print(p1.x)  # Выводит значение x (5)


# Класс Person с конструктором, принимающим имя и возраст
class Person:
    def __init__(self, name, age):
        self.name = name  # Присваиваем атрибут name
        self.age = age  # Присваиваем атрибут age

# Создание объекта класса Person
p1 = Person("John", 20)

# Вывод значений атрибутов объекта
print(p1.name)  # John
print(p1.age)   # 20


# Класс Verson с методом __str__, который определяет строковое представление объекта
class Verson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"  # Возвращает строку в формате "Имя (Возраст)"

# Создание объекта класса Verson
p1 = Verson("John", 20)

# Вывод объекта, который теперь корректно отображает строку, определенную в __str__
print(p1)  # John (20)


# Класс Merson с методом myfunc, который выводит приветствие
class Merson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

# Создание объекта класса Merson
p1 = Merson("Maria", 24)

# Изменение атрибута name у объекта p1
p1.name = "John"

# Вызов метода myfunc, который теперь использует обновленное имя
p1.myfunc()  # Выведет: Hello, my name is John
