text = input()
uppercase_num = 0
lowercase_num = 0

for char in text:
    if char.isupper():
        uppercase_num+=1
    if char.islower():
        lowercase_num+=1

print(f"Upper count: {uppercase_num}, Lower count: {lowercase_num}")    