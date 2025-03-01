import re

txt1 = "abb"
txt2 = "abbb"
x = re.search("^ab{2,3}$",txt1)
y = re.search("^ab{2,3}$",txt2)
print(x, y)