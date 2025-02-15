def main(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())

for square in main(a, b):
    print(square)
