class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length =0):
        self.length = length

    def getLength(self):
        self.length = float(input())

    def area(self):
        return self.length**2
        

value1 = Square()
value1.getLength()
print(value1.area())

value2 = Square()
print(value2.length)

