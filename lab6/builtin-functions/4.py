import time
import math

number = int(input("Enter a number: "))
delay = int(input("Enter a delay: "))

time.sleep(delay/1000)

result = math.sqrt(number)
print(f"Square root of {number} after {delay} miliseconds is 158.{result}")