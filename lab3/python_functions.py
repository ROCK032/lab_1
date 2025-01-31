# Функция принимает одно имя и выводит приветствие
def main(name):
    print("Hello " + name)

# Вызов функции с аргументом "Tomac"
main("Tomac")


# Функция принимает имя и город, затем выводит приветствие
def main1(name, city):
    print("Hello " + name + " from " + city)

# Вызов функции с аргументами "Tomac" и "London"
main1("Tomac", "London")


# Функция принимает произвольное количество имен и выводит второе имя из списка
def main2(*name):
    print("Hello " + name[1])  # Индексация начинается с 0, поэтому name[1] — это второй аргумент

# Вызов функции с тремя именами
main2("Tomac", "Jon", "Jonson")


# Функция принимает три именованных аргумента и выводит приветствие для первого ребенка
def main3(child1, child2, child3):
    print("Hello " + child1)

# Вызов функции с аргументами по ключу
main3(child1="Jon", child2="Megan", child3="Smith")


# Функция принимает произвольное количество именованных аргументов и выводит значение "lname"
def main4(**kind):
    print("Hello " + kind["lname"])  # Доступ к значению по ключу "lname"

# Вызов функции с двумя именованными аргументами
main4(fname="Jon", lname="Megan")


# Функция принимает страну с параметром по умолчанию "Almaty"
def main5(country="Almaty"):
    print("Hello, I am from " + country)

# Вызовы функции с разными странами
main5(country="America")
main5(country="Brazil")
main5(country="Canada")
main5()  # Используется значение по умолчанию "Almaty"
main5(country="China")


# Функция принимает список и выводит каждый элемент
def main6(food):
    for item in food:
        print(item)

# Создание списка фруктов
fruits = ["apple", "banana", "orange"]

# Вызов функции с переданным списком
main6(fruits)


# Функция принимает число и возвращает его, умноженное на 5
def main7(x):
    return x * 5

# Вывод результатов вызова функции
print(main7(3))  # 3 * 5 = 15
print(main7(5))  # 5 * 5 = 25


# Функция-заглушка (ничего не делает, но не вызывает ошибку)
def main8():
    pass


# Рекурсивная функция, суммирующая все числа от x до 0
def tri_recursion(x):
    if x > 0:
        result = x + tri_recursion(x - 1)  # Рекурсивный вызов с уменьшением x
        print(result)  # Вывод промежуточного результата
    else:
        result = 0  # Базовый случай рекурсии (остановка)
    return result

# Запуск рекурсивной функции
print("Recursion Example Results:")
tri_recursion(6)
