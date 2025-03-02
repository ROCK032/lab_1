def main(s):
    upper_text = sum(1 for char in s if char.isupper())
    lower_text = sum(1 for char in s if char.islower())
    return upper_text, lower_text

text = input("Enter the text: ")
upper, lower = main(text)
print("Upper:", upper)
print("Lower:", lower)
