import re

txt = "_today_is_the_great_days"
x = re.sub(r'_([a-z])', lambda match: match.group(1).upper() , txt)

print(x)