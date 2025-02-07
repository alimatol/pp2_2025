def histogram(x, y, z):
    print('*' * x)
    print('*' * y)
    print('*' * z)
integers = []

for i in range(3):
    element = int(input())
    integers.append(element)

histogram(*integers)

