import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()
pattern = r"\d+\.\s+(.+?)\n(\d+,\d{3}) x (\d+,\d{2})\n(\d+,\d{2})"
matches = re.findall(pattern, text)

for i, match in enumerate(matches, start=1):
    name, quantity, price, total = match
    print(f"{i}. {name.strip()} — {quantity} шт. по {price} KZT, итого: {total} KZT")