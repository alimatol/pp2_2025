import re

txt = "abbb abbab"
x = re.search("^a*b*+",txt)

print(x)


