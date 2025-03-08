import os
path = os.getcwd()

if os.path.exists(path):
    print("exist")
    print(f"Dir: {os.path.dirname(path)}")
    print(f"File: {os.path.basename(path)}")
else:
    print("doesnt exist")
