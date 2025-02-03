def main(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

x = "madam"
print(main(x))

y = "hello"
print(main(y))
