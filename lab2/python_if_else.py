# Простое условие
x = 10
y = 20
if x > y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")

# Множественные условия
z = 30
if x > y and x > z:
    print("x is the largest")
elif y > x and y > z:
    print("y is the largest")
else:
    print("z is the largest")

# Тернарный оператор
result = "Even" if x % 2 == 0 else "Odd"
print(f"x is {result}")

# Условие с вложенными операторами
if x > 5:
    if y > 15:
        print("x > 5 and y > 15")
    else:
        print("x > 5 but y <= 15")

# Условие с использованием in
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Apple is in the list")

# Проверка пустого значения
string = ""
if not string:
    print("String is empty")