thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

newlist = []

for x in thislist:
  if "a" in x:
    newlist.append(x)

print(newlist)