import time
import math

print("Input: ")
num1 = int(input())
num2 = int(input())
seconds = num2 / 1000.0
square_root = math.sqrt(num1)
time.sleep(seconds)
print("Output:")
print(f"Square root of {num1} after {num2} milliseconds is {square_root}")
