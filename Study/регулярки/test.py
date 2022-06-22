import re

reg_exp = r"@\w+.(\w+)"
file = open("text.txt", "r", encoding="utf-8")

data = file.read()
arr = re.findall(reg_exp, data)


file.close()
print(arr)
