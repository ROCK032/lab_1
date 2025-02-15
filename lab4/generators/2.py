def main(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter n: "))
print(",".join(map(str, main(n))))
5