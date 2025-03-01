import re

txt = "jwnd_njdn njnjAfdd"
pattern = r"^[a-z]+_[a-z]+"

result = re.findall(pattern, txt)

print(result)
