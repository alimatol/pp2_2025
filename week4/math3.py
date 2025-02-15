import math


def cot(x):
    return 1/math.tan(x)

num = float(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

pi = math.pi

area = (num* pow(length, 2))/4 * cot(pi/num)

print("The area of the polygon is: ",round(area))

