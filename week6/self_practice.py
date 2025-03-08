import os

'''print(os.getcwd())
path = os.getcwd()
os.mkdir("my_dictonory")

os.makedirs("parent_dir/child_dir)

all_contents = os.listdir(path)
directories = [i for i in all_contents if os.path.isdir(i)]
files = [i for i in all_contents if os.path.isfile(i)]

print(directories, files, all_contents)'''



''' checking existence, readibility and writability'''
'''path = os.getcwd()

if os.path.exists(path):
    print("exist")
else:
    print("doesnt exist")

print(f"readible: {"yes" if os.access(path, os.R_OK) else "no"}")
print(f"Writability: {"yes" if os.access(path, os.W_OK) else "no"}")
print(f"executability: {"yes" if os.access(path,  os.X_OK) else "no"}")

path = os.getcwd()

if os.path.exists(path):
    print("exist")
    print(f"Dir: {os.path.dirname(path)}")
    print(f"File: {os.path.basename(path)}")
else:
    print("doesnt exist")'''

path = r"C:\Users\user\Documents\Challenging situation in the past.txt"
def count_lines(file):
    with open(file, 'r', encoding='utf-8-sig', errors='ignore' ) as text:
        return len(text.readlines())

line_count = count_lines(path)
print(line_count)
