import os

print(os.getcwd())
path = os.getcwd()

all_contents = os.listdir(path)
directories = [i for i in all_contents if os.path.isdir(i)]
files = [i for i in all_contents if os.path.isfile(i)]

print(directories, files, all_contents)