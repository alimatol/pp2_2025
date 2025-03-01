import re

txt = "TodayIsTheGreatDay"
x = re.split(r'(?=[A-Z])', txt)
x = [word for word in x if word]

print(x)