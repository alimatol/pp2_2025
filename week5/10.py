import re

txt = "AppleIsSweet"
x = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt).lower()

print(x)