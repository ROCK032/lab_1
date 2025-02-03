is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

numbers = [2, 3, 4, 5, 10, 13, 15, 17, 18, 19, 20]

prime_numbers = list(filter(is_prime, numbers))

print(prime_numbers)
