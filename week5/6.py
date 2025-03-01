import re

txt = "apple lemon, yogurt"
x = re.sub("\W", "|", txt)
print(x)