path =  r"C:\Users\user\Documents\Challenging situation in the past.txt"
list_words = ["apple", "banana", "orange"]

with open(path, 'w', encoding = "utf-8", errors ="ignore") as file:
    for word in list_words:
        file.write(word + "\n")

with open(path, 'r', encoding = "utf-8", errors = "ignore") as text:
    content = text.read()
    print(content)
