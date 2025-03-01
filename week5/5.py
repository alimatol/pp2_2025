import re

txt = "atdtfb"
pattern = r"a.*b$"
result = re.findall(pattern, txt)

print(result)
