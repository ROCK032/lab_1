import re

txt = input()

x = re.fullmatch(r'a(bb|bbb)', txt)

if x:
    print("True")
else:
    print("False")

