import re

txt = "Hello world SFFdcc!"

pattern = r"^[A-Z]{1}+[a-z]+"
result = re.findall(pattern, txt)

print(result)