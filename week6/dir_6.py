import os
import string

os.makedirs("letters", exist_ok = True)

def create_letter_files():
    for letter in string.ascii_uppercase:
        with open("letters/" +letter + ".txt", "w") as file:
            file.write(letter)

create_letter_files()
folder = "letters"
files = os.listdir(folder)
for file in files:
    print(file)
