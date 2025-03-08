import os
path =  r"C:\Users\user\Documents\Challenging situation in the past.txt"

with open(path, 'r', encoding = 'utf-8', errors = "ignore" ) as source:
    content = source.read()
    
os.makedirs("destination")

with open("destination/copied_file.txt", 'w', encoding = 'utf-8', errors = "ignore") as dest:
    dest.write(content)



