import re

txt = input()
x = re.fullmatch(r'[A-Z][a-z]+', txt)
if x:
    print("True")
else:
    print("False")