import re

txt = input()

x = re.fullmatch(r'a*b*', txt)

if x:
    print("True")
else:
    print("False")
