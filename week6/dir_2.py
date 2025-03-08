import os
path = os.getcwd()

if os.path.exists(path):
    print("exist")
else:
    print("doesnt exist")

print(f"readible: {"yes" if os.access(path, os.R_OK) else "no"}")
print(f"Writability: {"yes" if os.access(path, os.W_OK) else "no"}")
print(f"executability: {"yes" if os.access(path,  os.X_OK) else "no"}")