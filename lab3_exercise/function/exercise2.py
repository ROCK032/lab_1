def main(x):
    celsius = (5 / 9) * (x - 32)
    return celsius

x = float(input())
print(f"{x}°F = {main(x):.2f}°C")
