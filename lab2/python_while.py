# Простое использование while
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Цикл с break
n = 0
while n < 10:
    if n == 7:
        print("Breaking the loop at n=7")
        break
    print(n)
    n += 1

# Цикл с continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping iteration when i=3")
        continue
    print(i)
# Использование else с while
j = 0
while j < 3:
    print(j)
    j += 1
else:
    print("Loop finished")