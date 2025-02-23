import re

txt = input()
x = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), txt)
print(x)