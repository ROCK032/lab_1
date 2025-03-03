import string


text_list = list(string.ascii_uppercase)


for letter in text_list:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}")
