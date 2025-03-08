import os

path = os.getcwd()
path_file = r"C:\Users\user\Desktop\kbtu\university pp\PP2\week6\destination\copied_file.txt"
if os.path.exists(path_file):
    if os.access(path_file, os.R_OK) or os.access(path_file, os.W_OK):
        os.remove(path_file)


