import re

txt = input()
x = re.fullmatch(r'[a-z]+(_[a-z]+)*', txt)
if x:
    print("True")
else:
    print("False")